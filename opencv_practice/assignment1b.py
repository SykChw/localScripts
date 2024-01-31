# importing required libraries
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#'''
image = cv.imread('ShadowRemoval2.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(gray, 110, 200, cv.THRESH_BINARY)
blur = cv.GaussianBlur(thresh, (7, 7), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 100, 175)
dilated = cv.dilate(canny, (1, 1), iterations=1)

(cnt, hierarchy) = cv.findContours(dilated.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) 
rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB) 
cv.drawContours(rgb, cnt, -1, (255, 0, 0), 2) 

plt.imshow(rgb)
plt.show()


'''
# loading .jpg image using cv.imread() function into 'image'
image = cv.imread('ShadowRemoval2.jpg') 
# converting the RGB image in grayscale
# converting from a 3-channel image matrix to a 2-D matrix
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY) 

# applying a Gaussian filter (kernel dimensions of (11, 11))
blur = cv.GaussianBlur(gray, (11, 11), 0) 
# applying cv.Canny() for edge detection
canny = cv.Canny(blur, 30, 150, 3)
# dilating the image for more distinct edges
dilated = cv.dilate(canny, (3, 3), iterations=1) 


(cnt, hierarchy) = cv.findContours(dilated.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) 
rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB) 
cv.drawContours(rgb, cnt, -1, (255, 0, 0), 2) 

plt.imshow(rgb)
plt.show()
'''