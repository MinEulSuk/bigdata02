import numpy as np
import pandas as pd
import seaborn as sns

def square(x):
    return x * x

def cube(x):
    return x * x * x

mpg = sns.load_dataset('mpg')
df1 = pd.DataFrame(
    {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9],

    }
    , index=['1', '2', '3']
)
print(df1)
print(df1.apply(square)) # 각 원소에 제곱 함수 적용
print(df1.apply(cube)) # 각 원소에 세제곱 함수 적용