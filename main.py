import cv2

# def detect_gesture(frame):
#   roi = frame[100:300, 100:300]
#   gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
#   hand_detected = True
#   return hand_detected


cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    if not ret:
      print("Error")
      break

    # hand_detected = detect_gesture(frame.copy())

    # if hand_detected:
    #   cv2.putText(frame, "Hand Detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    # else:
    #   cv2.putText(frame, "No Hand Detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Gesture Control', frame)
    if cv2.waitKey(1) == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()