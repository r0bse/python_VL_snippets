ich_bin_ein_lambda = lambda arg = "defaultwert": print(arg)

if __name__ == "__main__":
    ich_bin_ein_lambda # failes
    ich_bin_ein_lambda()
    ich_bin_ein_lambda("foo bar")
