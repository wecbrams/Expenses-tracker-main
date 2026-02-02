import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_image(title, image):
    """Display image on screen."""
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

# Load the image
image = cv2.imread('example.jpg')

# Check if image exists
if image is None:
    print("Error: Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    show_image("Original Grayscale Image", gray)

    print("Choose an option:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Gaussian Blur (Smoothing)")
    print("4. Exit")

    while True:
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            # Sobel Edge Detection
            sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
            sobel_combined = cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
            show_image("Sobel Edge Detection", sobel_combined)

        elif choice == "2":
            # Canny Edge Detection
            print("Enter thresholds (default: 100 and 200)")
            t1 = int(input("Lower threshold: "))
            t2 = int(input("Upper threshold: "))
            edges = cv2.Canny(gray, t1, t2)
            show_image("Canny Edge Detection", edges)

        elif choice == "3":
            # Gaussian Blur
            print("Enter kernel size (odd number, e.g., 5): ")
            k = int(input("Kernel size: "))
            blurred = cv2.GaussianBlur(gray, (k, k), 0)
            show_image("Gaussian Blurred Image", blurred)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Enter 1–4.")
