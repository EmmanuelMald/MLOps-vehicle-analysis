
# ***Machine Learning Models***

Both machine learning models were developed in Python; the main libraries used were:

- *pandas*: Data Extraction &  Transformation 
- *numpy*: Data Transformation
- *scikit-learn*: Machine Learning development
- *joblib*: Save the trained ML model

## ***Feature Selection***

To choose the columns that will be used to train the model, a technique called ***Mutual Information*** was used. 

This technique is similar to correlation in the aspect that compares the relation between two variables; Nevertheless, ***Mutual Information can detect any kind of relation, not only linear as correlation does.***

*Mutual Information* (MI) is a concept from information theory that measures the amount of information shared between two random variables. It quantifies how much knowing one variable reduces the uncertainty about the other. In other words, it tells you how much information about one variable is gained by knowing the value of the other variable.

***MI goes from 0 to infinity, where 0 indicates no relation at all; In practice, MI values between 0.1 and 0.5 often indicate a moderate relationship, while values above 0.5 suggest a stronger relationship.***

As MI is is scale-dependent, you could choose the top K MI values, or the ones higher than some threshold. 

***MI only supports numeric values; so all the categorical features had to be encoded using an Ordinal Encoder.***

Also, a **pearson** and a **spearman** correlation was implemented to know which columns had a linear or near-linear correlation with the target. **Spearman** correlation is used to catch those near-linear relationships, whereas **pearson** is only capable to find linear relationships.

## ***Model Development***


To select which models to tests, the first thing to take into account is to know the type of the target and the objective you want to achieve.

If the objective is to find relations between your data that has not being discovered or labeled, this is, you do not have a built target (Y), then you should try with Unsupervised ML models. On the other hand, if you want to label a new data entry in an already labeled dataset, then you should try with Supervised ML models.

Another thing to take into account, is the data type of your target. If the target is a category, then you should try with classification models. Whether your data is numeric, then you should try with some regression ones.

Its also important to establish if you want to create a parametric or non-parametric model, this is, if you want to create a model based on some assumptions of the relations between your features and your target, or not. Based on this, you should try with some neural networks or not.

In this project, both targets, CO<sub>2</sub> emissions and autonomy are numeric and continous, so **supervised machine learning models, and specifically some regression models, are used**. 

### ***Feature Encoding***

Once the models has been selected, its necessary to encode the categorical features based on whether the labels are ordered or unordered, as all the ML models needs to work with numbers.

In this project, **OneHotEncoder** was used for unordered categorical features, and **OrdinalEncoder** for the ordered ones (if exists).

### ***Feature Normalization***

As almost every regression model is very sensitive to the order/hierarchy of the numbers, and the range of values of all the features are different, it was decided to use **MinMaxScaler** to set them all in the same range (0 to 1), avoiding modifying its distributions.

### ***Pipeline Generation***

As some transformations needs to be done to all the features in the cleaned dataset before being used by any Machine Learning model, **ColumnTransformer** was used to select which type of transformation (encoder/scaler) needs to be done to each feature; moreover, it can also be integrated with **Pipeline**, which orchestrates all the steps to be done to use the model, making it easier to generate a model that can only receive the "raw" dataset values, and return the estimation.


## ***Model Evaluation***

To evaluate the models, **cross validation** (cross_val_score) was used to prevent overfitting and ensuring that the model performs well on unseen data.


It evaluates the model's performance by training it on different subsets of the data and testing it on the remaining parts. This approach provides a more reliable estimate of a model's performance compared to a single train-test split, ensuring that the model's evaluation isn't dependent on any specific data partition.


In sklearn, cross validation allows to implement different evaluation metrics. In this project, two was used:

### **R2**

This metric tells how much of the variation of the data can be described by the model. R2 goes from 0 to 1. The nearest to 1, the better the model is.

### **Root Mean Squared Error (RMSE)**

It measures the average magnitude of the errors between predicted and actual values. It provides an idea of how well a model's predictions match the observed data. Lower values means a better model performance. Since RMSE has the same unit as the target variable, it's easy to interpret as the mean deviation to the real value. 
