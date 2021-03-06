# 2016 GDP 상위 10 을 막대그래프로 출력

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc, colors

f = open("2016_GDP.txt","r",encoding='utf-8')
f.readline()
list = f.readlines()

names = []
money = []

for row in list:
    row = row.split(':')
    names.append(row[1])
    money.append(row[2].strip().replace(",",""))

money = np.array(money,dtype=int)

rc('font',family=font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name())

plt.bar(range(10),money[:10], color = colors.BASE_COLORS)
plt.title('GDP 상위 10개 국가')
plt.xticks(range(10),names[:10],rotation="90")
plt.show()