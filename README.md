# Vehicle CO<sub>2</sub> emissions & autonomy estimators

The goal of this repository is to create and deploy some ML models that can predict:

- CO<sub>2</sub> emissions (g/km)

- Autonomy (km/L)

Based on some parameters such as fuel type, make, basemodel, etc. Allowing to experiment with personalized vehicles and see how each feature might impact on the car autonomy and CO<sub>2</sub> emissions. 

**This model can predict the automony and emissions of some different types of fuel: gasoline, electricity, hydrogen, among others**

## Content

[**How to run this repo**](#how-to-run-this-repo)

[**Machine Learning Models**](#machine-learning-models)

- [**CO<sub>2</sub> emissions estimator**](#co2-estimator)

- [**Autonomy estimator**](#autonomy-estimator-kml)

[**Documentation**](#documentation)


## How to run this repo:

### 1. Clone this repo

### 2. Install *pyenv* (optional)

I highly recommend to install [**pyenv**](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation) to manage the python versions in your computer.

Follow the link to find instructions about how to install it based on your operating system.

### 3. Install *poetry*

You can follow the instruction from the [**poetry documentation**](https://python-poetry.org/docs/#installing-with-the-official-installer)

I highly recommend using the official installer

### 4. Setting up your localdev

If you're using pyenv, I highly recommend to run this command on the root of this repository:

    # only if you haven't install python 3.11.4 yet
    pyenv install 3.11.4 

Then run:

    pyenv local 3.11.4

This will create a file in the root directory called *.python-version* which will save the python version that this repo will use (git will ignore this file)

After doing this, in the root of this repo, run:

    poetry install --all-extras

Then, run:

    poetry shell

This will allow to run all the scripts and notebooks of this repo!

## Machine Learning Models

### CO<sub>2</sub> estimator

This model returns the grams of CO<sub>2</sub> emitted per kilometer by a car based on the next parameters:

- Make
- Basemodel
- Engine displacement (L)
- Transmission
- Cylinders
- Vehicle size class
- Vehicle year
- Drive
- General fuel type
- Specific fuel type
- Electric motor
- Start-stop feature

A *multiple linear regression* was implemented in this model


To know more about how to use this model, go to [**CO<sub>2</sub> estimator**](https://emmanuelmald.github.io/Vehicle-CO2-Emissions-and-Autonomy-Estimators/machine_learning/)

### Autonomy Estimator (km/L)

This model returns the total estimated autonomy of a vehicle combining the city and highway consumption of the main fuel used.

The parameters used to estimate it are:

- Basemodel
- Engine displacement (L)
- Cylinders
- Make
- Transmission
- Vehicle size class

To know how to use this model, go to [**Autonomy estimator**](https://emmanuelmald.github.io/Vehicle-CO2-Emissions-and-Autonomy-Estimators/autonomy_estimator/)

## Documentation

All the information related to: 
- *Machine learning models*
- *Sources of data*
- *Deployment*

can be found in the [**Documentation**](https://emmanuelmald.github.io/Vehicle-CO2-Emissions-and-Autonomy-Estimators/) of this repository




