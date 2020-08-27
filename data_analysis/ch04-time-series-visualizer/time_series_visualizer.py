import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
currDir = ""
for aa in __file__.split("/")[:-1]:
    currDir = currDir + aa + "/"

try:
    print("Reading file ", currDir + "fcc-forum-pageviews.csv")
    df = pd.read_csv(currDir + "fcc-forum-pageviews.csv",
                     parse_dates=True,
                     index_col=0)
except:
    print("\n\nCannot Open file\n")
    raise

#print(df.info())


# Clean data
df = df [(df.value >= df.value.quantile(0.025)) & (df.value <= df.value.quantile(0.975))]



def draw_line_plot():
    # Draw line plot

    # Set the plot size
    plt.figure(figsize=(14, 8))

    # Create a figure and a set of subplots(1X1).
    fig, axs = plt.subplots(1, 1)

    # Set the title
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Now draw it.
    sns.lineplot(x=df.index, y="value", data=df, ax=axs)
    plt.xlabel('Date')
    plt.ylabel('Page Views')    
        
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot


    
    df2 = df.copy()
    df2 = df2.resample('M').mean()   
    df2["year"] = df2.index.year
    df2["month"] = df2.index.month
    
    #print(df2.info())

    mm = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df2.month = df2.month.apply(lambda x: mm[x-1])

    #print(df2.head())
    #print(df2.info())

    # Set the plot size
    plt.figure(figsize=(14, 8))

    # Create a figure and a set of subplots(1X1).
    fig, axs = plt.subplots(1, 1)

    
    sns.barplot(x=df2["year"], y=df2.value, data=df2, ax=axs, hue=df2.month, hue_order=mm, 
                 edgecolor=".2", palette="rainbow")

    plt.xlabel('Years')
    plt.ylabel('Average Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
