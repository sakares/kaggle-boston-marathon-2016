import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
plt.style.use('fivethirtyeight')


df = pd.read_csv('Desktop/kaggle-boston-marathon-2016/input/marathon_results_2016.csv')

top1000_runners = df[0:1000]

runners = top1000_runners


ax = sns.boxplot(x="M/F", y="Overall", data=runners)
ax = sns.stripplot(x="M/F", y="Overall", data=runners, jitter=True, edgecolor="gray")

runners.plot(kind="scatter", x="Age", y="Overall")

sns.jointplot(x="Age", y="Overall", data=runners, size=7)

sns.FacetGrid(runners, hue="M/F", size=7) \
  .map(plt.scatter, "Overall", "Age") \
  .add_legend()


sns.FacetGrid(runners, hue="M/F", size=7) \
   .map(sns.kdeplot, "Overall") \
   .add_legend()
   
   


