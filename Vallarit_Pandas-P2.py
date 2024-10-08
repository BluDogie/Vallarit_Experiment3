#PROBLEM 2: Save your file as Surname_Pandas-P2.py
# Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.

#a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
#b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
#c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
#d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

import pandas as pd #import pandas library

cars = pd.read_csv("cars.csv") #load the .csv file into a data frame named cars using pandas

# For Letter A
cars.iloc[:,::2].head() # Use iloc to specifically get which columns to display, specifically the columns that are odd-numbered.
# : to display all rows
# ::2 to start at the beginning and step by 2.

# For letter B.
cars.loc[cars['Model']=='Mazda RX4']

# For letter C.
cars.loc[cars['Model']=='Camaro Z28', ['Model','cyl']]

# For letter D.
models = ('Mazda RX4 Wag','Ford Pantera L','Honda Civic') # Set up a tuple for the models of the cars
cars.loc[cars['Model'].isin(models),['Model','cyl','gear']] # Use the .isin() function so that it can identify the elements of the variable in the dataframe.