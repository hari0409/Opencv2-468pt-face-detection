import cv2
import mediapipe as mp
from imgstack import stackImages
import mediapipe.python.solutions.drawing_utils

img1 = cv2.imread("Resources/scanned/a1.jpg")
img2 = cv2.imread("Resources/scanned/a2.jpg")
def mesher(img):
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
    return img

images=stackImages(0.5,[img1,img2])
cv2.imshow("Out", images)
cv2.waitKey(0)