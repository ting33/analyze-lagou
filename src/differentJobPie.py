
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

labels = ['数据分析','数据运营','数据产品经理','大数据开发','python工程师','测试开发工程师','算法工程师','java开发']
sizes = [2765,451,948,1588,1425,1569,4843,15504]
explode = (0.1,0,0,0,0,0,0,0) #距离中心的距离
plt.axis('equal')  # 使饼图为正圆形
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=150)
plt.title("不同岗位的数据量")
plt.legend(loc='upper right',bbox_to_anchor=(0.1, 1))
plt.savefig('不同岗位数据量分布.jpg')
plt.show()