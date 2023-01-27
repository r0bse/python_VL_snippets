import pandas as pd

def create_Percentage_Column():

    data = {
        "Name": ["Sally Meier", "Mary Jones", "John Doe"],
        "Points": [450, 400, 378]
    }

    # creating a pandas dataframe
    df = pd.DataFrame(data,columns=['Name','Points'])

    # Applying lambda function to find percentage of 'Total_Marks' column
    # using df.assign()
    df = df.assign(Percentage = lambda x: (x['Points'] /500 * 100))

    # displaying the data frame
    print(df)

def use_lambda_on_column():

    data = {
        "Name": ["Sally Meier", "Mary Jones", "John Doe"],
        "Points": [450, 400, 378]
    }

    # creating a pandas dataframe
    df = pd.DataFrame(data)
    # run a lambda on the "Points" Column and replace the original value in "df"
    df.Points = df.Points.apply(lambda x: (x * 2))

    # you can also give functions a parameter
    df.Points = df.Points.apply(add_4)

    # displaying the data frame
    print(df)

def print_head_tail_and_columns():

    data = {
        "Name": ["Sally Meier", "Mary Jones", "John Doe"],
        "Points": [450, 400, 378]
    }

    # creating a pandas dataframe
    df = pd.DataFrame(data)
    print(df.head(2))
    print(df.tail(2))
    print(df.columns.values)

def add_4(x):
    return x+4

if __name__ == "__main__":
    create_Percentage_Column()
    use_lambda_on_column()
    print_head_tail_and_columns()