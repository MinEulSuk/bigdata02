import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print(sns.get_dataset_names())


titanic = sns.load_dataset('titanic')
# print(titanic.head())
# print(titanic.describe())

#print(titanic[titanic['age'] <= 15])

#nlagrest를 통해 나이가 많은 5명 출력
print(titanic.nlargest(5, 'age'))



