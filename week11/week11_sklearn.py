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
#print(df_diabetes.tail())

df_diabetes['target'] = diabetes.target # 당뇨병 진행 정도 수치 추가
print(df_diabetes.tail())# 모든 컬럼이 스케일링 되어있음 정규분포를 기준으로 스케일링
print(df_diabetes['age'].describe()) # 나이 컬럼 통계량 확인

#시각화를 위한 matplotlib
fig,axes = plt.subplots(2,2, figsize=(12,8))

axes[0,0].hist(df_diabetes['s1'], bins=20) # TC 빈도수 체크 히스토그램
axes[0,0].set_title('Diabetes Data : TC Distribution')
axes[0,0].set_xlabel('TC')
axes[0,0].set_ylabel('Frequency')
axes[0,0].grid()

axes[0,1].boxplot([df_diabetes['s1'],df_diabetes['s2'], df_diabetes['s3']])
axes[0,1].set_title('Diabetes Data : TC, LDL, HDL Boxplot')
axes[0,1].set_xticklabels(['TC','LDL','HDL'])
axes[0,1].grid()

axes[1,0].scatter(df_diabetes['s1'], df_diabetes['target'],color='coral', alpha=0.6)
axes[1,0].set_title('Diabetes Data : TC vs Target')
axes[1,0].set_xlabel('TC')
axes[1,0].set_ylabel('Target')
axes[1,0].grid()

axes[1,1].scatter(df_diabetes['bmi'], df_diabetes['target'],color='green', alpha=0.6)
axes[1,1].set_title('Diabetes Data : bmi vs Target')
axes[1,1].set_xlabel('bmi')
axes[1,1].set_ylabel('Target')
axes[1,1].grid()




plt.show()






