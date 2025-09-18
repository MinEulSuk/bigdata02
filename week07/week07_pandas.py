import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
plt.figure(figsize=(15,12))
plt.subplot(2,3,1)# 2 rows, 3 columns, 1st plot
sns.boxplot(data=titanic,x="survived",y="age")# 박스플롯으로 표현
plt.title('Age distribution by survival status')# 생존에 따른 나이 분포
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Age")

plt.subplot(2,3,2)# 2 rows, 3 columns, 2nd plot
sns.boxplot(data=titanic,x="sex",y="age")# 박스플롯으로 표현
plt.title('Age distribution by gender')# 성별에 따른 나이 분포
plt.xlabel("gender")
plt.ylabel("Age")

plt.subplot(2,3,3)# 2 rows, 3 columns, 2nd plot
sns.boxplot(data=titanic,x="class",y="fare")# 박스플롯으로 표현
plt.title('fare distribution by class') # 클래스에 따른 요금 분포
plt.xlabel("Passenger class")
plt.ylabel("Fare")

plt.subplot(2,3,4)# 2 rows, 3 columns, 2nd plot
sns.boxplot(data=titanic,x="survived",y="fare")# 박스플롯으로 표현
plt.title('Fare distribution by survival status')# 요금에 따른 생존 분포
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Fare")
plt.show()

plt.subplot(2,3,5)# 2 rows, 3 columns, 2nd plot
sns.boxplot(data=titanic,x="sex",y="age",hue="survived",palette="Oranges")# 박스플롯으로 표현
plt.title('age by gender and survival')# 요금에 따른 생존 분포
plt.xlabel("Gender")
plt.ylabel("Age")
#plt.legend(title='Survived', labels=["No", "Yes"])

plt.show()


