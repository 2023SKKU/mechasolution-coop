import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./naver_goods.csv')

corr_li = []
item_li = ['우비', '크록스', '써큘레이터', '에어컨', '선풍기', '닭가슴살', '방향제', '텀블러', '보조배터리', '사과', '탄산수', '텐트', '자전거', '무선청소기', '에어프라이어', '모기퇴치제', '캡슐세제', '매트리스', '전신거울', '칫솔', '청바지', '우산꽃이', '신발건조기', '우산비닐', '물받이', '옷걸이', '장갑', '모기장', '원피스', '담요', '라면', '스마트폰', '핸드폰케이스', '그립톡', '요가매트', '샴푸', '덤벨']
for col in df.columns.to_list()[2:]:
    corr_val = df['우산'].corr(df[col], method='pearson')
    corr_li.append(corr_val)

print(corr_li)

corr_series = pd.Series(corr_li, index=item_li)
print(corr_series.sort_values(ascending=False))

