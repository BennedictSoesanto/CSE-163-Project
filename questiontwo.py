import pandas as pd

def main():
  df = pd.read_csv('Data.csv')
  df = df[df['ATP'] > 0]
  print(df.head())


if __name__ == '__main__':
  main()