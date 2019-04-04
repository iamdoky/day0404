# numpy     배열의 조작을 편리하게
# pandas    데이터프레임의 조작을 편리하게
# 머신러닝을 위한 많은 라이브러리들이 상대하는 데이터형태가 numpy . pandas를 취급한다.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Pandas 자료구조
# Series        --> 1차원 배열
# DataFrame     --> 2차원 배열

# 파이썬 기본배열로 Pandas 1차원 배열로 만들어보자
# a = [1,2,3,4,5]
# arr = pd.Series(a)
# print(a)
# print(arr)
# print(type(a))
# print(type(arr))


# Pandas의 1차원 배열인 Series를 파이썬 배열로 변경
# arr = pd.Series(['민방위','교육','센터','사이버'])
# print(arr)
# print(type(list(arr)))

# 설명서에서 Serire는 Pandas에서 1차원 배열을 취급한다라고 되어 있기
# Seires는 만들떄 2차원 배열을 매개변수로 주면 어떤일이????

# arr = pd.Series([[['문자열',2,3],[4,5,6]],[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# arr = pd.Series([['민방위','교육','센터','사이버'],['민방위','교육','센터','사이버'],['민방위','교육','센터','사이버'],['민방위','교육','센터','사이버'],])
# print(arr)
# 키와 벨류가 한쌍으로 되어있다. map과 비슷한 모양
# 키를 부여하지 않으면 차례대로 index가 부여되며 key를 부여할 수 있따
# a = pd.Series([5,9,3,2,8])
# print(a.values)
# print(type(a.values))
# print(a.index)
# 키를 부여한다. index = ['키2','키2' ...] 생략 시 차례대로 index가 부여된다.
# 키 값으로 데이터에 접근할 수 있다.. ==> 직관적이다.
# 키 값을 부여했더라도 index로도 접근가느하다.
# a = pd.Series([5,6,3,2,1], index=['김경민','오상훈','이성기','정연미','김도희'])
# keys = a.index
# for key in keys:            # Series의 키값으로 모두 가져온다.
#     print(key, a[key])      # Key의 개수만큼 반복 수행하여 각 요소의 key의 value를 출력

# print(a['김도희'])
# print(a[0])
# print(a[-1])
# print(a.index)

# Pandas의 Series는 파이썬 배열을 갖고 Key값을 부여해 직관적으로 접근할 수 있다.
# Python Dictionary를 갖고도 Series를 만들 수 있는지 실험해보자.

a = {'김경민':5,'오상훈':9,'이성기':3,'김도희':10,'박민서':12,}
s = pd.Series(a)
print(s)