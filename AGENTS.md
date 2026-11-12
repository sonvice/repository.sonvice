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

## 4. REGLA ESTRICTA DE INTERFAZ: PROHIBICIÓN ABSOLUTA DE EMOJIS (Iconos Nativos Únicamente)

> [!IMPORTANT]
> **LOS ADDONS Y COMPLEMENTOS NO DEBEN CONTENER EMOJIS BAJO NINGUNA CIRCUNSTANCIA.**
> Queda terminantemente prohibido insertar caracteres emoji Unicode (ej: 🏠, ⚡, 🎬, 🔥, 📺, 🍿, 🇪🇸, 🏆, 🔍, ⚙️, etc.) en etiquetas de menús (`label`), diálogos, notificaciones o archivos `settings.xml`.
> 
> * **Motivo técnico:** Las fuentes tipográficas estándar de Kodi (Estuary, CoreELEC, Android TV, LibreELEC) no incluyen glifos de emojis en sus tablas TTF y renderizan rectángulos rotos o caracteres basura vacíos (`[]` / ``).
> * **Solución obligatoria:** Si es necesario aportar riqueza visual a una entrada, se deben utilizar **únicamente iconos nativos de Kodi** mediante el parámetro `icon="DefaultX.png"`.
>   * Carpetas generales: `DefaultFolder.png`
>   * Películas: `DefaultMovies.png`
>   * Series: `DefaultTVShows.png`
>   * Seguir viendo / En progreso: `DefaultInProgressShows.png`
>   * Recientes / Novedades: `DefaultRecentlyAddedMovies.png` / `DefaultRecentlyAddedEpisodes.png`
>   * Plataformas y Estudios: `DefaultStudios.png`
>   * Ajustes / Programas: `DefaultAddonProgram.png`
>   * Búsqueda: `DefaultAddonsSearch.png`
>   * Géneros: `DefaultGenre.png`
>   * Años: `DefaultYear.png`
>   * Red / Magnets: `DefaultNetwork.png`
>   * Favoritos: `DefaultFavourites.png`

---

## 5. Estado Actual de Versiones y Motores (v4.1.0)
* **`plugin.video.stremio4kodi` (v4.1.0):** MediaCore + Configuración Móvil vía QR + Home Moderna + Widgets Kodi. Supresión definitiva de "Catálogos Stremio" por "Plataformas de Streaming" y "Colecciones y Sagas".
* **`repository.sonvice` (v1.0.11):** Repositorio en GitHub Pages con soporte multi-versión (`v4.1.0` última, `v4.0.0` MediaCore, `v3.7.33` Legacy).
* **`repository.sonvice` (v1.0.11):** Migración del repositorio a GitHub Pages (`https://sonvice.github.io/repository.sonvice/repo/`) con CDN Fastly global para eludir bloqueos de ISPs y resolver el error 403 Forbidden de jsDelivr.
