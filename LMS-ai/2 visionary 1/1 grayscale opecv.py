import cv2

# Load the image
image = cv2.imread('example.jpg')

if image is None:
    print("Error: Could not load the image. Please check the file path.")
    exit()

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Resize to 224x224
resized_image = cv2.resize(gray_image, (224, 224))

# Display the processed image
cv2.imshow('Processed Image', resized_image)

# Wait for a key press
key = cv2.waitKey(0)

# Save image if 's' or 'S' is pressed
if key in [ord('s'), ord('S')]:
    cv2.imwrite('grayscale_resized_image.jpg', resized_image)
    print("Image saved as grayscale_resized_image.jpg")
else:
    print("Image not saved")

# Clean up
cv2.destroyAllWindows()

# Print processed image dimensions
print(f"Processed Image Dimensions: {resized_image.shape}")
