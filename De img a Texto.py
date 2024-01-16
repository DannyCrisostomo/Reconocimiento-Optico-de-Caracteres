import pytesseract
import cv2
import os

# Descarga tesseract en el siguiente link
# https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe
os.system("cls")

ruta_del_motor_tesseract=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd=ruta_del_motor_tesseract
gray_img=cv2.imread('imagen.png',cv2.IMREAD_GRAYSCALE)
_,th=cv2.threshold(gray_img,138,255,cv2.THRESH_BINARY)
cv2.imshow("Ti",th)
cv2.waitKey(0)

# Realiza OCR para obtener el texto
text = pytesseract.image_to_string(th)

# Guarda el texto en un archivo de texto
output_file_path = 'output.txt'
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(text)

print(f"Texto exportado correctamente a '{output_file_path}'")