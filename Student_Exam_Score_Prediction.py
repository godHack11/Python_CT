import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("student_scores_dataset_large.csv")  

print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())

sns.pairplot(df)
plt.suptitle("Relationship Between Features", y=1.02)
plt.show()

plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

X = df[['Hours_Studied', 'Previous_Score', 'Attendance']] 
y = df['Final_Score']                                      

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Model Performance on Test Set:")
print("Mean Squared Error (MSE):", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

comparison_df = pd.DataFrame({'Actual Score': y_test.values, 'Predicted Score': y_pred})
print("\nComparison of Actual and Predicted Scores:")
print(comparison_df.head(10))
