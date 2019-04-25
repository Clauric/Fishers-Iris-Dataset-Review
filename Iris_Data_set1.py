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

Number = int(input("Please choose data set number "))

if Number == 1:
    iris_df = iris_ds

elif Number == 2:
    iris_df = iris_SA

elif Number == 3:
    iris_df = iris_VR

elif Number == 4:
    iris_df = iris_VA

if Number > 0 and Number < 5:

    # Choice of activity
    print()
    print("What facts do you want to find out about the Iris Dataset?")
    print()
    print("1) Description")
    print("2) Top 20 rows")
    print("3) Last 20 rows")
    print("4) Shape")
    print("5) Box and whisker plots")
    print("6) Histogram plots")
    print("7) Scatter plots")
    print("8) Sepal area")
    print("9) Petal area")
    print("10) Data types")
    print("11) Sepal ratio")
    print("12) Petal ratio")
    print("13) Min, Max, Mean")
    print("14) Other")
    print()

    Number = int(input("Please provide a number "))

    # Print description of the data set.
    if Number == 1:
        print()
        print(iris_df.describe())

    # Print top 20 rows of the data set.
    elif Number == 2:
        print()
        print(iris_df.head(20))

    # Print last 20 rows of the data set.
    elif Number == 3:
        print()
        print(iris_df.tail(20))

    # Print number of rows and cols in the data set.
    elif Number == 4:
        print()
        print("Rows,", "Cols")
        print(iris_df.shape)

    # Plot box and whisker of entire data set.
    elif Number == 5:
        iris_df.plot(kind="box", subplots = True, layout = (2,2), sharex = False, sharey = False)
        plt.show()

    # Plot histogram of entire data set.
    elif Number == 6:
        iris_df.hist()
        plt.show()

    # Scatter plot of entire data set.
    elif Number ==7:
        scatter_matrix(iris_df)
        plt.show()

    # Count, min, max, mean of sepals, including area.
    elif Number == 8:
        print()
        iris_df = iris_df.drop(columns=["Petal_length", "Petal_width"], axis=1)     # Drop petal information from data set
        iris_df["Sepal_area"] = iris_df.Sepal_width * iris_df.Sepal_length          # Formula for sepal area
        print(iris_df.groupby("Class").agg(["count","min","max","mean"]))

    # Count, min, max, mean of petals, including area.
    elif Number == 9:
        print()
        iris_df = iris_df.drop(columns=["Sepal_length", "Sepal_width"], axis=1)     # Drop sepal infomration from data set
        iris_df["Petal_area"] = iris_df.Petal_width * iris_df.Petal_length          # Formula for petal area
        print(iris_df.groupby("Class").agg(["count","min","max","mean"]))

    # Print data types of data set (by column).
    elif Number == 10:
        print()
        print(iris_df.dtypes)

    # Count, min, max, mean of sepals, including ratio.
    elif Number == 11:
        print()
        iris_df = iris_df.drop(columns=["Petal_length", "Petal_width"], axis=1)     # Drop petal information from data set
        iris_df["Sepal_ratio"] = iris_df.Sepal_width / iris_df.Sepal_length         # Formula for sepal ratio
        print(iris_df.groupby("Class").agg(["count","min","max","mean"]))

    # Count, min, max, mean of petals, including ratio.
    elif Number == 12:
        print()
        iris_df = iris_df.drop(columns=["Sepal_length", "Sepal_width"], axis=1)     # Drop sepal information from data set
        iris_df["Petal_ratio"] = iris_df.Petal_width / iris_df.Petal_length         # Formula for petal ratio
        print(iris_df.groupby("Class").agg(["count","min","max","mean"]))

    # Count, min, max, mean of petals and sepals.
    elif Number == 13:
        print()
        print(iris_df.groupby("Class").agg(["count","min","max","mean"]))

    # Other printouts.
    elif Number == 14:
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
