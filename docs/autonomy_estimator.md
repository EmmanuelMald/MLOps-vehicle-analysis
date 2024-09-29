# ***Autonomy Estimator***

## ***Feature Selection***

All the features used was the ones with a MI (mutual information) score higer than 0.3:

- ***basemodel***: Basemodel of the vehicle (ex: Forte, F-150, Mustang, etc).

- ***engine_displacement_liters***: Total volume that displace the cylinders (ex. 2, 4, 6, 8, etc)

- ***cylinders***: Number of cylinders of a vehicle. (ex: 3, 4, 8, etc)

- ***transmission***: Type of transmission. See all the transmissions [**here**](http://www.fueleconomy.gov/feg/findacarhelp.shtml#trany) (ex: Automatic 3-spd, Manual 4-spd, etc)

- ***vehicle_size_class***: Vehicle segment (ex: Compact Cars, Large Cars, Small Sport Utility Vehicle 2WD, etc)

The *engine_displacement_liters* and *cylinders* has a strong negative linear relation with the target variable (*combined_kmpl_for_fuel_type1*), with a spearman correlation lower than -0.8

## ***Model implemented***

Considering that the target variable is continous, and the high linear relationship between *engine_displacement_liters* and *cylinders*. It was decided to implement a **Multiple Linear Regression** and test its ability to predict new values.

### ***Feature Encoding***

In this case, as all the categories does not have any order/numeric relation, all of them were encoded using OneHotEncoder due to avoids possible relationships between categories that does not exist and might be created using **OrdinalEncoder**, especially when working with multiple linear regression, which is very sensitive to the order/hierarchy of the numbers. 

### ***Feature Normalizacion***

Also, as multiple linear regression is sensitive to the ranges of the features, it was decided to use MinMaxScaler to normalize all the numeric values in a range between 0 and 1. As all the categorical features also have values between 0 and 1 due to OneHotEncoder, it wasn't necessary to normalize them.

## ***Model Evaluation***

Using cross validation, the R2 was about 0.94, and the RMSE was near 1.11 km/L, making a very precise model. It wasn't necessary to create another model.