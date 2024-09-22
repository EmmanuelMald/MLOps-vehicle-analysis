# MLOps vehicle analysis

The goal of this repository is to create and deploy some ML models that can predict:

- CO<sub>2</sub> emissions (g/km)

- Autonomy (km/L)

Based on some parameters such as fuel type, make, basemodel, etc. Allowing to experiment with personalized vehicles and see how each feature might impact on the car autonomy and CO<sub>2</sub> emissions. 

## How to run this repo:

### 1. Clone this repo

### 2. Install *pyenv* (optional)

I highly recommend to install [**pyenv**](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation) to manage the python versions in your computer.

Follow the link to find instructions about how to install it based on your operating system.

### 3. Install *poetry*

You can follow the instruction from the [**poetry documentation**](https://python-poetry.org/docs/#installing-with-the-official-installer)

I highly recommend using the official installer

### 4. Setting up the your localdev

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
- Vehicle Size Class
- Vehicle Year
- Drive
- General fuel type
- Specific fuel type
- Electric motor
- Start-stop feature

A *multiple linear regression* was implemented in this model

## Official Documentation

All the information related to: 
- *Machine learning models*
- *Sources of data*
- *Deployment*

can be found in the [**Official Documentation**](https://emmanuelmald.github.io/MLOps-vehicle-analysis/) of this repository




