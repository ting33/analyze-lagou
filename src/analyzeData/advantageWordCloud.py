import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def create_word_cloud(f):
    wc = WordCloud(
        font_path="/System/Library/Fonts/STHeiti Medium.ttc",
        # background_color='white',
        max_words=20,
        width=2000,
        height=1200,
        # mask=plt.imread('/Users/zhouya/Downloads/sikao.jpg')  #背景图片
    )
    wordcloud = wc.generate(f)
    # 写词云图片
    wordcloud.to_file("wordcloud.jpg")
    # 显示词云文件
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

def remove_stop_words(f):
        stop_words = ['大平台', '双休', '下午茶', "福利好", "这里", "这些", "的"]
        for stop_word in stop_words:
            f = f.replace(stop_word,'')
        return f

def getCloudPic(f):
    #f是str类型
    data = remove_stop_words(f)
    create_word_cloud(data)

if __name__ == "__main__":
    df = pd.read_csv('/Users/zhouya/Documents/code/analyze-lagou/data/jobList_全国_3月_1.txt', sep='\t')
    # print(df.info())
    data_positionAdvantage=df['positionAdvantage'].to_list()
    #展示前20个热门福利,去掉大平台等词语
    text = " ".join(str(i) for i in data_positionAdvantage)
    getCloudPic(text)
