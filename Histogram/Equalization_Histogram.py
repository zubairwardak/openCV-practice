import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("image.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


hist, bins = np.histogram(image_grayscale.flatten(), 256, [0,256])

equalization_image = cv2.equalizeHist(image_grayscale)

equalization_hist , bins = np.histogram(equalization_image.flatten(), 256, [0, 256])

plt.figure(figsize=(12,10))

plt.subplot(2,2,1)
plt.imshow(image_grayscale, cmap='grey')
plt.title("Orignal Image")

plt.subplot(2,2,2)
plt.plot(hist, color='blue')
plt.title("Orignal Histogram Image")

plt.subplot(2,2,3)
plt.imshow(equalization_image, cmap='grey')
plt.title("Equlization Image")

plt.subplot(2,2,4)
plt.plot(equalization_hist, color='green')
plt.title("Equalization Histogram")

plt.tight_layout()
plt.show()