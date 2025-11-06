import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_diabetes


# 당뇨병 데이터셋 로딩
#나이 , 성별, 체질량지수, 평균혈압 , 총콜레스테롤 , 저밀도지단백콜레스테롤, 고밀도지단백콜레스테롤, 트리글리세라이드, 혈청인슐린, 혈당
#LDL(s2) (나쁨), HDL(s3) (좋음), TC(s4) (s1/s3), LTG(s5) (중성지방), GLU(s6) (공복혈당)
diabetes = load_diabetes()
#print(diabetes.feature_names)
#print(diabetes)
#print(type(diabetes))
#print(diabetes.info()) # 오류 : 판다스 배열이 아님
#print(diabetes.target) # 당뇨병 진행 정도 수치

df_diabetes = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
print(df_diabetes.tail())



