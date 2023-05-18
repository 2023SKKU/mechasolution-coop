import json
import csv
import urllib.request
client_id = "6XZbrFukBcbeIchUJqHe"
client_secret = "p4Nca6hWvN"
url = "https://openapi.naver.com/v1/datalab/search"


item_li = ['우산', '우비', '크록스', '써큘레이터', '에어컨', '선풍기', '닭가슴살', '방향제', '텀블러', '보조배터리', '사과', '탄산수', '텐트', '자전거', '무선청소기', '에어프라이어', '모기퇴치제', '캡슐세제', '매트리스', '전신거울', '칫솔', '청바지', '우산꽃이', '신발건조기', '우산비닐', '물받이', '옷걸이', '장갑', '모기장', '원피스', '담요', '라면', '스마트폰', '핸드폰케이스', '그립톡', '요가매트', '샴푸', '덤벨']

f = open('naver_goods.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow(['date']+item_li)

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")

date = []
data_li = []
flag = True
for item in item_li:
    body = "{\"startDate\":\"2023-03-01\",\"endDate\":\"2023-05-16\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\""+item+"\",\"keywords\":[\""+item+"\"]}]}"
    response = urllib.request.urlopen(request, data=body.encode("utf-8"))
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        res_json = json.loads(response_body.decode('utf-8'))

        temp = []
        for data in res_json['results'][0]['data']:
            if flag:
                date.append(data['period'])
            temp.append(data['ratio'])
        flag = False
        data_li.append(temp)
    else:
        print("Error Code:" + rescode)

print(date)
print(data_li)

for i in range(len(date)):
    temp = []
    for j in data_li:
        temp.append(j[i])
    wr.writerow([date[i]]+temp)

f.close()