import numpy as np # numerical computing 
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt #visualization
import seaborn as sns #modern visualization

import csv
import matplotlib.pyplot as plt
import random


sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (14, 8)




file_path = 'D:\\Projects\MSc\\Data Science\\20190216\Data_Set\\'
matches = pd.read_csv(file_path+'PSID.csv')

print(matches.hours)

print(list)
print(matches.hours)

labels = [ 'Red']
colours = ['red']
print(matches.describe())
hair_colour_freq = [5, 3, 2]
x_pos = np.arange(len(matches.hours))

fig, ax = plt.subplots(figsize=(7, 5))
ax.bar(x_pos, matches.hours, align='center')
