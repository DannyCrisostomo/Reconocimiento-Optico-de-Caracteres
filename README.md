# OCR App - Reconocimiento Óptico de Caracteres

Esta es una aplicación simple de reconocimiento óptico de caracteres (OCR) creada en Python con la interfaz gráfica de usuario (GUI) proporcionada por Tkinter. La aplicación utiliza la biblioteca Tesseract para realizar OCR en imágenes seleccionadas y convierte el texto reconocido en un archivo de texto.

## Instrucciones de Uso

1. **Descargar Tesseract:**
   Asegúrate de tener Tesseract instalado en tu sistema. Puedes descargarlo [aquí](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe).

2. **Ejecutar la Aplicación:**
   Ejecuta el script proporcionado y la interfaz de usuario se abrirá.

3. **Seleccionar una Imagen:**
   Utiliza el botón "Seleccionar Imagen" para elegir una imagen en los formatos admitidos (png, jpg, jpeg, gif). La imagen seleccionada se mostrará en un lienzo.

4. **Convertir a Texto:**
   Después de seleccionar una imagen, puedes hacer clic en "Convertir a Texto". Se te pedirá que ingreses un nombre para el archivo de texto resultante.

5. **Resultado OCR:**
   La aplicación realizará OCR en la imagen, guardará el texto en un archivo de texto y mostrará el resultado en una nueva ventana junto con la imagen procesada.

## Requisitos

- Python 3.x
- Tkinter
- OpenCV
- Pillow (PIL)
- Tesseract

## Configuración

Asegúrate de ajustar la variable `ruta_del_motor_tesseract` en el script con la ruta correcta de tu ejecutable de Tesseract.

```python
ruta_del_motor_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

## Notas

- La aplicación es compatible con imágenes en formato png, jpg, jpeg y gif.
- Asegúrate de proporcionar un nombre al archivo de texto al realizar la conversión.

¡Disfruta utilizando la aplicación OCR!
