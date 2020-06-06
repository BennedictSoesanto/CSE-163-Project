import pandas as pd

"""
twoSets predicts what would happen if players played two sets
If this would determine the outcome better than one set.
It sees if it can be more accurate in predicting if we can determine
a winner in a best out of 3 match
"""


def twoSets():
    data = pd.read_csv('~/Desktop/cse163/CSE-163-Project/TennisPart2.csv')
    data = data.dropna()
    print(data.head())

    features = data.loc[:, (data.columns != 'Wsets') &
                        (data.columns != 'Lsets')]
    labels = data['Wsets']

    print(features)
    print(labels)

    from sklearn.tree import DecisionTreeRegressor

    model = DecisionTreeRegressor()

    model.fit(features, labels)

    predictions = model.predict(features.loc[0:50:40])
    print('Predictions:', predictions)
    print('Actual     :', labels.loc[0:150:40].values)

    from sklearn.metrics import mean_squared_error

    predictions = model.predict(features)
    error = mean_squared_error(labels, predictions)
    print('Error      :', error)


"""
oneSet determines if it can predict a winner based on if that person
won their first set in a best out of 3 match. Therefore making it reasonable
that players shouldn't have to endure a grueling best out of 5.
"""


def oneSet():
    data = pd.read_csv('~/Desktop/cse163/CSE-163-Project/TennisPart2.csv')
    data = data.dropna()
    print(data.head())

    features = data.loc[:, (data.columns != 'Wsets') &
                        (data.columns != 'Lsets') &
                        (data.columns != 'W2') &
                        (data.columns != 'L2')]
    labels = data['Wsets']

    print(features)
    print(labels)

    from sklearn.tree import DecisionTreeRegressor

    model = DecisionTreeRegressor()

    model.fit(features, labels)

    predictions = model.predict(features.loc[0:50:40])
    print('Predictions:', predictions)
    print('Actual     :', labels.loc[0:150:40].values)

    from sklearn.metrics import mean_squared_error

    predictions = model.predict(features)
    error = mean_squared_error(labels, predictions)
    print('Error      :', error)
