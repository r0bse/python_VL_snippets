import pandas as pd


if __name__ == "__main__":

    df = pd.read_csv('static/covid_berlin.csv', sep=';', decimal=',')

    # Show dataframe
    print(df)