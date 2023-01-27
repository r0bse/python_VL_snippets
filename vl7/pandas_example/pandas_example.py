import pandas as pd


if __name__ == "__main__":

    data = {
        "name": ["Sally", "Mary", "John"],
        "age": [50, 40, 30],
        "qualified": [True, False, False]
    }

    df = pd.DataFrame(data)

    print(df)

    newdf = df.drop("age", axis='columns')

    print(newdf)