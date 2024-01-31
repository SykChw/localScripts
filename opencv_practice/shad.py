import cv2
import numpy as np

# Load the image
image_path = 'ShadowRemoval1.jpg'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Calculate the inverse of the grayscale image
inverse_gray = 255 - gray

# Apply Gaussian blur to the inverse grayscale image
blurred = cv2.GaussianBlur(inverse_gray, (21, 21), 0)

# Divide the grayscale image by the blurred image to get the shadow mask
shadow_mask = cv2.divide(gray, 255 - blurred, scale=256)

# Normalize the shadow mask
shadow_mask = cv2.normalize(shadow_mask, None, 0, 255, cv2.NORM_MINMAX)

# Convert the shadow mask to uint8 data type
shadow_mask = np.uint8(shadow_mask)

# Add the shadow mask to the original grayscale image
adjusted_image = cv2.add(gray, shadow_mask)

# Display the original image and the adjusted image
cv2.imshow('Original Image', image)
cv2.imshow('Adjusted Image', adjusted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
