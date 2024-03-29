# OCR App - Reconocimiento Óptico de Caracteres (Imagen a Texto)

Esta es una aplicación simple de reconocimiento óptico de caracteres (OCR) creada en Python con la interfaz gráfica de usuario (GUI) proporcionada por Tkinter. La aplicación utiliza la biblioteca Tesseract para realizar OCR en imágenes seleccionadas y convierte el texto reconocido en un archivo de texto.

## 🚀 Instrucciones de Uso

1. **Descargar Tesseract:**
   Asegúrate de tener Tesseract instalado en tu sistema. Puedes descargarlo [aquí](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe).

2. **Ejecutar la Aplicación:**
   Ejecuta el script proporcionado y la interfaz de usuario se abrirá.

3. **Seleccionar una Imagen:**
   Utiliza el botón "Seleccionar Imagen" 📷 para elegir una imagen en los formatos admitidos (png, jpg, jpeg, gif). La imagen seleccionada se mostrará en un lienzo.

4. **Convertir a Texto:**
   Después de seleccionar una imagen, haz clic en "Convertir a Texto" 🔄. Ingresa un nombre para el archivo de texto resultante cuando se te solicite.

5. **Resultado OCR:**
   La aplicación realizará OCR en la imagen, guardará el texto en un archivo de texto y mostrará el resultado en una nueva ventana junto con la imagen procesada.

## ⚙️ Requisitos

- Python 3.x
- Tkinter
- OpenCV
- Pillow (PIL)
- Tesseract

## 🛠️ Configuración

Asegúrate de ajustar la variable `ruta_del_motor_tesseract` en el script con la ruta correcta de tu ejecutable de Tesseract.

```python
ruta_del_motor_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```
## 📚 Bibliotecas Utilizadas

Este proyecto utiliza las siguientes bibliotecas y módulos de Python:

- **Tkinter:** Biblioteca estándar de Python para la creación de interfaces gráficas de usuario (GUI).
- **Pillow (PIL):** Biblioteca para manipulación de imágenes.
- **Pytesseract:** Herramienta de OCR (Reconocimiento Óptico de Caracteres) que utiliza Tesseract.
- **OpenCV:** Biblioteca de visión por computadora para procesamiento de imágenes.
- **Matplotlib:** Biblioteca para la visualización de gráficos y figuras.
- **OS:** Módulo para interactuar con el sistema operativo, utilizado para limpiar la pantalla en sistemas operativos Windows.

Ten en cuenta que puedes necesitar instalar estas bibliotecas antes de ejecutar la aplicación. Puedes instalarlas usando `pip`. Por ejemplo:
```python
pip install pillow pytesseract opencv-python matplotlib
```
## 📝 Notas

- La aplicación es compatible con imágenes en formato png, jpg, jpeg y gif.
- Asegúrate de proporcionar un nombre al archivo de texto al realizar la conversión.

## 📷 Imágenes de Ejecución

### Imagen a la que vamos extraer el texto
![Paso 1 - Seleccionar Imagen](https://github.com/DannyCrisostomo/Reconocimiento-Optico-de-Caracteres/blob/35a447865f35b54b3cafa0d93155f27d015270df/Ejecucion%20del%20programa/imagen.png)

### Interfaz Principal
![Interfaz Principal](https://github.com/DannyCrisostomo/Reconocimiento-Optico-de-Caracteres/blob/35a447865f35b54b3cafa0d93155f27d015270df/Ejecucion%20del%20programa/Interfaz%20principal.png)

### Interfaz Secundaria (Resultado OCR)
![Interfaz Secundaria](https://github.com/DannyCrisostomo/Reconocimiento-Optico-de-Caracteres/blob/35a447865f35b54b3cafa0d93155f27d015270df/Ejecucion%20del%20programa/Interfaz%20secundario.png)

### Texto Extraído de la Imagen
![Texto Extraído](https://github.com/DannyCrisostomo/Reconocimiento-Optico-de-Caracteres/blob/35a447865f35b54b3cafa0d93155f27d015270df/Ejecucion%20del%20programa/Texto%20extraido%20de%20la%20imagen.png)



¡Disfruta utilizando la aplicación OCR!
