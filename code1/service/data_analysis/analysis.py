# encoding=utf8
# author: Shize Deng
# create_time: 2024/12/3 18:51
# file: analysis.py
from sklearn.linear_model import LinearRegression


# Simulated data analysis predict usage_time(linear regression)
def analyze_device(decive_data):
    # I have already discussed this data format with Jiaqi Tang ,so I will use it directly
    X = [[decive_data["usage_time"]]]
    y = [decive_data["environment_data"]["temperature"]]
    model = LinearRegression()
    model.fit(X, y)
    prediction = model.predict([[decive_data["usage_time"] + 1]])
    return prediction[0]


# Simulated user data analysis predict usage_time(linear regression)
def analyze_user(user_data):
    # Already discussed this data format with Jiaqi Tang
    X = [[user_data["usage_time"]]]
    y = [user_data["energy_use"]]
    model = LinearRegression()
    model.fit(X, y)
    prediction = model.predict([[user_data["usage_time"] + 1]])
    return prediction[0]
