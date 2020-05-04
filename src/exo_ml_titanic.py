import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

dataframe = pd.read_csv('titanic.csv', sep=',')

X, y = dataframe.drop(['survived'], axis=1), dataframe[['survived']]
X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.2, random_state=42)

##Data preprocessing##
categorical_columns = ['pclass', 'sex', 'embarked', 'class', 'who', 'deck', 'embark_town', 'alive']
numerical_columns = ['age', 'sibsp', 'parch', 'fare']

categorical_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='constant', fill_value='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

numerical_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='mean'))
])

preprocessing = ColumnTransformer(
    [('cat', categorical_pipe, categorical_columns),
     ('num', numerical_pipe, numerical_columns)])

preprocessing.fit(X_train)
X_train_pret = preprocessing.transform(X_train)
X_test_pret = preprocessing.transform(X_test)

###Get column names#
categorical_pipe.fit(X_train[categorical_columns])
categorical_name = categorical_pipe.steps[1][1].get_feature_names(categorical_columns)

from sklearn.ensemble import GradientBoostingClassifier
gbc = GradientBoostingClassifier()
gbc.fit(X_train_pret, y_train)
pred_train = gbc.predict(X_train_pret)