# ***Data Preparation***

An ETL pipeline was implemented using pandas due to the amount of information is relatively small (thousands of rows); Nevertheless, if the amount of data reach millions or billions of rows, it might be worth it to implement distributed computing with pyspark. 

ETL stands for Extract-Transform-Load, it refers to gather information from some data source, modify this data to convert it in a more valuable asset, and then load or save this processed data in a database or file.

## ***Data Source***

Both machine learning models uses information from the [***All Vehicles Model dataset***](https://public.opendatasoft.com/explore/dataset/all-vehicles-model/table/?sort=modifiedon) from *OpenDataSoft*. This dataset has licence of *public domain*, and is constantly being updated with the most recent vehicle models. 

Up to the time this documentation is being written (September 2024), the most recent model year is 2024, and the last time this dataset was updated was in June 3, 2024.

Nevertheless, this project has been configured to retrieve the last version of this dataset each time that the notebooks are run.

The dataset has some column names that might not be so self-descriptive Nevertheless, this dataset has some metadata that can be used to understand the columns, in this case, a json file was created to store the metadata, which can be consulted [**here**](https://public.opendatasoft.com/explore/dataset/all-vehicles-model/information/?sort=modifiedon).

## ***Data Transformation***

Some of the processes that were implemented are:

**Basic Data Understanding**

Data understanding is not a data transformation process itself, but I consider important to understand the basics of each column, some of the questions answered in this process were:

- Does a column has the necessary not null values to be set as a parameter for the ML model? *In this section, if the column has a lot of missing values - more than 80%, then I wasn't used* 

- Is the information in that column meaningful for the model? *(This is a first approach, but It will be addressed in depth during feature selection - described in the [**Machine learning models**](http://localhost:8000/machine_learning/) section)*

- Are the column information easily retrievable/known to set it as a parameter to the models? *Its important to define parameters that can truly be known and set as entries of the model*

This first analysis was achievable using the metadata and some basic Exploratory Data Analysis.

### ***Changing Data Types***

There were some columns that should be used as numbers, or bool values, but the dataset was trating them as strings or viceversa. In that case, its important to set the right values to the columns to avoid errors. 

### ***Data Imputation***

- Is the information in that column meaningful for the model? *(This is a first approach, but It will be addressed in depth during feature selection)*

- Are the column information easily retrievable/known to set it as a parameter to the models? *Its important to define parameters that can truly be known*

Using the metadata and some basic Exploratory Data Analysis, some columns of the dataset were chosen to create the ML models. 

**Changing the data type of some columns**

There were some columns that should be used as numbers, or bool values, but the dataset was trating them as strings or viceversa. In that case, its important to set the right values to the columns to avoid errors. 

**Data imputation**

Is the process in which some missing data is filled with values according to the data. Use this method carefully, as this can modify the data distribution.

There are different methods for data imputation based on the type of the data and its context. For this project, some of the methods implemented were:

*KNNImputer:* 

This imputation model takes all the other features as inputs for a KNN model, where the target is the column that is trying to be imputed. 

For each null row, it sets the mean value of the K nearest neighbors.

This model, even when is used to set either categorical or numerical values, needs to work with numbers, so converting all the categorical features into numeric ones is mandatory.

All the features (numeric and categorical) were encoded using the OrdinalEncoder.

*Setting a value that represents the missing data*

In this case, 'False', '0', and 'None', are some of the values used on the different types of missing data.

### ***Dropping Duplicates***

Even when each row in the dataset has an unique ID, some columns that will be used by the model has the same values, so this rows were dropped. 

### ***Changing the Unit of Measure***

Some columns were originally measure using the english system of units. Nevertheless, to have a more intuitive vision of the units, the International  System of Units was used. To do so, some transformations had to be done.

### ***Renaming Columns***

As the original dataset didn't have intuitive column names, it was decided to change those names to more intuitive ones.

**Dropping duplicates**

Even when each row in the dataset has an unique ID, some columns that will be used by the model has the same values, so this rows were dropped. 

## ***Data Load***
Once the data was cleaned, the resulting dataset were saved as *vehicle_data_prepared.parquet*. 

Some of the advantages of the *parquet* extension over the *csv* or *xslx* extension is that the parquet file uses a column storage process rather than csv and xslx, that uses row storage process. This is a more efficient way to store data as it can retrieve only some columns instead of the whole dataset if needed. Also, parquet works better for large amount of data.