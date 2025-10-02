import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
#print(df.groupby("sex")["survived"].mean())
#정확하게 절반이라 femal third median 0.5
print(df.groupby(['sex', 'class'])['survived'].agg(['mean','count']))

