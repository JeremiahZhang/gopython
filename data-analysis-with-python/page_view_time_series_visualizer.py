import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
from datetime import datetime

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
my_dateparse = lambda x: datetime.strptime(x, "%Y-%m-%d")
df = pd.read_csv('fcc-forum-pageviews.csv', delimiter=',', parse_dates=['date'], \
                date_parser=my_dateparse, index_col=0)

# Clean data
mask = (df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))
df = df[mask]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20, 6))
    ax = sns.lineplot(data = df.reset_index(), x = 'date', y = 'value', palette = ['red'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['year'] = [d.year for d in df_bar.date]
    df_bar['month'] = [d.strftime('%B') for d in df_bar.date]
    df_bar = df_bar.drop(columns=['date'])
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().sort_values(ascending=True).rename_axis(['Years', 'Months']).reset_index(name='Average Page Views')

    # Draw bar plot
    hue_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    fig, ax = plt.subplots(figsize=(20, 36))
    ax = sns.barplot(x='Years', y='Average Page Views', hue='Months', hue_order=hue_order, data=df_bar)
    ax.legend(loc='upper left', title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box = df_box.rename(columns={'year': 'Year', 'month': 'Month', 'value': 'Page Views'})
    hue_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(20,10))
    sns.boxplot(x='Year', y='Page Views', data=df_box, ax=axes[0]).set(title='Year-wise Box Plot (Trend)')
    sns.boxplot(x='Month', y='Page Views', data=df_box,ax=axes[1], order=hue_order).set(title='Month-wise Box Plot (Seasonality)')
    plt.autoscale(tight=False)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
