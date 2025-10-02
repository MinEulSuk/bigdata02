import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

# print(df.head())
# print(df.info())
# print(df.describe())

# plt.figure(figsize=(8,4))
# sns.histplot(data=df, x="age", bins=16, kde=True)
# plt.ylabel("Frequency")
# plt.xlabel("Age")
# #plt.tight_layout()
# plt.title("Age Distribution of Titanic Passengers")
# plt.show()

# plt.figure(figsize=(8,4))
# sns.countplot(data=df,x="survived")
# plt.title("Survivors vs Non-Survivors on the Titanic")
# plt.ylabel("Count")
# plt.xlabel("Survived (0 = No, 1 = Yes)")
# #plt.tight_layout()
# plt.show()

# plt.figure(figsize=(8,4))
# sns.countplot(data=df,x="class",order=["First","Second","Third"])
# plt.title("Passenger Count by Class")
# plt.xlabel("class")
# plt.ylabel("Count")
# #plt.tight_layout()
# plt.show()

# plt.figure(figsize=(8,4))
# sns.countplot(data=df,x="sex",hue='survived')
# #남녀로 구분하고 생존자 수를 막대그래프로 표현
# plt.xlabel("sex")
# plt.ylabel("Count")
# #plt.tight_layout()
# plt.show()

# plt.figure(figsize=(8,4))
# sns.countplot(data=df,x="sex",hue='survived')
# #남녀로 구분하고 생존자 수를 막대그래프로 표현
# plt.legend(loc="upper right",title='Survived', labels=['No', 'Yes'])
# plt.xlabel("sex")
# plt.ylabel("Count")
# #plt.tight_layout()
# plt.show()

# plt.figure(figsize=(8,4))
# sns.boxplot(data=df,x="class",y="age",order=["First","Second","Third"])
# plt.title("Fare Distribution by Passenger Class")
# plt.xlabel("class")
# plt.ylabel("Age")
# plt.tight_layout()
# plt.show()

# plt.figure(figsize=(8,4))
# sns.violinplot(data=df,x="survived",y="age")
# plt.title("Age Distribution by Survival Status")
# plt.xlabel("Survived (0 = No, 1 = Yes)")
# plt.ylabel("age")
# #plt.tight_layout()
# plt.show()

plt.figure(figsize=(8,4))
sns.catplot(data=df,x="class",y="survived",kind="count",order=["First","Second","Third"],hue="sex")
plt.title("Age Distribution by Survival Status")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("age")
#plt.tight_layout()
plt.show()