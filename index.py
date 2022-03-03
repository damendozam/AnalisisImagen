#Librería
import cv2
import numpy as np

bgr=np.zeros((300,300,3),dtype=np.uint8)
bgr[:,:,:]=(0,255,255)
cv2.imshow('BGR',bgr)


cv2.waitKey(0)
cv2.destroyAllWindows()
