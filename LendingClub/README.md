# Lending Club

Lending Club (LC) is a lender that provides personal loans for debt consolidation and major purchases. The company works on a "peer to peer" basis, in that loans are often funded by individual investors who can look at a series of potential loan "investments" and choose to fund all or part of the loan. The goal of this analysis will be find out if machine learning and/or general EDA could be used to hypothetically improve one's returns beyond what one would get by selecting loans by the grades LC assigns to them, or by investing in a broad basket of loans. Unlike most machine learning problems where the accuracy is the primary objective, I intend to show how a "good" or "okay" model can dramatically improve returns in a peer to peer lending scenario if it identifies a significant percentage of the bad loans. A loan default can cost significantly more than paid off loan generates in profit, so within certain parameters a model that causes you to "miss out" on a number of good investments is still valuable if it flags a significant number of bad ones. The general idea is that since an individual investor can only invest in a limited number of loans, the goal is to minimize the # of bad loans in basket of loans that are selected for investment.

## Note on the data

Unless prior authorization is given Lending Club restricts the use of their data to investment evaluation purposes, so I've limited the scope of this project to looking at things from an investment perspective and have purposely avoided analyses that go beyond the scope of what's included in their public facing data for potential investors. Functionally this means that the EDA won't do things like profile ideal customers, and the predictive modeling will focus on minimizing losses.

If you want to replicate my results you will have to download the data for the 2015 calendar year directly from Lending Club, create a directory called 'data' and then update the file name where appropriate in the preprocessing file. Also, the LC files downloaded in an inconsistent matter whereas some opened up without issues and others didn't, in a few instances I had to open them up in Excel and then re-save them as a UTF-8 CSV.

Additionally: this code, analysis and files in this repository are strictly for educational purposes and are not meant to constitute investment advice.

## Replicating Results

In order to replicate my results, follow the precise order to clean and prepare the data:

1) Download data for the 2015 calendar year from the Lending Club web site
2) Use the LC_preprocessing_final.py file to handle initial dating cleaning, e.g. fixing data types, adding measures, etc.
3) Import the CSV created by the above file into the LC_Cleaning_LightEDA notebook, this file will
perform some high level cleaning + some light EDA. This notebook will handle things like missing values and filtering out irrelevant data.
4) Either import the output of the above notebook into the ml preparation script or into the EDA script. My suggestion is to do the EDA notebook first for additional context, prior to running the machine learning analysis.
5) After running the ml_prep_script, open up and run the machine learning notebook to generate those results. I.e. models, accuracy measures and investment analysis.

## This repository contains the following files

Note: in order to replicate my results, you should run the files and/or notebooks in the order they're listed below after first downloading the dataset from Lending Club.

1) **LC_preprocessing_final.py:** this python script imports the downloaded CSV file from the Lending Club web site and does the initial high level data cleaning related to items where the cleaning tasks are more intuitive and don't need significant study an analysis first. E.g. removing the '%' symbol from the values in the interest rate column. Cleaning tasks in this file included: taking log values of columns with large ranges (E.g. income ranged from several thousand to several million) calculating measures such as lost principle, the customer's monthly debt payments before and after the loan and expressing measures such as length of employment in months. Another reason for doing this work in a single script vs. a notebook is that due to the size
of the file, it was significantly faster to subset the file, update fields and calculate measures in a script vs a notebook.

2) **LC_Cleaning_LightEDA.ipynb:** this file is the second stage of cleaning the data, along with some high level EDA. The cleaning tasks in this file were of the type that required significant analysis, E.g. filling in missing values or condensing the categories of loan purposes. This file also hot encodes certain fields and then generates a CSV file that can then be picked up/used by the machine learning notebook. This file will generate a CSV file for the next stage.

3) **LC_EDA_FINAL.ipynb:** this notebook where the EDA was performed, inclusive of things such as calculating default rates, analyzing loan default trends and creating visualizations. This document takes as an input the CSV file generated by the notebook above. It also has a series of functions are used to generate most of the analysis simply for expediency sake, as it allows me or another user to quickly perform additional EDA or look at the data from another angle.

4) **ml_data_prep.py:** this file prepares the data for machine learning by removing certain columns and adding dummy variables. It also has helper functions for finding highly correlated features and deleting those columns from the dataset. The functions for finding feature correlations weren't used, as I did that work in the machine learning notebook as it was easier given the work I needed to do around analyzing investment returns prior to removing features and performing machine learning modeling. Since the purpose of this file is to be a general purpose machine learning preparing script, I left the correlated features functions in.

5) **Machine Learning Notebooks**

    * **LendingClub(all_Loans)_ML_FINAL(V1).ipynb:** this notebook contains three different machine learning models that compares output of three models (L1 logistic regression, L2 logistic regression & Decision Tree, calculates default rate for each and improved annualized return for the winning model.
    * **LendingClub(all_Loans)_ML_FINAL(V2).ipynb:** this notebook is identical to the notebook above in terms of results, but shifts all of the functions a lot of eda calculations to an external class (eda_class.py), in order to enhance readability. E.g. there aren't several panes of helper functions you have to scroll past prior to seeing the analysis and machine learning models. The caveat is that you have to download both the notebook and the helper class, as it isn't a stand alone notebook like the one above. I included it because I think that embedding classes is a good way to streamline notebooks for data presentation purposes.

### Updates

* 9/17/2020: added the README file, LC_proprocessing(final).py and the notebook used to perform additional data cleaning and feature engineering.
* 9/22/2020: added an initial draft of the most extensive EDA, future plan is to replace all the functions with an embedded class to make the output even cleaner.
* 9/26/2020: added **LendingClub(all_loans)_ML_FINAL(V1).ipynb** - notebook containing machine learning modeling + investment analysis. Also added a machine learning preparation script. **ml_data_prep.py**
* 10/02/2020: added a second notebook that uses a "helper class" that contains functions that executes a lot of the functionality, in order to make the notebook more readable. Also added the helper class eda_class.py.
