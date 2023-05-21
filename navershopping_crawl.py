import requests
from bs4 import BeautifulSoup as bs
import json
import csv
from time import sleep
from random import random, randrange

f = open('ns_요가_url.csv', 'w', encoding='utf-8')
wr = csv.writer(f)
wr.writerow(['url', 'chnlseq'])
url = 'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EC%9A%94%EA%B0%80%EB%A7%A4%ED%8A%B8&pagingIndex=1&pagingSize=80&productSet=total&query=%EC%9A%94%EA%B0%80%EB%A7%A4%ED%8A%B8&sort=rel&timestamp=&viewType=list'

res = requests.get(url)
html = res.text
print(html)
soup = bs(html, 'html.parser')

item_json = json.loads(soup.select_one('#__NEXT_DATA__').get_text())['props']['pageProps']['initialState']['products']['list']
item_href = []
channel_seq = []
for i in item_json:
    item = i['item']
    try:
        item['reviewCountSum']
        item['productName']
        try:
            r = requests.get(item['adcrUrl'])
            sleep(randrange(1, 4)+random())
            print(r.url)
            # item_href.append(r.url)
            # channel_seq.append(item['chnlSeq'])
            wr.writerow([r.url, item['chnlSeq']])
        except:
            r = requests.get(item['crUrl'])
            sleep(randrange(1, 4)+random())
            print(r.url)
            # item_href.append(r.url)
            # channel_seq.append(item['chnlSeq'])
            wr.writerow([r.url, item['chnlSeq']])
    except:
        pass

f.close()