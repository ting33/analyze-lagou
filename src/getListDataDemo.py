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
'cookie': 'LG_HAS_LOGIN=1; user_trace_token=20201227123216-576d0460-13a3-4014-b4aa-fdd94fed3236; _ga=GA1.2.523400344.1609043537; LGUID=20201227123216-013bb23c-8420-428d-9049-155a1c4fa5f4; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=42; privacyPolicyPopup=false; RECOMMEND_TIP=true; gate_login_token=8d03852c0ab0cba351381cab30d81ffdf126a2d646b95b6f2b0a63f5563a3eef; LG_LOGIN_USER_ID=1c1e36033fdabc408979b4ce7f7741b22d362fc5fa434b92bb6ef56565aaccf2; JSESSIONID=ABAAABAABAGABFA2D2C48D2B8A548255F1A886482F84D59; WEBTJ-ID=20210103123150-176c68408a53cf-0fe185c2736ea9-163a6153-1024000-176c68408a6971; _putrc=0E5FF97976740312123F89F2B170EADC; login=true; unick=%E5%91%A8%E9%9B%85; sensorsdata2015session=%7B%7D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1609582720,1609582764,1609594659,1609648311; index_location_city=%E4%B8%8A%E6%B5%B7; _gid=GA1.2.1196955537.1609927059; LGSID=20210106203027-e31e12c9-b45c-41f2-9848-e32bde1034bb; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F7929766.html; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=search_code; X_MIDDLE_TOKEN=ff094a5f34c07170065b970a841c2545; SEARCH_ID=9f67a514e9334dc0bec44eaf8eecab1d; X_HTTP_TOKEN=1d8f311350c7d50352073990613aa4d10d196fa2d6; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2212459930%22%2C%22%24device_id%22%3A%22171bea348f4b7-09156ce41a17a5-396b7506-1024000-171bea348f5237%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24os%22%3A%22MacOS%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2287.0.4280.88%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22first_id%22%3A%22171bea348f4b7-09156ce41a17a5-396b7506-1024000-171bea348f5237%22%7D; _gat=1; LGRID=20210106204345-b8e839df-b505-4f46-b6ec-3b8c1d5cf43d; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1609937026'

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


with open('/Users/zhouya/Documents/工作/mycode/analyze-lagou/data/jobListDemo.txt', 'a', encoding="utf-8") as wf:
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
