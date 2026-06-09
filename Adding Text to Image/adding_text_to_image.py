import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("bus.jpg") 

# Making a free space Canvas

# width, height = 700, 500
# blue = (255, 0 , 0)
# canvas = np.full((height, width, 3), blue, dtype=np.uint8)

canvas = np.full((500, 700, 3), (255, 0, 0), dtype=np.uint8)


# Adding Text to Image
# text = "Artificial Intellegent "
# font = cv2.FONT_HERSHEY_COMPLEX
# org = (50,100)
# scale = 1.5
# thickness = 1
# color = (255,255,255)
# cv2.putText(canvas, text, org, font, scale, color, thickness, cv2.LINE_AA)

cv2.putText(image, "openCv Image", (60,120), cv2.FONT_HERSHEY_COMPLEX, 3, (0 , 0 , 255), 1, cv2.LINE_AA )
cv2.imshow("image", image)


# adding multiple font to canva 
fonts = {
    cv2.FONT_HERSHEY_COMPLEX,
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
    cv2.FONT_HERSHEY_DUPLEX,
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
    cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
    cv2.FONT_HERSHEY_SIMPLEX
}

y_offset = 50
for i, font in enumerate(fonts):
    text = f"font {i+1}"
    cv2.putText(canvas, text, (50,y_offset), font, 2, (0,0,0), 2, cv2.LINE_AA)
    y_offset += 50

cv2.imshow("Canvas", canvas)


cv2.waitKey(0)
cv2.destroyAllWindows()