# sea-level-predictior

In this work I'm analysing a dataset of the global average sea level change since 1880 and using this data to predict the sea level change through year 2050 using linear regression.

I'm creating a function named `draw_plot()` that:
- Imports the data from `epa-sea-level.csv`.
- Uses matplotlib to create a scatter plot using the "Year" column as the x-axis and the "CSIRO Adjusted Sea Level" column as the y-axis.
- Uses the `linregress` function from `scipy.stats` to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
- Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.

![alt text](https://github.com/Lucas-a-pereira/sea-level-predictior/blob/main/sea_level_plot.png?raw=true)
