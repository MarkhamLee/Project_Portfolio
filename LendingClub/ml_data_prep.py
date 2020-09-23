import pandas as pd


# set parameters for seeing all columns

pd.set_option('max_columns', None)
pd.set_option('display.max_rows', None)


# import data

data_ml = pd.read_csv('data/LC_2015_clean(4).csv')

data_ml.head(10)


# select the columns we don't need and then remove them from the dataset

columns = ['issue_d', 'addr_state', 'grade', 'earliest_cr_line',
           'annual_inc', 'purpose', 'dti', 'application_type',
           'total_pymnt', 'total_pymnt_inv', 'total_rec_prncp',
           'total_rec_int', 'monthly_income', 'application_type',
           'mths_since_last_delinq', 'num_tl_120dpd_2m', 'revol_bal',
           'total_rec_late_fee', 'monthly_debt_payments',
           'pub_rec_bankruptcies', 'updated_monthly_debt_payments',
           'lost_principle', 'total_bal_ex_mort']


data_ml.drop(columns, inplace=True, axis=1)

# add dummy variables to the data frame

data_ml = pd.get_dummies(data_ml)

data_ml.head(20)


# rename the columns

data_ml.rename(columns={'loan_status_Fully Paid': 'paid'}, inplace=True)
data_ml.rename(columns={'loan_status_Charged Off': 'default'}, inplace=True)

data_ml


# drop the default column

columns = ['default']

data_ml.drop(columns, inplace=True, axis=1)

data_ml.to_csv(r'data/new_ml_data(paid-v6)_ALL.csv', index=False)

print('file processing complete')
