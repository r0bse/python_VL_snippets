import pandas as pd


if __name__ == "__main__":

    df = pd.read_csv('static/covid_berlin.csv', sep=';')

    # Show dataframe
    print(df)