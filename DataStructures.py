# Pandas dataframes seem to take the place of PowerShell Object in PS..
# Let's say we pull data from Yahoo finance like:

import yfinance as yf
import datetime as dt

enddate = dt.date.today()
startdate = enddate + dt.timedelta(days=-20)  # Retrieve 20 calendar days to allow for no-trading weekend days.
data = yf.download("BA", start=startdate, end=enddate)[-10:]  # Data of the lst 10 trading sessions of ticker "BA".

print("Data retrieved:")
print(data)
print(f"data type {type(data)}")  # data type <class 'pandas.core.frame.DataFrame'>

# Understanding pandas dataframe data structure

# Get list of column names:
print()
print("column list is returned by the .columns method:")
for column in data.columns:
    print(column, end=", ")
print()
print(f"column type {type(column)}")  # column type <class 'str'>

# Get list of row names:
print()
print("row list is returned by the .index method:")
for row in data.index:
    print(f"{row.year}-{row.month}-{row.day}", end=", ")
print()
print(f"row type {type(row)}")  # row type <class 'pandas._libs.tslibs.timestamps.Timestamp'>

# A specific value can be referred to by the .at method - intersection of row and column labels as in:
print()
print("A specific value can be referred to by the .at method - intersection of row and column labels")
print("as in data.at['2022-09-15', 'Adj Close']")
print(f"Adjusted closing price 'Adj Close' on 2022-09-15 is {data.at['2022-09-15', 'Adj Close']}")  # 149.77999877929688

