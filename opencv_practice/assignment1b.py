# importing required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

#'''
image = cv2.imread('ShadowRemoval2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 110, 200, cv2.THRESH_BINARY)
blur = cv2.GaussianBlur(thresh, (7, 7), cv2.BORDER_DEFAULT)
canny = cv2.Canny(blur, 100, 175)
dilated = cv2.dilate(canny, (1, 1), iterations=1)

(cnt, hierarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
cv2.drawContours(rgb, cnt, -1, (255, 0, 0), 2) 

plt.imshow(rgb)
plt.show()


'''
# loading .jpg image using cv2.imread() function into 'image'
image = cv2.imread('ShadowRemoval2.jpg') 
# converting the RGB image in grayscale
# converting from a 3-channel image matrix to a 2-D matrix
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

# applying a Gaussian filter (kernel dimensions of (11, 11))
blur = cv2.GaussianBlur(gray, (11, 11), 0) 
# applying cv2.Canny() for edge detection
canny = cv2.Canny(blur, 30, 150, 3)
# dilating the image for more distinct edges
dilated = cv2.dilate(canny, (3, 3), iterations=1) 


(cnt, hierarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
cv2.drawContours(rgb, cnt, -1, (255, 0, 0), 2) 

plt.imshow(rgb)
plt.show()
'''