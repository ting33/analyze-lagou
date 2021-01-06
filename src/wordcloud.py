import pandas as pd
df=pd.read_csv('/Users/zhouya/Documents/工作/mycode/analyze-lagou/data/jobDetail_全国.txt',sep='\t')
print(df.info())
# data1=df['岗位职责']
# data2=df['岗位要求']