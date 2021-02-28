import pandas as pd

pd.set_option('Display.max_columns', None)
df = pd.read_csv('/Users/zhouya/Documents/code/analyze-lagou/data/jobList_全国_3月_1.txt', sep='\t')
# 去除数据缺失多的列
df = df.drop(['positionAdvantage', 'companyLabelList', 'hitags', 'positionLables', 'skillLabels'], axis=1)
# 去除重复值和空值
df = df.dropna()
df = df.drop_duplicates(subset=['positionId'], keep='first')
# 过滤掉实习岗位
df.drop(df[df['jobNature'].str.contains('实习')].index, inplace=True)


# 把薪资都处理成10k-20k样式
def changeData(s):
    if '-' not in s:
        s = s + '-' + s
    return s


df['salary'] = df['salary'].apply(changeData)
# 计算出平均薪资
df['salary_mean'] = df['salary'].str.lower().str.extract('(\d+)k-(\d+)k').applymap(lambda x: int(x)).mean(axis=1)
# 拆出一个岗位最低和最高薪资
df['salary_low'] = df['salary'].map(lambda s: s.split('-')[0])
df['salary_high'] = df['salary'].map(lambda s: s.split('-')[1])


# 计算一个岗位平均年薪、最低年薪、最高年薪
def changeData1(x):
    x = int(x)
    if (x == 0):
        x = 12
    return x


df['salaryMonth'] = df['salaryMonth'].apply(changeData1)  # salarymonth是float类型且有很多0
df['year_salary_mean'] = df['salaryMonth'] * df['salary_mean']
df['salary_low'] = df['salary_low'].str.extract('(\d+)k').applymap(lambda x: int(x))
df['year_salary_low'] = df['salary_low'] * df['salaryMonth']
df['salary_high'] = df['salary_high'].str.extract('(\d+)k').applymap(lambda x: int(x))
df['year_salary_high'] = df['salary_high'] * df['salaryMonth']
print(df.info())
