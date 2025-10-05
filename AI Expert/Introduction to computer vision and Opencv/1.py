import cv2   # Import OpenCV

# Load an image
image = cv2.imread("SEPTERMBER29.jpg")  

# Create a resizable window
cv2.namedWindow("Loaded Image", cv2.WINDOW_NORMAL)  
cv2.resizeWindow("Loaded Image", 800, 500)  

# Show the image
cv2.imshow("Loaded Image", image)  

# Print image dimensions
print(f"Image Dimensions: {image.shape}")  

# Wait for a key press
cv2.waitKey(0)  
cv2.destroyAllWindows()

#pip install opencv-python
