import numpy as np
import pandas as pd
from tabulate import tabulate
#seed for responsibilty
np.random.seed(42)
#creating the data frame
data= {
  'Age':np.random.normal(30,10,100).astype(int),  # u,sigma,size
  'Income':np.random.normal(50,20,100).astype(int),
'Spending score':np.random.randint(1,100,100),
'Years with company ':np.random.normal(5,2,100).astype(int)  #1 lb included 100 excluded num=100
}
df=pd.DataFrame(data)
print(df)
correlation_matrix=df.corr()
print(tabulate(correlation_matrix,headers='keys',tablefmt='grid',numalign='center',floatfmt='.2f'))