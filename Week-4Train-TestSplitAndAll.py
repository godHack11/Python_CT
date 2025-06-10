# Train-Test Split, Cross-validation, Hyperparameter Tuning, Grid Search, Random Search

1. Train-Test Split
Building a machine learning-based project usually starts from data and ends in a data-driven decision. In between these two points, it includes various sub-steps, some are 
compulsorily required, and some we use to enhance performance. Data splitting is one of those sub-steps that are not only required, but if followed appropriately, we can get fruitful 
results from our model. So in this article, we will discuss the basic concepts of data splitting in machine learning.
  
Let’s start by knowing what data splitting is.

What is Data Splitting?
In data science or machine learning, data splitting comes into the picture when the given data is divided into two or more subsets so that a model can get trained, tested and evaluated.
In practice or in real-life projects, data splitting is an important aspect, and it becomes a must when models are based on the data as it ensures the making of machine learning models. 
Usually, we create two or three parts of the main dataset.
  
If two splits are there, it means one will be utilised for training and another one will be used for testing, or,
                                                                                                
If three splits are there will mean there are training, testing and validation sets.
  
Let’s say that we have a data set where the data is categorised based on males and females.

We know only two features for each person on the data: weight and voice pitch.
  
Before modelling this data, we perform a data split procedure to identify the best classification model for classifying the given data value as a male or a female.

How does Data Splitting work?
While performing supervised machine learning tasks, it is always recommended to split the data into three sets: training set, testing set and validation set. So, In the procedure when 
it comes to data split, first, we randomly split data into three sets:
  
Training set: A subset of the main dataset will feed into the model so that that model can learn the data patterns.
  
Validation Set: This set is used to understand the performance of the model in comparison to different models and hyperparameter choices.
  
Test set: This set checks the final model’s accuracy.
  
Let’s take a look at the details of these subsets of data.

A subset of data is responsible for training the model. Usually machine learning model learns to predict by understanding the patterns and relationships hidden inside the data. 
The model will learn from the patterns and relationships between weight and pitch variables in our example.
  
While taking train data from whole data, one should take higher representativeness of data into the consideration. This means the extracted data should have enough population for 
every class of the data. With this quality, one should also ensure that extracted data is unbiased because biased data can lead to an inaccurate model.
  
the above example represents a problem of classifying data into the male and female classes as a binary classification task. To resolve this problem, we can use a simple decision tree
model.
  
A decision tree will learn by splitting the data into nodes, using the selected feature ( None, Weight, Pitch of voice or both Weight and Pitch of voice.

Validation data
When building a machine learning model, we mostly try to train more than one model by changing model parameters or using different algorithms. For example, while building the 
decision tree model for our data, we did hyperparameter tuning and found that multiple models performed well in such conditions. Therefore, we need to choose a final model using 
different parameters.
                                                                                                                                          
It has been seen that if we use the same data for training and tuning of a model, tr represents over-fitness and becomes incapable of generalisation.
                                                                                                                                          
Here validation set from the data comes into the picture and works as independent and unbiased data, which also helps in the performance comparison of different models.
                                                                                                   
As this data helps choose the best model algorithm or parameter, we take the model into production after approximating the model’s performance. It is suggested not to use the test data to evaluate the model before selecting the optimum one.

Test Data                                                                                                 
As discussed in the above topic, after training, validating and selecting a model, we should take it to production after testing its performance for this extracted subset of data is 
called the test data.
                                                                                                   
We should be very careful with this step because if performed ahead of time can form overfitting and lead to unreliable performance. The test set should be used as the final form of 
evaluation when the use of the validation set is completed and the final model is selected.

About DSW
Data Science Wizards (DSW) is an Artificial Intelligence and Data Science start-up that primarily offers platforms, solutions, and services for making use of data as a strategy 
through AI and data analytics solutions and consulting services to help enterprises in data-driven decisions.
  
DSW’s flagship platform UnifyAI is an end-to-end AI-enabled platform for enterprise customers to build, deploy, manage, and publish their AI models. UnifyAI helps you to build your 
business use case by leveraging AI capabilities and improving analytics outcomes.

2. Cross-Validation (CV)
A technique for evaluating ML models by dividing the dataset into multiple parts (folds) and training/testing multiple times.

Most common: k-Fold Cross-Validation
	Split data into k equal parts
	Train on k-1 folds, test on the remaining 1
	Repeat k times and average the results  

Benefits:
	More robust evaluation than a single train-test split
	Helps detect variance and bias

3. Hyperparameter Tuning
The process of finding the best values for model hyperparameters (not learned from data).
Examples of hyperparameters:
	n_estimators in Random Forest
	C and gamma in SVM
	Learning rate in neural networks
  
Goal:
Optimize model performance by tuning values like regularization strength, tree depth, etc.
  
4. Grid Search
A brute-force technique that tests all possible combinations of hyperparameter values from a predefined grid.  
params = {
  'max_depth': [3, 5, 7],
  'min_samples_split': [2, 5]
}
This would test 3 × 2 = 6 combinations.

5. Random Search
Instead of trying all combinations like Grid Search, it randomly samples combinations from the parameter space.  

If you want to try 10 random configurations out of 1000+ possible, Random Search picks them at random.

Pros:
	Faster than Grid Search
	Often finds a good solution quickly

Cons:
	Less exhaustive than Grid Search























  

