import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sklearn

%matplotlib inline
from pylab import rcParams
rcParams['figure.figsize'] = 15, 10

"""Import Data"""
df = pd.read_csv('data/mall_customers.csv')
df.describe()
df.columns
# Index(['CustomerID', 'Genre', 'Age', 'Annual Income (k$)',
#        'Spending Score (1-100)'],
#       dtype='object')

df.head()

"""One Continuous Variable - Histogram / Boxplot"""
sns.distplot(df['Age'])
plt.show()

sns.distplot(df['Age'], kde=False)
plt.show()

sns.catplot(y='Age', data = df, kind = 'box')
plt.show()


"""Two Continuous Variables - Scatter"""
sns.relplot(x="Annual Income (k$)", y="Spending Score (1-100)", data = df)
sns.relplot(x="Annual Income (k$)", y="Spending Score (1-100)", hue="Genre", size="Age",sizes=(20, 200), data = df)


"""One Categorical Variables - Bar/Pie"""
sns.catplot(x = 'Genre', kind ='count', data = df)
bins = pd.IntervalIndex.from_tuples([(15, 24), (25, 34), (35, 44), (45, 54), (55, 64), (65, 74)])
df['Age (bin)'] = pd.cut(df['Age'], bins)
sns.catplot(x = 'Age (bin)', kind ='count', data = df)

"""Two Categorical variables - Side-by-side Bar/StackedBar"""
df[['Age', 'Age (bin)']]
sns.catplot(x = 'Age (bin)', kind ='count', hue = 'Genre',data = df)

"""One Continuous and One Categorical Variables - Boxplot"""
sns.catplot(y='Age', x= 'Genre', data = df, kind = 'box')
plt.show()

"""Save Plot"""
fig = sns.catplot(y='Age', x= 'Genre', data = df, kind = 'box')
fig.savefig('image')



""""Stock Price Case Study"""
# Downloading price data
from yahoo_fin.stock_info import *
nflx = get_data("nflx")
nflx.head()
nflx.tail()

# You can also pull data for a specific date range, like below:
nflx = get_data("nflx", start_date = "01/01/2019", end_date = "12/10/2019")
aapl = get_data("aapl", start_date = "01/01/2019", end_date = "12/10/2019")
amzn = get_data("amzn", start_date = "01/01/2019", end_date = "12/10/2019")

nflx = nflx[['close', 'volume']].rename(columns = {'close': 'NFLX Close', 'volume':'NFLX Volume'})
aapl = aapl[['close', 'volume']].rename(columns = {'close': 'AAPL Close', 'volume':'AAPL Volume'})
amzn = amzn[['close', 'volume']].rename(columns = {'close': 'AMZN Close', 'volume':'AMZN Volume'})


df = pd.concat([nflx, aapl, amzn], axis = 1)
df = df.reset_index()
df.head()

sns.lineplot(x="date", y="NFLX Close", data = df)
plt.show()

sns.lineplot(x="date", y="NFLX Close", data = df, label = 'NFLX')
sns.lineplot(x="date", y="AAPL Close", data = df, label = 'AAPL')
sns.lineplot(x="date", y="AMZN Close", data = df, label = 'AMZN')
plt.show()

df = df.set_index('date')
prices_df = df[['NFLX Close', 'AAPL Close', 'AMZN Close']].unstack().reset_index()
prices_df.head()
prices_df.columns = ['Stock', 'Date', 'Price']
sns.lineplot(x="Date", y="Price", hue="Stock", data = prices_df)
sns.catplot(x="Stock", y="Price", data = prices_df, kind = 'box', height = 8, aspect=1.5)
