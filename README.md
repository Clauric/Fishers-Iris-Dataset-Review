## Table of Contents
  * [Introduction](#Introduction)
  * [Fisher's Iris data set](#Fisher's-Iris-data-set)
    * [What is Fisher's Iris data set?](#What-is-Fisher's-Iris-dat-set?)
    * [Uses of fisher's Iris data set](#Used-of-fisher's-Iris-data-set)
    * [What are sepals and petals?](#What-are-sepals-and-petals?)
  * [Analysis and results](#Analysis-and-results)
  * [Technical information](#Technical_information)
  * [Bibliography](*Bibliography)


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

<img align="center" width="700" height="300" src="https://github.com/Clauric/GMIT-Programming-Scripting-Pands-Project/blob/master/Irises.jpg">

However, Kozaks and Lotaka note that there is disagreement between botanists over whether Irises have sepals and petals. This is due to the fact that iris sepals do not meet the definition of a sepal. A number of botanists argue that, at least, some irises (of which there are around 300 _(Pacific Bulb Society, 2019)_) do not have either sepals and petals, but instead tepals _(Kozak & Lotocka, 2013)_.
That being said, for the purposes of this review, it shall be assumed that the 3 irises in question have both sepals and petals, as per the data set.

# 2. Analysis and results

## Overall data
The first step in conducting any analysis on the data, it is important to ensure that the data is correct. According to the data set, there should be 150 rows of data, and 5 columns, of which 4 should be numerical values, and 1 column of names. In order to check this, the following scripts were run:

````python
print("Data Type")
print(iris_ds.dtypes)
print()
print("Rows,", "Cols")
print(iris_ds.shape)
````
This will return the following results, confirming that the data is in the format expected [1]:

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

The heads and tails of the data were also checked, in order to visualise the data, using the following code:

````python
print("Top 10 rows")
print(iris_ds.head(10))
print()
print("Bottom 10 rows")
print(iris_ds.tail(10))
````

This returned to following data, indicating that the information contained within the data was as expected:

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

A description fo the data will provide some idea with regards to the min, max, mean, variance, and standard deviation of the data. This will allow the examiner to understand the range of data being reviewed. However, it should be noted that it is already visible in the data above, there is a rather significant differencce between the lengths of the _I. setosa_ and the _I. Virginica_ across sepal lengths, petal lengths, and petal widths. This will somewhat skew the data presented in the description.

````python
print("Descriptive statistics of data set")
print(iris_ds.describe())
````
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

Even though there is a skew in data already visible, it is important to continue with a review of the overall data st, if only to be able to demonstrate the difference in the data later.

#### Graphs and plots

The box and whisker plot, as well as the scatter matrix can be used to show the range and scope of the data found in the data set.

<p align="center"><img width="640" height="478" src="https://github.com/Clauric/GMIT-Programming-Scripting-Pands-Project/blob/master/Box_Whisker_Entire_data.png"></p>

As can be seen from the plot of the sepal widths, there are a number of outliers (which are 150% of the interquartile range). However, 50% of the data points, around the median value, exist within a very short range. In contrast, the 50% range for the petal widths and lengths has a far larger range below the median value.

The scatter matrix shows a combination of both the scatter plots of the data points plotted against each other, as well as a line grapgh showing the distribution of the data plots, when plotted against itself.

<p align="center"><img width="600" height="600" src="https://github.com/Clauric/GMIT-Programming-Scripting-Pands-Project/blob/master/Scatter_matrix_Entire_data.png"></p>

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

[1]: All data in tables was returned in the Cmder command interface, and was translated into tables using the GitHub markup to produce the tables.

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
* Wilkin, R., 2012. Discriminating Fisher's iris data set by using petal areas. [Online] 
Available at: https://blogs.sas.com/content/iml/2012/08/09/discriminating-fishers-iris-data-by-using-the-petal-areas.html
[Accessed 10 April 2019].
