#Librería
import cv2
from cv2 import imshow
"""import pytesseract
tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'"""

imgText="cafe"
#Lectura de imagen
img= cv2.imread(imgText+'.png')
imshow('Imagen Original',img)

#Imagen escala de grises
imgGrau= cv2.imread(imgText+'.png',0)
imshow('Grises',imgGrau)

#Binarización
ret,tresh=cv2.threshold(imgGrau,150,255,cv2.THRESH_BINARY)
imshow('Binarizada',tresh)

#Binarización adaptativo
th1=cv2.adaptiveThreshold(imgGrau,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,40)
th2=cv2.adaptiveThreshold(imgGrau,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,40)
imshow('Promedio',th1)
imshow('Gaussiano',th2)

#Binarización Otsu
ret,th3=cv2.threshold(imgGrau,150,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
imshow('Otsu',th3)

#Letras
#print(pytesseract.image_to_string(th3))

cv2.waitKey(0)
cv2.destroyAllWindows()