# Creating a dataframe using List:
import pandas as pd

# list of strings
lyst = ['CSC', '102', 'is', 'the', 'best', 'course', 'ever']
 
# Calling DataFrame constructor on list
df = pd.DataFrame(lyst)
 
# Print the output.
print(df)

# Creating a dataframe using dict of narray/lists:
import pandas as pd
 
# initialize data of lists.
data = {'Name':['Angela', 'Precious', 'Luis', 'Ade'],
        'Age':[20, 21, 19, 18]}
 
# Create DataFrame
df = pd.DataFrame(data)
 
# Print the output.
print(df)
# Column Selection:
# Import pandas package
import pandas as pd
 
# Define a dictionary containing employee data
data = {'Name':['Clem', 'Prince', 'Edward', 'Adele'],
        'Age':[27, 24, 22, 32],
        'Address':['Abuja', 'Kano', 'Minna', 'Lagos'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
 
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
 
# select two columns
print(df[['Name', 'Qualification']])
# Row Selection:
import pandas as pd
 
# Define a dictionary containing employee data
data = {'Name':['Oyin', 'Mary', 'David', 'Bola'],
        'Age':[27, 24, 22, 32],
        'Address':['Asaba', 'Maiduguri', 'Onitsha', 'Kwara'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
 
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
 
# select first row
print(df.iloc[0])

# Select first row from file
import pandas as pd
 
# making data frame from csv file
data = pd.read_csv("employee_records.csv")
 
df = data.iloc[0]
 
# print excel
print(df)

# Selecting Row with Title Header
# importing pandas package
import pandas as pd
 
# making data frame from csv file
data = pd.read_csv("bcg.csv")
 
df = data.head(1)
 
# print excel
print(df)

# Looping over rows and columns
# importing pandas as pd
import pandas as pd
 
# dictionary of lists
dicts = {'name':["Abdul", "Chukwuemeka", "Seyi", "Matt"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
 
# creating a dataframe from a dictionary 
df = pd.DataFrame(dicts)
 
# iterating over rows using iterrows() function 
for i, j in df.iterrows():
    print(i, j)
    print()

# Looping over Columns :
# importing pandas as pd
import pandas as pd
 
# dictionary of lists
dicts = {'name':["Bello", "Kamara", "Ugochi", "David"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
 
# creating a dataframe from a dictionary 
df = pd.DataFrame(dicts)
 
# creating a list of dataframe columns
columns = list(df)
 
for i in columns:
 
    # printing the third element of the column
    print (df[i][2])

# Saving a DataFrame as CSV file
# importing pandas as pd
import pandas as pd
 
# dictionary of lists
records = {'name':["Abel", "Kamsi", "Oyode", "Chinelo"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
 
# creating a dataframe from a dictionary 
df = pd.DataFrame(records)
 
# saving the dataframe
df.to_csv('record.csv')
