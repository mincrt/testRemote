from matplotlib.pyplot import fill
import pandas as pd
import numpy as np

a = [1,2,3,4,5,6,7,8]
b = [1,2,4,8,16,32,64,128]
c = [8,7,6,5,4,3,2,1]
data = {"col1":a,"col2":b,"col3":c}
df = pd.DataFrame(data)
print(df)
print(df.diff(axis=0))
print(df.diff(axis=1))
print(df.diff(periods=3))
print(df.diff(periods=-2))
# data = [[5],[5],[pd.NA],[3],[-3.1],[5],[0.4],[6.7],[3]]
# row = ['A★','B★','C','D☆','E','F★','G','H','I☆']
# df = pd.DataFrame(data=data, index=row, columns=['Value'])
# print(df)
# df['average']=df['Value'].rank(method='average')
# df['min']=df['Value'].rank(method='min')
# df['max']=df['Value'].rank(method='max')
# df['first']=df['Value'].rank(method='first')
# df['dense']=df['Value'].rank(method='dense')
# print(df)
# df['keep']=df['Value'].rank(na_option='keep')
# df['top']=df['Value'].rank(na_option='top')
# df['bottom']=df['Value'].rank(na_option='bottom')
# df['pct']=df['Value'].rank(pct=True)
# print(df)

# col = ['col1','col2','col3']
# row = ['row1','row2','row3','row4']
# data = [['A',1,2],['B',3,4],['C',5,6],['D',7,8]]
# df = pd.DataFrame(data=data,index=row,columns=col)
# print(df)
# print(df.transpose())
# print(np.NaN)
# col = ['col1','col2','col3']
# row = ['row1','row2','row3']
# data = [[-1,2,-3.5],[4,-5.5, 3+4j],[7,np.NaN,0]]
# df = pd.DataFrame(data=data,index=row,columns=col)
# print(df)
# print(df.abs())


# col = ['col1','col2','col3']
# row = ['row1','row2','row3']
# data = [[1,2,3],[4,5,6],[7,np.NaN,9]]
# df = pd.DataFrame(data=data,index=row,columns=col)
# print(df)
# print(df.sum(axis=0,skipna=False))
# print(df.sum(axis=1,skipna=False))
# print(df.prod(axis=0,skipna=False))
# print(df.prod(axis=1,skipna=True))
# col = ['col1','col2','col3']
# row = ['row1','row2','row3']
# data = np.random.rand(3,3)*100
# df = pd.DataFrame(data=data, index=row, columns=col)
# print(df)
# print(df.round(-1))


# data = [[1,10,100],[2,20,200],[3,30,300]]
# col = ['col1','col2','col3']
# row = ['row1','row2','row3']
# df = pd.DataFrame(data=data,index=row,columns=col)
# result = df.mod(7)
# result = df.pow(3)
# print(result)
# result = df**3
# print(result)

# data2  = [[3],[4],[5]]
# df2 = pd.DataFrame(data=data2,index=['row1','row2','row3'],columns=['col1'])
# # print(df2)

# result = df.add(df2,fill_value=0)
# result = df.sub(df2,fill_value=0)
# result = df.mul(df2,fill_value=0)
# result = df.div(df2,fill_value=1)
# result = df.mod(df2,fill_value=1)
# # print(result)

# col = ['col1','col2']
# row = ['row1','row2']
# data1 = [[1,2],[3,4]]
# data2 = [[5,6],[7,8]]
# df1 = pd.DataFrame(data=data1)
# df2 = pd.DataFrame(data=data2)
# print(df1)
# print(df2)
# df3=df1.dot(df2)
# print(df3)