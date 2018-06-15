import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('cat.jpg',0)
plt.plot(5,5),plt.imshow(img,cmap= 'Greens')

plt.show()