import pandas as pd
import matplotlib.pyplot as plt

from pandas.plotting import scatter_matrix

# Load digits dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
name = ['Sepal_length', 'Sepal_width', 'Petal_length', 'Petal_width', 'Class']
iris_ds = pd.read_csv(url, names=name)

cols=iris_ds.columns.drop('Class')
iris_ds[cols]=iris_ds[cols].apply(pd.to_numeric, errors='coerce')

iris_ds.set_index('Class')

# Choice of activity
print()
print('What facts do you want to find out about the Iris Dataset?')
print('1) Description')
print('2) Top 20 rows')
print('3) Last 20 rows')
print('4) Shape')
print('5) Box and whisker plots')
print('6) Histogram plots')
print('7) Scatter plots')
print('8) Sepal area')
print('9) Petal area')
print('10) Data types')
print('11) Sepal ratio')
print('12) Petal ratio')
print('13) Min, Max, Mean')
print()

Number = int(input("Please provide a number "))

if Number == 1:
    print()
    print(iris_ds.describe())

elif Number == 2:
    print()
    print(iris_ds.head(20))

elif Number == 3:
    print()
    print(iris_ds.tail(20))
    
elif Number == 4:
    print()
    print('Rows,', 'Cols')
    print(iris_ds.shape)

elif Number == 5:
    iris_ds.plot(kind='box', subplots = True, layout = (2,2), sharex = False, sharey = False)
    plt.show()

elif Number == 6:
    iris_ds.hist()
    plt.show()

elif Number ==7:
    scatter_matrix(iris_ds)
    plt.show()

elif Number == 8:
    print()
    iris_ds.drop(columns=['Petal_length', 'Petal_width'], axis=1)
    iris_ds['Sepal_area'] = iris_ds.Sepal_width * iris_ds.Sepal_length
    print(iris_ds.groupby("Class").agg(["count","min","max","mean"]))

elif Number == 9:
    print()
    iris_ds['Petal_area'] = iris_ds.Petal_width * iris_ds.Petal_length
    print(iris_ds.groupby("Class").agg(["count","min","max","mean"]))

elif Number == 10:
    print()
    print(iris_ds.dtypes)

elif Number == 11:
    print()
    iris_ds['Sepal_ratio'] = iris_ds.Sepal_width / iris_ds.Sepal_length
    print(iris_ds.groupby("Class").agg(["count","min","max","mean"]))

elif Number == 12:
    print()
    iris_ds['Petal_ratio'] = iris_ds.Petal_width / iris_ds.Petal_length
    print(iris_ds.groupby("Class").agg(["count","min","max","mean"]))

elif Number == 13:
    print()
    print(iris_ds.groupby("Class").agg(["count","min","max","mean"]))
else:
    pass

print(iris_ds.Class.unique())
print(iris_ds.Class.nunique())
print(pd.crosstab(iris_ds.Sepal_length,iris_ds.Sepal_width))
print(pd.crosstab(iris_ds.Petal_length,iris_ds.Petal_width))
print(iris_ds.head(30))
