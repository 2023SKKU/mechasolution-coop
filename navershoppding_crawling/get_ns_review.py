import requests
import json
import pandas as pd
from random import random, randrange
from bs4 import BeautifulSoup as bs
from time import sleep
import csv

urls = pd.read_csv('ns_요가삭스_url.csv')
url_li = []


def get_url_li(x):
    url = x['url']
    chnlseq = x['chnlseq']
    if url[8:14] == 'search' or url[8:10] == 'cr':
        return
    if not url[8:13] == 'smart':
        return
    url_li.append([url, int(chnlseq)])


urls.apply(get_url_li, axis=1)
print(url_li)

cookies = {
    'NA_SAS': '1',
    'NA_SA': 'Y2k9MEEwMDAwMlpLQXp5ZG5MamswWUx8dD0xNjg0NjU1Nzk2fHU9aHR0cHMlM0ElMkYlMkZzbWFydHN0b3JlLm5hdmVyLmNvbSUyRmdvbXVuYXJhJTJGcHJvZHVjdHMlMkY0OTU5MDI0OTM1JTNGbl9tZWRpYSUzRDExMDY4JTI2bl9xdWVyeSUzRCUyNUVDJTI1OUElMjU5NCUyNUVBJTI1QjAlMjU4MCUyNUVCJTI1QTclMjVBNCUyNUVEJTI1OEElMjVCOCUyNm5fcmFuayUzRDElMjZuX2FkX2dyb3VwJTNEZ3JwLWEwMDEtMDItMDAwMDAwMDExNzcwMjkxJTI2bl9hZCUzRG5hZC1hMDAxLTAyLTAwMDAwMDA5NjA3Mzc1NyUyNm5fY2FtcGFpZ25fdHlwZSUzRDIlMjZuX21hbGxfaWQlM0RvcmllbnRicjElMjZuX21hbGxfcGlkJTNENDk1OTAyNDkzNSUyNm5fYWRfZ3JvdXBfdHlwZSUzRDIlMjZOYVBtJTNEY3QlMjUzRGxoeDJxcGxrJTI1N0NjaSUyNTNEMEEwMDAwMlpLQXp5ZG5MamswWUwlMjU3Q3RyJTI1M0RwbGElMjU3Q2hrJTI1M0QyMDM5OTlhNmE1NDAxZTU1ZDBmZTI0MzJlNGYyMmRmZTA1NWFmMTJk',
    'NVADID': '0A00002ZKAzydnLjk0YL',
    'NA_CO': 'ct%3Dlhx2qplk%7Cci%3D0A00002ZKAzydnLjk0YL%7Ctr%3Dpla%7Chk%3D203999a6a5401e55d0fe2432e4f22dfe055af12d%7Ctrx%3Dundefined',
    'wcs_bt': 's_56c9031416c7c56b:1684655796',
    'NNB': '3PM2SQOU6VFWI',
    'nx_ssl': '2',
    'ASID': 'afc335a00000018808d00bf600000053',
    '_ga': 'GA1.2.1183798841.1684295968',
    'page_uid': 'ibE36lp0JXossUYIP+dssssssfC-517358',
    '_naver_usersession_': 'qnjnEOyKl+L/Qci8bgYJXiM2',
}

