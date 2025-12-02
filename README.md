# ds4420-final-project

**Modeling Animal Shelter Outcomes with MLPs and Time Series**

This project aims to predict adoption outcomes to help optimize resources and improve animal welfare in animal shelters. This repository contains two methods: a multi-layer perceptron (MLP) to model pet attributes and a time series model to forecast seasonal trends. While these models operate independently, their insights can be used together to guide a shelter’s daily operations.


**Data**

The dataset used was sourced from the Austin Animal Center Outcomes public dataset published by the City of Austin Open Data Portal.

Data source link: https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Outcomes-10-01-2013-to-05-05-/9t4d-g238/about_data

The dataset contains ~173k records from 2013-2025, with the following features:

- Animal ID
- Date of Birth
- Name
- DateTime (data of outcome)
- MonthYear (month-year of outcome)
- Outcome Type (Adoption, Transfer, Return-to-owner, Euthanasia, Died, etc.)
- Outcome Subtype
- Animal Type (Dog, Cat, etc.)
- Sex upon Outcome (Male/Female, Neutered/Spayed)
- Age upon Outcome
- Breed
- Color


**MLP Model**

The DS420_Final_Project_MLP.ipynb file contains sufficient code to recreate the first method of this project. Re-run the cells to display the outputs if needed. 

We started by cleaning the data, which includes isolating the relevant, non-null features (name, animal type, Sex upon Outcome, Age upon Outcome, Breed, and Color). The name field was simplified to a binary "hasName" indicator, and “Sex upon Outcome” was split into biological sex and neutered/spayed status. Age values were standardized into years, and colors were grouped into broader categories (black, brown, etc.). Since breed contained 3,000+ unique labels, we represented it using embeddings. Finally, we limited Outcome Type to the top five most common classes for modeling.

Preprocessing steps were also completed to standardize numerical columns, as well as to separate train and test sets. The model takes two inputs: a breed ID processed through a 16-dimensional embedding layer, and all other numerical/categorical features passed as a standard feature vector. These inputs flow through hidden ReLU layers (64 -> 32 units), are concatenated, and then passed through an additional 64-unit hidden ReLU layer. The output layer uses a softmax activation to predict probabilities across the five outcome classes. The model is trained with the Adam optimizer and categorical cross-entropy loss, which is appropriate for multi-class classification.

Performance was examined through accuracy, precision, recall, F1 score, and a confusion matrix for true vs. predicted outcomes. Results show strong detection of common outcomes (Adoption, Transfer), with more errors for rarer classes.

**Time Series Model**

The __.R file contains sufficient code to recreate the second method of this project. Re-run the code blocks to display the outputs if needed.



**Streamlit App**

The app directory contains the files necessary to deploy our project application. The app.py file contains the code for the two tabs - a home tab containing the project overview and a results tab containing the interactive visual for the MLP. The requirements.txt file contains the imports/packages that are necessary to build the content of the app. The html file contains the confusion matrix and the jpg image for the home page, both which were imported into the app.py file. To run locally, make sure that all the imports are installed, and run 'streamlit run app/app.py.' To deploy the app from Github, we used the Streamlist Community Cloud website.

App link: https://ds4420-final-project.streamlit.app/
