import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
data = pd.read_csv("credit_score.csv")
print("First 5 rows:\n", data.head())
print("\nStatistical Summary:\n", data.describe())
print("\nData Types:\n", data.dtypes)
print("\nNull values:\n", data.isnull().sum())
for col in data.columns:
    data[col].fillna(data[col].mode()[0], inplace=True)
plt.figure(figsize=(8,5))
sns.boxplot(x="Occupation", y="Credit_Score", data=data)
plt.xticks(rotation=45)
plt.title("Credit Scores Based on Occupation")
plt.show()
X = data.drop("Credit_Score", axis=1)
y = data["Credit_Score"]
X = pd.get_dummies(X) 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
