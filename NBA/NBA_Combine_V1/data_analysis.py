"""
Markham Lee
CSE 163
Quiz Section AA
Final Project Part Two
This file contains the functions used to analyze the cleaned and
merged NBA from the data_processing file.
"""

import data_processing  # noqa: F401
import matplotlib.pyplot as plt
import seaborn as seabornInstance
import seaborn as sns

# hw2_manual.max_level(more_tests_dict)


def investigate_nba(nba):
    '''
    Calculates summary statistics for the NBA player data, mean, max,
    number of measurements, etc.
    '''

    # take a high level view of the NBA data
    nba_metrics = nba.describe()
    return nba_metrics

    # look at the WS metric, how does it correlate with other NBA stats?


def nba_correlations(nba):
    '''
    This looks at the WS metric and the other stats it correlates to
    i.e. asking how good is our chosen statistic?
    '''

    ws_corr = nba.corr().round(2)
    sns.heatmap(data=ws_corr, annot=True)
    plt.title('Winshare Correlation Matrix')
    plt.savefig('visualizations/NBA_WS_correlations.png', 
                bbox_inches='tight', pad_inches=0.1)


def ws_distribution(nba):
    '''
    This function takes in the clean nba data as an input
    and plots distrubution bar chart(s) of win share
    and points per game so we can see average and if the distrubution
    is normal
    '''

    plt.figure(figsize=(15, 10))
    plt.tight_layout()
    seabornInstance.distplot(nba['WS'])
    plt.title('Winshare Distribution')
    plt.savefig('visualizations/NBA_WS_distribution.png',
                bbox_inches='tight', pad_inches=0.1)

    plt.figure(figsize=(15, 10))
    plt.tight_layout()
    seabornInstance.distplot(nba['PPG'])
    plt.title('PPG Distribution')
    plt.savefig('visualizations/PPG_distribution.png', bbox_inches='tight',
                pad_inches=0.1)

def combine_draft_ws(combine):
    '''
    The purpose of this method is to answer the question: how good is the NBA
    evaluation system overall, by comparing draft position to WS and
    statistics in general.
    '''

    # subset the data to just compare draft position to stats

    combine_subset = combine[['Draft pick', 'WS', 'TRB', 'AST', 'STL', 'PPG', 
                              'BLK']]

    # create correlation plot and save to a PNG file
    draft_corr = combine_subset.corr().round(2)
    sns.heatmap(data=draft_corr, annot=True)
    plt.title('Draft Effectiveness Correlation Matrix')
    plt.savefig('visualizations/draft_correlations.png', bbox_inches='tight', 
                pad_inches=0.1)

    # linear plot to visualize the correlation between draft position and 
    # win share

    sns.lmplot(x='Draft pick', y='WS', data=combine_subset)
    plt.title('Draft Effectiveness Linear Plot for WS')
    plt.savefig('visualizations/draft_plot.png', bbox_inches='tight', 
                pad_inches=0.1)

    # linear plot to visualize the correlation between draft position and PPG
    sns.lmplot(x='Draft pick', y='PPG', data=combine_subset)
    plt.title('Draft Effectiveness Linear Plot for Points per Game')
    plt.savefig('visualizations/draft_ppg_plot.png', bbox_inches='tight', 
                pad_inches=0.1)


def combine_analysis_correlation(data):
    '''
    This function looks to see if there are any correlations
    between combine measurements and NBA performance.
    '''

    # combine data WS distribution

    plt.figure(figsize=(15, 10))
    plt.tight_layout()
    seabornInstance.distplot(data['WS'])
    plt.title('Combine Winshare Distribution')
    plt.savefig('visualizations/combine_WS_distribution.png', bbox_inches='tight',
                pad_inches=0.1)

    # compute correlation matrix

    combine_correlation = data[['WS', 'PPG', 'Draft pick', 'Wingspan',
                                'Vertical (Max)', 'Hand (Length)',
                                'Hand (Width)', 'Bench', 'Agility', 'Sprint']]

    combine_corr = combine_correlation.corr().round(2)
    sns.heatmap(data=combine_corr, annot=True)
    plt.title('Do Combine Measurements Correlate to In Game Performance?')
    plt.savefig('visualizations/combine_correlations(2).png',
                bbox_inches='tight', pad_inches=0.1)

    # what does a linear plot look like for the strongest correlators?

    # linear plot to visualize the correlation between WS and Wingspan
    sns.lmplot(x='Wingspan', y='WS', data=combine_correlation)
    plt.title('Wing Span vs. WS')
    plt.savefig('visualizations/wingspan_vs_ws.png', bbox_inches='tight',
                pad_inches=0.1)

    # linear plot to visualize the correlation between WS and Agility
    sns.lmplot(x='Agility', y='WS', data=combine_correlation)
    plt.title('Agility vs. WS')
    plt.savefig('visualizations/agility_vs_ws.png', bbox_inches='tight',
                pad_inches=0.1)


def combine_stats(data):
    '''
    Calculating some summary stats for the complete and clean merged
    combine and NBA data
    '''
    summary = data.describe()
    return summary


def main():
    # import cleaned NBA data
    nba_data = data_processing.import_nba_stats()
    clean_nba = data_processing.organize_nba_data(nba_data)
    print(investigate_nba(clean_nba))

    # plot correlation matrix for the NBA stats vs. Winshare
    nba_correlations(clean_nba)

    # plot distribution of average Win Share stats over the
    # past seven seasons.

    ws_distribution(clean_nba)

    # import all combine data
    all_combine = data_processing.import_combine()

    # import all combine with nba
    all_nba_combine = data_processing.merge_all_combine(all_combine, clean_nba)

    # generate correlation and linear regression plots for Winshare for
    # all players in the combine data set
    combine_draft_ws(all_nba_combine)

    # import complete combine data merged with nba
    clean_nba_combine = data_processing.merge_complete_combine(all_combine,
                                                               clean_nba)

    # high level combine analysis
    combine_analysis_correlation(clean_nba_combine)

    # get high level summary statistics of the merged and complete combine data
    overview = combine_stats(clean_nba_combine)
    print(overview)


if __name__ == '__main__':
    main()