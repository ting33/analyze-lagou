# 常见的相关的全国岗位的数量
import requests
import pandas as pd
import numpy as np

def job_names():
    return ['数据分析', '数据运营', '数据产品经理', '大数据开发', 'python工程师', '测试开发工程师', '算法工程师', 'java开发']


def get_job_count(url, job):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest',
        'cookie': 'LG_HAS_LOGIN=1; user_trace_token=20201227123216-576d0460-13a3-4014-b4aa-fdd94fed3236; _ga=GA1.2.523400344.1609043537; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1609043537; LGUID=20201227123216-013bb23c-8420-428d-9049-155a1c4fa5f4; gate_login_token=8d03852c0ab0cba351381cab30d81ffdf126a2d646b95b6f2b0a63f5563a3eef; LG_LOGIN_USER_ID=d805a08ae58f2243fc1d758421c972b61bedcafc16cc9f55b316b8eb44fc9c14; _putrc=0E5FF97976740312123F89F2B170EADC; JSESSIONID=ABAAAECABFAACEA6F15E4760421ADACD7B013C69CA832B6; login=true; unick=%E5%91%A8%E9%9B%85; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=42; privacyPolicyPopup=false; WEBTJ-ID=20201227162735-176a34f5c33b47-099e52681e603a-32687907-1024000-176a34f5c3468e; RECOMMEND_TIP=true; sensorsdata2015session=%7B%7D; index_location_city=%E4%B8%8A%E6%B5%B7; PRE_UTM=; PRE_HOST=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist%5F%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%2Fp-city%5F3%3Fpx%3Ddefault%23filterBox; LGSID=20201231181353-7d3efa5a-06b7-42fb-bf76-ba245cb66ca5; PRE_SITE=; _gid=GA1.2.1287297771.1609409634; TG-TRACK-CODE=index_search; SEARCH_ID=7936f3d25498415884b9fc5933693e2e; X_HTTP_TOKEN=1d8f311350c7d50313401490613aa4d10d196fa2d6; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2212459930%22%2C%22%24device_id%22%3A%22171bea348f4b7-09156ce41a17a5-396b7506-1024000-171bea348f5237%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24os%22%3A%22MacOS%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2286.0.4240.198%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22first_id%22%3A%22171bea348f4b7-09156ce41a17a5-396b7506-1024000-171bea348f5237%22%7D; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1609410432; LGRID=20201231182726-7564924e-6de7-4924-91d2-c7f567c27576'
    }
    data = {
        'first': 'true',
        'pn': 1,
        'kd': job
    }
    res = requests.post(url, headers=headers, data=data)
    page_data = res.json()
    job_count = page_data['content']['positionResult']['totalCount']
    return job_count


if __name__ == "__main__":
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'
    job_count = {}
    job_names = job_names()
    for i in job_names:
        count = get_job_count(url, i)
        job_count[i]=count
    df = pd.DataFrame(job_count,index = [0])
    df.to_csv('/Users/zhouya/Documents/工作/mycode/analyze-lagou/data/differentJobCount.txt', index=False)
