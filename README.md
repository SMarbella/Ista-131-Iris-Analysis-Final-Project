# ISTA 131: Iris Analysis Final Project
The dataset I used to generate my charts is the Iris Data Set from Machine Learning Repository by R. A. Fisher. The dataset has 50 samples of three iris species. The three iris species are Iris Setosa, Iris Versicolor, and Iris Virginica. Each of the flowers has unique traits correlated with their species. The program creates three charts.

Dataset Source: https://archive.ics.uci.edu/ml/datasets/iris

I created a program that analyzes and produces charts that show the differences between the petals and sepals of three types of irises. One function takes an iris DataFrame and creates a bar chart that displays the variations between the sepal and petal lengths in cm of the three iris species.

The second function takes an iris DataFrame and creates a scatter plot with linear regressions for each iris species. The scatter plot records the sepal widths and lengths for each flower species in cm.

The third function takes an iris DataFrame and creates a scatter plot with linear regressions for each iris species. The scatter plot records the petal widths and lengths for each flower species in cm.

# Lengths and Widths of Sepals and Petals
![Image](https://raw.githubusercontent.com/SMarbella/Ista-131-Iris-Analysis-Final-Project/main/Images/Sepal%20and%20Petal%20Lengths%20and%20Widths.png)

Each color in the legend represents the different irises. The bars show the average measurement of sepals and petals found in each iris species. The error bars at the top that represent the standard deviation show that not all irises will have the exact measured traits. The error bars show that sometimes the sepals or petals are wider or thinner than the average. The standard deviation shows the difference between the smallest sepals and petals and the largest sepals and petals.

# Measurement of Sepals in cm
![Image](https://raw.githubusercontent.com/SMarbella/Ista-131-Iris-Analysis-Final-Project/main/Images/Measurement%20of%20Sepals%20in%20cm.png)

Each iris species has varying lengths and widths of sepals in cm. Iris Virginica is known to have longest sepals with an average width, Iris Versicolor has thin sepals with an average length, and Iris Setosa has the shortest and widest sepals. Not all individual flower has traits that match their species' traits perfectly. Some individual flowers of each species have longer sepals than others, but they are more likely to inherit their own species' traits than another species' traits. Some Iris Virginica flowers and some Iris Versicolor flowers have traits that vary too much that some of them overlap with each other's linear regressions and are considered outliers of their own species.

# Measurement of Petals in cm
![Image](https://raw.githubusercontent.com/SMarbella/Ista-131-Iris-Analysis-Final-Project/main/Images/Measurement%20of%20Petals%20in%20cm.png)

Iris Setosa has the shortest and thinnest petals, Iris Versicolor has petals of both average length and width, and Iris Virginica has the longest and widest petals. It looks like the size of the petals is proportional to the size of the sepals because a smaller flower like the Iris Setosa tends to have a short sepal with small petals while a larger flower like the Iris Virginica tends to have large petals and longer sepals. Just like the sepal sizes, some Iris Versicolor flower petals overlap with the Iris Virginica petals. The Iris Setosa flowers are most distinguishable from the data since the petal sizes are too small to overlap with the two other species. In conclusion, if one were to have a bouquet of these three iris species, one would be able to easily identify the Iris Setosa flowers out of the bunch due to their distinctively small appearance compared to the other two species.
