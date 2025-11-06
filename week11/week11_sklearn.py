import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_diabetes, load_breast_cancer

cancer = load_breast_cancer()
#print(cancer)
#print(cancer.target) # 0 : 악성 1 : 양성
df_cancer = pd.DataFrame(data=cancer.data, columns=cancer.feature_names)
df_cancer['target'] = cancer.target
#print(df_cancer.tail(3))
#print(df_cancer.info())

plt.figure(figsize=(10, 6))
sns.boxplot(data=df_cancer, x='target', y='mean radius')

plt.title('Boxplot of Mean Radius by Cancer Type (0: Malignant, 1: Benign)')

plt.xlabel('Target')
plt.ylabel('Mean Radius')
plt.show()