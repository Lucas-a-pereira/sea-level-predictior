# Importing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Function to create the best fits and draw a plot out of them
def draw_plot():

    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    years_extended = np.arange(1880, 2051, 1)
    years_extended_2000 = np.arange(2000, 2051, 1)

    df2000 = df[(df['Year'] >= 2000)]

    # Create first line of best fit
    slope, intercept, r_value, p_value, se = linregress(x = df['Year'], y= df['CSIRO Adjusted Sea Level'])

    line = [slope*xi + intercept for xi in years_extended]

    # Create second line of best fit
    slope2, intercept2, r_value2, p_value2, se2 = linregress(x = df2000['Year'], y= df2000['CSIRO Adjusted Sea Level'])

    line2000 = [slope2*xi + intercept2 for xi in years_extended_2000]

    # Create scatter plot with the fits and original data
    fig, ax = plt.subplots(figsize = (8, 8))
    plt.plot(years_extended, line, color = 'orange', linewidth = 1.5, label = 'Fitted line (1880-2050)')
    plt.plot(years_extended_2000, line2000, color = 'red', linewidth = 1.5, label = 'Fitted line (2000-2050)')
    plt.scatter(data = df, x = 'Year', y = 'CSIRO Adjusted Sea Level', label = 'Original data')
    plt.xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
    plt.legend()
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()