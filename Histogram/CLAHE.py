import cv2
import matplotlib.pyplot as plt


image = cv2.imread("image.jpg")

image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

equalize_image = cv2.equalizeHist(image_grayscale)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4,4))

clahe_equalize_image = clahe.apply(image_grayscale)

plt.figure(figsize=(10,8))

plt.subplot(1, 3, 1)
plt.imshow(image_grayscale)
plt.title("GrayScale Image")

plt.subplot(1, 3, 2)
plt.imshow(equalize_image)
plt.title("Equalize  Image")

plt.subplot(1, 3, 3)
plt.imshow(clahe_equalize_image)
plt.title("CLAHE Equalize Image")

plt.show()