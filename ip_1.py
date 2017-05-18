import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('me.jpg',cv2.IMREAD_GRAYSCALE)
#cv2.imshow('image',img)


plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()

#cv2.waitKey(0)
#cv2.destroyAllWindows()
