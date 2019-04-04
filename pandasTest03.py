import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# csv 파일을 pandas를 사용하여 DataFrame으로 만든다.
df = pd.read_csv("Data/scores.csv")

# key를 name으로 지정하고 df에서 name을 지운다.
df.index = df['name']
del df['name']
print(df)

# henry의 정보를 출력해보자
print(df.loc['henry'])
print(df.loc['henry'].values)
print(df.iloc[9])

# andrew 부터 paul 까지의 정보를 출력
print(df.loc['andrew':'paul'])
print(df.iloc[1:7])

# adam , dan , walter의 정보를 출력
print(df.loc[['adam','dan','walter']])
print(df.iloc[[0,4,7]])
ps = ['adam','dan','walter']
print(df.loc[ps])

# 앞에서 5번째 학생들의 국어점수를 춤력
print(df.loc[:'dan']['kor'])
print(df.iloc[:5]['kor'])
print(df.loc[:'dan','kor'])

# 앞에서 5번쨰 학생들의 국어 수학점수를 출력
print(df.iloc[:5][['kor','mat']])
print(df.loc[:'dan',['kor','mat']])

# adam dan walter 의 bio를 제외한 과목의 점수를 출력
print(df.loc[['adam','dan','walter']][['kor','eng','mat']])
print(df.loc[['adam','dan','walter']].drop('bio',axis=1))
print(df.loc[['adam','dan','walter'],:'mat'])

names = ['adam','dan','walter']
subjects = ['kor','eng','mat']
print(df.loc[names,subjects])
print(df.loc[names],[subjects])

name = [0,4,7]
print(df.iloc[name,1:-1])



