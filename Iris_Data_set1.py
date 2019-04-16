import pandas as pd
import matplotlib.pyplot as plt

from pandas.plotting import scatter_matrix

# Load digits dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
name = ['Sepal-length', 'Sepal-width', 'Petal-length', 'Petal-width', 'Class']
iris_ds = pd.read_csv(url, names=name)

# Choice of activity
print('What facts do you want to find out about the Iris Dataset?')
print('1) Description')
print('2) Top 20 rows')
print('3) Last 20 rows')
print('4) Shape')
print('5) Box and whisker plots')
print('6) Histogram plots')
print('7) Scatter plots')
print()

Number = int(input("Please provide a number "))

if Number == 1:
    print(iris_ds.describe())

elif Number == 2:
    print(iris_ds.head(20))

elif Number == 3:
    print(iris_ds.tail(20))
    
elif Number == 4:
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

else:
    pass
