import pandas as pd
from sklearn.linear_model import LinearRegression
from collections import OrderedDict


def get_top_three_correllations():
    mental_health_data = pd.read_csv('./university_mental_health_iot_dataset.csv', sep=r'\s*,\s*', engine='python')
    mental_health_data.timestamp = pd.to_datetime(mental_health_data.timestamp)
    mental_health_data['hour'] = mental_health_data.timestamp.dt.hour
    mental_health_data['date'] = mental_health_data.timestamp.dt.date
    mental_health_data = mental_health_data.drop(['timestamp', 'date'], axis=1)
    mental_health_data = pd.get_dummies(mental_health_data, columns=['location_id'])

    X = mental_health_data.drop('stress_level', axis=1)
    Y = mental_health_data['stress_level']
    linear_model = LinearRegression()
    linear_model.fit(X, Y)
    linear_model.score(X, Y)
    predictors = X.columns
    # coef = pd.Series(linear_model.coef_,predictors).sort_values()
    coef = pd.Series(linear_model.coef_, predictors).sort_values(key=abs, ascending=False).head(3)
    top_three_correlatations = OrderedDict(coef)
    return  coef, top_three_correlatations

