import pandas as pd
import matplotlib.pyplot as plt
#不同城市柱状图
df=pd.read_csv('/Users/zhouya/Documents/工作/mycode/analyze-lagou/data/cleanTest.txt',sep='\t')
city=df['city'].value_counts()
print(city)
# print(len(city))
keys = city.index  # 等价于keys = city.keys()
goodcity=[]
goodvalue=[]
for key in keys:
    count=city[key]
    if count>30:
        goodcity.append(key)
        goodvalue.append(count)
values = city.values
plt.title("全国不同城市对数据分析岗位的需求",loc='center')
plt.xlabel('城市')
plt.ylabel("数量")
plt.bar(goodcity,goodvalue)
plt.savefig('不同城市的岗位需求-柱状图.jpg')
plt.show()


plt.pie(goodvalue,labels=goodcity,autopct='%1.1f%%',shadow=False,startangle=150)
plt.title("不同城市的岗位需求")
plt.legend(loc='upper right',bbox_to_anchor=(0.1, 1))
plt.savefig('不同城市的岗位需求-饼图.jpg')
plt.show()


