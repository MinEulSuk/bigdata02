import numpy as np
import pandas as pd
import seaborn as sns
#결측값을 어떻게 추출할 거냐?
mpg = sns.load_dataset('mpg')
# print(mpg.isnull().sum()) #컬럼별 결측값 개수
# print(mpg[mpg['horsepower'].isnull()]) #결측값이 하나라도 있는 행 추출

# 결측치 처리 #1
# mpg_drop = mpg.dropna()
# print(mpg_drop[mpg_drop['horsepower'].isnull()]) #결측값이 하나라도 있는 행 출력

# 결측치 처리 #2
# mpg = mpg.fillna(mpg['horsepower'].mean())
# print(mpg[mpg['horsepower'].isnull()]) #결측값이 하나라도 있는 행 출력

# 결측치 처리 #3 결측치가 있는 컬럼을 날려버림
#칼럼을 날리려면 빅데이터로서 필요가 없는 데이터(이름) or 결측치가 너무 많아서 어쩔 수 없이 날려야 하는 경우
mpg.drop(columns =['horsepower'], axis=1, inplace=True) #원본에 반영
print(mpg.info())


