import pandas as pd

df4 = pd.DataFrame({
    'date':['2025-09-11','2025-09-11','2025-09-12','2025-09-13 '],
    'city':['서울', '안양', '서울', '안양'],
    'tmp':[23, 22, 24, 26]},
    index=[1, 2, 3, 4]
)
print(df4[['date','tmp']])
#파이썬의 정규표현식 re 공부하면 좋다.
#filter.regex < 정규표현식의 약자
# i(index) iloc는 인덱스로 확인 loc은 컬럼으로 확인
# 깊은복사는 메모리를 더 차지함
# 얕은 복사는 포인터처럼 참조하는 느낌

print(df4.iloc[1:3])
print(df4.iloc[:,[0,2]])
print(df4.iloc[1:3,[0,2]])

