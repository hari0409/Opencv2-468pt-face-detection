import numpy as np
import cv2

def definer(x,tol):
    if x>=tol:
        img = np.zeros(shape=[512, 512, 3], dtype=np.uint8)
        img=cv2.rectangle(img,(0,200),(640,300),(255,0,255),cv2.FILLED)
        img=cv2.putText(img,"Both are Same",(150,265),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
        cv2.imshow("Process",img)
        cv2.waitKey(0)
    else:
        img = np.zeros(shape=[512, 512, 3], dtype=np.uint8)
        img = cv2.rectangle(img, (0, 200), (640, 300), (255, 0, 255), cv2.FILLED)
        img = cv2.putText(img, "Invalid Verification", (150, 265), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
        cv2.imshow("Process", img)
        cv2.waitKey(0)
