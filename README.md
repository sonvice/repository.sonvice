# Official Sonvice Kodi Repository (`repository.sonvice`)

[![Kodi Versions](https://img.shields.io/badge/Kodi-19%20|%2020%20|%2021%20(Matrix%20/%20Nexus%20/%20Omega)-blue.svg)](https://kodi.tv)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Latest Version](https://img.shields.io/badge/Repository-v1.0.11-success.svg)](https://github.com/sonvice/repository.sonvice/releases)

Official Kodi repository to index, distribute, and automatically update Sonvice addons, including **Stremio for Kodi** (`plugin.video.stremio4kodi`), across all supported platforms (Android TV, Google TV, Fire TV Stick, CoreELEC, LibreELEC, Linux, Windows, macOS).

Served via GitHub Pages with a global Fastly CDN to bypass ISP censorship and quota restrictions.

---

[ English ](#english) | [ Español ](#español)

---

<a name="english"></a>
## English

### Table of Contents
1. [Why You Must Install the Repository First (Technical Explanation)](#why-you-must-install-the-repository-first)
2. [Dual-Version Retention Policy](#dual-version-retention-policy-en)
3. [Didactic Step-by-Step Installation Guide](#didactic-step-by-step-installation-guide-en)
4. [How to Force an Update Check (Troubleshooting)](#how-to-force-an-update-check-en)
5. [Included Addons](#included-addons-en)
6. [Developer Packaging Guide (`generator.py`)](#developer-packaging-guide-en)

---

<a name="why-you-must-install-the-repository-first"></a>
### Why You Must Install the Repository First (Technical Explanation)

Kodi's Virtual File System (`zip://https://...`) **does not operate like a traditional browser or download manager**:

* **The Common Mistake:** If a user attempts to install a full video addon (such as Stremio for Kodi, which contains more than 70 internal files and packages) by clicking directly on its remote `.zip` file inside *"Install from zip file"*, Kodi opens individual partial HTTP Range requests for each directory and file. On Android TV, Fire TV Stick, or weak Wi-Fi networks, this quickly saturates Kodi's socket pool and throws the error:
  ```text
  Failed to unpack archive
  ```
* **The Correct Solution:** The repository file (`repository.sonvice-1.0.11.zip`) contains only two files and weighs less than 30 KB, downloading in under 0.5 seconds over any connection. Once the repository is installed in Kodi:
  1. Kodi downloads the complete addon ZIP to local disk storage (`special://home/addons/packages/`).
  2. Extraction is performed locally at maximum bus speed without socket timeouts.
  3. **Silent background automatic updates** are permanently enabled.

---

<a name="dual-version-retention-policy-en"></a>
### Dual-Version Retention Policy

To maintain maximum stability across diverse hardware, the repository intentionally maintains **only two versions** of Stremio for Kodi:

1. **Latest Stable Version (`v4.1.x` - Recommended):**
   * Features the MediaCore orchestrator, Modern Streaming Home, Spanish Booster scoring engine, and QR Mobile Setup.
2. **Classic / Legacy Version (`v3.7.33`):**
   * Lightweight monolithic version preserved for low-spec devices or users who prefer direct Stremio menu navigation.

The automated repository packaging script cleans up intermediate versions to ensure a clear choice for users.

---

<a name="didactic-step-by-step-installation-guide-en"></a>
### Didactic Step-by-Step Installation Guide

#### Step 1: Enable Unknown Sources
1. Open Kodi and click the **Settings** icon (gear icon on the top-left).
2. Select **System** and navigate to the **Add-ons** tab on the left.
3. Toggle on **Unknown sources**.
4. Confirm the prompt by selecting **Yes**.

#### Step 2: Register the Repository Source
1. Return to the **Settings** menu and click **File manager**.
2. Select **Add source**.
3. Click on the `<None>` field and enter the exact URL:
   ```text
   https://sonvice.github.io/repository.sonvice/
   ```
4. In the name box below, enter an easy identifier, for example:
   ```text
   Sonvice Repo
   ```
5. Click **OK** to save the source.

#### Step 3: Install the Repository from ZIP
1. Return to Kodi's home screen and open the **Add-ons** section.
2. Click the open box icon (**Add-on browser**) at the top-left.
3. Select **Install from zip file**.
4. Choose **Sonvice Repo**.
5. Select the repository package:
   ```text
   repository.sonvice-1.0.11.zip
   ```
6. Wait a few seconds until the notification appears: **Sonvice Repository Add-on installed**.

#### Step 4: Install Stremio for Kodi
1. In the same Add-on browser menu, select **Install from repository**.
2. Select **Sonvice Repository**.
3. Open **Video add-ons**.
4. Select **Stremio for Kodi** and click **Install** on the bottom-right.
5. Confirm any required dependencies by clicking **OK**.

---

<a name="how-to-force-an-update-check-en"></a>
### How to Force an Update Check (Troubleshooting)

#### Symptom
You have installed the repository, but when checking available addon versions, Kodi does not show the v4 update or reports that it is updated while still running the older version.

#### Cause
Kodi caches addon repository indexes in a local SQLite database (`Addons33.db`) to avoid repeated network requests. By default, Kodi only re-checks remote repositories once every 24 hours.

#### Solution: Force an Immediate Check
1. Go to **Add-ons** ➔ **Install from repository**.
2. Highlight **Sonvice Repository** (do not click to enter).
3. Open the **Context Menu**:
   * TV Remote / FireStick: Long-press the OK/Center button or press the Menu button (three horizontal lines).
   * PC / Mac: Right-click with your mouse or press the `C` key.
   * Touchscreen: Press and hold on the repository name.
4. From the popup menu, select **Check for updates**.
5. Kodi immediately queries the CDN, updates its index, and displays the update notification.

---

<a name="included-addons-en"></a>
### Included Addons

| Addon ID | Name | Description |
| :--- | :--- | :--- |
| `repository.sonvice` | **Sonvice Repository** | Official repository for automatic background updates. |
| `plugin.video.stremio4kodi` | **Stremio for Kodi** | Modular orchestrator with support for Stremio, Torznab, Real-Debrid, TorrServer, and AceStream. |
| `service.subtitles.opensubtitles-stremio` | **OpenSubtitles v3** | Free, zero-configuration subtitle service for the Kodi player. |

---

<a name="developer-packaging-guide-en"></a>
### Developer Packaging Guide (`generator.py`)

Repository indexing and ZIP distribution is fully automated via `generator.py`:

```bash
# 1. Update the version number in addon.xml (e.g. plugin.video.stremio4kodi/addon.xml)
# 2. Run the packaging generator:
python3 generator.py

# 3. Verify updated indexes (repo/addons.xml and repo/addons.xml.md5)
# 4. Commit and push:
git add -A
git commit -m "Publish version X.Y.Z"
git push origin main
```

---

<a name="español"></a>
## Español

### Indice de Contenidos
1. [Por Que Instalar el Repositorio Primero (Fundamento Tecnico)](#por-que-instalar-el-repositorio-primero-es)
2. [Politica de Retencion de Versiones (Dual-Version)](#politica-de-retencion-de-versiones-dual-version-es)
3. [Guia Didactica de Instalacion Paso a Paso](#guia-didactica-de-instalacion-paso-a-paso-es)
4. [Como Forzar la Comprobacion de Actualizaciones (Solucion de Problemas)](#como-forzar-la-comprobacion-de-actualizaciones-es)
5. [Complementos Incluidos](#complementos-incluidos-es)
6. [Guia de Compilacion para Desarrolladores (`generator.py`)](#guia-de-compilacion-para-desarrolladores-es)

---

<a name="por-que-instalar-el-repositorio-primero-es"></a>
### Por Que Instalar el Repositorio Primero (Fundamento Tecnico)

El sistema de archivos virtuales de Kodi (VFS) al tratar con rutas remotas (`zip://https://...`) **no se comporta como un navegador o gestor de descargas tradicional**:

* **El error comun:** Si un usuario intenta instalar un addon complejo (como Stremio4Kodi, que contiene mas de 70 archivos y librerias internas) seleccionando directamente el archivo `.zip` remoto en la opcion *"Instalar desde un archivo .zip"*, el motor VFS de Kodi abre conexiones HTTP parciales (Range Requests) separadas para cada directorio y fichero. En sistemas como Android TV, Fire TV Stick o routers domesticos, este comportamiento satura el numero de sockets abiertos y Kodi muestra el siguiente error:
  ```text
  Fallo al descomprimir el archivo (Failed to unpack archive)
  ```
* **La solucion correcta:** El archivo del repositorio (`repository.sonvice-1.0.11.zip`) contiene unicamente dos ficheros ligeros y pesa menos de 30 KB, por lo que se instala de forma instantanea (menos de 0.5 segundos) a traves de la red. Una vez instalado el repositorio en Kodi:
  1. Kodi descarga el archivo ZIP completo directamente al almacenamiento temporal local (`special://home/addons/packages/`).
  2. La extraccion se realiza en local a maxima velocidad sin cuellos de botella de red.
  3. Se activan las **actualizaciones automaticas silenciosas en segundo plano**.

---

<a name="politica-de-retencion-de-versiones-dual-version-es"></a>
### Politica de Retencion de Versiones (Dual-Version)

A fin de mantener la maxima estabilidad en todo tipo de dispositivos, el repositorio mantiene intencionadamente **unicamente dos versiones simultaneas** de Stremio for Kodi:

1. **Ultima Version Estable (`v4.1.x` - Recomendada):**
   * Incorpora el orquestador MediaCore (busqueda simultanea en Stremio, Torznab, DHT y AceStream).
   * Motor de clasificacion inteligente **Spanish Booster** (priorizacion de enlaces en Castellano, Dual y Latino).
   * Home Moderna unificada y Widgets exportables a cualquier skin de Kodi.
   * Configuracion remota desde el telefono movil mediante codigo QR y Web UI local.
2. **Version Antigua / Clasica (`v3.7.33`):**
   * Version monolitica clasica sin dependencias complejas, conservada permanentemente para dispositivos de muy bajos recursos o usuarios que prefieran la interfaz tradicional de menus directos de Stremio.

---

<a name="guia-didactica-de-instalacion-paso-a-paso-es"></a>
### Guia Didactica de Instalacion Paso a Paso

#### Paso 1: Habilitar Origenes Desconocidos
1. Abre Kodi y haz clic en el icono de **Ajustes** (icono de engranaje en la parte superior izquierda).
2. Entra en **Sistema** y selecciona en el panel izquierdo la pestana **Add-ons**.
3. Activa la casilla **Origenes desconocidos**.
4. Pulsa **Si** en el mensaje de advertencia de seguridad.

#### Paso 2: Registrar la URL del Repositorio en el Gestor de Archivos
1. Regresa al menu de **Ajustes** y entra en **Explorador de archivos**.
2. Selecciona **Anadir fuente**.
3. Haz clic sobre el campo `<Ninguno>` y escribe con exactitud:
   ```text
   https://sonvice.github.io/repository.sonvice/
   ```
4. En el campo de nombre inferior, introduce un identificador claro, por ejemplo:
   ```text
   Sonvice Repo
   ```
5. Pulsa **OK** para registrar la fuente.

#### Paso 3: Instalar el Repositorio desde el archivo ZIP
1. Regresa al menu principal de Kodi y entra en el apartado **Add-ons**.
2. Haz clic en el icono de la caja abierta (**Explorador de complementos**) situado en la esquina superior izquierda.
3. Elige la opcion **Instalar desde un archivo .zip**.
4. Selecciona la fuente registrada: **Sonvice Repo**.
5. Selecciona el archivo del repositorio:
   ```text
   repository.sonvice-1.0.11.zip
   ```
6. Aguarda unos instantes hasta que aparezca la notificacion: **Sonvice Repository Complemento instalado**.

#### Paso 4: Instalar Stremio for Kodi
1. En el mismo menu del Explorador de complementos, selecciona **Instalar desde repositorio**.
2. Elige **Sonvice Repository**.
3. Entra en **Complementos para video**.
4. Selecciona **Stremio for Kodi** y haz clic en el boton **Instalar** (abajo a la derecha).
5. Confirma las dependencias requeridas pulsando **OK**.

---

<a name="como-forzar-la-comprobacion-de-actualizaciones-es"></a>
### Como Forzar la Comprobacion de Actualizaciones (Solucion de Problemas)

#### Sintoma
Has instalado el repositorio, pero al entrar a ver las versiones disponibles no aparece la nueva version v4 o Kodi muestra que esta actualizado pero continua ejecutando la version anterior.

#### Causa
Kodi almacena en una base de datos local interna (`Addons33.db` en SQLite) el indice de complementos para no saturar los servidores con peticiones constantes. Por defecto, Kodi revisa si hay versiones nuevas en los repositorios una vez cada 24 horas.

#### Solucion: Forzar la Actualizacion Inmediata
1. Entra en **Add-ons** ➔ **Instalar desde repositorio**.
2. Resalta con el cursor la entrada **Sonvice Repository** (sin hacer clic para entrar en ella).
3. Abre el **Menu contextual**:
   * **En mando de TV / Android TV / FireStick:** Manten pulsado el boton central (OK) o presiona el boton con tres lineas horizontales (Menu).
   * **En ordenador (PC / Mac):** Haz clic con el boton derecho del raton o pulsa la tecla `C` del teclado.
   * **En dispositivos tactiles (Movil / Tablet):** Manten pulsado sobre el nombre del repositorio.
4. En el menu emergente que aparece, pulsa en **Comprobar actualizaciones** (Check for updates).
5. Kodi contactara de inmediato con el servidor CDN, leera el indice `addons.xml` mas reciente y descargara la actualizacion a la version mas reciente.

---

<a name="complementos-incluidos-es"></a>
### Complementos Incluidos

| Identificador | Complemento | Descripcion |
| :--- | :--- | :--- |
| `repository.sonvice` | **Sonvice Repository** | Repositorio oficial para recibir correcciones y actualizaciones automaticas. |
| `plugin.video.stremio4kodi` | **Stremio for Kodi** | Orquestador multimedia con soporte para Stremio, Torznab, Real-Debrid, TorrServer y AceStream. |
| `service.subtitles.opensubtitles-stremio` | **OpenSubtitles v3** | Servicio de subtitulos automaticos y gratuitos sin registro para el reproductor de Kodi. |

---

<a name="guia-de-compilacion-para-desarrolladores-es"></a>
### Guia de Compilacion para Desarrolladores (`generator.py`)

El mantenimiento y empaquetado del repositorio esta automatizado mediante el script Python `generator.py`:

```bash
# 1. Modificar el codigo o subir la version en addon.xml (ej. plugin.video.stremio4kodi/addon.xml)
# 2. Ejecutar el generador desde la raiz del repositorio:
python3 generator.py

# 3. Comprobar que los archivos de indice (repo/addons.xml y repo/addons.xml.md5) se han actualizado
# 4. Confirmar y subir a GitHub:
git add -A
git commit -m "Publish version X.Y.Z"
git push origin main
```

---

## License / Licencia

Distributed under the **MIT License**. See `LICENSE` for more information.
