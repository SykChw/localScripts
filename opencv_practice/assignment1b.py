import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('ShadowRemoval1.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 60, 200, cv.THRESH_BINARY)
blur = cv.GaussianBlur(thresh, (7, 7), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 100, 175)
dilated = cv.dilate(canny, (1, 1), iterations=0)
(cnt, hierarchy) = cv.findContours(dilated.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) 
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB) 
cv.drawContours(rgb, cnt, -1, (255, 0, 0), 2) 

plt.imshow(rgb)
plt.show()

'''
image = cv2.imread('ShadowRemoval1.jpg') 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

blur = cv2.GaussianBlur(gray, (11, 11), 0) 
canny = cv2.Canny(blur, 30, 150, 3) 
dilated = cv2.dilate(canny, (1, 1), iterations=0) 

(cnt, hierarchy) = cv2.findContours( 
	dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2) 

plt.imshow(rgb)
plt.show()
'''