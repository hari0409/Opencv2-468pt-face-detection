# Opencv2-468pt-face-detection
This face detection involves the usage of mediapipe,numpy,cv2
Here first the image is read and processed by media pipe to get all the 468 points and the test image undergoes the same process and the tolrerance for the image recognition is given as a input
Then for every two point in the processed images of the source the slope is found and stored in a List
The same if done for the test image.
The the number of similar slopes in the array is calculated using numpy and the tolerance is calulated 
if tolerance is greater than the minimum,then teh images are similar
else
They are diffrent
![proj1](https://user-images.githubusercontent.com/73524123/116968547-5428c600-acd2-11eb-8f7e-e64cc9a778b0.png)
Result is :
![image](https://user-images.githubusercontent.com/73524123/116968698-9eaa4280-acd2-11eb-83d9-876d6e733add.png)

NOTE: the value of tolerance,number loop for the elements of the array can be modified for faster processing But,accuracy decreases
You can also see the meshes if you want by running the "two_img_mesh.py" for the same images that you use for comparision.
Eg:
In Mesh:
![image](https://user-images.githubusercontent.com/73524123/116968602-6e62a400-acd2-11eb-9c90-21ea55ba8576.png)
Orginal:
![image](https://user-images.githubusercontent.com/73524123/116968769-c5687900-acd2-11eb-8b22-2abe2011ad2a.png)

