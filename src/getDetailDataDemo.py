# 获取每个职位的具体内容
# encoding="utf-8"
import json
import requests
from lxml.html import etree, HTMLParser

url = 'https://www.lagou.com/jobs/8144561.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Host': 'www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest',
    'cookie': 'LG_HAS_LOGIN=1; user_trace_token=20201227123216-576d0460-13a3-4014-b4aa-fdd94fed3236; _ga=GA1.2.523400344.1609043537; LGUID=20201227123216-013bb23c-8420-428d-9049-155a1c4fa5f4; JSESSIONID=ABAAAECABFAACEA6F15E4760421ADACD7B013C69CA832B6; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=42; privacyPolicyPopup=false; WEBTJ-ID=20201227162735-176a34f5c33b47-099e52681e603a-32687907-1024000-176a34f5c3468e; RECOMMEND_TIP=true; sensorsdata2015session=%7B%7D; index_location_city=%E4%B8%8A%E6%B5%B7; _gid=GA1.2.1287297771.1609409634; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1609043537,1609495379; TG-TRACK-CODE=index_search; LGSID=20210102114841-7bb8e7dc-0406-4b6f-ac2d-964b1aebf6a0; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist%5F%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; SEARCH_ID=66413fc2d7be4252b1b888d04f3a7d4e; X_MIDDLE_TOKEN=ff094a5f34c07170065b970a841c2545; gate_login_token=8d03852c0ab0cba351381cab30d81ffdf126a2d646b95b6f2b0a63f5563a3eef; LG_LOGIN_USER_ID=1c1e36033fdabc408979b4ce7f7741b22d362fc5fa434b92bb6ef56565aaccf2; _putrc=0E5FF97976740312123F89F2B170EADC; login=true; unick=%E5%91%A8%E9%9B%85; X_HTTP_TOKEN=1d8f311350c7d50356106590613aa4d10d196fa2d6; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2212459930%22%2C%22%24device_id%22%3A%22171bea348f4b7-09156ce41a17a5-396b7506-1024000-171bea348f5237%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24os%22%3A%22MacOS%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2286.0.4240.198%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22first_id%22%3A%22171bea348f4b7-09156ce41a17a5-396b7506-1024000-171bea348f5237%22%7D; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1609560166; LGRID=20210102120246-b78f8968-ec35-40e6-82f3-b2f5ba734b09'

}
res = requests.get(url, headers=headers)
# print(res.status_code)
res.encoding = 'utf-8'
content = res.text
print(content)
# 创建文档树
html_obj = etree.HTML(content, parser=HTMLParser(encoding='utf-8'))
jobDetail = html_obj.xpath('//div[@class="job-detail"]/text()')
print(jobDetail)
print('工作职责' in jobDetail  and '任职要求')

cur_str = ''
with open('/Users/zhouya/Documents/工作/mycode/analyze-lagou/data/jobDetailDemo.txt', 'a', encoding="utf-8") as wf:
    # s='中文'
    # wf.write(s)
    for value in jobDetail:
        if ('职责' in value.strip()):
            cur_str = ''
        elif ('要求' in value.strip()):
            # 写入工作职责
            wf.write(cur_str + '\t')
            cur_str = ''
        else:
            cur_str += value.strip()
    # 写入工作要求,并且加入换行符
    wf.write(cur_str + '\n')
