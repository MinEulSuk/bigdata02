import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

wh = pd.read_csv('wh.csv')
# new_wh = wh.query('Weight<390') # 이상치 제거 버전
# print(new_wh.info())
# print(new_wh.describe())

criteria = wh['Weight'].quantile(0.9999) # 99.99% 데이터 지점
print(criteria)
print(round(criteria,1))#255.9
new_wh = wh[wh['Weight'] < criteria]
print(new_wh.info())

