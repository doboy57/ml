import pandas as pd

nyc = pd.read_csv("ave_hi_nyc_jan_1895-2018.csv")

print(nyc.head(3))

print(nyc.Date.values)

print(nyc.Date.values.reshape(-1, 1))

print(nyc.Temperature.values)

print(nyc.Temperature.values.reshape(-1, 1))

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    nyc.Date.values.reshape(-1, 1), nyc.Temperature.values, random_state=11
)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X=x_train,y=y_train)

coef = lr.coef_
intercept = lr.intercept_

predicted = lr.predict(x_test)

expected = y_test

print(predicted[:10])
print(expected[:10])

predit = lambda x: coef * x + intercept 

print(predit(2025))