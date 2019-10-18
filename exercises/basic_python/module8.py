import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sklearn

"""Import Data"""
df = pd.read_csv('data/mall_customers.csv')
df = pd.read_excel('data/mall_customers.xlsx')

"""Data Frame Attributes"""
df.shape
df.columns
df.info()
df['Age'].mean()
df.describe(include = 'all')
df['Genre'].value_counts()

"""Head and Tail"""
df.head()
df.tail()

"""Select Column Data"""
df['Age']
df[['Genre', 'Age']]

"""Filtering the DataFrame"""
male_df = df[df['Genre'] == 'Male']

"""Export CSV Data"""
male_df.to_csv('data/mall_customers_male.csv')
