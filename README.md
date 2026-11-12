# Repositorio Oficial Sonvice para Kodi (`repository.sonvice`)

[![Kodi Versions](https://img.shields.io/badge/Kodi-19%20|%2020%20|%2021%20(Matrix%20/%20Nexus%20/%20Omega)-blue.svg)](https://kodi.tv)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Latest Version](https://img.shields.io/badge/Repository-v1.0.11-success.svg)](https://github.com/sonvice/repository.sonvice/releases)

Repositorio oficial para indexar, distribuir y actualizar de forma automatica los complementos de Sonvice en Kodi, incluyendo **Stremio for Kodi** (`plugin.video.stremio4kodi`), en todas las plataformas compatibles (Android TV, Google TV, Fire TV Stick, CoreELEC, LibreELEC, Linux, Windows y macOS).

Distribucion optimizada a traves de GitHub Pages con CDN global de baja latencia para garantizar maxima disponibilidad frente a bloqueos de operadoras.

---

## Indice de Contenidos

1. [Por Que Instalar el Repositorio Primero (Fundamento Tecnico)](#por-que-instalar-el-repositorio-primero-fundamento-tecnico)
2. [Politica de Retencion de Versiones (Dual-Version)](#politica-de-retencion-de-versiones-dual-version)
3. [Guia Didactica de Instalacion Paso a Paso](#guia-didactica-de-instalacion-paso-a-paso)
4. [Como Forzar la Comprobacion de Actualizaciones (Solucion de Problemas)](#como-forzar-la-comprobacion-de-actualizaciones-solucion-de-problemas)
5. [Complementos Incluidos](#complementos-incluidos)
6. [Guia de Compilacion para Desarrolladores (`generator.py`)](#guia-de-compilacion-para-desarrolladores-generatorpy)

---

## Por Que Instalar el Repositorio Primero (Fundamento Tecnico)

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

## Politica de Retencion de Versiones (Dual-Version)

A fin de mantener la maxima estabilidad en todo tipo de dispositivos, el repositorio mantiene intencionadamente **unicamente dos versiones simultaneas** de Stremio for Kodi:

1. **Ultima Version Estable (`v4.1.x` - Recomendada):**
   * Incorpora el orquestador MediaCore (busqueda simultanea en Stremio, Torznab, DHT y AceStream).
   * Motor de clasificacion inteligente **Spanish Booster** (priorizacion de enlaces en Castellano, Dual y Latino).
   * Home Moderna unificada y Widgets exportables a cualquier skin de Kodi.
   * Configuracion remota desde el telefono movil mediante codigo QR y Web UI local.
2. **Version Antigua / Clasica (`v3.7.33`):**
   * Version monolitica clasica sin dependencias complejas, conservada permanentemente para dispositivos de muy bajos recursos o usuarios que prefieran la interfaz tradicional de menus directos de Stremio.

El script empaquetador del repositorio elimina de forma automatica versiones intermedias para evitar confusiones al usuario.

---

## Guia Didactica de Instalacion Paso a Paso

### Paso 1: Habilitar Origenes Desconocidos
1. Abre Kodi y haz clic en el icono de **Ajustes** (icono de engranaje en la parte superior izquierda).
2. Entra en **Sistema** y selecciona en el panel izquierdo la pestana **Add-ons**.
3. Activa la casilla **Origenes desconocidos**.
4. Pulsa **Si** en el mensaje de advertencia de seguridad.

### Paso 2: Registrar la URL del Repositorio en el Gestor de Archivos
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

### Paso 3: Instalar el Repositorio desde el archivo ZIP
1. Regresa al menu principal de Kodi y entra en el apartado **Add-ons**.
2. Haz clic en el icono de la caja abierta (**Explorador de complementos**) situado en la esquina superior izquierda.
3. Elige la opcion **Instalar desde un archivo .zip**.
4. Selecciona la fuente registrada: **Sonvice Repo**.
5. Selecciona el archivo del repositorio:
   ```text
   repository.sonvice-1.0.11.zip
   ```
6. Aguarda unos instantes hasta que aparezca la notificacion: **Sonvice Repository Complemento instalado**.

### Paso 4: Instalar Stremio for Kodi
1. En el mismo menu del Explorador de complementos, selecciona **Instalar desde repositorio**.
2. Elige **Sonvice Repository**.
3. Entra en **Complementos para video**.
4. Selecciona **Stremio for Kodi** y haz clic en el boton **Instalar** (abajo a la derecha).
5. Confirma las dependencias requeridas pulsando **OK**.

---

## Como Forzar la Comprobacion de Actualizaciones (Solucion de Problemas)

### Sintoma
Has instalado el repositorio, pero al entrar a ver las versiones disponibles no aparece la nueva version v4 o Kodi muestra que esta actualizado pero continua ejecutando la version anterior.

### Causa
Kodi almacena en una base de datos local interna (`Addons33.db` en SQLite) el indice de complementos para no saturar los servidores con peticiones constantes. Por defecto, Kodi revisa si hay versiones nuevas en los repositorios una vez cada 24 horas.

### Solucion: Forzar la Actualizacion Inmediata
1. Entra en **Add-ons** ➔ **Instalar desde repositorio**.
2. Resalta con el cursor la entrada **Sonvice Repository** (sin hacer clic para entrar en ella).
3. Abre el **Menu contextual**:
   * **En mando de TV / Android TV / FireStick:** Manten pulsado el boton central (OK) o presiona el boton con tres lineas horizontales (Menu).
   * **En ordenador (PC / Mac):** Haz clic con el boton derecho del raton o pulsa la tecla `C` del teclado.
   * **En dispositivos tactiles (Movil / Tablet):** Manten pulsado sobre el nombre del repositorio.
4. En el menu emergente que aparece, pulsa en **Comprobar actualizaciones** (Check for updates).
5. Kodi contactara de inmediato con el servidor CDN, leera el indice `addons.xml` mas reciente y descargara la actualizacion a la version mas reciente.

---

## Complementos Incluidos

| Identificador | Complemento | Descripcion |
| :--- | :--- | :--- |
| `repository.sonvice` | **Sonvice Repository** | Repositorio oficial para recibir correcciones y actualizaciones automaticas. |
| `plugin.video.stremio4kodi` | **Stremio for Kodi** | Orquestador multimedia con soporte para Stremio, Torznab, Real-Debrid, TorrServer y AceStream. |
| `service.subtitles.opensubtitles-stremio` | **OpenSubtitles v3** | Servicio de subtitulos automaticos y gratuitos sin registro para el reproductor de Kodi. |

---

## Guia de Compilacion para Desarrolladores (`generator.py`)

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

El script empaquetador genera automaticamente entradas `ZipInfo` con formato de directorio explicito (`dir/`) para garantizar compatibilidad con el motor de descompresion nativo de Kodi y descarta archivos no necesarios para produccion (`.git`, `__pycache__`, ficheros `.md`, etc.).

---

## Licencia

Distribuido bajo licencia **MIT License**. Consulta el archivo `LICENSE` para mas detalles.
