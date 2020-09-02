"""
Markham Lee
CSE 163
Summer 2020
Section AA
This file contains the functions that are used to clean up,
subset and merge the datasets that we will be performing
analysis on. The functions in this file import the nba
player data, the combine data, clean the data and join it.
"""


import pandas as pd
import os
import glob2 as glob


def import_nba_stats():
    '''
    this function will import a directory full of csv files and then aggregate
    them into a single pandas data frame when passed a directory as a variable
    os is used to access the directory and glob is used to facilitate aggregating each csv into one file
    the 'header =1' command is used as the csv files have an erroneous extra row
    '''

    df_nba = pd.concat([pd.read_csv(f, header=1) for f in
                        glob.glob(os.path.join('nba_stats',
                                  "*.csv"))], sort=False)
    return df_nba


def organize_nba_data(data):
    '''
    This function organizes the nba data for easier analysis. First it by
    calculating the PPG metrics since it's not in the original dataset
    (points divided by games). Next, it then subsets the data so that it's
    only for an individual player's seasons with 58 games or more, an then
    aggregates the data so it's each player's average stats over the seasons
    in the data set. Finally, it takes a subset of the stats focusing on
    Player, PPG, WS, TRB, ORB, DRB, AST, STL, BLKs and TOV.
    '''

    # calculate points per game (PPG) points divided by games
    data.loc[:,'PPG'] = data['PTS'] / data['G']

    # subset the data to only include seasons where the athlete played 58
    # games, I.e. had a statistically significant season.

    nba_significant = data[(data['G'] >= 58)]

    # subset the data to only include the statistics we want to track,
    # since many are calculated from others (so they correlate) or
    # won't be useful

    nba_subset = nba_significant[['Player', 'Season', 'WS', 'G', 'MP', 'ORB',
                                  'DRB', 'TRB','AST', 'STL', 'BLK', 'PTS',
                                  'PPG']]

    # Aggregate the data by player so it's each player's average stats over
    # the time period instead of showing each player's individual season stats.

    clean_data = nba_subset.groupby('Player').mean()

    # sort in order of highest to lowest Win Share - helps with quickly
    # viewing the data

    clean_data = clean_data.sort_values('WS', ascending=False)

    return(clean_data)


def import_combine():
    '''
    This function imports the combine data into a pandas data frame
    '''

    all_combine_data = pd.read_csv('new_data/nba_draft_combine_all_years.csv')
    return all_combine_data


def merge_all_combine(data, nba):
    '''
    This function takes the data frame with all of the combine data and then
    merges it with the NBA player data, so we have a dataset that only includes
    combine data for players who were a) drafted b) played at least one 58 game
    season in the NBA.
    '''

    nba_all = pd.merge(nba, data, on='Player')
    return(nba_all)


def merge_complete_combine(data, nba):
    '''
    This function takes the combine data and then removes any players for
    which we don't have a complete set of combine data. E.g. Anthony Davis didn't
    participate in the sprint, agility or strength tests in his combine.
    '''
    # drops the instances where we don't have a complete data set for a player

    data = data.dropna()

    # merge with NBA player data set

    nba_complete = pd.merge(nba, data, on='Player')
    return(nba_complete)


def main():
    nba = import_nba_stats()
    clean_nba = organize_nba_data(nba)
    combine = import_combine()
    (combine, clean_nba)
    merge_complete_combine(combine, clean_nba)


if __name__ == '__main__':
    main()
