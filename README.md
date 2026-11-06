<div align="center">

# 📦 Sonvice Kodi Repository

[![Kodi Versions](https://img.shields.io/badge/Kodi-19%20|%2020%20|%2021%20(Matrix%20/%20Nexus%20/%20Omega)-blue.svg)](https://kodi.tv)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Latest Version](https://img.shields.io/badge/Repository-v1.0.10-success.svg)](https://github.com/sonvice/repository.sonvice/releases)

**Official Kodi repository for Sonvice addons.**  
Install, manage, and automatically receive updates for high-performance Kodi addons including **Stremio for Kodi** across all platforms (Android, CoreELEC, Linux, Windows, macOS).

---

[ 🇬🇧 **English** ](#-english) &nbsp; | &nbsp; [ 🇪🇸 **Español** ](#-español)

---

</div>

<a name="-english"></a>
## 🇬🇧 English

### 🌟 Features & Included Add-ons

* **[Stremio for Kodi (`plugin.video.stremio4kodi`)](https://github.com/sonvice/repository.sonvice):** Seamless Stremio library integration for Kodi, multi-platform torrent streaming (Elementum support on Android/Linux/CoreELEC), AceStream live sports integration, subtitle auto-fetching, and high-performance playback.
* **Automatic Background Updates:** Once installed, all Sonvice addons receive updates automatically via our low-latency CDN (jsDelivr / GitHub).
* **Multi-Platform Support:** Compatible with Android (TV/Mobile), CoreELEC / LibreELEC, Linux, Windows, and macOS running Kodi 19+ (Matrix, Nexus, Omega).

---

### ⚙️ Prerequisites (Enable Unknown Sources)

Before installing any third-party repository in Kodi, ensure external sources are allowed:

1. Launch **Kodi** and open **Settings** (gear icon ⚙️ on the top left).
2. Go to **System** ➔ **Add-ons**.
3. Toggle on **Unknown sources**.
4. Confirm the prompt by selecting **Yes**.

---

### 📥 Installation Methods

Choose the method that works best for your device:

#### Method 1: Via Kodi File Manager (Recommended for Smart TVs & TV Boxes)

This method requires no web browser or external USB drive.

1. In Kodi, go to **Settings (⚙️)** ➔ **File manager**.
2. Select **Add source**.
3. Click on `<None>` and enter the exact URL:
   ```text
   https://sonvice.github.io/repository.sonvice/
   ```
4. Enter a name for this media source (e.g., `Sonvice Repo`) and select **OK**.
5. Return to the Kodi Home Screen and select **Add-ons**.
6. Click the open box icon (**Add-on Browser**) at the top left.
7. Select **Install from zip file** (select `Yes` if warned).
8. Choose **Sonvice Repo** (the source name you created).
9. Select **`repository.sonvice-1.0.10.zip`**.
10. Wait a few seconds until you see the **Sonvice Repository Add-on installed** notification.

---

#### Method 2: Direct ZIP Download (PC & Mobile)

If you have a browser or access to your device's filesystem:

1. Download the latest repository ZIP file directly:  
   👉 [**Download repository.sonvice-1.0.10.zip**](https://cdn.jsdelivr.net/gh/sonvice/repository.sonvice@main/repo/repository.sonvice/repository.sonvice-1.0.10.zip)  
   *(Alternative mirror: [GitHub Raw](https://raw.githubusercontent.com/sonvice/repository.sonvice/main/repo/repository.sonvice/repository.sonvice-1.0.10.zip))*
2. Open Kodi ➔ **Add-ons** ➔ **Add-on Browser** (open box icon).
3. Select **Install from zip file**.
4. Navigate to your **Downloads** folder, choose `repository.sonvice-1.0.10.zip`, and click **OK**.

---

### 🚀 Installing Add-ons from the Repository

Once the repository is installed, adding plugins is quick and simple:

1. Open Kodi and navigate to **Add-ons**.
2. Click the **Add-on Browser** icon (open box at top left).
3. Select **Install from repository**.
4. Choose **Sonvice Repository**.
5. Go to **Video add-ons**.
6. Select **Stremio for Kodi** and click **Install**.
7. Confirm any required dependencies by clicking **OK**.

---

### 🛠️ Developer Guide: Publishing Updates

This repository includes an automated build tool (`generator.py`) to index and package releases:

```bash
# 1. Update the version number in the addon's addon.xml (e.g., plugin.video.stremio4kodi)
# 2. Rebuild repository packages and indexes
python3 generator.py

# 3. Commit and push the generated files to GitHub
git add -A
git commit -m "Release vX.Y.Z: update summary"
git push origin main

# 4. Purge jsDelivr CDN cache for instant global synchronization
curl -s "https://purge.jsdelivr.net/gh/sonvice/repository.sonvice@main/repo/addons.xml"
curl -s "https://purge.jsdelivr.net/gh/sonvice/repository.sonvice@main/repo/addons.xml.md5"
```

---

<a name="-español"></a>
## 🇪🇸 Español

### 🌟 Características y Complementos Incluidos

* **[Stremio for Kodi (`plugin.video.stremio4kodi`)](https://github.com/sonvice/repository.sonvice):** Integración fluida de tu catálogo de Stremio en Kodi, reproducción torrent multiplataforma (soporte integrado para Elementum en Android/Linux/CoreELEC), compatibilidad con emisiones en vivo por AceStream, descarga automática de subtítulos y máxima estabilidad.
* **Actualizaciones Automáticas en Segundo Plano:** Una vez instalado el repositorio, todos los complementos de Sonvice se actualizarán de forma transparente a través de nuestra red CDN optimizada (jsDelivr / GitHub).
* **Compatibilidad Multiplataforma:** Compatible con Android (TV / Móvil), CoreELEC / LibreELEC, Linux, Windows y macOS bajo Kodi 19 o superior (Matrix, Nexus, Omega).

---

### ⚙️ Requisito Previo (Activar Orígenes Desconocidos)

Antes de instalar cualquier repositorio externo en Kodi, asegúrate de habilitar esta opción:

1. Abre **Kodi** y pulsa en **Ajustes** (icono del engranaje ⚙️ arriba a la izquierda).
2. Entra en **Sistema** ➔ **Add-ons** (Complementos).
3. Activa la opción **Orígenes desconocidos**.
4. En el cuadro de aviso que aparece, pulsa **Sí**.

---

### 📥 Métodos de Instalación

Elige el método que mejor se adapte a tu dispositivo:

#### Método 1: Desde el Gestor de Archivos de Kodi (Recomendado para Smart TV y TV Box)

Este método no requiere navegador web ni pendrive USB:

1. En Kodi, ve a **Ajustes (⚙️)** ➔ **Explorador de archivos** (Gestor de archivos).
2. Haz clic en **Añadir fuente**.
3. Pulsa sobre `<Ninguno>` e introduce exactamente esta dirección:
   ```text
   https://sonvice.github.io/repository.sonvice/
   ```
4. Escribe un nombre para identificar la fuente (por ejemplo: `Sonvice Repo`) y pulsa **OK**.
5. Regresa al menú principal de Kodi y entra en **Add-ons**.
6. Pulsa en el icono de la caja abierta (**Explorador de complementos**) arriba a la izquierda.
7. Selecciona **Instalar desde un archivo .zip** (confirma con `Sí` si te muestra advertencia).
8. Selecciona **Sonvice Repo** (la fuente que creaste en el paso 4).
9. Elige el archivo **`repository.sonvice-1.0.10.zip`**.
10. Espera unos segundos hasta que aparezca la notificación: **Sonvice Repository Complemento instalado**.

---

#### Método 2: Descarga Directa del archivo ZIP (PC y Móviles)

Si cuentas con navegador web o gestor de descargas en tu dispositivo:

1. Descarga directamente el archivo ZIP del repositorio:  
   👉 [**Descargar repository.sonvice-1.0.10.zip**](https://cdn.jsdelivr.net/gh/sonvice/repository.sonvice@main/repo/repository.sonvice/repository.sonvice-1.0.10.zip)  
   *(Enlace alternativo: [GitHub Raw](https://raw.githubusercontent.com/sonvice/repository.sonvice/main/repo/repository.sonvice/repository.sonvice-1.0.10.zip))*
2. Abre Kodi ➔ **Add-ons** ➔ **Explorador de complementos** (icono de la caja abierta).
3. Selecciona **Instalar desde un archivo .zip**.
4. Navega hasta tu carpeta de **Descargas**, selecciona `repository.sonvice-1.0.10.zip` y pulsa **OK**.

---

### 🚀 Cómo Instalar Complementos desde el Repositorio

Una vez instalado el repositorio, agregar los addons es muy sencillo:

1. En Kodi, ve a **Add-ons**.
2. Pulsa en el **Explorador de complementos** (icono de la caja abierta).
3. Selecciona **Instalar desde repositorio**.
4. Entra en **Sonvice Repository**.
5. Selecciona la categoría **Complementos para vídeo**.
6. Elige **Stremio for Kodi** y pulsa en **Instalar**.
7. Si te solicita instalar dependencias complementarias, confirma con **OK**.

---

### 🛠️ Guía para Desarrolladores: Publicación de Actualizaciones

El repositorio incluye un script automatizado (`generator.py`) para empaquetar e indexar nuevas versiones:

```bash
# 1. Modifica la versión en el addon.xml del complemento correspondiente (ej. plugin.video.stremio4kodi)
# 2. Genera los paquetes ZIP y regenera los índices del repositorio
python3 generator.py

# 3. Sube los cambios generados al repositorio GitHub
git add -A
git commit -m "Publicar vX.Y.Z: resumen de cambios"
git push origin main

# 4. Purga la caché de jsDelivr para sincronización inmediata a nivel mundial
curl -s "https://purge.jsdelivr.net/gh/sonvice/repository.sonvice@main/repo/addons.xml"
curl -s "https://purge.jsdelivr.net/gh/sonvice/repository.sonvice@main/repo/addons.xml.md5"
```

---

## 📄 License / Licencia

Distributed under the **MIT License**.
