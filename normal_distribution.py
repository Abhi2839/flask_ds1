import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
#normal distri
u,sigma=0,0.1
ss=np.random.normal(u,sigma,1000)  #1000 num of vals
count,bins,ignored=plt.hist(ss,30,density=True)
plt.plot(bins,1/(sigma*np.sqrt(2*np.pi))*np.exp(-(bins-u)**2/(2*sigma**2)),linewidth=2,color='r')
plt.title('Normal distribution')
plt.show()
