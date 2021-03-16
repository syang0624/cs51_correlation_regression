#import all the necessary libraries

%matplotlib inline
import pandas as pd
import numpy as np
from scipy import stats
#from scipy.stats import linregress
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True, font_scale = 1.2)
sns.set_style("whitegrid")
plt.rcParams.update({'font.size': 14})
import os #install statsmodels
os.system('pip install statsmodels')
import statsmodels.api as statsmodels # useful stats package with regression functions
import statsmodels.formula.api as smf


#import the data set

df = pd.read_csv('kc_house_data.csv')
print(df)
data_frame = pd.DataFrame(['Living Area (sqft)','Price ($ in millions)'])
price = df["Price ($ in millions)"]
living_area = df["Living Area (sqft)"]

z_scores = stats.zscore(df) #calculate z-scores of df'

abs_z_scores = np.abs(z_scores)
filtered_entries = (abs_z_scores < 3).all(axis=1)
new_df = df[filtered_entries] #eliminate the outliers that are more than three SDs away

print(new_df)
new_df.head()
new_price = new_df["Price ($ in millions)"]
new_living_area = new_df["Living Area (sqft)"]
