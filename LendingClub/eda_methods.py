import pandas as pd



def calc_performance(df):

    output_list = []

    avg_interest_rate = 100 * df['int_rate'].mean()

    avg_loan_size = df['funded_amnt'].mean()

    avg_lost_principle = df['lost_principle'].mean()

    avg_rec_interest = df['total_rec_int'].mean()

    avg_gains = df['net_gain'].mean()

    avg_gains_per = 100 * (avg_gains/avg_loan_size)

    avg_total_payments = df['total_payments'].mean()

    gains_dec = avg_gains_per / 100

    # multiply total payments by 30 to get the approximate # of days
    days = avg_total_payments * 30

    # calculate annualized return
    annualized_return = (((1 + gains_dec) ** (365/days)) - 1) * 100

    # add calculations to output list

    output_list = [avg_interest_rate, avg_loan_size, avg_lost_principle,
                   avg_rec_interest, avg_gains, avg_gains_per,
                   avg_total_payments, annualized_return]

    return output_list


def add_df(data, df):

    # convert list to series

    list_series = pd.Series(data, index=df.columns)

    df = df.append(list_series, ignore_index=True)

    df = df.round(3)

    return df





def main():

    # empty data frame to store index

    performance_df = pd.DataFrame(columns=['avg_interest_rate',
                                           'avg_loan_amount',
                                           'avg_lost_principle',
                                           'avg_interest_received',
                                           'avg_gains($)',
                                           'avg_gains(%)',
                                           'avg_total_payments',
                                           'annualized_return'])

    # create empty list to store index for the above

    # df_index = []

    data = pd.read_csv('data/LC_2015_clean(4).csv')
    perf_list = calc_performance(data)

    perf_df = add_df(perf_list, performance_df)




    print(perf_df)

    # print(test)
    # ty = pd.DataFrame(test)
    # ty.head()


if __name__ == '__main__':
    main()
