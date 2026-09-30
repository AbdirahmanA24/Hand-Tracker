import cv2
import mediapipe as mp

#the following solutions pipeline shortcuts throw an AttributeError on fresh installs due to new google updates on mediapipe

try:
    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils

    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7 
    )
except AttributeError as e:
    print(f"Archival Run Failed: Google has deprecated this layout. Error: {e}")
    exit()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )
            
    cv2.imshow("MediaPipe Hands (Legacy Archive)", frame)
    
    # Press Esc (27) to exit 
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
