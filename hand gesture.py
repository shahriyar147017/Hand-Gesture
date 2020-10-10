import cv2
import numpy as np
import pyautogui


capture = cv2.VideoCapture(0)

lower_Yellow = np.array([22, 93, 0])
upper_Yellow = np.array([45, 255, 255])
previous_y = 0
while True:
    ret, frame = capture.read ()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange (hsv, lower_Yellow, upper_Yellow)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours (frame, contours, -1, (0, 255, 0), 2)

    for c in contours:
        area = cv2.contourArea(c)
        if area > 1500:
            #print (area)
            #cv2.drawContours (frame, c, -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle (frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
            if y < previous_y:
                pyautogui.press('up')
            elif y > previous_y:
                pyautogui.press('down')
            previous_y = y

    #cv2.imshow ('mask', mask)
    cv2.imshow ('frame', frame)

    if cv2.waitKey(10) == ord ('s'):
        break


capture.release()
cv2.destroyAllWindows()

