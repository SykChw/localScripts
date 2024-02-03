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

'''
import cv2
import numpy as np

# Load the image
image = cv2.imread('BookCount_2.jpeg')

# Convert the image to grayscale
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(image, (11, 11), 0)
blur = image - blur
eroded = cv2.erode(blur, (11, 11), iterations=20)
eroded = cv2.GaussianBlur(eroded, (11, 11), 0)
eroded = cv2.erode(blur, (11, 11), iterations=20)


# Apply Canny edge detection
edges = cv2.Canny(blur, 40, 150)
cv2.imshow('Edges', edges)

# Apply Probabilistic Hough Transform
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=300, minLineLength=500, maxLineGap=9)

# Draw the detected lines on the image (for visualization)
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Count the number of books based on the number of detected lines
num_books = len(lines) if lines is not None else 0

# Display the result
cv2.putText(image, f'Number of Books: {num_books}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.imshow('Books with Lines Detected', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''