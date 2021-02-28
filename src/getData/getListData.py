import requests
import math
import time
import random


# 爬取数据，拉钩网做了反扒，每页请求url都是一样的，但是可以直接用ajax请求获取数据，并且全国和具体的城市url还是不一样的
def post_url(url, num):
    # url='https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'
    user_agent = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)"]
    headers = {
        'User-Agent': random.choice(user_agent),
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest',
        'cookie': 'user_trace_token=20210227163256-745d7d2e-b493-44e8-863b-6c6556292afd; __lg_stoken__=67d91f293484edb92bd1de6a6b5f878f2320fc62d67b2e9463a8723fe3428cccec2b25ea28bbfde6825b425a5a6c853d5aad06f678233641a83020366ee5bd920f9068a1b98f; JSESSIONID=ABAAABAABEIABCIEA3F5404D6CB13B598B0FFA9F406C386; WEBTJ-ID=20210227%E4%B8%8B%E5%8D%884:32:57163257-177e29e8ba199a-0e5f00bb921f13-121a4759-1024000-177e29e8ba29f7; LGUID=20210227163257-adfad951-745b-4249-bd7e-59040cd984f5; _ga=GA1.2.1309414705.1614414778; sajssdk_2015_cross_new_user=1; sensorsdata2015session=%7B%7D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1614414778; _gid=GA1.2.487793097.1614414778; LGSID=20210227213138-2ae5a4b0-8eec-4a52-bc97-61e19b9d1770; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist%5F%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; _gat=1; gate_login_token=7ae37c84b649be1193f65814c07edba1c322b9b8b227a283f8e99e81c9b07be8; LG_LOGIN_USER_ID=34d41090bfa57e0767f491a0f681559338a351878213853fc9b17f3c9c9d01ee; LG_HAS_LOGIN=1; _putrc=0E5FF97976740312123F89F2B170EADC; login=true; unick=%E5%91%A8%E9%9B%85; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=42; privacyPolicyPopup=false; index_location_city=%E4%B8%8A%E6%B5%B7; RECOMMEND_TIP=true; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=293b0e12237a50625472344161b7ef16b0aeef9971; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2212459930%22%2C%22first_id%22%3A%22177e29e8f148cf-03752c7e1e6ec-121a4759-1024000-177e29e8f15524%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22MacOS%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2288.0.4324.192%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22%24device_id%22%3A%22177e29e8f148cf-03752c7e1e6ec-121a4759-1024000-177e29e8f15524%22%7D; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1614432746; LGRID=20210227213429-7cb73f8b-0f2f-48e6-824e-f107bf7a42a2; SEARCH_ID=1d39b83c151146c29693ca4a869a2e17'
    }
    data = {
        'first': 'true',
        'pn': num,
        'kd': '数据分析'
    }
    res = requests.post(url, headers=headers, data=data)
    page_data = res.json()
    return page_data


# 计算一共有多少页
def get_page_num(count):
    page_num = math.ceil(count / 15)  # 每页展示15个数据
    return page_num


# 转换数据时对list类型数据做兼容，有的数据可能返回为空，debug发现type类型为none
def correct_list(list):
    if list is None:
        return []
    else:
        return list


# 需要的字段
def get_key_names():
    return ['positionId', 'city', 'companyShortName', 'companyId', 'companySize', 'createTime', 'education',
            'famousCompany', 'financeStage', 'industryField', 'salary', 'salaryMonth', 'workYear',
            'jobNature', 'positionAdvantage', 'district', 'hunterJob']


def get_key_list_names():
    return ['companyLabelList', 'hitags', 'positionLables', 'skillLabels']


# 处理每一页数据
def get_page_info(job_list):
    with open('../jobList_上海_3月.txt', 'a', encoding="utf-8") as wf:
        for i in job_list:
            cur_str = ''
            for key in get_key_names():
                cur_str += (str(i[key]) + '\t')

            for key_list in get_key_list_names():
                cur_str += (','.join(correct_list(i[key_list])) + '\t')

            wf.write(cur_str.strip() + '\n')


# 不同的城市有不同的url
def main(url, city):
    first_page = post_url(url, 1)
    totalCount = first_page['content']['positionResult']['totalCount']
    # 保存一下每个城市爬出来数据总量
    with open('../jobCount_数据分析_3月.txt', 'a', encoding="utf-8") as wf:
        wf.write(city + '\t' + str(totalCount) + '\n')
    num = get_page_num(totalCount)
    print("数据分析开发相关职位总数:{},总页数为:{}".format(totalCount, num))
    time.sleep(10)  # 为了不频繁请求
    for i in range(1, num + 1):
        page_data = post_url(url, i)
        job_list = page_data['content']['positionResult']['result']
        get_page_info(job_list)
        print("第{}页数据".format(i))
        time.sleep(50)


if __name__ == "__main__":
    # 全国
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'
    main(url, '全国')
    # url='https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
    # main(url, '北京')
    # url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false'
    # main(url, '上海')
