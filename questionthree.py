"""
CSE 163 Project
Solution to Question 3
Bennedict, Sidarth, Darren
"""


import pandas as pd


def main():
    df = pd.read_csv('Data.csv', engine='python')
    print(df.head())


if __name__ == '__main__':
    main()
