# Opencv2-468pt-face-detection
This face detection involves the usage of mediapipe,numpy,cv2
Here first the image is read and processed by media pipe to get all the 468 points and the test image undergoes the same process and the tolrerance for the image recognition is given as a input
Then for every two point in the processed images of the source the slope is found and stored in a List
The same if done for the test image.
The the number of similar slopes in the array is calculated using numpy and the tolerance is calulated 
if tolerance is greater than the minimum,then teh images are similar
else
They are diffrent
NOTE: the value of tolerance,number loop for the elements of the array can be modified for faster processing But,accuracy decreases
