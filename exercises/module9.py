import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sklearn

%matplotlib inline

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
sns.relplot(x="Annual Income (k$)", y="Spending Score (1-100)", data = df);
sns.relplot(x="Annual Income (k$)", y="Spending Score (1-100)", hue="Genre", size="Age",sizes=(20, 200), data = df);


"""One Categorical Variables - Bar/Pie"""
sns.catplot(x = 'Genre', kind ='count', data = df)

"""Two Categorical variables - Side-by-side Bar/StackedBar"""
bins = pd.IntervalIndex.from_tuples([(15, 24), (25, 34), (35, 44), (45, 54), (55, 64), (65, 74)])
df['Age (bin)'] = pd.cut(df['Age'], bins)
df[['Age', 'Age (bin)']]
sns.catplot(x = 'Age (bin)', kind ='count', hue = 'Genre',data = df)

"""One Continuous and One Categorical Variables - Boxplot"""
sns.catplot(y='Age', x= 'Genre', data = df, kind = 'box')
plt.show()

"""Save Plot"""
fig = sns.catplot(y='Age', x= 'Genre', data = df, kind = 'box')
fig.savefig('image')
