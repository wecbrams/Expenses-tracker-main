import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    """Apply the specified color filter to the image."""
    filtered_image = image.copy()

    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0  # Green channel to 0
        filtered_image[:, :, 0] = 0  # Blue channel to 0

    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0  # Green channel to 0
        filtered_image[:, :, 2] = 0  # Red channel to 0

    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0  # Blue channel to 0
        filtered_image[:, :, 2] = 0  # Red channel to 0

    elif filter_type == "increase_red":
        red_channel = filtered_image[:, :, 2]
        filtered_image[:, :, 2] = np.clip(cv2.add(red_channel, 50), 0, 255)

    elif filter_type == "decrease_blue":
        blue_channel = filtered_image[:, :, 0]
        filtered_image[:, :, 0] = np.clip(cv2.subtract(blue_channel, 50), 0, 255)

    return filtered_image

# Load the image
image_path = 'example.jpg'  # Replace with your image path
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
else:
    filter_type = "original"  # Default filter type

    print("=== Color Filter Controls ===")
    print("r - Red Tint")
    print("g - Green Tint")
    print("b - Blue Tint")
    print("i - Increase Red Intensity")
    print("d - Decrease Blue Intensity")
    print("o - Original Image")
    print("q - Quit")
    print("==============================")

    while True:
        if filter_type == "original":
            filtered_image = image.copy()
        else:
            filtered_image = apply_color_filter(image, filter_type)

        cv2.imshow("Filtered Image", filtered_image)

        key = cv2.waitKey(0) & 0xFF

        if key == ord('r'):
            filter_type = "red_tint"
        elif key == ord('g'):
            filter_type = "green_tint"
        elif key == ord('b'):
            filter_type = "blue_tint"
        elif key == ord('i'):
            filter_type = "increase_red"
        elif key == ord('d'):
            filter_type = "decrease_blue"
        elif key == ord('o'):
            filter_type = "original"
        elif key == ord('q'):
            print("Exiting...")
            break
        else:
            print("Invalid key! Use 'r', 'g', 'b', 'i', 'd', 'o', or 'q'.")

    cv2.destroyAllWindows()
