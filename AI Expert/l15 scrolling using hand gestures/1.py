import cv2
import time
import pyautogui
import mediapipe as mp

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Configurations
SCROLL_SPEED = 300
SCROLL_DELAY = 1  # seconds between scrolls
CAM_WIDTH, CAM_HEIGHT = 640, 480

# ---------------------------------------------------
# Function to detect gestures (open palm or fist)
# ---------------------------------------------------
def detect_gesture(landmarks, handedness):
    fingers = []

    # Fingertip and pip landmark indices
    tips = [
        mp_hands.HandLandmark.INDEX_FINGER_TIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
        mp_hands.HandLandmark.RING_FINGER_TIP,
        mp_hands.HandLandmark.PINKY_TIP,
    ]

    # Check if fingers are up (except thumb)
    for tip in tips:
        if landmarks.landmark[tip].y < landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    # Check thumb separately (horizontal comparison)
    thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]

    if (handedness == "Right" and thumb_tip.x < thumb_ip.x) or (
        handedness == "Left" and thumb_tip.x > thumb_ip.x
    ):
        fingers.append(1)
    else:
        fingers.append(0)

    total_fingers = sum(fingers)

    if total_fingers == 5:
        return "scroll_up"
    elif total_fingers == 0:
        return "scroll_down"
    else:
        return "none"


# ---------------------------------------------------
# Initialize camera
# ---------------------------------------------------
cap = cv2.VideoCapture(0)
cap.set(3, CAM_WIDTH)
cap.set(4, CAM_HEIGHT)

last_scroll = 0
p_time = 0

print("🖐️ Gesture Scroll Control Active")
print("Open palm → Scroll Up")
print("Fist → Scroll Down")
print("Press 'q' to exit\n")

# ---------------------------------------------------
# Main loop
# ---------------------------------------------------
while cap.isOpened():
    success, img = cap.read()
    if not success:
        break

    # Flip and convert color (for mirror view)
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process image for hand landmarks
    results = hands.process(img_rgb)
    gesture, handedness = "none", "Unknown"

    if results.multi_hand_landmarks:
        for hand_landmarks, handedness_info in zip(
            results.multi_hand_landmarks, results.multi_handedness
        ):
            handedness = handedness_info.classification[0].label
            gesture = detect_gesture(hand_landmarks, handedness)

            # Draw hand landmarks
            mp_drawing.draw_landmarks(
                img, hand_landmarks, mp_hands.HAND_CONNECTIONS
            )

    # Handle scroll actions
    if (time.time() - last_scroll) > SCROLL_DELAY:
        if gesture == "scroll_up":
            pyautogui.scroll(SCROLL_SPEED)
        elif gesture == "scroll_down":
            pyautogui.scroll(-SCROLL_SPEED)
        last_scroll = time.time()

    # FPS Calculation
    fps = 1 / (time.time() - p_time) if (time.time() - p_time) > 0 else 0
    p_time = time.time()

    # Display info on screen
    cv2.putText(
        img,
        f"FPS: {int(fps)} | Hand: {handedness} | Gesture: {gesture}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 0, 0),
        2,
    )
    # Show video
    cv2.imshow("Gesture Scroll Control", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
