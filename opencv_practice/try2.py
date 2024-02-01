import cv2
import numpy as np

# Load the image
image = cv2.imread('BookCount_2.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (11, 11), 0)
# Apply Canny edge detection
edges = cv2.Canny(blur, 40, 150)
cv2.imshow('Edges', edges)
# Apply Probabilistic Hough Transform
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=9)

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
