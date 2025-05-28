import cv2
import matplotlib.pyplot as plt

# Load image
image = cv2.imread('example.jpg')

# Validate image loading
if image is None:
    print("Error: Image could not be loaded. Check the file path.")
    exit()

# Convert BGR to RGB for Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB Image")
plt.axis('off')
plt.show()

# Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')
plt.show()

# Image dimensions
height, width = image.shape[:2]

# Crop safely: rows 100–300, cols 200–400
if 300 > height or 400 > width:
    print("Error: Cropping region exceeds image dimensions.")
else:
    cropped_image = image[100:300, 200:400]
    cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
    plt.imshow(cropped_rgb)
    plt.title("Cropped Region")
    plt.axis('off')
    plt.show()
