import pandas as pd

# Read the CSV file
df = pd.read_csv("test_dataframe/csv_comma_no_quote.csv")

# Create a new dataframe that is seperated by semicolon + no quote
df.to_csv("test_dataframe/csv_semi_no_quote.csv",
               index = False,
               sep = ";",
               quoting = 0)

# Create a new dataframe that is seperated by tab + no quote
df.to_csv("test_dataframe/csv_tab_no_quote.csv",
               index = False,
               sep = "\t",
               quoting = 0)

# Create a new dataframe that is seperated by semicolon + double quote
df.to_csv("test_dataframe/csv_semi_double_quote.csv",
               index = False,
               sep = ";",
               quotechar = "\"",
               quoting = 1)

# Create a new dataframe that is seperated by tab + double quote
df.to_csv("test_dataframe/csv_tab_double_quote.csv",
               index = False,
               sep = "\t",
               quotechar = "\"",
               quoting = 1)

# Create a new dataframe that is seperated by comma + single quote
df.to_csv("test_dataframe/csv_comma_single_quote.csv",
               index = False,
               sep = ",",
               quotechar = "\'",
               quoting = 1)

# Create a new dataframe that is seperated by semicolon + single quote
df.to_csv("test_dataframe/csv_semi_single_quote.csv",
               index = False,
               sep = ";",
               quotechar = "\'",
               quoting = 1)

# Create a new dataframe that is seperated by tab + single quote
df.to_csv("test_dataframe/csv_tab_single_quote.csv",
               index = False,
               sep = "\t",
               quotechar = "\'",
               quoting = 1)