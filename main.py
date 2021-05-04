from photo468 import photo
from definer import definer
from approxiator import predict

# Tolerance that can be accepted
tol=float(input("tolerance"))

# Giving the image to process and give all the slopes
m1=photo("Resources/scanned/k1.jpg",n=10)
m2=photo("Resources/scanned/face2.jpg",n=10)

# Predict the value of Tolerance
x=predict(m1,m2)
print("Found Tolerance==",x)

# Print the Result
definer(x,tol)
