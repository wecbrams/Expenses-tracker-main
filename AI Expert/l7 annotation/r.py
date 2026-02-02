import cv2
import matplotlib.pyplot as plt

image_path = 'sept29.jpeg'
image = cv2.imread(image_path)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width, _ = image_rgb.shape

# Rectangle 1
rect1_width, rect1_height = 150, 150
top_left1 = (20, 20)

# ❌ Incorrect: Too many values, and wrong logic
# bottom_right = (top_left1[0], rect1_width, top_left1[1] + rect1_height)

# ✅ Fixed:
bottom_right1 = (top_left1[0] + rect1_width, top_left1[1] + rect1_height)

cv2.rectangle(image_rgb, top_left1, bottom_right1, (0, 255, 255), 3)

# Rectangle 2
rect2_width, rect2_height = 200, 150
top_left2 = (width - rect2_width - 20, height - rect2_height - 20)

# ❌ Incorrect: Wrong number of coordinates, and bad math
# bottom_right2 = (top_left2[0], rect2_width, top_left2[1] + rect2_height)

# ✅ Fixed:
bottom_right2 = (top_left2[0] + rect2_width, top_left2[1] + rect2_height)

cv2.rectangle(image_rgb, top_left2, bottom_right2, (255, 0, 255), 3)

# Calculate centers
center1_x = top_left1[0] + rect1_width // 2

# ❌ Incorrect: using x instead of y
# center1_y = top_left1[0] + rect1_height // 2

# ✅ Fixed:
center1_y = top_left1[1] + rect1_height // 2

center2_x = top_left2[0] + rect2_width // 2

# ❌ Incorrect: using x instead of y
# center2_y = top_left2[0] + rect2_height // 2

# ✅ Fixed:
center2_y = top_left2[1] + rect2_height // 2

# ❌ Incorrect: missing comma between radius and color
# cv2.circle(image_rgb, (center1_x, center1_y), 15(0,255,0),-1)

# ✅ Fixed:
cv2.circle(image_rgb, (center1_x, center1_y), 15, (0, 255, 0), -1)
cv2.circle(image_rgb, (center2_x, center2_y), 15, (0, 0, 255), -1)

# ❌ Incorrect: Missing second point of line
# cv2.line(image_rgb, (center1_x, center1_y), (0,225,0),3)

# ✅ Fixed:
cv2.line(image_rgb, (center1_x, center1_y), (center2_x, center2_y), (0, 255, 0), 3)

font = cv2.FONT_HERSHEY_SIMPLEX

# ✅ Correct
cv2.putText(image_rgb, "Region 1", (top_left1[0], top_left1[1] - 10), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)

# ❌ Incorrect: Using top_left1 again for Region 2
# cv2.putText(image_rgb, "Region 2", (top_left1[0], top_left1[1] - 10), ...)

# ✅ Fixed:
cv2.putText(image_rgb, "Region 2", (top_left2[0], top_left2[1] - 10), font, 0.7, (255, 0, 255), 2, cv2.LINE_AA)

# ❌ Incorrect: wrong y-coordinate (center1_x used instead of center1_y)
# cv2.putText(image_rgb, "Center 1", (center1_x - 40, center1_x + 40), ...)

# ✅ Fixed:
cv2.putText(image_rgb, "Center 1", (center1_x - 40, center1_y + 40), font, 0.6, (0, 255, 0), 2, cv2.LINE_AA)

# ❌ Incorrect: wrong coordinates (center2_y used for x)
# cv2.putText(image_rgb, "Center 2", (center2_y - 40, center1_y + 40), ...)

# ✅ Fixed:
cv2.putText(image_rgb, "Center 2", (center2_x - 40, center2_y + 40), font, 0.6, (0, 0, 255), 2, cv2.LINE_AA)

# Arrow lines (height indicator)
arrow_start = (width - 50, 20)
arrow_end = (width - 50, height - 20)

# ❌ Typo: 'tiplLength' instead of 'tipLength'
# cv2.arrowedLine(image_rgb, arrow_start, arrow_end, (255,255,0),3, tiplLength=0.05)

# ✅ Fixed:
cv2.arrowedLine(image_rgb, arrow_start, arrow_end, (255, 255, 0), 3, tipLength=0.05)
cv2.arrowedLine(image_rgb, arrow_end, arrow_start, (255, 255, 0), 3, tipLength=0.05)

# Label for image height
height_label_position = (arrow_start[0] - 150, (arrow_start[1] + arrow_end[1]) // 2)
cv2.putText(image_rgb, f"Height: {height}px", height_label_position, font, 0.8, (255, 255, 0), 2, cv2.LINE_AA)

# Display
plt.figure(figsize=(12, 8))
plt.imshow(image_rgb)

# ❌ Typo in title
# plt.title("Annotedted image with regions,center and ni-directional Hieght")

# ✅ Fixed:
plt.title("Annotated Image with Regions, Centers, and Bi-Directional Height")
plt.axis('off')
plt.show()
