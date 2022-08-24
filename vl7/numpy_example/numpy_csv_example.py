import numpy as np

#The default data type(dtype) parameter for numpy.loadtxt( ) is float.
data = np.loadtxt("covid_berlin.csv", dtype=str)
print(data)

# fname	            file, file name, list to read.
# dtype	            The data type of the resulting array. If none, then the data type will be determined by the content of each column.
# comments	        All characters occurring on a line after a comment are discarded.
# delimiter	        The string is used to separate values. By default, any whitespace occurring consecutively acts as a delimiter.
# skip_header	    The number of lines to skip at the beginning of a file.
# skip_footer	    The number of lines to skip at the end of a file.
# missing_values	The set of strings corresponding to missing data.
# filling_values	A set of values that should be used when some data is missing.
# usecols	        The columns that should be read. It begins with 0 first. For example, usecols = (1,4,5) will extract the 2nd,5th and 6th columns.
data = np.genfromtxt(fname = "covid_berlin.csv",
                     dtype=None,
                     delimiter=";",
                     skip_header = 0,
                     skip_footer = 0,
                     missing_values=None,
                     filling_values=0,
                     usecols=(1,2,3,4,5,7,8,9),
                     encoding="UTF-8"
                     )
print(data)

