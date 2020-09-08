import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats


def draw_plot():
  # Read data from file
  # df=pd.read_csv("epa-sea-level.csv")

    currDir = ""
    for aa in __file__.split("/")[:-1]:
        currDir = currDir + aa + "/"

    try:
        print("Reading file ", currDir + "epa-sea-level.csv")
        df = pd.read_csv(currDir + "epa-sea-level.csv")
    except:
        print("\n\nCannot Open file\n")
        raise

    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
    plt.xlabel('Year', fontsize=14, color='red')
    plt.ylabel('Sea Level (inches)')
    plt.title("Rise in Sea Level")
    plt.axis([1850.0, 2075.0, 0, 12])
    plt.grid(True)

    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    # plt.plot(df["Year"], intercept + slope*df["Year"], 'r', label='fitted line')

    # Create new Panda Series till 2050 for predicting future
    years = df["Year"]
    more = pd.Series([ii for ii in range(df["Year"].max() + 1, 2050)])
    years = years.append(more)
    print(years)

    # Now plot a line  that predicts the sealevel till 2050 using current slope
    plt.plot(years, intercept + slope*years, 'r', label='fitted line')


    # Predict using data from year 2000 through the most recent year
    df1 = df.query("Year > 1999")
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(df1["Year"], df1["CSIRO Adjusted Sea Level"])
    years = df1["Year"]
    years = years[years > 1999]
    more = pd.Series([ii for ii in range(df1["Year"].max() + 1, 2050)])
    years = years.append(more)
    years = years.reset_index(drop=True)
    plt.plot(years, intercept + slope*years, 'r', label='ffitted line')


    plt.show()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()



if __name__ == "__main__":
    draw_plot()