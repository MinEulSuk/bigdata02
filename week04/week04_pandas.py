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
print(mpg.info())


