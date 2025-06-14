Confusion Matrix, Accuracy, Precision, Recall, F1-score, ROC curve, AUC score, Mean Squared Error, Root Mean Squared Error, R-squared

Classification Metrics
Most of the classification model metrics are best defined using a Confusion matrix. So, what is a confusion matrix? Let us consider a classification example. Assume that there are a 
total of 100 samples of animals. Among them, there are 20 dogs, 55 cats, and 25 birds. An ideal multi-class classifier will predict the following,

If we consider it as a binary class, then there are 20 dogs and 80 other animals. Let the classifier predict a dog (P-positive class) and not a dog (N-negative class). An ideal 
binary classifier will predict the following:

But, the multi-class classifier predicted the following:

So, out of 20 dogs, it predicted 15 correct, out of 55 cats, it predicted 30 correct, and out of 25 birds, it predicted 10 correct.
  
So, out of 20 dogs, it predicted 15 correct (true positive), and out of 80 not dogs, it predicted 60 correct (true negative). It predicted 5 dogs as not dogs (false negative) and 20 
not dogs as dogs (false positive).

The Confusion matrix gives us clues as to where our classifier is going wrong.

Let us add some terminology to this using the simple binary classifier:

- True Positives (TP): Predicted positive and actual was also positive. In the above example, it’s 15.
- True Negatives (TN): Predicted negative and actual was also negative. In the above example, it’s 60.
- False Positives (FP): Predicted positive and actual was negative. In the above example, it’s 20. In hypothesis testing, this is known as Type I Error ( the error of rejecting a null 
  hypothesis when it is actually true. In other words, this is the error of accepting an alternative hypothesis when the results can be attributed to chance).
- False Negatives (FN): Predicted negative and actual was positive. In the above example, it’s 5. In hypothesis testing, this is known as Type II Error (the error of not rejecting a 
  null hypothesis when the alternative hypothesis is the true state of nature. In other words, this is the error of failing to accept an alternative hypothesis when we don’t have 
  adequate power).

Once we have this data, let us discuss the metrics to evaluate a machine learning model.
Note: Unlike binary classification, there are no positive or negative classes in multi-class classification. Metrics TP, TN, FP, and FN can be calculated for each class.

1- (Overall) Accuracy
It is the proportion of the predictions that are correct. In other words, it is the ratio between the number of correctly predicted samples and the total samples.
  
Accuracy= (TP+TN)/(TP+FP+FN+TN) =(TP+TN)/total = (15+60)/100 = 0.75
Most of the time, the prediction class might be imbalanced. For instance, if the number of positive classes in the dataset is high and the classifier predicts all the classes as 
positive, the accuracy will still be high. In the above example, if it predicted all the samples as not a dog, then the accuracy would be (0+80)/100 = 0.8, which is not correct as the 
model is not predicting and considers all the samples as not dogs. So, other metrics are used.
  
Let us consider a multi-class case to better understand the Overall Accuracy.

The diagonal elements represent the counts that were correctly classified.
Overall Accuracy = correctly classified/total = 15+30+10/100 = 0.55

2- Average Accuracy
Let us consider a multi-class case:

Correctly classified= 15+30+10 = 55
TP dog= 15
TN dog = Correctly classified - TP dog = 55=15=40
FP dog = 20+0 = 20
FN dog = 5+0 = 5
Accuracy of class Dog =Acc. dog = (TP dog +TN dog)/(TP dog+FP dog+FN dog+TN dog)
=(15+40)/(15+20+5+40) = 55/80 = 0.68
Similarly, we can calculate accuracy for other classes.
Average Accuracy = (Acc. dog+Acc. cat+Acc. bird)/total classes= (0.68+0.55+0.73)/3 = 0.65

3- Error Rate / Misclassification Rate
Proportion of the predictions that are not correct = (FP+FN)/total = (20+5)/100 = 0.25 . This is equal to 1.0-Accuracy !
Error Rate is also called Misclassification Rate.

4- Precision
What’s the proportion of positive class identifications is correct? In other words, if the classifier predicted a positive class, how often is it correct?
Precision for Dog= TP/Predicted positive = TP/(TP+FP) = 15/35 = 0.42
Out of all the times Dog was predicted, 42% of the time, the classifier was correct.
Multi-class:

- Precision for Dog = TP dog / (TP dog + FP dog) = TP dog / Total predicted as dog = 15/35 = 0.42
- Precision for Cat = TP cat / (TP cat + FP cat) = TP cat / Total predicted as cat = 30/50 = 0.6
- Precision for Bird = TP bird / (TP bird + FP bird) = TP bird / Total predicted as bird = 10/15 = 0.66

5- Recall
What’s the proportion of the actual positive class is identified correctly? In other words, when it’s actually positive, how often does it predict positive?

Recall for Dog= TP/Actual positive = TP/(TP+FN) = 15/20 = 0.75

Out of all the times Dog labels should have been predicted, the classifier correctly predicted 75% of the labels.
Multi-class:

