import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

features = ['Place', 'ProductId', 'Month', 'Year']
target = 'total_fare'

X_train = train_data[features]
y_train = train_data[target]

X_test = test_data[features]
y_test = test_data[target]

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, 'model.pkl')

y_pred = model.predict(X_test)

model = LinearRegression()
model.fit(X_train, y_train)

r2 = r2_score(y_test, y_pred) * 100
mse = mean_squared_error(y_test, y_pred)

min_val = min(y_test.min(), y_pred.min())
max_val = max(y_test.max(), y_pred.max())

plt.scatter(y_test, y_pred, c='blue')
plt.plot([min_val, max_val], [min_val, max_val], 'r--')
plt.title(f'Сравнение фактических и предсказанных цен на такси\n'
          f'Точность модели: {r2:.1f}%')

plt.show()