# Pandas
# Pandas is a Python library used for data manipulation, analysis, and cleaning.
# It provides powerful data structures like:
# Series 1D labeled array like a column in Excel
# DataFrame 2D labeled table like a whole Excel sheet or SQL table

# Uses of Pandas
# Easy to read and write CSV/Excel files
# Handle missing data
# Powerful grouping, filtering, and aggregating
# Easy data transformation (merge, join, pivot, etc.)
# Fast and efficient with large datasets

# Basic Concepts
import pandas as pd

import pandas as pd

data = {
    "Name": ["Shubham", "Mohit", "Gelson"],
    "Age": [21, 20, 21],
    "City": ["Nagpur", "Haryana", "Gaya"]
}

df = pd.DataFrame(data)
print(df)

# Reading from a File
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")

# Viewing Data
df.head()        # First 5 rows
df.tail()        # Last 5 rows
df.info()        # Structure of DataFrame
df.describe()    # Summary stats for numeric columns

# Selecting Data
df["Name"]               # Single column
df[["Name", "Age"]]      # Multiple columns
df.loc[1]                # Row by index label
df.iloc[1]               # Row by index position
df[df["Age"] > 20]       # Filtering rows

# Adding/Modifying Columns
df["New_Column"] = df["Age"] * 2

# Handling Missing Data
df.dropna()              # Drop rows with NaN
df.fillna(0)             # Fill NaN with 0

# Saving Data
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
