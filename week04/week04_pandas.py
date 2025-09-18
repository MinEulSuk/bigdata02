import numpy as np
import pandas as pd
import seaborn as sns
#결측값을 어떻게 추출할 거냐?
mpg = sns.load_dataset('mpg')
# print(mpg.isnull().sum()) #컬럼별 결측값 개수
# print(mpg.isnull()) #각 데이터별 결측값 여부
# print(mpg[mpg['horsepower'].isnull()]) #결측값이 하나라도 있는 행 추출
mpg_nan = mpg[mpg['horsepower'].isnull()]
print(mpg_nan[['mpg','horsepower','displacement','origin']]) #결측값이 있는 행의 특정 컬럼들만 추출