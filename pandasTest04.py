import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
# scores.csv 파일을 읽어들여 학생의 이름을 index키 로 설정하고 이름 칼럼은 삭제하여 출력

df = pd.read_csv("Data/scores.csv")
df.index = df['name']
del df['name']

rc('font',family=font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name())

#  모든 학생의 국어점수를 출력
# print(df.iloc[:]['kor'])
# print(df.loc[:,'kor'])
# print(df['kor'])

# 모든과목의 점수를 출력
# print(df['kor','eng','mat','bio'])

# ben학생의 과목별 점수를 막대그래프
ben_score = np.array(df.loc['ben',['kor','eng','mat','bio']],dtype=int)
ben_col = np.array(df.columns[1:5])
# plt.bar(range(4),ben_score,)
# plt.show()

# 모든학생의 국어점수를 막대그래프로 출력
score = np.array(df['kor'])
names = np.array(df.index)
# plt.bar(range(len(score)),score)
# plt.show()

plt.subplot(211)
plt.title('벤의 점수와 모든 학생의 국어점수')
plt.bar(range(len(ben_score)),ben_score)
plt.xticks(range(len(ben_score)),ben_col,rotation="40")
plt.subplot(212)
plt.bar(range(len(score)),score)
plt.xticks(range(len(score)),names,rotation="40")
plt.savefig("student.png")
plt.show()

# plt.bar(range(len(df.index)),df['kor'])
# plt.xticks(range(len(df.index)),df.index, rotation=45)
# plt.show()

# plt.subplot(2,1,1)
# plt.bar(range(len(ben_score),ben_score))
# plt.xticks(range(len(ben_score)),ben_col, rotation=45)
# plt.subplot(2,1,2)
# plt.bar(range(len(df.index)),df['kor'])
# plt.xticks(range(len(df.index)),df.index, rotation=45)
# plt.savefig("student.png")
# plt.show()






