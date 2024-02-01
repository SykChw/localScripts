import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('ShadowRemoval2.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary mask
_, binary_mask = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)

# Invert the binary mask
inverse_binary_mask = cv2.bitwise_not(binary_mask)

# Convert the inverse binary mask to a 3-channel image
inverse_binary_mask = cv2.cvtColor(inverse_binary_mask, cv2.COLOR_GRAY2RGB)

# Increase the brightness of shadows using the inverse binary mask
brightened_image = cv2.add(image, inverse_binary_mask)

plt.imshow(brightened_image)
plt.show()