- Recall for Dog = TP dog / (TP dog + FN dog) = TP dog / Total actual dog = 15/20 = 0.75
- Recall for Cat = TP cat / (TP cat + FN cat) = TP cat / Total actual cat = 30/55 = 0.54
- Recall for Bird = TP bird / (TP bird + FN bird) = TP bird / Total actual bird = 10/25 = 0.4
- Recall is also called Sensitivity or True Positive Rate (TPR).

6- Specificity / True Negative Rate (TNR)
As Recall deals with positive class, Specificity deals with negative class. In other words, when it’s actually negative, how often does it predict negative?
Specificity = TN/Actual negative= TN/(FP+TN) = 60/80 = 0.75
Specificity is also called True Negative Rate (TNR)

7- False Positive Rate (FPR)
False Positive Rate is important when plotting the ROC curve. This is equal to 1.0-Specificity(TNR). In other words, when it’s actually negative, how often does it predict positive?

FPR = FP/Actual negative= FP/(FP+TN) = 20/80 = 0.25

This metric is important in the medical testing field. A false positive means that a person is tested as positive, while the actual result should have been negative.

8- False Negative Rate (FNR) / Miss Rate
False Negate Rate (FNR) is calculated similarly to FPR. This metric is important in the medical testing field. A false negative means that a person is tested as negative, while the 
actual result should have been positive.

FNR = FN/Actual positive= FN/(TP+FN) = 5/20 = 0.25

FNR is also called Miss Rate.  

9- F1 Score / F-score / F-measure
want to consider both Precision and Recall. This can be achieved through an F1 Score. It is defined as the harmonic mean of the model’s precision and recall. In other words, it is a 
weighted average of the Precision and Recall.

F1 Score for Dog = 2* (Precision*Recall)/(Precision+Recall)
= 2* (0.42*0.75)/(0.42+0.75) =0.53

For multi-class classification, we can compute the F1 Score for each class as we know the Precision and Recall for each class which was computed in the above sections.

F1 Score is also called as F-score or F-measure.

10- ROC (Receiver Operating Curve)
ROC curve has the True Positive Rate (TPR/Recall/Sensitivity) on the y-axis against False Positive Rate (FPR = 1.0-Specificity) on the x-axis at various cut-off thresholds (0 to 1) 
of a binary classifier. In general, the default cut-off threshold is 0.5.

Each point on the ROC plot represents a sensitivity/specificity pair corresponding to a particular decision threshold. A perfect classifier has a ROC plot that passes through the 
upper left corner (1.0 sensitivity and 1.0 specificity). ROC plot shows overall model performance. The threshold selection is based on whether we would rather minimize False 
Positive Rate (FPR) or maximize True Positive Rate (TPR), which is a business decision.

11- AUC (Area Under the Curve)
It is the area under the ROC plot, which is between 0 and 1. It is the best way to summarize the model performance as a single number. The higher the AUC (~1), the better the model 
performance, and the importance of higher AUC is based on the business decision. This metric is helpful with highly unbalanced classes.

Regression Metrics
The output of a regression model is always a continuous quantity. 
1- Mean Absolute Error (MAE)

This metric calculates the average absolute distance (error) between the predicted and actual values.
MAE penalizes the euclidean distance in error and is more appropriate if the sample variance does not exist. This metric is robust to outliers.
2- Mean Squared Error (MSE)

This metric calculates the average squared distance (error) between the predicted and actual values. The output is a non-negative value, and it would be better if we bring this near 0.
MSE penalizes the square of the error and is a consistent estimator of the error variance. Thus, large errors are penalized more than small ones.
3- Root Mean Square Error (RMSE)

This metric calculates the average deviation in predictions from the actual values. It assumes that error is unbiased and follows a normal distribution. RMSE penalizes large errors 
and is better for large values of actual or prediction. Outliers impact this metric, and care must be taken to remove them. The output is a non-negative value, and it would be better 
if we bring this near 0.

4- Root Mean Squared Logarithmic Error (RMSLE)
This metric is good if we have outliers. It penalizes the underestimations more than the overestimations. This metric is helpful if the targets are having exponential growth and care 
about percentage errors rather than the absolute value of errors. This metric can be used if actual or predicted have zero-valued elements. But this is not appropriate if either is 
negative valued.

5- R-Squared (coefficient of determination)
Values typically range from 0 to 1, with higher values showing that the model is a better fit. The best possible score is 1.0, and it can be negative. Adding more predictor variables 
to our model will increase the value of R-squared but can lead to overfitting.

6- Adjusted R-Squared
N - number of data points in the dataset
p - number of independent variables
Adjusted R-squared adjusts for the number of variables in a model. If we add more useful variables, the value will increase, and if we add less useful/redundant variables, the value 
will decrease. It adds precision and reliability by considering the impact of additional independent variables that are not handled by just R-Squared measurements. In general, the 
Adjusted R-squared is positive. It is always lower than the R-Squared value.
We can use the Adjusted R-squared to compare models with different numbers of predictors.















  




