import pandas as pd
import numpy as np

data=np.arange(1,15,2)

#series object creation using Numpy
srs=pd.Series(data)
print(srs)
print(srs.dtype)

#Data Frame Cretion using list if lengths of arrays are not matching then it will fill values as NaN

df1=pd.DataFrame([[1,2,3,4,5],[1,2,3]])
print(df1)

#Data Frame Cretion using Dict if lengths of arrays are not matching then it will throughs a error.

#df2=pd.DataFrame({'a':[1,2,3,4,5],'b':[1,2,3]}) # ValueError: arrays must all be same length
df2=pd.DataFrame({'a':[1,2,3,4,5],'b':[1,2,3,4,5]})
print(df2)


#DataFrame Creation Using csv file
df=pd.read_csv('F:\\ML\\Hacker Earth\\20-11-2020-Problem\\dataset\\train.csv')
print(df.columns)

