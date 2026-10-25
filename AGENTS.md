# AGENTS.md — Guía para Agentes de Codificación (Repository)

Este archivo proporciona contexto y directrices técnicas sobre la arquitectura del repositorio de addons de Kodi `repository.sonvice`.

---

## 1. Estructura del Repositorio

El directorio contiene los archivos necesarios para indexar, empaquetar y distribuir las actualizaciones de los addons de Sonvice para Kodi.

* **`repository.sonvice/` (Subdirectorio):** Contiene el código fuente y el `addon.xml` del propio complemento de repositorio.
* **`repo/` (Directorio de salida):** Carpeta autogenerada donde se almacenan las versiones en ZIP y los archivos de índice global `addons.xml` y `addons.xml.md5`.
* **`generator.py`:** Script en Python que automatiza la compilación del repositorio.
* **`index.html`:** Flat index generado automáticamente para permitir a los usuarios instalar los archivos ZIP agregando la URL directa en el gestor de archivos de Kodi.

---

## 2. CDN Mirrors (jsDelivr)

Para evitar bloqueos impuestos por ISPs (operadoras de internet) al dominio `raw.githubusercontent.com`, el archivo `addon.xml` del propio repositorio (`repository.sonvice/repository.sonvice/addon.xml`) apunta a la red de distribución jsDelivr:

* Info: `https://cdn.jsdelivr.net/gh/sonvice/repository.sonvice@main/repo/addons.xml`
* Checksum: `https://cdn.jsdelivr.net/gh/sonvice/repository.sonvice@main/repo/addons.xml.md5`
* Datadir: `https://cdn.jsdelivr.net/gh/sonvice/repository.sonvice@main/repo/`

Cualquier cambio en la versión del repositorio o de los addons se sincronizará automáticamente a través de este CDN gratis una vez que se haga `git push` a la rama `main` en GitHub.

Para evitar retrasos por la caché del CDN al lanzar una actualización importante, se debe purgar inmediatamente la caché con:
```bash
curl -s "https://purge.jsdelivr.net/gh/sonvice/repository.sonvice@main/repo/addons.xml"
curl -s "https://purge.jsdelivr.net/gh/sonvice/repository.sonvice@main/repo/addons.xml.md5"
```

---

## 3. Pautas para Actualizaciones

1. **No editar archivos en `repo/` directamente:** Estos archivos se sobrescriben cada vez que se ejecuta el script de empaquetado.
2. **Procedimiento para publicar actualizaciones:**
   - Modifica el código del addon deseado (ej: `plugin.video.stremio4kodi`).
   - Sube la versión del addon en su respectivo `addon.xml`.
   - Ejecuta:
     ```bash
     python3 generator.py
     ```
   - Haz commit de todos los archivos cambiados en este repositorio (incluyendo el directorio `repo/` y los ZIPs resultantes) y súbelo a GitHub:
     ```bash
     git add -A
     git commit -m "Publish vX.Y.Z: <resumen de cambios>"
     git push origin main
     ```
   - Purga la caché de jsDelivr con los dos comandos `curl` indicados arriba.

---

## 4. Estado Actual de Versiones y Motores (v3.7.12)
* **`plugin.video.stremio4kodi` (v3.7.12):** Incluye soporte nativo para streaming mediante TorrServer MatriX en RAM, modo de selección "Auto" con failover transparente a Elementum si el PC está en reposo o apagado (≤600ms), auto-heal de Elementum mediante reinicio por JSON-RPC, y resolución directa a `xbmc.Player().play()` con metadatos de subtítulos y puntos de reanudación.
