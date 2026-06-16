import cv2
import matplotlib.pyplot as plt


image = cv2.imread("shapes.jpg")

image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.Canny(image_gray, 80, 150)

# contours, hierarchy = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# contours_image = image.copy()

# cv2.drawContours(contours_image, contours, -1, (0 , 255, 0), 5)

# plt.figure(figsize=(12, 6))

# plt.subplot(1,3,1)
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.title("Orignal Image")

# plt.subplot(1,3,2)
# plt.imshow(gray, cmap="grey")
# plt.title("mask")

# plt.subplot(1,3,3)
# plt.imshow(cv2.cvtColor(contours_image, cv2.COLOR_BGR2RGB))
# plt.title("Contours image")

# plt.show()


retval, binary = cv2.threshold(image_gray, 200, 256, cv2.THRESH_BINARY)
plt.imshow(binary, cmap='grey')

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

contours_image = image.copy()

cv2.drawContours(contours_image, contours, -1, (0 , 255, 0), 5)

plt.figure(figsize=(12, 6))

plt.subplot(1,3,1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Orignal Image")

plt.subplot(1,3,2)
plt.imshow(binary, cmap="grey")
plt.title("mask")

plt.subplot(1,3,3)
plt.imshow(cv2.cvtColor(contours_image, cv2.COLOR_BGR2RGB))
plt.title("Contours image")

plt.show()