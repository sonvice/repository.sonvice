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

## 5. Política Estricta de Versiones (Dual-Version Retention: v4.x y v3.x)

El repositorio mantiene intencionadamente **únicamente dos versiones** de `plugin.video.stremio4kodi`:
1. **Última Versión Estable (`v4.1.0+`):** MediaCore + Configuración Móvil vía QR + Home Moderna + Widgets Kodi.
2. **Versión Antigua / Clásica (`v3.7.33`):** Versión monolítica legacy ligera para usuarios con dispositivos muy antiguos o que prefieran la interfaz tradicional de menús Stremio directos.

> [!WARNING]
> **No acumular versiones intermedias (ej. `v4.0.0`):** `generator.py` limpia automáticamente los ZIPs obsoletos de la raíz y del flat index `index.html`. Los usuarios únicamente deben poder elegir entre la versión más reciente y la última versión clásica de la rama v3.

---

## 6. Arquitectura de Distribución y Gestor de Archivos (index.html)

### 6.1. Prioridad Absoluta del Repositorio en `index.html`
Al agregar la URL de GitHub Pages en el Gestor de Archivos de Kodi (`https://sonvice.github.io/repository.sonvice/`), la página [`index.html`](file:///home/wilson/Pictures/plugin.video.stremio4kodi_v3.2.3/repository.sonvice/index.html) lista en **primer lugar** el archivo `repository.sonvice-X.X.X.zip` etiquetado como `Repositorio (Recomendado)`.

* **Motivo técnico crítico:** El motor VFS de Kodi (`zip://https://...`) **no es un gestor de descargas**. Si un usuario intenta instalar un addon pesado (>50 archivos) directamente desde un enlace ZIP remoto en "Instalar desde un archivo .zip", Kodi abre peticiones Range HTTP separadas para cada archivo y directorio, saturando el socket y arrojando el error `Failed to unpack archive`.
* **Flujo correcto:** El usuario instala primero el repositorio (`repository.sonvice-X.X.X.zip`, 2 ficheros, 0.5s) y luego instala el addon desde el repositorio oficial de Kodi, lo cual descarga el archivo completo a `special://home/addons/packages/` y lo extrae localmente a máxima velocidad, habilitando además las actualizaciones automáticas.

### 6.2. Reglas del Empaquetador (`generator.py`)
* **Entradas de Directorio Explícitas:** El empaquetador genera entradas `ZipInfo` con barra final (`dir/`) para cada subcarpeta, asegurando que el unzipper de Kodi reconozca la estructura de directorios en disco.
* **Exclusión de Archivos Innecesarios:** Se descartan de los paquetes finales las carpetas `.git`, `.github`, `.antigravitycli`, `__pycache__`, y archivos de desarrollo como `.gitignore`, `*.md` (`README.md`, `AGENTS.md`) y `.pdf`.
