import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

wh = pd.read_csv('wh.csv')
print(wh.head())
print(wh.info())
print(wh.describe())
# 파운드 ( 1 == 453.592그램) , 인치 (1 == 2.54센티미터)
print(wh.query('Weight > 350'))
print(wh[wh['Weight'] > 350]) # '' 생각해야함
