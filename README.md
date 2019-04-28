## Table of Contents
  * [Introduction](#Introduction)
  * [Fisher's Iris data set](#1-fishers-iris-data-set)
    * [What is Fisher's Iris data set?](#what-is-fishers-iris-data-set)
    * [Uses of fisher's Iris data set](#uses-of-fishers-iris-data-set)
    * [What are sepals and petals?](#what-are-sepals-and-petals)
  * [Analysis and results](#2-analysis-and-results)
    * [Overall Data](#overall-data)
  * [Technical information](#3-technical-information)
  * [Codes](#4-codes)
  * [Bibliography](#5-bibliography)


# Introduction

This report is aimed at providing an understanding of “Fisher’s” Iris data set. The report is broken down into three main sections:

1. Fisher’s Iris data set

    What is Fisher’s Iris data set?
  
    Uses of Fisher’s Iris data set
    
    What are sepals and petals?

2. Analysis and results

3. Technical information


The 1st section will provide a brief outline of what is Fisher’s Iris data set, including its history, as well as the current uses of the data. The 2nd section will cover some analysis undertaken, showing how the data set can be broken down and used. There will also be a discussion of any issues that might arise from using this data. The last section will cover the technical information on how the accompanying Python script was used, including the Python packages required, and code used.

# 1. Fisher’s Iris data set

## What is Fisher’s Iris data set?

The data set known as Fisher’s Iris data set is a collection of measurements compiled by the researcher Edgar Anderson in 1935 _(Anderson, 1935)_. These measurements comprise 150 rows of data, with each row containing 5 data points. These data points refer to the widths and lengths of petal and sepals, as well as the identified genus of the plant. 100 of the rows of data, comprising flowers from the _Iris Setosa_ and _Iris Versicolor_ species, were collected from the Gaspé Peninsula in Quebec, Canada. Anderson noted that _"all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus"_ _(Anderson, 1936)_. This amounted to 50 rows of data per flower. Anderson’s original purpose of collecting the data was to see if _I. Versicolor_ was a result of a hybridisation event between _I. Setosa_ and _I. Virginica_, as all three plants are found in the same geographical area _(Ibid)_.

<img align="left" width="150" height="150" src="https://github.com/Clauric/GMIT-Programming-Scripting-Pands-Project/blob/master/RA_FIsher.jpg">

In 1936, the biologist and statistician RA Fisher conducted similar research on _I. Virginica_. This research, when added to Anderson’s original research, gave rise to the Fisher’s Iris data set (100 rows of data from Anderson, 50 from Fisher). Fisher conducted statistical analysis of the data collected to help determine if there was a method of discriminating between the flowers, based solely on the data collected (without using the names) _(Fisher, 1936)_. The data suggested that _I. Setosa_ could be so discriminated, however, there was some overlap between _I. Versicolor_, and _I. Virginica (Ibid)_.

## Uses of Fisher’s Iris data set

Google Scholar notes that Fisher’s 1936 paper has been cited 15,800 times, while searching Google using the term _“Fisher’s Iris data set”_ returns more than 8.9m hits (as of 27th April, 2019). This suggests that this is a very popular data set. Due to the simple structure of the data, as well as its small size, the data set is often used in a number of scenarios. These scenarios include training students on data analysis, using a variety of statistical approaches, as well as a learning test bed for machine learning programs. This is due to the fact there are 2 distinct clusters within the data, and allows for the demonstration multivariate analysis, clustering, data classification, pattern recognition _(Hoey, n.d.)_.

## What are sepals and petals?
As can be seen from the image below, petals and sepals are parts of the flower of the Iris. The sepals are designed to protect the reproductive parts _“within the flower bud”_, and are normally green _(Kozak & Lotocka, 2013)_. In contrast, petals are used for signalling (to pollinators) that pollen and nectar are available within the flower. As such, they are normally _“brightly coloured”_ _(ibid)_.

<img align="center" width="734" height="411" src="https://github.com/Clauric/GMIT-Programming-Scripting-Pands-Project/blob/master/Irises.jpg">

However, Kozaks and Lotaka note that there is disagreement between botanists over whether Irises have sepals and petals. This is due to the fact that iris sepals do not meet the definition of a sepal. A number of botanists argue that, at least, some irises (of which there are around 300 _(Pacific Bulb Society, 2019)_) have neither sepals or petals, but instead tepals _(Kozak & Lotocka, 2013)_.
That being said, for the purposes of this review, it shall be assumed that the 3 irises in question have both sepals and petals, as per the data set.

# 2. Analysis and results

## Overall data
The first step in conducting any analysis on the data, it is important to ensure that the data is correct. According to the data set, there should be 150 rows of data, and 5 columns, of which 4 should be numerical values, and 1 column of names.

| Data Type | |
| --------- | ---------- |
| Sepal_length | float64 |
| Sepal_width | float64 |
| Petal_length | float64 |
| Petal_width | float64 |
| Class | object |
| dtype: object |  |

| Rows | Cols
| ---- | ----- |
| 150 | 5 |

#### Heads and tails

The heads and tails of the data should also be checked, to ensure that the data is as expected.

###### Top 10 rows 

| Class | Sepal_length | Sepal_width | Petal_length | Petal_width |
| ------- | ------- | ------- | ------- | ------- |
| Iris-setosa | 5.1 | 3.5 | 1.4 | 0.2 |
| Iris-setosa | 4.9 | 3.0 | 1.4 | 0.2 |
| Iris-setosa | 4.7 | 3.2 | 1.3 | 0.2 |
| Iris-setosa | 4.6 | 3.1 | 1.5 | 0.2 |
| Iris-setosa | 5.0 | 3.6 | 1.4 | 0.2 |
| Iris-setosa | 5.4 | 3.9 | 1.7 | 0.4 |
| Iris-setosa | 4.6 | 3.4 | 1.4 | 0.3 |
| Iris-setosa | 5.0 | 3.4 | 1.5 | 0.2 |
| Iris-setosa | 4.4 | 2.9 | 1.4 | 0.2 |
| Iris-setosa | 4.9 | 3.1 | 1.5 | 0.1 |

##### Bottom 10 rows 

| Class | Sepal_length | Sepal_width | Petal_length | Petal_width |
| ------- | ------- | ------- | ------- | ------- |
| Iris-virginica | 6.7 | 3.1 | 5.6 | 2.4 |
| Iris-virginica | 6.9 | 3.1 | 5.1 | 2.3 |
| Iris-virginica | 5.8 | 2.7 | 5.1 | 1.9 |
| Iris-virginica | 6.8 | 3.2 | 5.9 | 2.3 |
| Iris-virginica | 6.7 | 3.3 | 5.7 | 2.5 |
| Iris-virginica | 6.7 | 3.0 | 5.2 | 2.3 |
| Iris-virginica | 6.3 | 2.5 | 5.0 | 1.9 |
| Iris-virginica | 6.5 | 3.0 | 5.2 | 2.0 |
| Iris-virginica | 6.2 | 3.4 | 5.4 | 2.3 |
| Iris-virginica | 5.9 | 3.0 | 5.1 | 1.8 |

#### Description of data

A description of the data will provide some idea with regards to the min, max, mean, variance, and standard deviation of the data. This will allow the examiner to understand the range of data being reviewed. However, it should be noted that it is already visible in the data above, there is a rather significant difference between the lengths of the _I. setosa_ and the _I. Virginica_ across sepal lengths, petal lengths, and petal widths. This will somewhat skew the data presented in the description.

Descriptive statistics of data set

|  | Sepal_length | Sepal_width | Petal_length | Petal_width |
| --- | --- | --- | --- | --- |
| count  | 150.000000 | 150.000000  | 150.000000 | 150.000000 |
| mean  |    5.843333  |  3.054000  |   3.758667  |  1.198667 |
| std | 0.828066  |  0.433594  |   1.764420  |  0.763161 |
| min | 4.300000  |  2.000000  |   1.000000  |  0.100000 |
| 25% | 5.100000  |  2.800000  |   1.600000  |  0.300000 |
| 50% | 5.800000  |  3.000000  |   4.350000  |  1.300000 |
| 75% | 6.400000  |  3.300000  |   5.100000  |  1.800000 |
| max | 7.900000  |  4.400000  |   6.900000  |  2.500000 |

An easier way to read the data would be as follows:

All Irises

| Class | Count | Min | Mean | Max | Range | Var | Std Dev |
| ---- | ---- | ----- | ----- | ------ | -------- | ---- | ---- |
| Sepal length | 150 | 4.3 | 5.84 | 7.9 | 3.60 | 0.68 | 0.82 |
| Sepal width | 150 | 2.0 | 3.05 | 4.4 | 2.40 | 0.18 | 0.43 |
| Petal length | 150 | 1.0 | 3.75 | 6.9 | 5.9 | 3.11 | 1.76 |
| Petal width | 150 | 0.1 | 1.19 | 2.5 | 2.4 | 0.58 | 0.76 |

Comparing the minima, means, and maxima (from the description) and the values for _I. Setosa_ (from the head printout), it is clear that there is significant differences in the sepal widths, as well as the petal widths and lengths. However, it is important to continue with a review of the overall data set, if only to be able to demonstrate the difference in the data later.

#### Graphs and plots

The box and whisker plot, as well as the scatter matrix can be used to show the range and scope of the data found in the data set.

<p align="center"><img width="640" height="478" src="https://github.com/Clauric/GMIT-Programming-Scripting-Pands-Project/blob/master/Box_Whisker_Entire_data.png"></p>

As can be seen from the plot of the sepal widths, there are a number of outliers (which are 150% of the interquartile range). However, 50% of the data points, around the median value, exist within a very short range. In contrast, the 50% range for the petal widths and lengths has a far larger range below the median value.

The scatter matrix shows a combination of both the scatter plots of the data points plotted against each other, as well as a line graph showing the distribution of the data plots, when plotted against itself.

<p align="center"><img width="600" height="600" src="https://github.com/Clauric/GMIT-Programming-Scripting-Pands-Project/blob/master/Scatter_matrix_Entire_data.png"></p>

As can be seen in the scatter plots above, there is a distinct split in the data, where the data seems to cluster in two different areas. This would suggest that there is a difference in measurements between the data for one of the irises, when compared to the other two. Additionally, the distribution graphs, show that while sepal widths and lengths seem to be normally distributed [2], the distribution of the petal widths and lengths show bimodal distribution. This further reinforces the idea that there are 2 clusters in the data.

##### Data splitting

Based on the issue with the data being bimodal, it is appropriate that the data should be split by iris type. Doing this will allow for more accurate data to be gathered for each iris separately. By doing this splitting, we will be left with 3 sets of data, each with the same columns, but having only 50 rows of data each.

After splitting the data, and we can ascertain the following data about the individual data sets:

##### Iris Setosa

| Class | Count | Min | Mean | Max | Range | Var | Std Dev |
| ---- | ---- | ----- | ----- | ------ | -------- | ---- | ---- |
| Sepal length | 50 | 4.3 | 5.00 | 5.8 | 1.5 | 0.12 | 0.35 |
| Sepal width |50 | 2.3 | 3.41 | 4.4 | 2.10 | 0.14 | 0.38 |
| Petal length | 50 | 1.0 | 1.46 | 1.9 | 0.89 | 0.03 | 0.17 |
| Petal width |50 | 0.1 | 0.24 | 0.6 | 0.5 | 0.01 | 0.10 |

###### Iris Versicolor

| Class | Count | Min | Mean | Max | Range | Var | Std Dev |
| ---- | ---- | ----- | ----- | ------ | -------- | ---- | ---- |
| Sepal length | 50 | 4.9 | 5.93 | 7.0 | 2.09 | 0.26 | 0.51 |
| Sepal width |50 | 2.0 | 2.77 | 3.4 | 1.4 | 0.09 | 0.31 |
| Petal length | 50 | 3.0 | 4.26 | 5.1 | 2.09 | 0.22 | 0.46 |
| Petal width |50 | 1.0 | 1.32 | 1.8 | 0.8 | 0.03 | 0.19 |

##### Iris Virginica

| Class | Count | Min | Mean | Max | Range | Var | Std Dev |
| ---- | ---- | ----- | ----- | ------ | -------- | ---- | ---- |
| Sepal length | 50 | 4.9 | 6.58 | 7.9 | 3.0 | 0.40 | 0.63 |
| Sepal width |50 | 2.2 | 2.97 | 3.8 | 1.59 | 0.10 | 0.32 |
| Petal length | 50 | 4.5 | 5.55 | 6.9 | 2.40 | 0.30 | 0.55 |
| Petal width |50 | 1.4 | 2.02 | 2.5 | 1.1 | 0.07 | 0.27 |

The data demonstrates that for the mean sepal lengths _I. Versicolor_ and _I. Virginica_ are 18.6% and 31.6% greater than the mean of _I. Setosa_ respectively. Likewise, there are large differences in mean petal lengths (191.7%, and 280.1%), and mean petal lengths (450% and 741.67%) between _I. Versicolor_ and _I. Virginica_ and _I. Setosa_). From ths we can surmise that the two clusters seen on the scatter plots are _I. Setosa_ (smaller, isolated cluster), and _I. Versicolor_ and _I. Virginica_ (larger cluster).

#### Data split box and whiskers plots

The box and whisker plots of the individual iris species also becomes more uniform, when compared to the entire data set, after the data is split.

<p><img align="center" width="320" height="239" src="https://github.com/Clauric/GMIT-Programming-Scripting-Pands-Project/blob/master/BWIS.png" title="Box and whisker plot - I. Setosa"></p>
<p><img align="justify"width="320" height="239" src="https://github.com/Clauric/GMIT-Programming-Scripting-Pands-Project/blob/master/BWIVE.png" title="Box and whisker plot - I. Versicolor">
<img align="justify" width="320" height="239" src="https://github.com/Clauric/GMIT-Programming-Scripting-Pands-Project/blob/master/BWIVI.png" title="Box and whisker plot - I. Virginica"></p>

Focusing on _I. Versicolor_ and _I. Virginica_, an examination of the box and whisker plots would suggest that _I. Virginica_ has larger petal widths and lengths, as well sepal widths. This is supported by the data data generated for the minima, mean, and maxima of both plants. There is, however, some overlap between the flowers, in terms of sepal and petal sizes, especially in the lower and middle ranges of _I. Virginica_.

# 3. Technical information

Languages and platforms used for the data analysis:

#### Language:
* Python 3.7.3

#### Packages / Libraries:
* Matplotlib 3.0.3
* Numpy 1.16.2
* Pandas 0.24.2

#### Compiler:
* Anaconda 1.7.2

#### Additional imports needed:
* Scatter_matrix from pandas.plotting

#### Other information:
* Written in: Visual Studio Code v1.33.1
* Source of Iris data set: https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv

All the codes in this repository have been tested using <a href="https://cmder.net/">Cmder</a>, with the <a href="https://www.anaconda.com/">Anaconda</a> being the default Python platform.  

# 4. Codes

The following codes were used to generate the data found in the report. All the codes can be found in the python script accompanying this report.

##### Import data

````python
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"            # URL of data source being used
name = ["Sepal_length", "Sepal_width", "Petal_length", "Petal_width", "Class"]          # Headers of rows, as data source does not contain any
iris_ds = pd.read_csv(url, names=name)                                                  # Loading of data set to "iris_ds"
````

##### Data shape and size:

````python
print("Data Type")
print(iris_ds.dtypes)
print()
print("Rows,", "Cols")
print(iris_ds.shape)
````

##### Head and tail

````python
print("Top 10 rows")
print(iris_ds.head(10))
print()
print("Bottom 10 rows")
print(iris_ds.tail(10))
````

##### Description of data

````python
print("Descriptive statistics of data set")
print(iris_ds.describe())
````

##### Box Whisker plot

````python
iris_ds.plot(kind="box", subplots = True, layout = (2,2), sharex = False, sharey = False)
plt.suptitle("Box and whisker diagrams for sepals and petals")
plt.show()
````

##### Scatter Matrix plot

````python
scatter_matrix(iris_ds, figsize=(6, 6), diagonal='kde')
plt.suptitle("Scatter matrix for sepal and petals")                                  
plt.show()
````

##### Create data set only containing one iris species

````python
iris_ds = iris_ds.drop("Iris-versicolor", axis=0)                                   # Removes the Iris Versicolor data from the data set
iris_ds = iris_ds.drop("Iris-virginica", axis=0)                                    # Removes the Iris Virginica data from the data set
....

iris_ds = iris_ds.drop("Iris-setosa", axis=0)                                       # Removes the Iris Setosa data from the data set
iris_ds = iris_ds.drop("Iris-virginica", axis=0)                                    # Removes the Iris Virginica data from the data set
....

iris_ds = iris_ds.drop("Iris-versicolor", axis=0)                                   # Removes the Iris Versicolor data from the data set
iris_ds = iris_ds.drop("Iris-setosa", axis=0)                                       # Removes the Iris Setosa data from the data set
````

##### Change columns from widths and lengths to areas and ratios

```` python
iris_ds["Sepal_area_(cm^2)"] = iris_ds.Sepal_width * iris_ds.Sepal_length         # Formula for sepal area
iris_ds["Sepal_ratio"] = iris_ds.Sepal_width / iris_ds.Sepal_length               # Formula for sepal ratio
iris_ds["Petal_area_(cm^2)"] = iris_ds.Petal_width * iris_ds.Petal_length         # Formula for petal area
iris_ds["Petal_ratio"] = iris_ds.Petal_width / iris_ds.Petal_length               # Formula for petal ratio
iris_ds = iris_ds.drop(columns=["Petal_length", "Petal_width"], axis=1)           # Drop petal information from data set
iris_ds = iris_ds.drop(columns=["Sepal_length", "Sepal_width"], axis=1)           # Drop sepal infomration from data set
````

##### Create horizontal table of statistics

````python
print(data_name)                                                                # Label for table
print("Class\t\t\tCount\tMin\tMean\tMax\tRange\tVar\tStd Dev")                  # Create table columns
print("-----------------------------------------------------------------------------------------")

i = 0                                                   
while i < 4:                                                                    # While i less than number of columns, starting at 0
....

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
````

[1]: All data in tables was returned in the Cmder command interface, and was translated into tables using the GitHub markup to produce the tables.

[2]: The distributions are not perfectly normal, with the sepal length being a more Gaussian distribution, while the sepal width being more normal. Both distributions are somewhat right skewed.

# Bibliography

* Aggarwal, E., 2017. Pandas Python Tutorial - Learn by Examples. [Online] 
Available at: https://www.listendata.com/2017/12/python-pandas-tutorial.html
[Accessed 1 April 2019].
* Anderson, E., 1935. The irises of the Gaspé Peninsula. Bulletin of the American Iris Society, Volume 59, pp. 2 - 5.
* Anderson, E., 1936. The Species Problem in Iris. Annals of the Missouri Botanical Garden, 23(3), pp. 457 - 509.
* Benson-Putnins, D., Bonfardin, M. & Magnoni, D., 2011. Spectral Clustering and Visualization: A Novel Clustering of Fisher's Iris Data Set. SIAM Undergraduate Research Online, Volume 4, pp. 1 - 15.
* Data Made Simple, 2019. DataMadeSimple.com. [Online] 
Available at: http://www.datasciencemadesimple.com/
[Accessed 2 April 2019].
* El-Shaarawi, A. & Anquandah, J. S., n.d. Environmental Statistics Report on Edgar Anderson's Iris Data Analysis. African Institute For Mathematical Science.
* Fisher, R. A., 1936. The use of multiple measurements in taxonomic problems. Annals of Eugenics, 7(2), pp. 179 - 188.
* Hoey, P. S., n.d. Statistical Analysis of the Iris Flower Dataset. [Online] 
Available at: http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf
[Accessed 31 March 2019].
* Idiap Research Institute, 2017. A Complete Application: Analysis of the Fisher Iris Dataset. [Online] 
Available at: https://pythonhosted.org/bob/temp/bob.db.iris/doc/example.html
[Accessed 2 April 2019].
* Kaggle.com, 2018. Machine learning Basics with Iris data. [Online] 
Available at: https://www.kaggle.com/biphili/machine-learning-basics-with-iris-data/data
[Accessed 31 March 2019].
* Kaggle.com, 2019. https://www.kaggle.com/xuhewen/iris-dataset-visualization-and-machine-learning. [Online] 
Available at: https://www.kaggle.com/xuhewen/iris-dataset-visualization-and-machine-learning
[Accessed 31 March 2019].
* Kaggle.com, 2019. Machine Learning with Iris Dataset. [Online] 
Available at: https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset
[Accessed 31 March 2019].
* Kozak, M. & Lotocka, B., 2013. What should we know about the famous Iris data?. Curren Science, 10(5), pp. 579 - 580.
* Matplotlib.org, 2019. Matplotlib Docs. [Online] 
Available at: https://matplotlib.org/contents.html
[Accessed 10 April 2019].
* Ogundowole, O. O., 2017. Basic Analysis of Iris Data set Using Python. [Online] 
Available at: https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
[Accessed 1 April 2019].
* Pacific Bulb Society, 2019. Iris. [Online] 
Available at: https://www.pacificbulbsociety.org/pbswiki/index.php/Iris
[Accessed 15 April 2019].
* Paruchuri, V., 2016. Pandas Tutorial: Data analysis with Python: Part 1. [Online] 
Available at: https://www.dataquest.io/blog/pandas-python-tutorial/
[Accessed 2 April 2019].
* Wilkin, R., 2012. Discriminating Fisher's iris data set by using petal areas. [Online] 
Available at: https://blogs.sas.com/content/iml/2012/08/09/discriminating-fishers-iris-data-by-using-the-petal-areas.html
[Accessed 10 April 2019].
