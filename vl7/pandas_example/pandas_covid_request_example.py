import pandas as pd
import requests
from pandas import DataFrame

url  = "https://www.berlin.de/lageso/gesundheit/infektionskrankheiten/corona/tabelle-indikatoren-gesamtuebersicht/index.php/index/all.json?q="

if __name__ == "__main__":

    response = requests.request("get", url).json()
    df = DataFrame(response["index"])

    # Show dataframe
    print(df)

