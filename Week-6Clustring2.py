Bagging, Boosting, Stacking, Random Forest, Gradient Boosting

1. Bagging Algorithm
Bagging classifier can be used for both regression and classification tasks. Here is an overview of Bagging classifier algorithm:

* Bootstrap Sampling: Divides the original training data into ‘N’ subsets and randomly selects a subset with replacement in some rows from 
  other subsets. This step ensures that the base models are trained on diverse subsets of the data and there is no class imbalance.

* Base Model Training: For each bootstrapped sample we train a base model independently on that subset of data. These weak models are trained
  in parallel to increase computational efficiency and reduce time consumption. We can use different base learners i.e. different ML models 
  as base learners to bring variety and robustness.

* Prediction Aggregation: To make a prediction on testing data combine the predictions of all base models. For classification tasks it can 
  include majority voting or weighted majority while for regression it involves averaging the predictions.

* Out-of-Bag (OOB) Evaluation: Some samples are excluded from the training subset of particular base models during the bootstrapping method. 
  These “out-of-bag” samples can be used to estimate the model’s performance without the need for cross-validation.

* Final Prediction: After aggregating the predictions from all the base models, Bagging produces a final prediction for each instance.

Python pseudo code for Bagging Estimator implementing libraries:
a). Importing Libraries and Loading Data

* BaggingClassifier: for creating an ensemble of classifiers trained on different subsets of data.
* DecisionTreeClassifier: the base classifier used in the bagging ensemble.
* load_iris: to load the Iris dataset for classification.
* train_test_split: to split the dataset into training and testing subsets.
* accuracy_score: to evaluate the model’s prediction accuracy.

from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

b). Loading and Splitting the Iris Dataset

* data = load_iris(): loads the Iris dataset, which includes features and target labels.
* X = data.data: extracts the feature matrix (input variables).
* y = data.target: extracts the target vector (class labels).
* train_test_split(...): splits the data into training (80%) and testing (20%) sets, with random_state=42 to ensure reproducibility.

data = load_iris()
X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

c). Creating a Base Classifier

Decision tree is chosen as the base model. They are prone to overfitting when trained on small datasets making them good candidates for bagging.

base_classifier = DecisionTreeClassifier(): initializes a Decision Tree classifier, which will serve as the base estimator in the Bagging ensemble.

base_classifier = DecisionTreeClassifier()

d). Creating and Training the Bagging Classifier

* A BaggingClassifier is created using the decision tree as the base classifier.
* n_estimators = 10 specifies that 10 decision trees will be trained on different bootstrapped subsets of the training data.                                                                                                                                

bagging_classifier = BaggingClassifier(base_classifier, n_estimators=10, random_state=42)
bagging_classifier.fit(X_train, y_train)

e). Making Predictions and Evaluating Accuracy

* The trained bagging model predicts labels for test data.
* The accuracy of the predictions is calculated by comparing the predicted labels (y_pred) to the actual labels (y_test).

y_pred = bagging_classifier.
predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

2. Boosting Algorithm
Boosting is an ensemble technique that combines multiple weak learners to create a strong learner. Weak models are trained in series such 
that each next model tries to correct errors of the previous model until the entire training dataset is predicted correctly. One of the most 
well-known boosting algorithms is AdaBoost (Adaptive Boosting). Here is an overview of Boosting algorithm:

* Initialize Model Weights: Begin with a single weak learner and assign equal weights to all training examples.

* Train Weak Learner: Train weak learners on these dataset.

* Sequential Learning: Boosting works by training models sequentially where each model focuses on correcting the errors of its predecessor. 
  Boosting typically uses a single type of weak learner like decision trees.

* Weight Adjustment: Boosting assigns weights to training datapoints. Misclassified examples receive higher weights in the next iteration so 
  that next models pay more attention to them.

Python pseudo code for boosting Estimator implementing libraries:
a). Importing Libraries and Modules

* AdaBoostClassifier from sklearn.ensemble: for building the AdaBoost ensemble model.
* DecisionTreeClassifier from sklearn.tree: as the base weak learner for AdaBoost.
* load_iris from sklearn.datasets: to load the Iris dataset.
* train_test_split from sklearn.model_selection: to split the dataset into training and testing sets.
* accuracy_score from sklearn.metrics: to evaluate the model’s accuracy.        

from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

b). Loading and Splitting the Dataset

