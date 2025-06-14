Confusion Matrix, Accuracy, Precision, Recall, F1-score, ROC curve, AUC score, Mean Squared Error, Root Mean Squared Error, R-squared

Classification Metrics
Most of the classification model metrics are best defined using a Confusion matrix. So, what is a confusion matrix? Let us consider a classification example. Assume that there are a 
total of 100 samples of animals. Among them, there are 20 dogs, 55 cats, and 25 birds. An ideal multi-class classifier will predict the following,

If we consider it as a binary class, then there are 20 dogs and 80 other animals. Let the classifier predict a dog (P-positive class) and not a dog (N-negative class). An ideal 
binary classifier will predict the following:

But, the multi-class classifier predicted the following:
So, out of 20 dogs, it predicted 15 correct, out of 55 cats, it predicted 30 correct, and out of 25 birds, it predicted 10 correct.
So, out of 20 dogs, it predicted 15 correct (true positive), and out of 80 not dogs, it predicted 60 correct (true negative). It predicted 5 dogs as not dogs (false negative) and 20 not dogs as dogs (false positive).
The Confusion matrix gives us clues as to where our classifier is going wrong.
Let us add some terminology to this using the simple binary classifier:
True Positives (TP): Predicted positive and actual was also positive. In the above example, it’s 15.
True Negatives (TN): Predicted negative and actual was also negative. In the above example, it’s 60.
False Positives (FP): Predicted positive and actual was negative. In the above example, it’s 20. In hypothesis testing, this is known as Type I Error ( the error of rejecting a null hypothesis when it is actually true. In other words, this is the error of accepting an alternative hypothesis when the results can be attributed to chance).
False Negatives (FN): Predicted negative and actual was positive. In the above example, it’s 5. In hypothesis testing, this is known as Type II Error (the error of not rejecting a null hypothesis when the alternative hypothesis is the true state of nature. In other words, this is the error of failing to accept an alternative hypothesis when we don’t have adequate power).
































