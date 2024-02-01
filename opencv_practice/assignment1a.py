import cv2
import numpy as np

img = cv2.imread('BookCount_1.jpeg')
cv2.imshow('Books', img)


# Converting to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 110, 200, cv2.THRESH_BINARY)
#blur = cv2.GaussianBlur(gray, (3, 3), cv2.BORDER_DEFAULT)
edges = cv2.Canny(thresh, 50, 150, apertureSize=3)
cv2.imshow('edges', edges)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

num_books = len(lines) if lines is not None else 0
# Display the result
cv2.putText(img, f'Number of Books: {num_books}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.imshow('Books with Lines Detected', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
