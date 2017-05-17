# -*- coding: cp1252 -*-
import numpy
import cv2

img=cv2.imread('me.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('ímage',gray)


cv2.waitKey(0)
cv2.destroyAllWindows()
