import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sklearn


"""Case Study: Credit Scoring"""

# Step 1: Load Data
import pandas as pd
credit = pd.read_csv('data/credit.csv')

credit.head(10)
credit.describe()
credit['Creditability'].value_counts()
y = credit['Creditability']
X = credit.drop(columns = ['Creditability'])


# Step 2: Split and Randomize Data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=33)

# Step 3 Define Classifier
from sklearn.ensemble import GradientBoostingClassifier
clf = GradientBoostingClassifier()

# Step 4 Train the Classifier
clf.fit(X_train,y_train)

# Step 5:  Evaluate the Classifier
clf.score(X_test,y_test)

# Step 6: Save the Model
import joblib
joblib.dump(clf, 'mymodel.pkl')

# Step 7: Load the Model & Prediction
clf = joblib.load('mymodel.pkl')
clf.predict(X_test)

"""Case Study: Customer Segmentation"""
customers=pd.read_csv('data/mall_customers.csv')
customers.head()
X=customers[['Annual Income (k$)', 'Spending Score (1-100)']]

from sklearn.cluster import KMeans
cluster=KMeans(n_clusters=5, random_state = 33)
cluster.fit(X)
labels=cluster.labels_
centroids=cluster.cluster_centers_

X['label'] = labels
X.head()

label_color_map = {
    0: 'r',
    1: 'b',
    2: 'g',
    3: 'c',
    4: 'm'
}

# Visualising the clusters
fig = plt.figure(figsize=(8,6))
for label, color in label_color_map.items():
    plt.scatter(X[X['label'] == label]['Annual Income (k$)'],
                X[X['label'] == label]['Spending Score (1-100)'],
                s = 100, c = color,
                label ='cluster {}'.format(label))
plt.scatter(centroids[:,0],centroids[:,1],
            s = 300, c = 'yellow',
            label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Monthly Income ')
plt.ylabel('Spending Score (1-100)')
plt.legend()
fig.savefig('image')
plt.show()
