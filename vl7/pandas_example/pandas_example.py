import pandas as pd


if __name__ == "__main__":

    # Creating and initializing a nested list
    age = [['Aman', 95.5, "Male"], ['Sunny', 65.7, "Female"],
         ['Monty', 85.1, "Male"], ['toni', 75.4, "Male"]]

    # Creating a pandas dataframe
    df = pd.DataFrame(age, columns=['Name', 'Marks', 'Gender'])

    # Printing dataframe
    print(df)

    #refer to the row index:
    print(df.loc[0])
    df.drop('column_name', axis=1, inplace=True)
