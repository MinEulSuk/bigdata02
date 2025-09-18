import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('savant_data.csv')

#print(df.info())
#print(df['player_name'])
df_new = df[['player_id','player_name','total_pitches','velocity','hrs','so','bb']]
#print(df_new.head(5))
#print(df_new.query('player_name == "Ohtani, Shohei"'))
#print(df_new.sort_values('velocity', ascending=False).head(10))
#print(df_new.sort_values('hrs', ascending=False).head(10))

print(df_new.query('player_name == "Ohtani, Shohei"'))
print(df_new.describe())
#ohtani = df_new.query('player_name == "Ohtani, Shohei"')
#plt.title('Ohtani, Shohei',fontsize=20,fontweight='bold')
#plt.xlabel('Velocity',fontsize=14)
#plt.ylabel('Total Pitches',fontsize=14)
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)
#plt.show()
#문제 total_pitches가 1000이 넘는 선수는 몇명인가?
#해결 과정 : df_new
#query로도 똑같이 처리할 수 있음
print(len(df_new[df_new['total_pitches'] >1000]))
# plt.figure(figsize=(10,5))
# plt.boxplot(df_new['total_pitches'])
# plt.show()
