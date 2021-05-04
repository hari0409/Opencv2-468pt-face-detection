# Imports
import time

import cv2
import mediapipe as mp
from imgstack import stackImages
import mediapipe.python.solutions.drawing_utils

def photo(url,n):
    ll=[]
    ans=[]
    img=cv2.imread(url)
    mpdraw=mp.python.solutions.drawing_utils
    mpfacemesh=mp.solutions.face_mesh
    facemesh=mpfacemesh.FaceMesh(max_num_faces=2)
    drawspec=mpdraw.DrawingSpec(thickness=2,circle_radius=1)
    img=cv2.flip(img,1)
    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result=facemesh.process(imgrgb)
    for k in range(0, 1, 1):
        for face in result.multi_face_landmarks:
            mpdraw.draw_landmarks(img,face,mpfacemesh.FACE_CONNECTIONS,drawspec,drawspec)
            for id,lm in enumerate(face.landmark):
                ih,iw,ic=img.shape
                x,y=int(lm.x*iw),int(lm.y*ih)
                val = [x, y]
                ll.append(val)
        break
    print("Performing Calculation")
    for i in range(0, int(len(ll)/n), 1):
        for j in range(i + 1,int(len(ll)/n), 1):
            try:
                m = (ll[j][1] - ll[i][1]) / (ll[j][0] - ll[i][0])
            except ZeroDivisionError:
                m = 0
            ans.append(m)
    print("Calculation Finished")
    print(len(ans))
    return ans
