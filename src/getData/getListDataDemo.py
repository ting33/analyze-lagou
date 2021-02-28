import random

import requests

url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
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
    'cookie': 'user_trace_token=20210227163256-745d7d2e-b493-44e8-863b-6c6556292afd; __lg_stoken__=67d91f293484edb92bd1de6a6b5f878f2320fc62d67b2e9463a8723fe3428cccec2b25ea28bbfde6825b425a5a6c853d5aad06f678233641a83020366ee5bd920f9068a1b98f; JSESSIONID=ABAAABAABEIABCIEA3F5404D6CB13B598B0FFA9F406C386; WEBTJ-ID=20210227%E4%B8%8B%E5%8D%884:32:57163257-177e29e8ba199a-0e5f00bb921f13-121a4759-1024000-177e29e8ba29f7; LGSID=20210227163257-3c4641af-1955-4e65-9b27-758f8922b5cc; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist%5F%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; LGUID=20210227163257-adfad951-745b-4249-bd7e-59040cd984f5; _ga=GA1.2.1309414705.1614414778; _gat=1; sajssdk_2015_cross_new_user=1; sensorsdata2015session=%7B%7D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1614414778; _gid=GA1.2.487793097.1614414778; X_HTTP_TOKEN=293b0e12237a50625235144161b7ef16b0aeef9971; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22177e29e8f148cf-03752c7e1e6ec-121a4759-1024000-177e29e8f15524%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22MacOS%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2288.0.4324.192%22%7D%2C%22%24device_id%22%3A%22177e29e8f148cf-03752c7e1e6ec-121a4759-1024000-177e29e8f15524%22%7D; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1614415326; LGRID=20210227164206-19e3d7fc-f49f-40a8-935e-e9ed43f305d2; SEARCH_ID=5c10607a47ab4176aaae13ad4a311de1'
}
data = {
    'first': 'true',
    'pn': 17,
    'kd': '数据分析'
}
res = requests.post(url, headers=headers, data=data)
page_data = res.json()
print(page_data)
job_list = page_data['content']['positionResult']['result']
print(type(job_list))
print(job_list)


def correct_list(list_1):
    if list_1 is None:
        return []
    else:
        return list_1


def get_key_names():
    return ['positionId', 'city', 'companyShortName', 'companyId', 'companySize', 'createTime', 'education',
            'famousCompany', 'financeStage', 'industryField', 'salary', 'salaryMonth', 'workYear',
            'jobNature', 'positionAdvantage']

def get_key_list_names():
    return ['companyLabelList', 'hitags', 'positionLables']


with open('jobListDemo.txt', 'a', encoding="utf-8") as wf:
    for i in job_list:
        cur_str = ''
        for key in get_key_names():
            cur_str += (str(i[key]) + '\t')

        for key_list in get_key_list_names():
            cur_str += (','.join(correct_list(i[key_list])) + '\t')

        wf.write(cur_str.strip() + '\n')

        # cur_str = str(i['positionId']) + '\t' + i['city'] + '\t' + i['companyShortName'] + '\t' + str(
        #     i['companyId']) + '\t' + ','.join(correct_list(i['companyLabelList'])) + '\t' + i['companySize'] + '\t' + i[
        #               'createTime'] + '\t' + i[
        #               'education'] + '\t' + str(i['famousCompany']) + '\t' + i['financeStage'] + '\t' + i[
        #               'industryField'] + '\t' + ','.join(correct_list(i['hitags'])) + '\t' + ','.join(
        #     correct_list(i['positionLables'])) + '\t' + i[
        #               'salary'] + '\t' + str(i['salaryMonth']) + '\t' + str(i['workYear']) + '\t' + i[
        #               'jobNature'] + '\t' + i[
        #               'positionAdvantage'] + '\n'
        # wf.write(cur_str)
