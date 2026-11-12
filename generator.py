import os
import zipfile
import hashlib
import xml.etree.ElementTree as ET
import shutil

# Paths
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
ADDONS = [
    {"id": "plugin.video.stremio4kodi", "path": os.path.join(REPO_DIR, "..", "plugin.video.stremio4kodi")},
    {"id": "repository.sonvice", "path": os.path.join(REPO_DIR, "repository.sonvice")},
    {"id": "service.subtitles.opensubtitles-stremio", "path": os.path.join(REPO_DIR, "..", "service.subtitles.opensubtitles-stremio")}
]
ROOT_EXPORTS = ["repository.sonvice", "plugin.video.stremio4kodi"]
EXTRA_EXPORTS = [
    {
        "addon_id": "plugin.video.stremio4kodi",
        "version": "3.7.33",
        "label": "plugin.video.stremio4kodi-3.7.33.zip"
    }
]
OUTPUT_DIR = os.path.join(REPO_DIR, "repo")

def generate_repo():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    # We will build a manual root element to avoid XML declaration issues
    addons_xml = ET.Element("addons")
    
    for addon in ADDONS:
        addon_id = addon["id"]
        addon_path = addon["path"]
        
        if not os.path.exists(addon_path):
            print(f"Skipping {addon_id}, path not found: {addon_path}")
            continue
            
        # Parse addon.xml
        xml_path = os.path.join(addon_path, "addon.xml")
        tree = ET.parse(xml_path)
        root = tree.getroot()
        version = root.attrib["version"]
        
        # Append to master xml
        addons_xml.append(root)
        
        # Create output directory for this addon
        addon_out_dir = os.path.join(OUTPUT_DIR, addon_id)
        if not os.path.exists(addon_out_dir):
            os.makedirs(addon_out_dir)
            
        # Copy assets (icon, fanart) if they exist
        for asset in ["icon.png", "fanart.jpg"]:
            # Check in addon_path directly
            src = os.path.join(addon_path, asset)
            if not os.path.exists(src):
                # Also check in resources/media
                src = os.path.join(addon_path, "resources", "media", asset)
            if os.path.exists(src):
                shutil.copy(src, os.path.join(addon_out_dir, asset))
                
        # Zip addon
        zip_name = f"{addon_id}-{version}.zip"
        zip_path = os.path.join(addon_out_dir, zip_name)
        
        # Remove old zip to avoid packing it inside or other issues
        if os.path.exists(zip_path):
            os.remove(zip_path)
            
        print(f"Packaging {addon_id} v{version} into {zip_name}...")
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
            for root_dir, dirs, files in os.walk(addon_path):
                # Skip git, cache, github and build files
                parts = os.path.normpath(root_dir).split(os.sep)
                if any(x in parts for x in [".git", ".github", ".antigravitycli", "__pycache__", "repo"]):
                    continue
                dirs[:] = sorted([d for d in dirs if d not in [".git", ".github", ".antigravitycli", "__pycache__", "repo"]])
                
                rel_dir = os.path.relpath(root_dir, os.path.dirname(addon_path))
                if rel_dir != ".":
                    z.write(root_dir, rel_dir)

                for file in sorted(files):
                    if file.startswith(".") or file.endswith(".zip") or file.endswith(".pdf") or file.endswith(".md"):
                        continue
                    full_path = os.path.join(root_dir, file)
                    rel_path = os.path.relpath(full_path, os.path.dirname(addon_path))
                    z.write(full_path, rel_path)
                    
    # Write addons.xml
    addons_xml_path = os.path.join(OUTPUT_DIR, "addons.xml")
    xml_str = ET.tostring(addons_xml, encoding="utf-8")
    
    # Pretty print XML manually to avoid minidom issues in python 3
    from xml.dom import minidom
    dom = minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent="    ", encoding="utf-8")
    
    with open(addons_xml_path, "wb") as f:
        f.write(pretty_xml)
        
    # Write addons.xml.md5
    md5 = hashlib.md5()
    with open(addons_xml_path, "rb") as f:
        md5.update(f.read())
    with open(addons_xml_path + ".md5", "w") as f:
        f.write(md5.hexdigest())
        
    # Delete old zips in root to avoid version accumulation, preserving allowed extra exports
    allowed_root_zips = set()
    for addon in ADDONS:
        if addon["id"] in ROOT_EXPORTS and os.path.exists(addon["path"]):
            xml_path = os.path.join(addon["path"], "addon.xml")
            if os.path.exists(xml_path):
                tree = ET.parse(xml_path)
                allowed_root_zips.add(f"{addon['id']}-{tree.getroot().attrib['version']}.zip")
    for extra in EXTRA_EXPORTS:
        allowed_root_zips.add(f"{extra['addon_id']}-{extra['version']}.zip")

    for file in os.listdir(REPO_DIR):
        if file.endswith(".zip") and file not in allowed_root_zips:
            try:
                os.remove(os.path.join(REPO_DIR, file))
            except Exception:
                pass
        
    # Clean up obsolete addon directories in repo/ (e.g. removed addons)
    active_ids = {addon["id"] for addon in ADDONS}
    for item in os.listdir(OUTPUT_DIR):
        item_path = os.path.join(OUTPUT_DIR, item)
        if os.path.isdir(item_path) and item not in active_ids:
            print(f"Removing obsolete repo directory: {item}")
            shutil.rmtree(item_path)

    # Copy primary installer zips and extra exports to root for flat File Manager index
    for addon in ADDONS:
        addon_id = addon["id"]
        if addon_id not in ROOT_EXPORTS:
            continue
        addon_path = addon["path"]
        if not os.path.exists(addon_path):
            continue
        xml_path = os.path.join(addon_path, "addon.xml")
        tree = ET.parse(xml_path)
        root = tree.getroot()
        version = root.attrib["version"]
        
        src_zip = os.path.join(OUTPUT_DIR, addon_id, f"{addon_id}-{version}.zip")
        dest_zip = os.path.join(REPO_DIR, f"{addon_id}-{version}.zip")
        if os.path.exists(src_zip):
            shutil.copy(src_zip, dest_zip)

    # Copy extra exports from repo/ to root
    for extra in EXTRA_EXPORTS:
        extra_zip = f"{extra['addon_id']}-{extra['version']}.zip"
        src_extra = os.path.join(OUTPUT_DIR, extra['addon_id'], extra_zip)
        dest_extra = os.path.join(REPO_DIR, extra_zip)
        if os.path.exists(src_extra) and not os.path.exists(dest_extra):
            shutil.copy(src_extra, dest_extra)
        
    # Write index.html for Kodi File Manager Add Source
    index_path = os.path.join(REPO_DIR, "index.html")
    html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Sonvice Kodi Repository</title>
    <style>
        body { font-family: sans-serif; background: #121212; color: #ffffff; padding: 40px 20px; text-align: center; }
        h1 { color: #00bcd4; margin-bottom: 5px; }
        p { color: #888; font-size: 1.1em; margin-bottom: 30px; }
        ul { list-style: none; padding: 0; max-width: 600px; margin: 0 auto; text-align: left; }
        li { margin: 15px 0; background: #1e1e1e; padding: 15px 20px; border-radius: 8px; border: 1px solid #333; display: flex; justify-content: space-between; align-items: center; }
        a { color: #e91e63; text-decoration: none; font-size: 1.1em; font-weight: bold; }
        a:hover { color: #ff4081; text-decoration: underline; }
        .tag { font-size: 0.85em; padding: 3px 8px; border-radius: 4px; font-weight: normal; }
        .tag-latest { background: #00e676; color: #000; }
        .tag-legacy { background: #ffa000; color: #000; }
        .tag-repo { background: #00bcd4; color: #000; }
    </style>
</head>
<body>
    <h1>Sonvice Kodi Repository</h1>
    <p>Añade esta URL en el Gestor de Archivos de Kodi para instalar el repositorio o descargar los complementos:</p>
    <ul>
"""
    # Sort exports so repository is displayed first (recommended entry point for users)
    ordered_exports = ["repository.sonvice", "plugin.video.stremio4kodi"]
    for export_id in ordered_exports:
        match = next((a for a in ADDONS if a["id"] == export_id), None)
        if not match or not os.path.exists(match["path"]):
            continue
        xml_path = os.path.join(match["path"], "addon.xml")
        tree = ET.parse(xml_path)
        root = tree.getroot()
        version = root.attrib["version"]
        zip_rel_path = f"{export_id}-{version}.zip"
        tag_class = "tag-repo" if "repository" in export_id else "tag-latest"
        tag_text = "Repositorio (Recomendado)" if "repository" in export_id else f"v{version} (Última Versión)"
        html_content += f'        <li><a href="{zip_rel_path}">{export_id}-{version}.zip</a><span class="tag {tag_class}">{tag_text}</span></li>\n'

    for extra in EXTRA_EXPORTS:
        extra_zip = f"{extra['addon_id']}-{extra['version']}.zip"
        tag_desc = f"v{extra['version']} (Versión Antigua)"
        html_content += f'        <li><a href="{extra_zip}">{extra_zip}</a><span class="tag tag-legacy">{tag_desc}</span></li>\n'
        
    html_content += """    </ul>
</body>
</html>"""
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print("Repository generation complete with flat index.html!")

if __name__ == "__main__":
    generate_repo()
