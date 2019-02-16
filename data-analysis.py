# -*- coding: utf-8 -*-
import numpy as np # numerical computing 
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt #visualization
import seaborn as sns #modern visualization

#Sample

sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (14, 8)

matches = pd.read_csv('PSID.csv')

print(matches)

matches.shape
print(matches.shape)

matches.info()

matches.describe()
print(matches.describe())

matches.head(2)
#print(matches.head(2))

matches['Seq No'].max()

matches['educatn'].unique()

print(matches['educatn'].unique())

sns.countplot(x='educatn', data=matches)
plt.show()

np.random.choice(matches['Seq No'], 100)
print(np.random.choice(matches['Seq No'], 100))

