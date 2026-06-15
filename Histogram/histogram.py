import cv2
import matplotlib.pyplot as plt


# image = cv2.imread("image.jpg")

# if image is None:
#     print("Image not found!")
# else:
#     print("Image loaded successfully")

image = cv2.imread("image.jpg")

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Histogram on RGB Image

channels = cv2.split(image_rgb)
colors = ["red", "green", "blue"]

for channel, color in zip(channels, colors):
    hist = cv2.calcHist([channel], [0], None, [256], [0,256])
    plt.plot(hist, color=color)

plt.title("Color Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency ")
plt.show()

# Histogram on HSV image
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(image_hsv)

h_hist = cv2.calcHist([h],[0],None, [180], [0,180])
s_hist = cv2.calcHist([s],[0],None, [256], [0,256])
v_hist = cv2.calcHist([v],[0],None, [256], [0,256])


fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].plot(h_hist, color='orange')
axes[0].set_title("Hue Histogram")
axes[0].set_xlabel("Bins")
axes[0].set_ylabel("Frequencys")

axes[1].plot(s_hist, color='green')
axes[1].set_title("Saturation Histogram")
axes[1].set_xlabel("Bins")
axes[1].set_ylabel("Frequencys")

axes[2].plot(v_hist, color='blue')
axes[2].set_title("Value Histogram")
axes[2].set_xlabel("Bins")
axes[2].set_ylabel("Frequencys")

plt.tight_layout()
plt.show()