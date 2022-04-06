import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv', delimiter=',')

# Add 'overweight' column
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
conditions = [
    (df['BMI'] <= 25),
    (df['BMI'] > 25)
]
values = [0, 1]

df['overweight'] = np.select(conditions, values)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
conditions_chole = [
    (df['cholesterol'] == 1),
    (df['cholesterol'] > 1),
]
df['cholesterol'] = np.select(conditions_chole, values)

conditions_gluc =[
    (df['gluc'] == 1),
    (df['gluc'] > 1)
]
df['gluc'] = np.select(conditions_gluc, values)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df[['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke', 'cardio']].melt(
        id_vars='cardio'
    )

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'])['value'].count().reset_index(name='total')

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x="variable", y="total", col="cardio", data=df_cat, hue="value", kind="bar").fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    mask = (df['ap_lo'] <= df['ap_hi']) & \
           (df['height'] >= df['height'].quantile(0.025)) & \
           (df['height'] <= df['height'].quantile(0.975)) & \
           (df['weight'] >= df['weight'].quantile(0.025)) & \
           (df['weight'] <= df['weight'].quantile(0.975))
    df_heat = df[mask].drop(columns='BMI')

    # Calculate the correlation matrix
    corr = df_heat.corr()
    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(16, 7))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, fmt='.1f', mask=mask, vmax=0.3, square=True)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
