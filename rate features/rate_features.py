import pandas
import numpy as np
from sklearn.tree import DecisionTreeClassifier

data = pandas.read_csv('../titanic.csv', ',')
answer = open("rating.txt", 'w')

data = pandas.DataFrame.dropna(data.filter(['Pclass', 'Fare', 'Age', 'Sex', 'Survived']))

y = data['Survived']

data = data.filter(['Pclass', 'Fare', 'Age', 'Sex'])
data = data.replace(['male', 'female'], [1, 0])

clf = DecisionTreeClassifier(random_state=241)
clf.fit(np.array(data), np.array(y))

imp = clf.feature_importances_
answer.write('{}'.format(imp))
