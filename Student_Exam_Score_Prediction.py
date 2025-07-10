# Student Score Prediction using Regression
# This project aims to predict students' exam scores based on features such as the number of hours studied, previous exam 
# scores, and attendance. Regression techniques will be used to build a model that estimates the exam score of a student given
# these input features. The project can provide insights into factors influencing student performance and help educators 
# identify students who may need additional support.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

data = {
    'Hours_Studied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Previous_Score': [50, 52, 55, 60, 65, 68, 70, 75, 80, 85],
    'Attendance': [60, 65, 70, 75, 80, 85, 85, 90, 95, 100],
    'Final_Score': [55, 58, 60, 65, 70, 73, 75, 80, 85, 90]
}

df = pd.DataFrame(data)

print("Sample Data:")
print(df.head())

sns.pairplot(df)
plt.suptitle("Feature Relationships", y=1.02)
plt.show()

X = df[['Hours_Studied', 'Previous_Score', 'Attendance']]
y = df['Final_Score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nModel Evaluation:")
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

results = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred})
print("\nComparison of Actual vs Predicted Final Scores:")
print(results)

