import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data

currDir = ""
for aa in __file__.split("/")[:-1]:
    currDir = currDir + aa + "/"

try:
    print("Reading file ", currDir + "medical_examination.csv")
    df = pd.read_csv(currDir + "medical_examination.csv")
except:
    print("\n\nCannot Open file\n")
    raise

# print(df)
# print(df.shape)


# Add 'overweight' column - Add an 'overweight' column to the data. To determine if a person is
# overweight, first calculate their BMI by dividing their weight in kilograms by the square of
# their height in meters.

# https://www.dataquest.io/blog/tutorial-add-column-pandas-dataframe-based-on-if-else-condition/
df['overweight'] = np.where((df.weight/(df.height ** 2) * 10000) > 25, 1, 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.where(df.cholesterol > 1, 1, 0)
df['gluc'] = np.where(df.gluc > 1, 1, 0)

# Draw Categorical Plot


def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol',
    # 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, value_vars=["active", "alco",
                                     "cholesterol", "gluc",
                                     "overweight", "smoke"],
                     id_vars="cardio")

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature.
    # You will have to rename one of the collumns for the catplot to work correctly.

    # Add a new col for later use to keep counts
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'],
                            as_index=False).count()

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(data=df_cat,
                    kind="bar",
                    x="variable",
                    y='total',
                    hue="value",
                    col="cardio")

    fig = g.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():

    # Clean the data. The right way. Do it all in one shot else your quartile calculations will be based on
    # smaller datasets !!
    df_heat = df[(df.height >= df.height.quantile(0.025)) &
                 (df.height <= df.height.quantile(0.975)) &
                 (df['ap_lo'] <= df['ap_hi']) &
                 (df.weight >= df.weight.quantile(0.025)) &
                 (df.weight <= df.weight.quantile(0.975))
                 ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(9, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, fmt='.1f', linewidths=1, mask=mask,
                vmax=.8, center=0.09, square=True, cbar_kws={'shrink': 0.5})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
