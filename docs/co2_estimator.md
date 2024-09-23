
# ***CO<sub>2</sub> emission estimator***

## ***Feature Selection***

All the features used was the ones with a MI value higher than 0.2, this is:

- ***basemodel***: Basemodel of the vehicle (ex: Forte, F-150, Mustang, etc).

- ***engine_displacement_liters***: Total volume that displace the cylinders (ex. 2, 4, 6, 8, etc)

- ***transmission***: Type of transmission. See all the transmissions [**here**](http://www.fueleconomy.gov/feg/findacarhelp.shtml#trany) (ex: Automatic 3-spd, Manual 4-spd, etc)

- ***make***: The company or brand that manufactured a vehicle (ex: Lamborghini, Ford, Kia, etc)

- ***cylinders***: Number of cylinders of a vehicle. (ex: 3, 4, 8, etc)

- ***vehicle_size_class***: Vehicle segment (ex: Compact Cars, Large Cars, Small Sport Utility Vehicle 2WD, etc)

- ***year***: Model year of the vehicle (ex: 2024, 2020, etc)

- ***drive***: Vehicle's drivetrain (ex: Rear-Wheel Drive, 4-Wheel Drive, etc)

- ***fuel_type***: Generic Fuel type, its a category that mix fuel_type1 and fuel_type2 (ex: Premium, Regular, Premium and Electricity, Regular Gas and Electricity, Hydrogen, etc)

- ***electric_motor***: Type of electric motor (ex: 240V Li-Ion, 48V Li-Ion, 82 kW AC Induction, 81 kW AC PMSM, etc)

- ***fuel_type1***: The main or principal fuel that a vehicle uses (ex: Diesel, Regular Gasoline, Premium Gasoline, Electricity, etc)

- ***start_stop***: If vehicle has start-stop technology (ex: True, False)

One important first conclusion is that, even when there exists hybrid vehicles, the second fuel type (fuel_type2) is not a good predictor of the CO<sub>2</sub> emissions. 

It was also found that the *engine_displacement_liters* and the *cylinders* features had a strong linear relationship with the target variable (*co2_tailpipe_gpkm*). With a spearman and pearson correlation higher than 0.8

## ***Model implemented***

Considering that the target variable is continous, and the high linear relationship between *engine_displacement_liters* and *cylinders*. It was decided to implement a **Multiple Linear Regression** and test its ability to predict new values.

### ***Feature Encoding***

In this case, as all the categories does not have any order/numeric relation, all of them were encoded using OneHotEncoder due to avoids possible relationships between categories that does not exist and might be created using **OrdinalEncoder**, especially when working with multiple linear regression, which is very sensitive to the order/hierarchy of the numbers. 

*In case a category feature has an ordered labels, then those should be encoded using OrdinalEncoder, which would respect the hierarchy of the labels setting higher numbers to them.

### ***Feature Normalizacion***

Also, as multiple linear regression is sensitive to the ranges of the features, it was decided to use MinMaxScaler to normalize all the numeric values in a range between 0 and 1. As all the categorical features also have values between 0 and 1 due to OneHotEncoder, it wasn't necessary to normalize them.

## ***Model Evaluation***

Using cross validation, the mean R2 was about 0.95, and RMSE near 17 g/km, making it a very precise model. So it wasn't necessary to create another model.



