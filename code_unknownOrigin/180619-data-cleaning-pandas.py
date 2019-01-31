# Pandas commands for dealing with common(?) data cleaning issues
import pandas as pd

# LOOK AT DATA FOR OBVIOUS ISSUES
df.colname.describe() # For numeric data
df.colname.value_counts() # Unique values and counts (for categorical data)
df.head() # Print first five rows
df.tail() # Print last five rows

# STANDARDIZE DATA TYPE
# Change data type of columns 
# (quick check to see if obvious errors are thrown)
df.colname = pd.to_numeric(df.colname, errors='raise')
df.colname = pd.to_datetime(df.colname, format='%Y-%m-%d-%H-%M-%S')

# Standardize string data
df.colname = df.colname.str.strip() # remove leading and trailing whitespace
df.colname = df.colname.str.replace(' ', '') # remove all whitespace
df.colname = df.colname.str.lower() # standardize strings to avoid search mismatch by case
# Note: can concatenate commands:
df.colname = df.colname.str.strip().str.lower().str.replace(' ', '_')

# DUPLICATE DATA
# Check ID column for duplicates
print(df.duplicated(colname).sum()) # print # duplicates in that column

# Remove duplicates in a specific column only (such as the ID column)
df = df.drop_duplicates(keep='first', subset=colname)

# MISSING DATA
# Check for missing data
print(df.colname.isnull().sum()) # print # entries with missing data in the column

# Fill in missing data with a static value
df.colname.fillna(0.1)
# Fill in missing data with data from another column
df.colname.fillna(df.replacementcol, inplace=True)

# INCORRECT DATA 
# If there is a known threshold of true values you want to clip to
df.colname = df.colname.clip(lower=0.001, upper=100)

# IMPORTING SPECIAL / WEIRD DATA
# Importing standard but large CSVs
df = pd.read_csv("filename.csv", low_memory=False) # Avoid memory errors

# Import CSVs with special string characters
df = pd.read_csv("filename.csv", encoding='latin1') # Or other relevant encoding

# Read space-separated files
df = pd.read_csv('filename.dat', sep='\s+')

# Do some other random string operations when dividing up a file into columns
# (This example just seperates by spaces)
content = [i.strip().split() for i in open("filename").readlines()]
colnames = ['colname1', 'colname2', 'colname3', 'colname4']
df = pd.DataFrame(content, columns=colnames)