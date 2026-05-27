# Sonvice Kodi Repository

Este es el repositorio oficial de addons de **Sonvice** para Kodi. Aloja e indexa complementos de forma remota, permitiendo instalarlos y mantenerlos actualizados automáticamente en cualquier dispositivo (Android, CoreELEC, Windows, etc.).

---

## 📥 Cómo Instalar el Repositorio en Kodi

Para agregar este repositorio a tu Kodi y poder instalar los complementos, sigue estos pasos:

1. **Descarga el archivo ZIP del repositorio** en tu dispositivo usando el siguiente enlace:
   [**Descargar repository.sonvice-1.0.0.zip**](https://raw.githubusercontent.com/sonvice/repository.sonvice/main/repo/repository.sonvice/repository.sonvice-1.0.0.zip?v=2)
   
   *(Dirección directa para navegadores o Kodi: `https://raw.githubusercontent.com/sonvice/repository.sonvice/main/repo/repository.sonvice/repository.sonvice-1.0.0.zip?v=2`)*

2. Abre Kodi y ve a **Ajustes** -> **Sistema** -> **Add-ons** (Complementos) y asegúrate de tener activada la opción **Orígenes desconocidos**.

3. Vuelve a la pantalla de **Add-ons** y haz clic en el icono de la caja abierta (**Explorador de complementos**).

4. Selecciona **Instalar desde un archivo .zip**.

5. Busca y selecciona el archivo `repository.sonvice-1.0.0.zip` que acabas de descargar.

¡Listo! Verás una notificación confirmando que **Sonvice Repository** se ha instalado con éxito.

---

## 🚀 Cómo Instalar Addons desde el Repositorio

Una vez instalado el repositorio, puedes instalar sus addons y recibirán actualizaciones automáticas en segundo plano:

1. Ve a **Explorador de complementos** -> **Instalar desde repositorio**.
2. Selecciona **Sonvice Repository**.
3. Entra en **Complementos de video** (o la categoría correspondiente).
4. Selecciona **Stremio for Kodi** y haz clic en **Instalar**.

---

## 🛠️ Desarrollo: Cómo publicar actualizaciones (Para el Autor)

Este repositorio cuenta con un script automatizado `generator.py` que simplifica enormemente la publicación de nuevas versiones.

### Flujo de trabajo para actualizar un addon:

1. Realiza las modificaciones pertinentes en la carpeta de tu addon (ej: `plugin.video.stremio4kodi`).
2. Sube el número de versión en el archivo `addon.xml` de dicho addon (ej: de `3.2.3` a `3.2.4`).
3. Abre tu terminal en la carpeta raíz de este repositorio (`repository.sonvice`) y ejecuta el generador:
   ```bash
   python3 generator.py
   ```
   *(El script reconstruirá automáticamente los paquetes ZIP actualizados y regenerará los índices `addons.xml` y `addons.xml.md5` correspondientes).*
4. Sube los cambios generados a GitHub:
   ```bash
   git add .
   git commit -m "Publicar actualización del addon a v3.2.4"
   git push
   ```

Una vez subido, todos los dispositivos remotos que tengan el repositorio instalado recibirán de forma transparente y automática la nueva versión en segundo plano.
