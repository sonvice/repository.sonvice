import os
import zipfile
import hashlib
import xml.etree.ElementTree as ET
import shutil

# Paths
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
ADDONS = [
    {"id": "plugin.video.stremio4kodi", "path": os.path.join(REPO_DIR, "..", "plugin.video.stremio4kodi")},
    {"id": "repository.sonvice", "path": os.path.join(REPO_DIR, "repository.sonvice")}
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
            for root_dir, _, files in os.walk(addon_path):
                # Skip git, cache, and build files (checking exact folder names, not substrings)
                parts = os.path.normpath(root_dir).split(os.sep)
                if any(x in parts for x in [".git", ".antigravitycli", "__pycache__", "repo"]):
                    continue
                for file in files:
                    if file.endswith(".zip"):
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
        ul { list-style: none; padding: 0; max-width: 500px; margin: 0 auto; }
        li { margin: 20px 0; background: #1e1e1e; padding: 15px; border-radius: 8px; border: 1px solid #333; }
        a { color: #e91e63; text-decoration: none; font-size: 1.2em; font-weight: bold; }
        a:hover { color: #ff4081; text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Sonvice Kodi Repository</h1>
    <p>Añade esta URL en el Gestor de Archivos de Kodi para instalar los addons:</p>
    <ul>
"""
    for addon in ADDONS:
        addon_id = addon["id"]
        addon_path = addon["path"]
        if not os.path.exists(addon_path):
            continue
        xml_path = os.path.join(addon_path, "addon.xml")
        tree = ET.parse(xml_path)
        root = tree.getroot()
        version = root.attrib["version"]
        zip_rel_path = f"repo/{addon_id}/{addon_id}-{version}.zip"
        html_content += f'        <li><a href="{zip_rel_path}">{addon_id} v{version} (ZIP)</a></li>\n'
        
    html_content += """    </ul>
</body>
</html>"""
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print("Repository generation complete with index.html!")

if __name__ == "__main__":
    generate_repo()
