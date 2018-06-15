import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('cat.jpg')

blur = cv2.blur(img,(50,50))

plt.subplot(121),plt.imshow(img),plt.title('original')
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')


plt.show()