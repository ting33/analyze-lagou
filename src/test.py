#处理一些非常规的数据
import pandas as pd
df = pd.read_csv('/Users/zhouya/Documents/code/analyze-lagou/data/jobList_全国_3月_1.txt', sep='\t')
# test=df['salary']
# print(test.head())
print(df.info())
a=pd.Series(['25k-45K','20k-35k','15k-25k','20k-40k','20k'])
#series的str.lower()方法  https://www.cnblogs.com/P--K/p/11148250.html
a1=a.str.lower()
#series 的str.extract()方法
def changeData(s):
    if '-' not in s:
      s=s+'-'+s
    return s

a2=a1.apply(changeData)

a3=a2.str.extract('(\d+)k-(\d+)k')

print(a2)

print(df['famousCompany'].value_counts())

print(df['industryField'].value_counts())

print(df['skillLables'].value_counts())

print(df['district'].value_counts())
print(df['salary'].value_counts())

x=22
y=str(x)+'k'




