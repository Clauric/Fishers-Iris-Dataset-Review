# Table of Contents

[Introduction](#Introduction)


# Introduction

This report is aimed at providing an understanding of “Fisher’s” Iris data set. The report is broken down into three main sections:

1. Fisher’s Iris data set

    1.1. What is Fisher’s Iris data set?
  
    1.2. Uses of Fisher’s Iris data set

2. Analysis and results

    2.1
    
    2.2
    
    2.3

3. Technical information


The 1st section will provide a brief outline of what is Fisher’s Iris data set, including its history, as well as the current uses of the data. The 2nd section will cover some analysis undertaken, showing how the data set can be broken down and used. There will also be a discussion of any issues that might arise from using this data. The last section will cover the technical information on how the accompanying Python script was used, including the Python packages required, and code used.

# Fisher’s Iris data set

## What is Fisher’s Iris data set?

The data set known as Fisher’s Iris data set is a collection of measurements compiled by the researcher Edgar Anderson in 1935 _(Anderson, 1935)_. These measurements comprise 150 rows of data, with each row containing 5 data points. These data points refer to the widths and lengths of petal and sepals, as well as the identified genus of the plant. 100 of the rows of data, comprising flowers from the _Iris Setosa_ and _Iris Versicolor_ species, were collected from the Gaspé Peninsula in Quebec, Canada. Anderson noted that _"all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus"_ _(Anderson, 1936)_. This amounted to 50 rows of data per flower. Anderson’s original purpose of collecting the data was to see if _I. Versicolor_ was a result of a hybridisation event between _I. Setosa_ and _I. Virginica_, as all three plants are found in the same geographical area _(Ibid)_.

In 1936, the biologist and statistician RA Fisher conducted similar research on _I. Virginica_. This research, when added to Anderson’s original research, gave rise to the Fisher’s Iris data set (100 rows of data from Anderson, 50 from Fisher). Fisher conducted statistical analysis of the data collected to help determine if there was a method of discriminating between the flowers, based solely on the data collected (without using the names) _(Fisher, 1936)_. The data suggested that _I. Setosa_ could be so discriminated, however, there was some overlap between _I. Versicolor_, and _I. Virginica (Ibid)_.

## Uses of Fisher’s Iris data set

Google Scholar notes that Fisher’s 1936 paper has been cited 15,800 times, while searching Google using the term _“Fisher’s Iris data set”_ returns more than 8.9m hits (as of 27th April, 2019). This suggests that this is a very popular data set. Due to the simple structure of the data, as well as its small size, the data set is often used in a number of scenarios. These scenarios include training students on data analysis, using a variety of statistical approaches, as well as a learning test bed for machine learning programs. This is due to the fact there are 2 distinct clusters within the data, and allows for the demonstration multivariate analysis, clustering, data classification, pattern recognition _(Hoey, n.d.)_.

# Technical information

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
* Wilkin, R., 2012. Discriminating Fisher's iris data set by using petal areas. [Online] 
Available at: https://blogs.sas.com/content/iml/2012/08/09/discriminating-fishers-iris-data-by-using-the-petal-areas.html
[Accessed 10 April 2019].
