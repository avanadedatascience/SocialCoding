import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

dataframe = pd.read_csv('titanic.csv', sep=',')

X, y = dataframe.drop(['survived'], axis=1), dataframe[['survived']]
X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.2, random_state=42)

print('number of passengers in train data: ', len(y_train))
print('number of passengers in test data: ', len(y_test))
print('percentage of survived in train data: ', y_train.mean().values[0] )
print('percentage of survived in test data: ', y_test.mean().values[0] )
print('\n')
print('Statistic description of train data:')
print(X_train.describe())
print('\n')
print('Statistic description of test data:')
print(X_test.describe())