* data = load_iris(): loads the Iris dataset, which includes features and target labels.
* X = data.data: extracts the feature matrix (input variables).
* y = data.target: extracts the target vector (class labels).
* train_test_split(...): splits the data into training (80%) and testing (20%) sets, with random_state=42 to ensure reproducibility.

data = load_iris()
X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

c). Defining the Weak Learner

We are creating the base classifier as a decision tree with maximum depth 1 (a decision stump). This simple tree will act as a weak learner 
for the AdaBoost algorithm, which iteratively improves by combining many such weak learners.

base_classifier = DecisionTreeClassifier(max_depth=1)

d). Creating and Training the AdaBoost Classifier

* base_classifier: The weak learner used in boosting.
* n_estimators = 50: Number of weak learners to train sequentially.
* learning_rate = 1.0: Controls the contribution of each weak learner to the final model.
* random_state = 42: Ensures reproducibility.

adaboost_classifier = AdaBoostClassifier(
    base_classifier, n_estimators=50, learning_rate=1.0, random_state=42
)
adaboost_classifier.fit(X_train, y_train)

e). Making Predictions and Calculating Accuracy

We are calculating the accuracy of the model by comparing the true labels y_test with the predicted labels y_pred. The accuracy_score 
function returns the proportion of correctly predicted samples. Then, we print the accuracy value.
        
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

3. Stacking
Stacking is a ensemble learning technique where the final model known as the “stacked model" combines the predictions from multiple base 
models. The goal is to create a stronger model by using different models and combining them.  

Architecture of Stacking
Stacking architecture is like a team of models working together in two layers to improve prediction accuracy. Each layer has a specific job 
and the process is designed to make the final result more accurate than any single model alone. It has two parts:

a). Base Models (Level-0)

These are the first models that directly learn from the original training data. You can think of them as the “helpers” that try to make 
predictions in their own way.

* Base models can be Decision Tree, Logistic Regression, Random Forest, etc.
* Each model is trained separately using the same training data.

b). Meta-Model (Level-1)

This is the final model that learns from the output of the base models instead of the raw data. Its job is to combine the base models 
predictions in a smart way to make the final prediction.

* A simple Linear Regression or Logistic Regression can act as a meta-model.
* It looks at the outputs of the base models and finds patterns in how they make mistakes or agree.

Steps to Implement Stacking:
  
* Start with training data: We begin with the usual training data that contains both input features and the target output.
* Train base models: The base models are trained on this training data. Each model tries to make predictions based on what it learns.
* Generate predictions: After training the base models make predictions on new data called validation data or out-of-fold data. 
  These predictions are collected.
* Train meta-model: The meta-model is trained using the predictions from the base models as new features. The target output stays the same 
  and the meta-model learns how to combine the base model predictions.
* Final prediction: When testing the base models make predictions on new, unseen data. These predictions are passed to the meta-model which 
  then gives the final prediction.
* With stacking we can improve our models performance and its accuracy.

4. Gradient Boosting 
Gradient Boosting is a ensemble learning method used for classification and regression tasks. It is a boosting algorithm which combine 
multiple weak learner to create a strong predictive model. It works by sequentially training models where each new model tries to correct 
the errors made by its predecessor.

In gradient boosting each new model is trained to minimize the loss function such as mean squared error or cross-entropy of the previous 
model using gradient descent. In each iteration the algorithm computes the gradient of the loss function with respect to predictions and 
then trains a new weak model to minimize this gradient. Predictions of the new model are then added to the ensemble (all models prediction) 
and the process is repeated until a stopping criterion is met.  

Shrinkage and Model Complexity
A key feature of Gradient Boosting is shrinkage which scales the contribution of each new model using learning rate (denoted as η).

* Smaller learning rates: mean the contribution of each tree is smaller which reduces the risk of overfitting but requires more trees to 
  achieve the same performance.
* Larger learning rates: mean each tree has a more significant impact but this can lead to overfitting.
 
There's a trade off between the learning rate and the number of estimators (trees) a smaller learning rate usually means more trees are 
required to achieve optimal performance.

Gradient Boosting Regression - Implementation:

import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score

data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

gbr = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
gbr.fit(X_train, y_train)

y_pred = gbr.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("✅ Gradient Boosting Regression Results:")
print(f"Mean Squared Error: {mse:.4f}")
print(f"R² Score: {r2:.4f}")






  













                                                                          
