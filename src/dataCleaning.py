#基本的清洗数据
import pandas as pd
df = pd.read_csv('/Users/zhouya/Documents/工作/mycode/analyze-lagou/data/jobList_全国_1.txt', sep='\t')
# print(df.info())
# print("原始数据大小{}".format(df.shape))

#positionAdvantage ,companyLabelList,hitags,positionLables缺失的较多，并且这几列都是单独拿出来分析的，可以先不要
df=df.drop(['positionAdvantage','companyLabelList','hitags','positionLables'],axis=1)
print("去除缺失多的列{}".format(df.shape))
#判断是否有空值
# print(df.isnull().sum(axis=0))
df=df.dropna()
print("删除空值{}".format(df.shape))
#判断是否有重复的数据
print(any(df.duplicated()))
df=df.drop_duplicates(subset=['positionId'],keep='first')
print("去重后数据大小{}".format(df.shape))
print(any(df.duplicated()))
#过滤掉实习岗位
df.drop(df[df['jobNature'].str.contains('实习')].index, inplace=True)
print("去掉实习岗位的数据{}".format(df.shape))
#写入到新的文件里
df.to_csv('/Users/zhouya/Documents/工作/mycode/analyze-lagou/data/cleanTest.txt', sep='\t', index=False)
