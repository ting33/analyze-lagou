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
        'cookie': 'LG_HAS_LOGIN=1; user_trace_token=20201227123216-576d0460-13a3-4014-b4aa-fdd94fed3236; _ga=GA1.2.523400344.1609043537; LGUID=20201227123216-013bb23c-8420-428d-9049-155a1c4fa5f4; JSESSIONID=ABAAAECABFAACEA6F15E4760421ADACD7B013C69CA832B6; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=42; privacyPolicyPopup=false; WEBTJ-ID=20201227162735-176a34f5c33b47-099e52681e603a-32687907-1024000-176a34f5c3468e; RECOMMEND_TIP=true; sensorsdata2015session=%7B%7D; _gid=GA1.2.1287297771.1609409634; X_MIDDLE_TOKEN=ff094a5f34c07170065b970a841c2545; gate_login_token=8d03852c0ab0cba351381cab30d81ffdf126a2d646b95b6f2b0a63f5563a3eef; LG_LOGIN_USER_ID=1c1e36033fdabc408979b4ce7f7741b22d362fc5fa434b92bb6ef56565aaccf2; _putrc=0E5FF97976740312123F89F2B170EADC; login=true; unick=%E5%91%A8%E9%9B%85; index_location_city=%E5%8C%97%E4%BA%AC; _gat=1; LGSID=20210102213739-bb5572bf-4f66-460a-8e7e-d739434fdfb3; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Fsc.000000KS8YIvjbGY6uWacdCzRxGadhgZxDZuL--hAgrpSkHLPucraTUawB2RkxSNN2exqK29jvNRaHF70qJiUUnwZqzoLIXSEJ8HWfy57juvHin0L-0xSGBH9ZRFMIgyYTxhhpoXJ1GPHWfgGkJXMWSgI6DmpqneqEwZXV90mdR24Z5CLQzvomsdic%5FRFvZ7ZGPf38AbycvHcpCcrhPIZGgwVz81.7Y%5FNR2Ar5Od663rj6tJQrGvKD77h24SU5WudF6ksswGuh9J4qt7jHzk8sHfGmYt%5FrE-9kYryqM764TTPqKi%5FnYQZHuukL0.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqs2v4%5FsKdTvNzgLw4TARqn0K9u7qYXgK-5Hn0IvqzujL0oUhY0ZFWIWYk0ZNzU7qGujYkPHczPj6dPH010Addgv-b5HD1rjT1P1DY0AdxpyfqnH0LrHmzPWm0UgwsU7qGujYknHR1P0KsI-qGujYs0A-bm1dri6KWThnqnWTkPH0%26ck%3D3787.12.112.403.128.330.146.220%26dt%3D1609495372%26wd%3D%25E6%258B%2589%25E9%2592%25A9%26tpl%3Dtpl%5F11534%5F23295%5F19442%26l%3D1522485503%26us%3DlinkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520-%252520%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%25258B%252589%2525E5%25258B%2525BE%21%2526linkType%253D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm%5Fsource%3Dm%5Fcf%5Fcpt%5Fbaidu%5Fpcbt; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1609582720,1609582720,1609582764,1609594659; X_HTTP_TOKEN=1d8f311350c7d50337649590613aa4d10d196fa2d6; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2212459930%22%2C%22%24device_id%22%3A%22171bea348f4b7-09156ce41a17a5-396b7506-1024000-171bea348f5237%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24os%22%3A%22MacOS%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2286.0.4240.198%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22first_id%22%3A%22171bea348f4b7-09156ce41a17a5-396b7506-1024000-171bea348f5237%22%7D; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1609594674; TG-TRACK-CODE=search_code; LGRID=20210102213758-ae49d3d7-a655-417c-8517-fee1d874e4fe; SEARCH_ID=036dd605b5a24082b08566141fd0fe8a'

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
            'jobNature', 'positionAdvantage']


def get_key_list_names():
    return ['companyLabelList', 'hitags', 'positionLables']


# 处理每一页数据
def get_page_info(job_list):
    with open('/Users/zhouya/Documents/工作/mycode/analyze-lagou/data/jobList_上海.txt', 'a', encoding="utf-8") as wf:
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
    with open('/Users/zhouya/Documents/工作/mycode/analyze-lagou/data/jobCount_数据分析.txt', 'a', encoding="utf-8") as wf:
        wf.write(city + '\t' + str(totalCount) + '\n')
    num = get_page_num(totalCount)
    print("数据分析开发相关职位总数:{},总页数为:{}".format(totalCount, num))
    time.sleep(10)  # 为了不频繁请求
    for i in range(1, num + 1):
        page_data = post_url(url, i)
        job_list = page_data['content']['positionResult']['result']
        get_page_info(job_list)
        print("第{}页数据".format(i))
        time.sleep(100)


if __name__ == "__main__":
    #全国
    # url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'
    # main(url, '全国')
    # url='https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
    # main(url, '北京')
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false'
    main(url, '上海')

