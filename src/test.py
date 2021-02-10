#处理一些非常规的数据
import pandas as pd
# df = pd.read_csv('/Users/zhouya/code/mycode/analyze-lagou/data/cleanTest.txt', sep='\t')
# test=df['salary']
# print(test.head())
a=pd.Series(['25k-45K','20k-35k','15k-25k','20k-40k'])
#series的str.lower()方法  https://www.cnblogs.com/P--K/p/11148250.html
a1=a.str.lower()
#series 的str.extract()方法
a2=a1.str.extract('(\d+)[k]-(\d+)k')
print(a2)
