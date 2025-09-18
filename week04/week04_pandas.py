import numpy as np
import pandas as pd
import seaborn as sns

mpg = sns.load_dataset("mpg")
print(mpg.value_counts())#

df = pd.DataFrame({
    'city': ['anyang', 'seoul', 'seoul', 'anyang','seoul', 'incheon'],
    'name': ['tom','jerry','park','kim','park','lee'],
    },index = [1,2,3,4,5,6]
)
print(df)
# print(df.value_counts()) # index를 제외한 모든 컬럼의 값이 동일한 행의 개수를 세어줌 즉 중복값
# print(df.shape) # (6, 2)
print(df['city'].nunique()) # 도시가 몇개인지 세기 # 3

