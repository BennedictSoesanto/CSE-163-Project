"""
CSE 163 Project
Solution Q3
Bennedict, Sidarth, Darren
"""


import pandas as pd


def create_list(data):
    """
    Creates and returns a list of players in the ATP dataset sorted
    by player rankings
    """
    pass


def compare_data(list1, list2):
    """
    Calculates and displays the percentage match of the two given
    lists
    """
    score = 0
    for i in range(list1.length()):
        if list1[i] == list2[i]:
            score += 1
    percentage = int(score / len(list1) * 100)
    if percentage >= 80:
        print('The results are accurate!')
    else:
        print('The results are inaccurate!')
    print('Percentage Match: ', percentage)


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
    percentage_match = compare_data(player_list, existing_list)


if __name__ == '__main__':
    main()
