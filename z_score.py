import numpy as np
data=[1,2,3,4,5,6,7,8,9,10]
mean=np.mean(data)
std_dev=np.std(data)
z_score=[(x-mean)/std_dev for x in data]
print(z_score)