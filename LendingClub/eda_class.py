import pandas as pd


class EDA:

    def __init__(self):

        self._perf_df = pd.DataFrame(columns=['avg_interest_rate',
                                              'avg_loan_amount',
                                              'avg_lost_principle',
                                              'avg_interest_received',
                                              'avg_gains($)',
                                              'avg_gains(%)',
                                              'avg_total_payments',
                                              'annualized_return'])

    def calc_performance(self, df):

        # this method takes a data frame with loan information as an input
        # and then calculates high level performance metrics with respect
        # to investment gains.

        self._output_list = []

        # this function calculates high level data like average interest,
        # loan size, net gains and annualized returns

        # calculate average interest rate
        avg_interest_rate = 100 * df['int_rate'].mean()

        # calculate average loan size
        avg_loan_size = df['funded_amnt'].mean()

        # calculate average gains in terms of dollars earned
        avg_gains = df['net_gain'].mean()

        # calculate average gains in terms of %
        avg_gains_per = 100 * (avg_gains/avg_loan_size)

        avg_total_payments = df['total_payments'].mean()

        gains_dec = avg_gains_per / 100

        # multiply total payments by 30 to get the approximate # of days
        days = avg_total_payments * 30

        # calculate annualized return
        annualized_return = (((1 + gains_dec) ** (365/days)) - 1) * 100

        # add calculations to output list

        self._output_list = [avg_interest_rate, avg_loan_size,
                             avg_gains, avg_gains_per,
                             avg_total_payments, annualized_return]

        return self._output_list

    def add_df(self, data, df):

        # provided with a list and a data frame this method will
        # insert that list as a row in that data frame

        # convert list to series

        list_series = pd.Series(data, index=df.columns)

        df = df.append(list_series, ignore_index=True)

        self._df = df.round(3)

        return self._df

    def find_correlations(self, data, threshold):

        # identify correlated features and then remove them from the
        # data 'data_ml' data frame

        self._correlated_features = set()

        # drop the target variable (paid) and others that
        # aren't just included for annualized return calculations
        # not for machine learning

        # columns to drop
        columns = ['paid', 'total_payments', 'net_gain']
        cordata = data.drop(columns, axis=1)

        cor_matrix = cordata.corr()

        for i in range(len(cor_matrix.columns)):
            for j in range(i):
                if abs(cor_matrix.iloc[i, j]) > threshold:
                    colname = cor_matrix.columns[i]
                    self._correlated_features.add(colname)

        return list(self._correlated_features)

    def subset_data(self, data, removal_list):

        self._data = data

        # this function will remove the correlated features from the dataset
        # inputs: data frame, removal list from prior function
        # this and the other function will built to be reusable for a
        # variety of projects and to avoid errors related to typing
        # in column name by hand
        # this column can also be generally used to remove any columns
        # from a data frame

        self._data.drop(removal_list, inplace=True,  axis=1)

        return self._data

    def add_column(self, col_list, data, position, title):

        self._data = data

        self._data.insert(position, title, col_list, True)

        return self._data
