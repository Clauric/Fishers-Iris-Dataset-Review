import pandas as pd
import matplotlib.pyplot as plt

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

# Create new data set for Iris Setosa
iris_SA = iris_ds.drop("Iris-versicolor", axis=0)                                       
iris_SA = iris_SA.drop("Iris-virginica", axis=0)

# Create new data set for Iris Versicolor
iris_VR = iris_ds.drop("Iris-setosa", axis=0)
iris_VR = iris_VR.drop("Iris-virginica", axis=0)

# Create new data set for Iris Viginica
iris_VA = iris_ds.drop("Iris-setosa", axis=0)
iris_VA = iris_VA.drop("Iris-versicolor", axis=0)                                                             

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
    iris_df = iris_ds
    data_set = "entire Iris data set"

elif Number == 2:
    iris_df = iris_SA
    data_set = "Iris Setsosa data set"

elif Number == 3:
    iris_df = iris_VR
    data_set = "Iris Veriscolor data set"

elif Number == 4:
    iris_df = iris_VA
    data_set = "Iris Virginia data set"

else:
    pass

# Provide choice to use original or modified data set
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
    iris_df["Sepal_area_(cm^2)"] = iris_df.Sepal_width * iris_df.Sepal_length         # Formula for sepal area
    iris_df["Sepal_ratio"] = iris_df.Sepal_width / iris_df.Sepal_length               # Formula for sepal ratio
    iris_df["Petal_area_(cm^2)"] = iris_df.Petal_width * iris_df.Petal_length         # Formula for petal area
    iris_df["Petal_ratio"] = iris_df.Petal_width / iris_df.Petal_length               # Formula for petal ratio
    iris_df = iris_df.drop(columns=["Petal_length", "Petal_width"], axis=1)           # Drop petal information from data set
    iris_df = iris_df.drop(columns=["Sepal_length", "Sepal_width"], axis=1)           # Drop sepal infomration from data set
    data_set = "modified",data_set

if Number > 0 and Number < 5:

    # Choice of activity
    print()
    print("What facts do you want to find out about the", data_set, "?")
    print()
    print("1) Data types and shape")
    print("2) Top and bottom 10 rows")
    print("3) Box and whisker plots")
    print("4) Histogram plots")
    print("5) Scatter plots")
    print("6) Standard descriptive statistics")
    print("7) Min, Mean, Median, Max, Range, Variance, and Standard deviation")

    # Include additional choice if using entire data set
    if Number_data==1:
        print("8) Other information")
    
    print()
    Number = int(input("Please provide a number "))

    # Print data types
    if Number == 1:
        print()
        print("Data Type")
        print(iris_df.dtypes)
        print()
        print("Rows,", "Cols")
        print(iris_df.shape)

    # Print top 20 rows of the data set.
    elif Number == 2:
        print()
        print(iris_df.head(10))
        print(iris_df.tail(10))

    # Print box whisker plots.
    elif Number == 3:
        iris_df.plot(kind="box", subplots = True, layout = (2,2), sharex = False, sharey = False)
        plt.show()

    # Plot histogram of entire data set.
    elif Number == 4:
        iris_df.hist()
        plt.show()

    # Scatter plot of entire data set.
    elif Number ==5:
        scatter_matrix(iris_df)
        plt.show()

    # Print desccription of data set
    elif Number == 6:
        print()
        print("Descriptive statistics of data set")
        print(iris_df.describe())
        
    # Min, Mean, Median, Max, Range, Variance, and Standard deviation
    elif Number == 7:
        print()
        print(iris_df.groupby("Class").agg(["count","min","max","mean"]))
        
    # Other printouts.
    elif Number == 8:
        print()
        print(iris_df.Class.unique())                                               # Print names of unique classes (Iris types) in data set
        print()
        print(iris_df.Class.nunique())                                              # Print number of unique classes (Iris types) in data set
        print()
        print(pd.crosstab(iris_df.Sepal_length,iris_df.Sepal_width))                # Print crosstabulation table of sepal lengths v sepal widths
        print()
        print(pd.crosstab(iris_df.Petal_length,iris_df.Petal_width))                # Print crosstabulation table of petal length v petal widths

    else:
        print("Thank you. Come again")

else:
    pass
