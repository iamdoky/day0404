import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# DataFrame 생성하기.
# df = pd.DataFrame([[1,2,3,],[4,5,6]])
# print(df)
# print(type(df))


# csv 파일을 pandas를 사용하여 DataFrame으로 만든다.
df = pd.read_csv("Data/scores.csv")
# print(df)                 # DataFrame
# print(type(df))           # Type 확인
# print(df.columns)         # Column 확인
# print(df.index)           # Key , index 확인
# print(df.values)          # Values 확인
# print(type(df.values))    # numpy를 반환하여 준다.
# print(df['kor'])          # 국어 점수만 출력
# print(df[2])              # 오류

# Pandas의 DataFrame에서 행에 접근하려면 함수를 사용하여야 한다. => loc / iloc
# Key 값을 부여하지 않고 행에 접근하려면 index에 접근하여야 한다.
# key에 값을 부여하지 않으면 loc / iloc는 차이가 없다. 하지만
# Key 값을 부여 했다면 loc로 접근하며 그렇지 않다면 iloc를 접근한다.
print(df)
print(df.loc[2])
print(df.loc[2].values)
print(df.iloc[2].values)



