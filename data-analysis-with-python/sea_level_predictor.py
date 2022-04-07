import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', delimiter=',')

    # Create scatter plot
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']
    plt.scatter(x=x, y=y)

    # Create first line of best fit
    res_one = linregress(x, y)
    x_fit = np.arange(1880, 2051)
    y_fit = res_one.intercept + res_one.slope * x_fit
    plt.plot(x_fit, y_fit, 'r', label='fitted line 1')

    # Create second line of best fit
    mask = df['Year'] >= 2000
    df_sec = df[mask]
    x_sec = df_sec['Year']
    y_sec = df_sec['CSIRO Adjusted Sea Level']
    
    res_sec = linregress(x_sec, y_sec)
    x_fit_sec = np.arange(2000, 2051)
    y_fit_sec = res_sec.intercept + res_sec.slope * x_fit_sec
    plt.plot(x_fit_sec, y_fit_sec, 'g', label='fitted line 2')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()