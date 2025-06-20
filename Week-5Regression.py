Regressions
Simple Linear Regression, Multiple Linear Regression, Polynomial Regression, Ridge Regression, Lasso Regression, ElasticNet Regression

1. Linear Regression

Linear regression is used for predictive analysis. Linear regression is a linear approach for modeling the relationship between the criterion or the scalar response and the multiple 
predictors or explanatory variables. Linear regression focuses on the conditional probability distribution of the response given the values of the predictors. For linear regression, 
there is a danger of overfitting. The formula for linear regression is:

Syntax:
y = θx + b
where,

θ - It is the model weights or parameters
b - It is known as the bias.
This is the most basic form of regression analysis and is used to model a linear relationship between a single dependent variable and one or more independent variables.
Here, a linear regression model is instantiated to fit a linear relationship between input features (X) and target values (y). This code is used for simple demonstration of the approach.
                                                                                                                                                
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X_new)

2. Multiple Linear Regression
      
	Definition: Models the relationship between two or more independent variables and a dependent variable.
	Equation:
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_n X_n + \epsilon
	Use case: Predicting house prices based on area, number of bedrooms, and location.

3. Polynomial Regression

This is an extension of linear regression and is used to model a non-linear relationship between the dependent variable and independent variables. Here as well syntax remains the same 
but now in the input variables we include some polynomial or higher degree terms of some already existing features as well. Linear regression was only able to fit a linear model to 
the data at hand but with polynomial features, we can easily fit some non-linear relationship between the target as well as input features.

Here is the code for simple demonstration of the Polynomial regression approach.

from sklearn.linear_model import PolynomialRegression

model = PolynomialRegression(degree=2)

model.fit(X, y)
y_pred = model.predict(X_new)                

4. Ridge Regression

Ridge regression is a technique for analyzing multiple regression data. When multicollinearity occurs, least squares estimates are unbiased. This is a regularized linear regression 
model, it tries to reduce the model complexity by adding a penalty term to the cost function. A degree of bias is added to the regression estimates, and as a result, ridge regression 
reduces the standard errors.

Cost = argmin β∈R∥i−Xβ∥2+λ∥β∥2Cost= β∈Rargmin∥i−Xβ∥2+λ∥β∥2
Here is the code for simple demonstration of the Ridge regression approach.

from sklearn.linear_model import Ridge

model = Ridge(alpha=0.1)
model.fit(X, y)

y_pred = model.predict(X_new)

5. Lasso Regression

Lasso regression is a regression analysis method that performs both variable selection and regularization. Lasso regression uses soft thresholding. Lasso regression selects only a 
subset of the provided covariates for use in the final model.

This is another regularized linear regression model, it works by adding a penalty term to the cost function, but it tends to zero out some features' coefficients, which makes it 
useful for feature selection.

from sklearn.linear_model import Lasso

model = Lasso(alpha=0.1)
model.fit(X, y)

y_pred = model.predict(X_new)

6. ElasticNet Regression

Linear Regression suffers from overfitting and can’t deal with collinear data. When there are many features in the dataset and even some of them are not relevant to the predictive 
model. This makes the model more complex with a too-inaccurate prediction on the test set (or overfitting). Such a model with high variance does not generalize on the new data. So,
to deal with these issues, we include both L-2 and L-1 norm regularization to get the benefits of both Ridge and Lasso at the same time. The resultant model has better predictive 
power than Lasso. It performs feature selection and also makes the hypothesis simpler. The modified cost function for Elastic-Net Regression is given below:

1m[∑l=1m(y(i)−h(x(i)))2+λ1∑j=1nwj+λ2∑j=1nwj2]m1[∑l=1m(y(i)−h(x(i)))2+λ1​∑j=1n​wj​+λ2​∑j=1n​wj2​]

where,

w(j) represents the weight for the jth feature.  
n is the number of features in the dataset.
lambda1 is the regularization strength for the L1 norm.
lambda2 is the regularization strength for the L2 norm.

from sklearn.linear_model import ElasticNet

model = ElasticNet(alpha=0.1, l1_ratio=0.5)
model.fit(X, y)

y_pred = model.predict(X_new)

























