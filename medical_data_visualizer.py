import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Task 1: Import the data from medical_examination.csv and assign it to the df variable
df = pd.read_csv('medical_examination.csv')

# Task 2: Create the overweight column in the df variable
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2) > 25
df['overweight'] = df['overweight'].astype(int)

# Task 3: Normalize data by making 0 always good and 1 always bad
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Task 4: Draw the Categorical Plot in the draw_cat_plot function
def draw_cat_plot():
    df_cat = pd.melt(df, value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], id_vars='cardio')
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', kind='bar', data=df_cat)
    ax = fig.axes[0]  # Get the axis object from the figure
    return fig.fig  # Return the figure object

def draw_heat_map():
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
                 (df['height'] >= df['height'].quantile(0.025)) & 
                 (df['height'] <= df['height'].quantile(0.975)) & 
                 (df['weight'] >= df['weight'].quantile(0.025)) & 
                 (df['weight'] <= df['weight'].quantile(0.975))]
    corr = df_heat.corr()  # Calculate the correlation matrix
    mask = np.triu(np.ones_like(corr, dtype=bool))  # Create a mask for the upper triangle
    fig, ax = plt.subplots(figsize=(10, 8))  # Create a figure and axis
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cmap='coolwarm', ax=ax)  # Create the heatmap
    return fig  # Return the figure object

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
