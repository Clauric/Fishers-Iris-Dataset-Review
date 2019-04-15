import sklearn
import matplotlib.pyplot as plt

from sklearn import datasets

# Load digits dataset
iris = datasets.load_iris()

# Create feature matrix
X = iris.data

# Create target vector
y = iris.target

# View the first observation's feature values
i = 0

while i < 150:
    print (X[i], iris.target[i])
    i += 1
