# Pandas Project
# Student Name: Mark Biggar
# Student Number: G00376334

# Write a program to examine the Fisher's Iris data set

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.plotting import scatter_matrix

# Load digits dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"            # URL of data source being used
name = ["Sepal_length", "Sepal_width", "Petal_length", "Petal_width", "Class"]          # Headers of rows, as data source does not contain any
iris_ds = pd.read_csv(url, names=name)                                                  # Loading of data set to "iris_ds"

# Force conversion of values that look like number to numbers
cols=iris_ds.columns.drop("Class")
iris_ds[cols]=iris_ds[cols].apply(pd.to_numeric, errors="coerce")                       

# Set the indexing column to Class
iris_ds = iris_ds.set_index("Class")                                                    

# Choose data set
print()
print("Which data set would you like to use?")                                          # Allows users to examine only a subset of the dats
print()
print("1) All data in Fisher's Iris data set")                                          # Entire data set
print("2) Iris Setosa data set")                                                        # Only Iris Setosa data
print("3) Iris Versicolor data set")                                                    # Only Iris Versicolor data set
print("4) Iris Virginica data set")                                                     # Only Iris Virginica data set
print()
Number = int(input("Please choose data set number "))                                   
Number_data = Number

# Reassign the individual data sets as the main data set
if Number == 1:
    data_set = "entire Iris data set"                                                   # Set variable name to entire data set
    data_name = "All Irises"                                                            # Set variable name to all Irises

elif Number == 2:
    iris_ds = iris_ds.drop("Iris-versicolor", axis=0)                                   # Removes the Iris Versicolor data from the data set
    iris_ds = iris_ds.drop("Iris-virginica", axis=0)                                    # Removes the Iris Virginica data from the data set
    data_set = "Iris Setsosa data set"                                                  # Sets variable name to Iris Setosa data set
    data_name = "Iris Setosa"                                                           # Set variable name to Iris Setosa

elif Number == 3:
    iris_ds = iris_ds.drop("Iris-setosa", axis=0)                                       # Removes the Iris Setosa data from the data set
    iris_ds = iris_ds.drop("Iris-virginica", axis=0)                                    # Removes the Iris Virginica data from the data set
    data_set = "Iris Versicolor data set"                                               # Sets variable name to Iris Versicolor data set
    data_name = "Iris Versicolor"                                                       # Set variable name to Iris Versicolor

elif Number == 4:
    iris_ds = iris_ds.drop("Iris-versicolor", axis=0)                                   # Removes the Iris Versicolor data from the data set
    iris_ds = iris_ds.drop("Iris-setosa", axis=0)                                       # Removes the Iris Setosa data from the data set
    data_set = "Iris Virginica data set"                                                # Sets variable name to Iris Virginica data set
    data_name = "Iris Virginica"                                                        # Set variable name to Iris Virginica

else:
    pass

