import pandas as pd

df4 = pd.DataFrame({
    'date':['2025-09-11','2025-09-11','2025-09-12','2025-09-13 '],
    'city':['서울', '안양', '서울', '안양'],
    'tmp':[23, 22, 24, 22]},
    index=[1, 2, 3, 4]
)
print(df4)
# df7 = df4.drop(columns=['date','city']) #drop specific columns
# print(df7)
# df8 = df4[df4.tmp <= 23]
# print(df8)
#df8 = df4.duplicated() # 중복값 찾기
#데이터 분석을 할때 결측값이 반드시 있기때문에 생각을 해야함
#pivot함수를 사용했을때 결측값이 생긴다.
#결측치 처리에대한 대처가 필수불가결하다.

df6 = df4.pivot(index='date',)
print(df8)