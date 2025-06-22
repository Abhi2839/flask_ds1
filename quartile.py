import numpy as np
data=[1,2,3,4,5,6,7,8,9,10]
Q1=np.percentile(data,25)
Q2=np.median(data)
Q3=np.percentile(data,75)
IQR=Q3-Q1
print("Q1:",Q1)
print("Q2:",Q2)
print("Q3:",Q3)
print("IQR:",IQR)