headers = {
    'authority': 'smartstore.naver.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'NA_SAS=1; NA_SA=Y2k9MEEwMDAwMlpLQXp5ZG5MamswWUx8dD0xNjg0NjU1Nzk2fHU9aHR0cHMlM0ElMkYlMkZzbWFydHN0b3JlLm5hdmVyLmNvbSUyRmdvbXVuYXJhJTJGcHJvZHVjdHMlMkY0OTU5MDI0OTM1JTNGbl9tZWRpYSUzRDExMDY4JTI2bl9xdWVyeSUzRCUyNUVDJTI1OUElMjU5NCUyNUVBJTI1QjAlMjU4MCUyNUVCJTI1QTclMjVBNCUyNUVEJTI1OEElMjVCOCUyNm5fcmFuayUzRDElMjZuX2FkX2dyb3VwJTNEZ3JwLWEwMDEtMDItMDAwMDAwMDExNzcwMjkxJTI2bl9hZCUzRG5hZC1hMDAxLTAyLTAwMDAwMDA5NjA3Mzc1NyUyNm5fY2FtcGFpZ25fdHlwZSUzRDIlMjZuX21hbGxfaWQlM0RvcmllbnRicjElMjZuX21hbGxfcGlkJTNENDk1OTAyNDkzNSUyNm5fYWRfZ3JvdXBfdHlwZSUzRDIlMjZOYVBtJTNEY3QlMjUzRGxoeDJxcGxrJTI1N0NjaSUyNTNEMEEwMDAwMlpLQXp5ZG5MamswWUwlMjU3Q3RyJTI1M0RwbGElMjU3Q2hrJTI1M0QyMDM5OTlhNmE1NDAxZTU1ZDBmZTI0MzJlNGYyMmRmZTA1NWFmMTJk; NVADID=0A00002ZKAzydnLjk0YL; NA_CO=ct%3Dlhx2qplk%7Cci%3D0A00002ZKAzydnLjk0YL%7Ctr%3Dpla%7Chk%3D203999a6a5401e55d0fe2432e4f22dfe055af12d%7Ctrx%3Dundefined; wcs_bt=s_56c9031416c7c56b:1684655796; NNB=3PM2SQOU6VFWI; nx_ssl=2; ASID=afc335a00000018808d00bf600000053; _ga=GA1.2.1183798841.1684295968; page_uid=ibE36lp0JXossUYIP+dssssssfC-517358; _naver_usersession_=qnjnEOyKl+L/Qci8bgYJXiM2',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

for i in range(len(url_li)):
    test = requests.get(url_li[i][0], cookies=cookies, headers=headers)
    sleep(randrange(1, 4)+random())
    html = test.text
    soup = bs(html, 'html.parser')
    product_no = json.loads(soup.select_one('html > body > script').get_text()[27:])['product']['A']['productNo']
    print(product_no)
    url_li[i].append(product_no)

cookies = {
    'NNB': '3PM2SQOU6VFWI',
    'nx_ssl': '2',
    'ASID': 'afc335a00000018808d00bf600000053',
    '_ga': 'GA1.2.1183798841.1684295968',
    'page_uid': 'ibE36lp0JXossUYIP+dssssssfC-517358',
    '_naver_usersession_': 'v7G9EUOz7Aa/FsXcLRT9zv6k',
}

headers = {
    'authority': 'smartstore.naver.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'NNB=3PM2SQOU6VFWI; nx_ssl=2; ASID=afc335a00000018808d00bf600000053; _ga=GA1.2.1183798841.1684295968; page_uid=ibE36lp0JXossUYIP+dssssssfC-517358; _naver_usersession_=v7G9EUOz7Aa/FsXcLRT9zv6k',
    'origin': 'https://smartstore.naver.com',
    'referer': 'https://smartstore.naver.com/gomunara/products/4959024935?n_media=11068&n_query=%EC%9A%94%EA%B0%80%EB%A7%A4%ED%8A%B8&n_rank=1&n_ad_group=grp-a001-02-000000011770291&n_ad=nad-a001-02-000000096073757&n_campaign_type=2&n_mall_id=orientbr1&n_mall_pid=4959024935&n_ad_group_type=2&NaPm=ct%3Dlhx2qplk%7Cci%3D0A00002ZKAzydnLjk0YL%7Ctr%3Dpla%7Chk%3D203999a6a5401e55d0fe2432e4f22dfe055af12d',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

json_data = {
    'page': 1,
    'pageSize': 20,
    'merchantNo': '500036051',
    'originProductNo': '4942461452',
    'sortType': 'REVIEW_RANKING',
}

f = open('ns_요가삭스_review_txt.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow(['content', 'star_rating', 'review_ranking_score'])

for urls in url_li:
    url = urls[0]
    mall_no = urls[1]
    p_no = urls[2]
    json_data['merchantNo'] = str(mall_no)
    json_data['originProductNo'] = p_no
    for i in range(1, 6):
        json_data['page'] = i
        res = requests.post(
            'https://smartstore.naver.com/i/v1/reviews/paged-reviews',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        sleep(randrange(1, 4)+random())
        try:
            review_json = json.loads(res.text)
            review_json = review_json['contents']
            for item in review_json:
                cont = item['reviewContent']
                cont = cont.replace('\n', ' ').replace(',', ' ')
                sr = item['reviewScore']
                rs = item['reviewRankingScore']
                wr.writerow([cont, sr, rs])
        except:
            pass

f.close()
