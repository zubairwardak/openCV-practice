import cv2
import matplotlib.pyplot as plt

image = cv2.imread("bus.jpg", cv2.IMREAD_GRAYSCALE)


sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_combine = cv2.magnitude(sobel_x, sobel_y)

laplacian = cv2.Laplacian(image , cv2.CV_64F, ksize=3)
laplacian_abs = cv2.convertScaleAbs(laplacian)

canny = cv2.Canny(image, 180, 200)

title = ["Orignal Image", "Sobel Edge Image", "Laplacian Edge", "Laplacian Abs", "Canny Edge"]
image = [image, sobel_combine, laplacian, laplacian_abs, canny]

plt.figure(figsize=(12, 10))

for i in range(len(title)):
    plt.subplot(2,3,i+1)
    plt.imshow(image[i], cmap='gray')
    plt.title(title[i])
    plt.axis('off')

plt.show()

# plt.subplot(2,2,2)
# plt.imshow(sobel_combine)
# plt.title("Sobel Edge Detection")
# plt.axis('off')

# plt.subplot(2,2,3)
# plt.imshow(laplacian)
# plt.title("Laplacian Edge Detection")
# plt.axis('off')

# plt.subplot(2,2,4)
# plt.imshow(canny)
# plt.title("Canny Edge Detection")
# plt.axis('off')

# plt.show()