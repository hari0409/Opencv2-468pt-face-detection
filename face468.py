import cv2
import mediapipe as mp
import time
from imgstack import  stackImages

#OPENGING OF WEBCAM
import mediapipe.python.solutions.drawing_utils
def video():
    cap=cv2.VideoCapture(0)
    ptime=0
    count=0
    mpdraw=mp.python.solutions.drawing_utils
    mpfacemesh=mp.solutions.face_mesh
    facemesh=mpfacemesh.FaceMesh(max_num_faces=2)
    drawspec=mpdraw.DrawingSpec(thickness=1,circle_radius=1)
    while True:
        success,img=cap.read()
        img=cv2.flip(img,1)
        imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        result=facemesh.process(imgrgb)
        if result.multi_face_landmarks:
            for face in result.multi_face_landmarks:
                mpdraw.draw_landmarks(img,face,mpfacemesh.FACE_CONNECTIONS,drawspec,drawspec)
                for id,lm in enumerate(face.landmark):
                    ih,iw,ic=img.shape
                    x,y,z=int(lm.x*iw),int(lm.y*ih),int(lm.z*ic)
                    print(id,x,y,z)
        ctime=time.time()
        fps=1/(ctime-ptime)
        ptime=ctime
        cv2.putText(img,f'FPS {int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),2)
        imgrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        imgblur = cv2.GaussianBlur(imgrey, (7, 7), 1)
        imgcanny = cv2.Canny(imgrey, 50, 50)
        images=stackImages(0.5,([img,imgrey,imgcanny]))
        cv2.imshow("Result",images)
        if cv2.waitKey(1) & 0xFF==ord('s'):
            cv2.imwrite("Resources/scanned/recog_"+str(count)+".jpg",img)
            count+=1
        if cv2.waitKey(1) & 0xFF==ord(' '):
            break
    return 0
