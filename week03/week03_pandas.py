#딕셔너리 컬럼이름으로 사용됨 , 밸류값으로 리스트 사용됨
# df = pd.DataFrame(
#     {"a" : [4, 5, 6],
#      "b" : [7, 8, 9],
#      "c" : [10, 11, 12]},
#     index = [1, 2, 3])


import pandas as pd

df1 = pd.DataFrame(
    {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9],

    }
    , index=['1', '2', '3']
)
print(df1)

df2 = pd.DataFrame(
    [
        [1,4,7],
        [2,5,8],
        [3,6,9],
    ]
    ,index=[1, 2, 3],columns=['A', 'B', 'C']
    )
# 파이썬은 순서가 바뀌어도 괜찮다 index columns
print(df2)

#함수를 연속적으로 코딩하는 것이 메소드 체이닝
#melt - reshape 함수
df3 = pd.melt(df2).rename(columns={
        'variable':'var',
        'value':'val'
    }).query('val > 5')

print(df3)