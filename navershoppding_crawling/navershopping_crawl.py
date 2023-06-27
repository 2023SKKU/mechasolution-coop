import requests
from bs4 import BeautifulSoup as bs
import json
import csv
from time import sleep
from random import random, randrange
import math
import pandas as pd

cf = open('ns_reviewss2.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(cf)
wr.writerow(['userid', 'product_category', 'productName', 'content', 'star_rating', 'review_ranking_score', 'time'])

# 여기를 자기 키워드로 바꾸세요
item_li = ['세제', '런닝머신', '역류방지쿠션', '여행용캐리어', '빨래건조기', '인테리어소품', '슬립온', '차키케이스', '파라핀치료기',
           '남자팬티']
for item_name in item_li:
    print(item_name)
    '''
    f = open('ns_{}_url.csv'.format(item_name), 'w', encoding='utf-8', newline='')
    wr2 = csv.writer(f)
    wr2.writerow(['url', 'chnlseq'])
    url = 'https://search.shopping.naver.com/search/all?frm=NVSHCHK&origQuery={}&pagingIndex=1&pagingSize=40&productSet=checkout&query={}&sort=review&timestamp=&viewType=list'.format(item_name, item_name)

    res = requests.get(url)
    html = res.text
    soup = bs(html, 'html.parser')
    item_json = json.loads(soup.select_one('#__NEXT_DATA__').get_text())['props']['pageProps']['initialState']['products']['list']
    item_href = []
    channel_seq = []
    cnt = 0
    now_mode = 'smartstore'
    for i in item_json:
        print(cnt, i)
        if cnt == 3:
            break
        item = i['item']
        try:
            r = requests.get(item['adcrUrl'])
            sleep(randrange(0, 3)+random())
            print(r.url)
            if r.url[8:13] == 'smart':
                now_mode = 'smartstore'
            elif r.url[8:13] == 'brand':
                now_mode = 'brand'
            else:
                continue
            cnt += 1
            #url_li.append([url, int(item['chnlSeq'])])
            wr2.writerow([r.url, item['chnlSeq']])
        except:
            try:
                r = requests.get(item['crUrl'])
                sleep(randrange(0, 3) + random())
                print(r.url)
                if not r.url[8:13] == 'smart' and not r.url[8:13] == 'brand':
                    continue
                cnt += 1
                # url_li.append([url, int(item['chnlSeq'])])
                wr2.writerow([r.url, item['chnlSeq']])
            except:
                pass

    f.close()
    '''

    urls = pd.read_csv('ns_{}_url.csv'.format(item_name))
    url_li = []


    def get_url_li(x):
        url = x['url']
        chnlseq = x['chnlseq']
        if not url[8:13] == 'smart' and not url[8:13] == 'brand':
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

    now_mode = 'smartstore'
    for i in range(len(url_li)):
        try:
            test = requests.get(url_li[i][0], cookies=cookies, headers=headers)
            if test.url[8:13] == 'brand':
                now_node = 'brand'
            # print(test.status_code)
            st = randrange(0, 3)+random()
            sleep(st)
            html = test.text
            soup = bs(html, 'html.parser')
            product_no = json.loads(soup.select_one('html > body > script').get_text()[27:])['product']['A']['productNo']
            product_name = soup.select_one('h3').get_text()
            print(product_no, product_name)
            url_li[i].append(product_no)
            url_li[i].append(product_name)
        except Exception as e:
            print(e)
    cookies = {
        'NNB': '3PM2SQOU6VFWI',
        'nx_ssl': '2',
        'ASID': 'afc335a00000018808d00bf600000053',
        '_ga': 'GA1.2.1183798841.1684295968',
        'nid_inf': '-1253602480',
        'NID_AUT': '0BsaLEzG4vh+eAaiwsuc7/L+9zhdTfghJzY8zCtvOi3++PpMhBixLYqZDNnYVlUy',
        'NID_JKL': 'WdNIOVVJc6f0f1z6NEQ1UJVXPrTRaPofPux4pFNt+kg=',
        'NID_SES': 'AAABpxy/j7trLyz5Duj7vI6E8YU41OUCPFc8m0IrGl6y+23NaCMM1YcdE1azZgel8t8t1Kpcb6lxVzeRVNDgT4+CCR7gMmi3mvujgVBjtldComsLVJE+AJ8Jj6LixSSqJlHln7DklgwQQ2wur8gbRKqRnlai9MoNIJlWR7735G386NxbVRzMnQr4yVChZcbuTedl0JM6YIcNxPCvKym2KRsW3K6RAHlX1RV0I2h/ey9HPxy0NTTFcxjxX4j/rS0r7mcN8ztSPPew0WwnO+JBd2f/eIn+ToAnk21ppldBog7FB/1YFcNUAHtcdi0aNQqKUBa6G7HViaCKmFtjheBiIZVt0Rk8KbcUfFCW3fTQpXopfOGjSpZRz0gseWvTGnR8VckmLcDsednGfEti23QA4AXls8GMSkizQ8adcw/I8avlTbeyfoaoafUiBOmRyzLycHgQYsrkUv6YNgKVwxYRKe4KKto+bIZ00lHzixrbyeCpv5T4UDCdK1As+fQY5gLZKv70D4xv2NOOfnHlQNqIwXuef7mFWjw2if9CJdlgaxlHPFNHLtQG0HnQM9gwWfQa5IOMhQ==',
    }

    headers = {
        'authority': '{}.naver.com'.format(now_mode),
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': 'NNB=3PM2SQOU6VFWI; nx_ssl=2; ASID=afc335a00000018808d00bf600000053; _ga=GA1.2.1183798841.1684295968; nid_inf=-1253602480; NID_AUT=0BsaLEzG4vh+eAaiwsuc7/L+9zhdTfghJzY8zCtvOi3++PpMhBixLYqZDNnYVlUy; NID_JKL=WdNIOVVJc6f0f1z6NEQ1UJVXPrTRaPofPux4pFNt+kg=; NID_SES=AAABpxy/j7trLyz5Duj7vI6E8YU41OUCPFc8m0IrGl6y+23NaCMM1YcdE1azZgel8t8t1Kpcb6lxVzeRVNDgT4+CCR7gMmi3mvujgVBjtldComsLVJE+AJ8Jj6LixSSqJlHln7DklgwQQ2wur8gbRKqRnlai9MoNIJlWR7735G386NxbVRzMnQr4yVChZcbuTedl0JM6YIcNxPCvKym2KRsW3K6RAHlX1RV0I2h/ey9HPxy0NTTFcxjxX4j/rS0r7mcN8ztSPPew0WwnO+JBd2f/eIn+ToAnk21ppldBog7FB/1YFcNUAHtcdi0aNQqKUBa6G7HViaCKmFtjheBiIZVt0Rk8KbcUfFCW3fTQpXopfOGjSpZRz0gseWvTGnR8VckmLcDsednGfEti23QA4AXls8GMSkizQ8adcw/I8avlTbeyfoaoafUiBOmRyzLycHgQYsrkUv6YNgKVwxYRKe4KKto+bIZ00lHzixrbyeCpv5T4UDCdK1As+fQY5gLZKv70D4xv2NOOfnHlQNqIwXuef7mFWjw2if9CJdlgaxlHPFNHLtQG0HnQM9gwWfQa5IOMhQ==',
        'origin': 'https://smartstore.naver.com',
        'referer': 'https://smartstore.naver.com/dederit/products/8118956887',
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
        'sortType': 'REVIEW_SCORE_ASC',
    }

    for urls in url_li:
        print(urls)
        try:
            url = urls[0]
            mall_no = urls[1]
            p_no = urls[2]
            json_data['merchantNo'] = str(mall_no)
            json_data['originProductNo'] = p_no
            i = 1
            total_review_num = 20
            while i <= math.ceil(total_review_num/20):
                if i > 500:
                    break
                json_data['page'] = i
                res = requests.post(
                    'https://{}.naver.com/i/v1/reviews/paged-reviews'.format(now_mode),
                    cookies=cookies,
                    headers=headers,
                    json=json_data,
                )
                print(i)
                #print(res.text)
                if res.text == 'OK':
                    break
                review_json = json.loads(res.text)
                review_cont = review_json['contents']
                total_review_num = int(review_json['totalElements'])
                i += 1
                for item in review_cont:
                    userid = item['writerMemberId']
                    cont = item['reviewContent']
                    review_time = item['createDate']
                    cont = cont.replace('\n', ' ').replace(',', ' ')
                    sr = item['reviewScore']
                    rs = item['reviewRankingScore']
                    wr.writerow([userid, item_name, urls[3], cont, sr, rs, review_time])
        except Exception as e:
            print(e)

cf.close()
