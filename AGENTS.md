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

## 2. CDN & Distribución (GitHub Pages + Fastly)

Para evitar bloqueos impuestos por ISPs (operadoras de internet) al dominio `raw.githubusercontent.com` y evitar los límites de cuota/403 de jsDelivr, el archivo `addon.xml` del propio repositorio (`repository.sonvice/repository.sonvice/addon.xml`) apunta a GitHub Pages con CDN global Fastly:

* Info: `https://sonvice.github.io/repository.sonvice/repo/addons.xml`
* Checksum: `https://sonvice.github.io/repository.sonvice/repo/addons.xml.md5`
* Datadir: `https://sonvice.github.io/repository.sonvice/repo/`

Cualquier cambio en la versión del repositorio o de los addons se sincronizará automáticamente a través de este CDN una vez que se haga `git push` a la rama `main` en GitHub.

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

---

## 4. Estado Actual de Versiones y Motores (v4.0.0)
* **`plugin.video.stremio4kodi` (v4.0.0):** MediaCore — Nueva arquitectura modular inspirada en HolyArrs ("One UI, One Media Core"). Desacoplamiento en hubs independientes: Playback Hub (TorrServer prioritario, Debrid, Elementum, AceStream con fallback <1s), Sources Hub (Stremio, Torznab para Jackett/Prowlarr, DHT), Scoring Engine con deduplicación por infoHash y Metadata Hub.
* **`repository.sonvice` (v1.0.11):** Migración del repositorio a GitHub Pages (`https://sonvice.github.io/repository.sonvice/repo/`) con CDN Fastly global para eludir bloqueos de ISPs y resolver el error 403 Forbidden de jsDelivr.
