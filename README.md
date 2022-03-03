# Binarización
## Instalaciones
### Open CV
pip install opencv-python
### Tesseract (Imagen a Text)
pip install pytesseract
https://es.osdn.net/projects/sfnet_tesseract-ocr-alt/downloads/tesseract-ocr-setup-3.02.02.exe/

## Métodos
### Binarización simple
cv2.threshold([ImagenGrises],[límiteInferior],[límiteSuperior],[Método])

### Binarización Adaptable
cv2.adaptiveThreshold([ImagenGrises],[límiteSuperior],[Tipo de binarización],[Método],c2,c2)

## Binarización OTSU
cv2.threshold([ImagenGrises],[No importa],[No importa],cv2.THRESH_BINARY+cv2.THRESH_OTSU)

