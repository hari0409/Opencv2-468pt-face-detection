import numpy as np

def approx(a,b):
    return np.isclose(a, b, rtol=0.01, atol=0.01, equal_nan=False)

def predict(m1,m2):
    print("Calculating Tolerance")
    print("Calculation of Tolerance may take some time!!")
    t=0
    f=0
    total=0
    for i in m1:
        for j in m2:
            ans=approx(i,j)
            if ans==True:
                t+=1
                total+=1
            elif ans==False:
                f+=1
                total+=1
    print(t)
    print(f)
    print(total)
    return (t/total)*100