if Number > 0 and Number < 5:
    # Provide choice to use original or modified data set
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print()
    print("Would you like to use the initial data set, or a data set where the petal and sepal lengths and widths have been replaced with the areas and rations of the petal and sepals?")
    print()
    print("Area for petal/sepal = width x length")
    print("Ratio for petal/sepal = length / width")
    print()
    print("1) Original data set")                                                         # Original data
    print("2) Areas and ratios")                                                          # New data
    print()
    Number = int(input("Please choose data set option "))

    # Remove petal and sepal lengths and widths
    if Number == 2:
        iris_ds["Sepal_area_(cm^2)"] = iris_ds.Sepal_width * iris_ds.Sepal_length         # Formula for sepal area
        iris_ds["Sepal_ratio"] = iris_ds.Sepal_width / iris_ds.Sepal_length               # Formula for sepal ratio
        iris_ds["Petal_area_(cm^2)"] = iris_ds.Petal_width * iris_ds.Petal_length         # Formula for petal area
        iris_ds["Petal_ratio"] = iris_ds.Petal_width / iris_ds.Petal_length               # Formula for petal ratio
        iris_ds = iris_ds.drop(columns=["Petal_length", "Petal_width"], axis=1)           # Drop petal information from data set
        iris_ds = iris_ds.drop(columns=["Sepal_length", "Sepal_width"], axis=1)           # Drop sepal infomration from data set

    if Number > 0 and Number < 3:                                                           # Only available if the user chose 1 or 2 on last input

        # Choice of activity
        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
        print()
        print("What facts do you want to find out about the", data_set, "?")
        print()
        print("1) Data types and shape")                                                    # Provide information on data and shape of the data set
        print("2) Top and bottom 10 rows")                                                  # Provides the top and bottom 10 rows of the data set
        print("3) Box and whisker plots")                                                   # Plots a box and whisker plot of the data set
        print("4) Histogram plots")                                                         # Plots a histogram of the data set
        print("5) Scatter plots")                                                           # Provides a scatter plot of the data set
        print("6) Standard descriptive statistics")                                         # Provides the standard statistics created by pandas for the data set

        if Number_data!=1:                                                                  # Only available if a subset of the data is chosen
            print("7) Min, Mean,  Max, Range, Variance, and Standard Deviation")            # Provides data similar to the standard statistics, but in a table format
        
        print()
        Number = int(input("Please provide a number "))

        print("______________________________________________________________________________________________________________________________________________________")
        
        # Print data types
        if Number == 1:
            print()
            print("Data Type")
            print(iris_ds.dtypes)
            print()
            print("Rows,", "Cols")
            print(iris_ds.shape)

        # Print top 20 rows of the data set.
        elif Number == 2:
            print()
            print("Top 10 rows")
            print(iris_ds.head(10))
            print()
            print("Bottom 10 rows")
            print(iris_ds.tail(10))

        # Print box whisker plots.
        elif Number == 3:
            iris_ds.plot(kind="box", subplots = True, layout = (2,2), sharex = False, sharey = False)
            plt.show()

        # Plot histogram of entire data set.
        elif Number == 4:
            iris_ds.hist()
            plt.show()

        # Scatter plot of entire data set.
        elif Number ==5:
            scatter_matrix(iris_ds)
            plt.show()

        # Print desccription of data set
        elif Number == 6:
            print()
            print("Descriptive statistics of data set")
            print(iris_ds.describe())
            
        # Min, Mean, Max, Range, Variance, and Standard deviation
        elif Number == 7 and Number_data!=1:
            print()
            print(data_name)                                                                # Label for table
            print("Class\t\t\tCount\tMin\tMean\tMax\tRange\tVar\tStd Dev")                  # Create table columns
            print("-----------------------------------------------------------------------------------------")
       
            i = 0                                                   
            while i < 4:                                                                    # While i less than number of columns, starting at 0
                
                # Naming of rows
                if i==0:
                    Col_name = "Sepal Area (cm^2)"
                elif i==1:
                    Col_name = "Sepal Ratio     "
                elif i==2:
                    Col_name = "Petal Area (cm^2)"
                elif i==3:
                    Col_name = "Petal Ratio     "
                
                # Calculations
                Count = iris_ds.shape[0]                                                    # Count number of rows
                Count = int(Count)
                Min = iris_ds.iloc[:,i].min()                                               # Identify minimum value in column
                Mean = iris_ds.iloc[:,i].mean()                                             # Identify mean/average value in column
                Max = iris_ds.iloc[:,i].max()                                               # Identify maximum value in column
                Range = Max - Min                                                           # Identify difference between maximum and minimum values
                Variance = iris_ds.iloc[:,i].var()                                          # Identify variance in column for data set
                StdDev = iris_ds.iloc[:,i].std()                                            # Identify standard deviation in column for data set
                
                Min = str(Min)                                                              # Convert to string to be subscriptable
                Mean = str(Mean)                                                            # Convert to string to be subscriptable
                Max = str(Max)                                                              # Convert to string to be subscriptable
                Range = str(Range)                                                          # Convert to string to be subscriptable
                Variance = str(Variance)                                                    # Convert to string to be subscriptable
                StdDev = str(StdDev)                                                        # Convert to string to be subscriptable

                # Print table row be row for each column
                print(Col_name, "\t", Count, "\t", Min[:4], "\t", Mean[:4], "\t", Max[:4], "\t", Range[:4], "\t", Variance[:4], "\t", StdDev[:4])
                i = i + 1

        else:
            print("Thank you. Come again")

    else:
        pass

# End of module
