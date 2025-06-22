import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
n,p=10,0.5
bionomial =np.random.binomial(n,p,1000)
plt.hist(bionomial,bins=10,density=True,alpha=0.6,color='b')
plt.title('Bionomial distribution')
plt.show()