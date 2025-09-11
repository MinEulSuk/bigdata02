import pandas as pd

df4 = pd.DataFrame({
    'date':['2025-09-11','2025-09-11','2025-09-12','2025-09-13 '],
    'city':['서울', '안양', '서울', '안양'],
    'tmp':[23, 22, 24, 26]},
    index=[1, 2, 3, 4]
)
print(df4)
df9 =df4.sample(n=2) # 중복되지않은 row 2개 랜덤하게 추출
print(df9)
df10 = df4.nsmallest(2,'tmp')  # 가장 작은 값 두개 nlagrest면 큰값 두개
print(df10)
#tail 원본기준 아래서 n개  head 원본기준 위에서 n개 기본5개

