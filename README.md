# Big Data Analytics HWs

## Overview
These homeworks (HW2-4) were assigned for the course 'Big Data Analytics'.

### Programmed by...
  Alexis Ayuso

## HW2
Goal: to practice one NoSQL database: MongoDB.

Create a python code (.py) with PyMongo library to insert documents, 
print all the data in the MongoDB, 
to query students who took a course and to query a student's grade for a course.

## HW3
### 1. General Plotting Assignment
#### Pair Plots
Goal : Write Python3 code (.ipynb) to show the pair plots. File named "01.ipynb". 

Using Iris Data Set, plot pairwise relationships using both pair plot and pair grid. 
Create a grid of axes, use scatter plot for each pairing of variables, 
and plot Kernel density estimate (kdf) for the mariginal plots along the diagonal.

#### Box Plots
Goal: Write Python3 code to show the box plots. File named "02.ipynb".

Using Forest Fire Data Set, plot boxplots. 
Show boxplots of "FFMC" for each day in the week using Pandas library, 
boxplots of "DMC" for each day in the week using Matplotlib library, 
and boxplots of "DC" for each day in the week using Seaborn library.

### 2. Plotting Assignment for Large Datasets

Goal: Write Python3 code (.ipynb) to draw data points for a large dataset. File named "03.ipynb".

Use python code to find out how many points the dataset has.
Use Pandas' read_parquet method to read the dataset and get the size. 
Use Datashader to understand and plot the dataset.

## HW4
Goal: Write Python3 code (.ipynb) to count words in bible.txt using various methods.

Create a version of bible.txt with words in uppercase saved as bible_uppercase.txt.
Count words in the bible_uppercase.txt by using for loop, map, and with parallel implementation by using Python's multiprocessing API.
