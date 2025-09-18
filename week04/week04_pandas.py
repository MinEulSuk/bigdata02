import numpy as np
import pandas as pd
import seaborn as sns

mpg = sns.load_dataset("mpg")
# print(mpg.info())

# print(mpg.head(3))
# print(mpg.tail(3))
# mpg_desc = mpg.sort_values(by=['mpg'],ascending = False)
# print(mpg_desc)
#print(mpg.describe())

print(mpg[mpg['mpg'] > 40]) # 조건식으로도 가능 이게 쿼리문보다 빠름
print(mpg.query('mpg > 40')) # 쿼리문으로도 가능 이게 조건문보다 느림 함수호출에 걸리는 시간때문에
# print(mpg.drop_duplicates()) # 칼럼 기준으로 중복값 없애기

#print(mpg.sample(n = 5)) # 랜덤으로 5개 행 출력
#print(mpg.nlargest(5, 'mpg')) # mpg 칼럼 기준으로 큰값 5개 출력
#print(mpg.nsmallest(5, 'mpg')) # mpg 칼럼 기준으로 작은값 5개 출력

#print(mpg[['displacement', 'horsepower','weight','acceleration','model_year']]) # 너무 길다
#slice로 처리하면 추출할 수 있다.
#print(mpg.iloc[:,2:7]) # 2~6까지 출력 # iloc는 위치기반 인덱싱 위에 것과 동일하게 작동
#print(mpg.loc[:, 'displacement':'model_year']) # loc는 라벨기반 인덱싱 - 가독성이 좋음

#print(mpg.filter(regex='.me')) # me로 끝나는 칼럼명 추출

