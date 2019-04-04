import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc

def students(names):
    rc('font', family=font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name())

    df = pd.read_csv("Data/scores.csv")
    df.index = df['name']
    del df['name']
    try:
        score = np.array(df.loc[names,['kor','eng','mat','bio']],dtype=int)
        col = np.array(df.columns[1:5])

        plt.title(names+'의 점수와 모든 학생의 국어점수')
        plt.bar(range(len(score)),score)
        plt.xticks(range(len(score)),col,rotation="40")
        fname = 'static/'+names+'.png'
        plt.savefig(fname)
        plt.close()
    except KeyError:
        fname = 'no'
    return fname








