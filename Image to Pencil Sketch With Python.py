import cv2

# Load an image
image_path = 'pavan.jfif'  # Replace with your image file path
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
inverted_gray_image = cv2.bitwise_not(gray_image)

# Apply Gaussian blur to the inverted image
blurred_image = cv2.GaussianBlur(inverted_gray_image, (111, 111), 0)

# Invert the blurred image
inverted_blurred_image = cv2.bitwise_not(blurred_image)

# Create the pencil sketch image by blending the original and inverted blurred images
pencil_sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

# Save or display the pencil sketch image
output_path = 'pencil_sketch.jpg'  # Replace with your desired output file path
cv2.imwrite(output_path, pencil_sketch)

# Display the original and pencil sketch images side by side
cv2.imshow('Original Image', image)
cv2.imshow('Pencil Sketch', pencil_sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
