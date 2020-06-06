"""
CSE 163 Project
Solution Q3
Bennedict, Sidarth, Darren
"""


import pandas as pd
import numpy as np


def create_list(data):
    """
    Creates and returns a list of players in the ATP dataset sorted
    by player rankings
    """
    # Removing unused values
    data = data.loc[:, ['Series', 'Round', 'Winner', 'W2', 'L2', 'W3',
                        'L3', 'W4', 'L4', 'W5', 'L5']]
    # Handling Series column
    masters_cup = data['Series'] == 'Masters Cup'
    one_thousand = data['Series'] == 'Masters 1000'
    masters = data['Series'] == 'Masters'
    grand_slam = data['Series'] == 'Grand Slam'
    mask = masters_cup | one_thousand | masters | grand_slam
    data.loc[np.logical_not(mask), 'Series'] = 1
    data.loc[mask, 'Series'] = 2
    # Handling Round column
    zero = data['Round'] == '0th Round'
    first = data['Round'] == '1st Round'
    second = data['Round'] == '2nd Round'
    third = data['Round'] == '3rd Round'
    fourth = data['Round'] == '4th Round'
    round_robin = data['Round'] == 'Round Robin'
    mask = zero | first | second | third | fourth | round_robin
    data.loc[mask, 'Round'] = 1
    data.loc[data['Round'] == 'Quarterfinals', 'Round'] = 2
    data.loc[data['Round'] == 'Semifinals', 'Round'] = 3
    data.loc[data['Round'] == 'The Final', 'Round'] = 4
    data.astype({'Series': 'int32', 'Round': 'int32'})
    # Handling score difference
    five_rounds = data[data['W5'].notnull()]
    four_rounds = data[(data['W4'].notnull()) & (data['W5'].isnull())]
    three_rounds = data[(data['W3'].notnull()) & (data['W4'].isnull())]
    two_rounds = data[(data['W2'].notnull()) & (data['W3'].isnull())]
    five_rounds['Score Diff'] = five_rounds['W5'] - five_rounds['L5']
    four_rounds['Score Diff'] = four_rounds['W4'] - four_rounds['L4']
    three_rounds['Score Diff'] = three_rounds['W3'] - three_rounds['L3']
    two_rounds['Score Diff'] = two_rounds['W2'] - two_rounds['L2']
    # Assigning  weighed scores
    two_rounds['Weighed'] = two_rounds['Series'] * two_rounds['Round']
    two_rounds['Weighed'] += (two_rounds['Score Diff'] / 10)
    three_rounds['Weighed'] = three_rounds['Series'] * three_rounds['Round']
    three_rounds['Weighed'] += (three_rounds['Score Diff'] / 10)
    four_rounds['Weighed'] = four_rounds['Series'] * four_rounds['Round']
    four_rounds['Weighed'] += (four_rounds['Score Diff'] / 10)
    five_rounds['Weighed'] = five_rounds['Series'] * five_rounds['Round']
    five_rounds['Weighed'] += (five_rounds['Score Diff'] / 10)
    # Grouping by player names
    two_rounds = two_rounds.loc[:, ['Winner', 'Weighed']]
    three_rounds = three_rounds.loc[:, ['Winner', 'Weighed']]
    four_rounds = four_rounds.loc[:, ['Winner', 'Weighed']]
    five_rounds = five_rounds.loc[:, ['Winner', 'Weighed']]
    result = pd.concat([two_rounds, three_rounds, four_rounds, five_rounds])
    result = result.reset_index(drop=False)
    result = result.groupby('Winner')['Weighed'].mean()
    # Reordering in descending weighed score
    result = result.sort_values(ascending=False)
    result = result.index.tolist()
    return result


def compare_data(list1, list2):
    """
    Calculates and displays the percentage match of the two given lists
    for the first 30 elements
    """
    score = 0
    list1 = list1[:30]
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            score += 1
    percentage = score / len(list1) * 100
    print('Percentage Match: {0:.2f}%'.format(percentage))
    for i in range(len(list1)):
        if list1[i] in list2:
            score += 1
    percentage = score / len(list1) * 100
    print('Percentage Match per thirty elements: {0:.2f}%'.format(percentage))


def main():
    # Initialize data frame
    df = pd.read_csv('Data.csv', engine='python')

    # Creating the player list from the csv file
    player_list = create_list(df)

    # Creating the existing list from txt file
    existing_list = []
    with open('player-rankings.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            existing_list.append(line)

    # Calculate and display percentage match of the lists
    compare_data(player_list, existing_list)


if __name__ == '__main__':
    main()
