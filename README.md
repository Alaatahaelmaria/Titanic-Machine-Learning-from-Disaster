# Titanic-Machine-Learning-from-Disaster
Clean a dataset by removing missing values and outliers and Calculate summary statistics (mean, median, mode, standard deviation) for a dataset

Outliers are values in data that differ extremely from a major sample of the data, the presence of outliers can significantly reduce the performance and accuracy of a predictable model.

The measure of how good a machine learning model depends on how clean the data is, and the presence of outliers may be as a result of errors during the collection of data, but some of this extreme values may be valid and legitimate.for example, the comparison of the goal scores of Ronaldo or Messi with other average players ,the earnings of the top actors like Dwayne Johnson and Ryan Reynolds with otherle actors, we can see clearly it is incomparable and the margin will be very significant.

so during data analysis, this score and earnings may appear as an outlier, that is why there is a need for broader and extensive analysis on the data to figure out and differentiate extreme values from outliers.

we are going to use the titanic dataset to identify, clean, and replace outliers. now, let's explore our data and do some basic data preprocessing.

Boxplot visualization outliers :



![image](https://github.com/Alaatahaelmaria/Titanic-Machine-Learning-from-Disaster/assets/72944935/f9532fed-363e-4b9b-9335-15ae226e6f1d)
![image](https://github.com/Alaatahaelmaria/Titanic-Machine-Learning-from-Disaster/assets/72944935/cb8da09f-b76f-4390-b416-ea40ed05957a)

Skewness
the skewness value should be within the range of -1 to 1 for a normal distribution, any major changes from this value may indicate the presence of outliers.


Flooring And Capping
in this quantile-based technique, we will do the flooring(e.g 25th percentile) for the lower values and capping(e.g for the 75th percentile) for the higher values. These percentile values will be used for the quantile-based flooring and capping.

the code below drops the outliers by removing all the values that are below the 25th percentile and above the 75th percentile of the ‘Fare’ variable.

Removing Outliers from dataset:

![image](https://github.com/Alaatahaelmaria/Titanic-Machine-Learning-from-Disaster/assets/72944935/687f0ce4-ebdb-4d1d-9e4f-0a4e65f39b6b)


And Here Dashboard Using Excel after removing and cleaning missing and outliers data :




