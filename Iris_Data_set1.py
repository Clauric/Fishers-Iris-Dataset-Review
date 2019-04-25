import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate as tb

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
print("Which data set would you like to use?")
print()
print("1) All data in Fisher's Iris data set")
print("2) Iris Setosa data set")
print("3) Iris Versicolor data set")
print("4) Iris Virginica data set")
print()
Number = int(input("Please choose data set number "))
Number_data = Number

# Reassign the individual data sets as the main data set
if Number == 1:
    data_set = "entire Iris data set"
    data_name = "All Irises"

elif Number == 2:
    iris_ds = iris_ds.drop("Iris-versicolor", axis=0)
    iris_ds = iris_ds.drop("Iris-virginica", axis=0) 
    data_set = "Iris Setsosa data set"
    data_name = "Iris Setosa"

elif Number == 3:
    iris_ds = iris_ds.drop("Iris-setosa", axis=0)
    iris_ds = iris_ds.drop("Iris-virginica", axis=0) 
    data_set = "Iris Versicolor data set"
    data_name = "Iris Versicolor"

elif Number == 4:
    iris_ds = iris_ds.drop("Iris-versicolor", axis=0)
    iris_ds = iris_ds.drop("Iris-setosa", axis=0) 
    data_set = "Iris Virginica data set"
    data_name = "Iris Virginica"

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
    print("1) Original data set")
    print("2) Areas and ratios")
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

    if Number > 0 and Number < 3:

        # Choice of activity
        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
        print()
        print("What facts do you want to find out about the", data_set, "?")
        print()
        print("1) Data types and shape")
        print("2) Top and bottom 10 rows")
        print("3) Box and whisker plots")
        print("4) Histogram plots")
        print("5) Scatter plots")
        print("6) Standard descriptive statistics")

        if Number_data!=1:
            print("7) Min, Mean, Median, Max, Range, Variance, and Standard deviation")
        
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
            
        # Min, Mean, Median, Max, Range, Variance, and Standard deviation
        elif Number == 7 and Number_data!=1:
            print()
            print(data_name)
            
            table = ("Sepal_area_(cm^2)",iris_ds.min("Sepal_area_(cm^2)"),iris_ds.mean("Sepal_area_(cm^2)"),"4","3","5","4","3")
            print(tb(table,headers = ["Field","Min", "Mean", "Median", "Max", "Range", "Variance", "Standard Deviation"]))
        
        else:
            print("Thank you. Come again")

    else:
        pass

# End of module
