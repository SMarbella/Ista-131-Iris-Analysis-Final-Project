"""
Name: Stephanie Marbella
Section B
Section leader: Ales Waskow
April 23, 2021
ISTA 131
Assignment: Final Project

This final project module analyzes the iris data sets of 50 samples of three
iris species. The three irises that are being analyzed are Iris Setosa, Iris
Versicolor, and Iris Virginica. The module shows three graphs related to the
widths and lengths of sepals and petals in cm. The first graph compares the
lengths and widths of sepals and petals of the three species. The second and
third graphs create scatter plots with linear regressions that show the
different traits found in each iris species.
"""

import pandas as pd, numpy as np, matplotlib.pyplot as plt
import statsmodels.api as sm

def get_data():
    """
    This function uses the iris.data file and creates a DataFrame table from
    it.

    Returns: A DataFrame table.
    """
    fname = 'iris.data'
    columns = ['Sepal_Length_cm', 'Sepal_Width_cm', 'Petal_Length_cm', 'Petal_Width_cm', 'Class']
    df = pd.read_csv(fname,
                     names=columns,
                     header=None)
    return df

def get_data_iris_setosa(df):
    """
    This function uses the iris.data file and extracts the calculated data
    from the Iris Setosa flowers.
    
    df: An iris DataFrame table.

    Returns: A DataFrame table.
    """
    Iris_setosa = []

    # Gets the min and max values for sepal length and width.
    Iris_setosa.append(df["Sepal_Length_cm"].loc[0:49].min())
    Iris_setosa.append(df["Sepal_Length_cm"].loc[0:49].max())
    Iris_setosa.append(df["Sepal_Width_cm"].loc[0:49].min())
    Iris_setosa.append(df["Sepal_Width_cm"].loc[0:49].max())
    
    # Gets the average sepal size.
    Iris_setosa.append(df["Sepal_Length_cm"].loc[0:49].mean())
    Iris_setosa.append(df["Sepal_Width_cm"].loc[0:49].mean())
    
    # Gets the standard deviation of the sepal length and width.
    Iris_setosa.append(df["Sepal_Length_cm"].loc[0:49].std(ddof=1))
    Iris_setosa.append(df["Sepal_Width_cm"].loc[0:49].std(ddof=1))
    
    # Gets the min and max values for petal length and width.
    Iris_setosa.append(df["Petal_Length_cm"].loc[0:49].min())
    Iris_setosa.append(df["Petal_Length_cm"].loc[0:49].max())
    Iris_setosa.append(df["Petal_Width_cm"].loc[0:49].min())
    Iris_setosa.append(df["Petal_Width_cm"].loc[0:49].max())
    
    # Gets the average petal size.
    Iris_setosa.append(df["Petal_Length_cm"].loc[0:49].mean())
    Iris_setosa.append(df["Petal_Width_cm"].loc[0:49].mean())
    
    # Gets the standard deviation of the petal length and width.
    Iris_setosa.append(df["Petal_Length_cm"].loc[0:49].std(ddof=1))
    Iris_setosa.append(df["Petal_Width_cm"].loc[0:49].std(ddof=1))
    
    return Iris_setosa

def get_data_iris_versicolor(df):
    """
    This function uses the iris.data file and extracts the calculated data
    from the Iris Versicolor flowers.
    
    df: An iris DataFrame table.

    Returns: A DataFrame table.
    """
    Iris_versicolor = []

    # Gets the min and max values for sepal length and width.
    Iris_versicolor.append(df["Sepal_Length_cm"].loc[50:99].min())
    Iris_versicolor.append(df["Sepal_Length_cm"].loc[50:99].max())
    Iris_versicolor.append(df["Sepal_Width_cm"].loc[50:99].min())
    Iris_versicolor.append(df["Sepal_Width_cm"].loc[50:99].max())
    
    # Gets the average sepal size.
    Iris_versicolor.append(df["Sepal_Length_cm"].loc[50:99].mean())
    Iris_versicolor.append(df["Sepal_Width_cm"].loc[50:99].mean())
    
    # Gets the standard deviation of the sepal length and width.
    Iris_versicolor.append(df["Sepal_Length_cm"].loc[50:99].std(ddof=1))
    Iris_versicolor.append(df["Sepal_Width_cm"].loc[50:99].std(ddof=1))
    
    # Gets the min and max values for petal length and width.
    Iris_versicolor.append(df["Petal_Length_cm"].loc[50:99].min())
    Iris_versicolor.append(df["Petal_Length_cm"].loc[50:99].max())
    Iris_versicolor.append(df["Petal_Width_cm"].loc[50:99].min())
    Iris_versicolor.append(df["Petal_Width_cm"].loc[50:99].max())
    
    # Gets the average petal size.
    Iris_versicolor.append(df["Petal_Length_cm"].loc[50:99].mean())
    Iris_versicolor.append(df["Petal_Width_cm"].loc[50:99].mean())
    
    # Gets the standard deviation of the petal length and width.
    Iris_versicolor.append(df["Petal_Length_cm"].loc[50:99].std(ddof=1))
    Iris_versicolor.append(df["Petal_Width_cm"].loc[50:99].std(ddof=1))
    
    return Iris_versicolor

def get_data_iris_virginica(df):
    """
    This function uses the iris.data file and extracts the calculated data
    from the Iris Virginica flowers.
    
    df: An iris DataFrame table.

    Returns: A DataFrame table.
    """
    Iris_virginica = []

    # Gets the min and max values for sepal length and width.
    Iris_virginica.append(df["Sepal_Length_cm"].loc[100:].min())
    Iris_virginica.append(df["Sepal_Length_cm"].loc[100:].max())
    Iris_virginica.append(df["Sepal_Width_cm"].loc[100:].min())
    Iris_virginica.append(df["Sepal_Width_cm"].loc[100:].max())
    
    # Gets the average sepal size.
    Iris_virginica.append(df["Sepal_Length_cm"].loc[100:].mean())
    Iris_virginica.append(df["Sepal_Width_cm"].loc[100:].mean())
    
    # Gets the standard deviation of the sepal length and width.
    Iris_virginica.append(df["Sepal_Length_cm"].loc[100:].std(ddof=1))
    Iris_virginica.append(df["Sepal_Width_cm"].loc[100:].std(ddof=1))
    
    # Gets the min and max values for petal length and width.
    Iris_virginica.append(df["Petal_Length_cm"].loc[100:].min())
    Iris_virginica.append(df["Petal_Length_cm"].loc[100:].max())
    Iris_virginica.append(df["Petal_Width_cm"].loc[100:].min())
    Iris_virginica.append(df["Petal_Width_cm"].loc[100:].max())
    
    # Gets the average petal size.
    Iris_virginica.append(df["Petal_Length_cm"].loc[100:].mean())
    Iris_virginica.append(df["Petal_Width_cm"].loc[100:].mean())
    
    # Gets the standard deviation of the petal length and width.
    Iris_virginica.append(df["Petal_Length_cm"].loc[100:].std(ddof=1))
    Iris_virginica.append(df["Petal_Width_cm"].loc[100:].std(ddof=1))
    
    return Iris_virginica

def get_data_per_iris(df):
    """
    This function extracts each flower species and calculates the Min, Max,
    Mean, and SD for the lengths of their sepals and petals.
    
    df: An iris DataFrame table.

    Returns: A DataFrame table.
    """
    classes = []
    for plant in df["Class"]:
        if plant not in classes:
            classes.append(plant)
    new_df = pd.DataFrame(index = classes,
                          columns = ["Sepal_L_Min", "Sepal_L_Max",
                                     "Sepal_W_Min", "Sepal_W_Max",
                                     "Sepal_L_Mean", "Sepal_W_Mean",
                                     "Sepal_L_SD", "Sepal_W_SD",
                                     "Petal_L_Min", "Petal_L_Max",
                                     "Petal_W_Min", "Petal_W_Max",
                                     "Petal_L_Mean", "Petal_W_Mean",
                                     "Petal_L_SD", "Petal_W_SD"],
                          dtype = np.float64)
    # Fills in data for the flowers.
    Iris_setosa = get_data_iris_setosa(df)
    Iris_versicolor = get_data_iris_versicolor(df)
    Iris_virginica = get_data_iris_virginica(df)
    
    new_df.loc["Iris-setosa"] = Iris_setosa
    new_df.loc["Iris-versicolor"] = Iris_versicolor
    new_df.loc["Iris-virginica"] = Iris_virginica
    
    return new_df

def make_fig1(df):
    """
    This function takes an iris DataFrame and creates a bar chart that displays
    the variations between the sepal and petal lengths in cm of the three iris
    species.
    
    df: An iris DataFrame table.

    Returns: Nothing.
    """
    
    plt.style.use("dark_background")
    
    # Colors the background, bars, and face the appropriate colors.
    df[["Sepal_W_Mean", "Sepal_L_Mean", "Petal_W_Mean", "Petal_L_Mean"]].T.plot(kind="bar",
                                                 yerr=df[["Sepal_W_SD", "Sepal_L_SD", "Petal_W_SD", "Petal_L_SD"]].values,
                                                 legend=True,
                                                 ecolor="black",
                                                 capsize=8,
                                                 color=["yellow", "green", "red"],
                                                 edgecolor="black")
    ax = plt.gca()
    ax.set_facecolor('white')
    
    # Colors the fonts red.
    ax.set_ylabel("Sepal and Petal Lengths and Widths", color="red", fontsize=24)
    ax.set_xticklabels(["Sepal Widths", "Sepal Lengths", "Petal Widths", "Petal Lengths"], color="red", rotation=360, fontsize=18)
    ax.tick_params(axis="x", colors="red")
    ax.tick_params(axis="y", colors="red")
    
    # Colors the axis red.
    ax.spines["top"].set_color("red")
    ax.spines["bottom"].set_color("red")
    ax.spines["left"].set_color("red")
    ax.spines["right"].set_color("red")

def make_fig2(df):
    """
    This function takes an iris DataFrame and creates a scatter plot with the
    linear regressions for each iris species. The scatter plot records the
    sepal widths and lengths for each flower species in cm.
    
    df: An iris DataFrame table.

    Returns: Nothing.
    """
    
    plt.title("Measurement of Sepals in cm", fontsize=20)
    plt.ylabel("Sepal Length", fontsize=20)
    plt.xlabel("Sepal Width", fontsize=20)
    
    # Plots the lengths and widths of Setosa sepals.
    setosa_sepals_df = pd.DataFrame({"Sepal_W": df["Sepal_Width_cm"].loc[0:49], 
                              "Sepal_L": df["Sepal_Length_cm"].loc[0:49]},
                          dtype = np.float64)
    
    plt.scatter(x = setosa_sepals_df.Sepal_W, y = setosa_sepals_df.Sepal_L,
                                   label='Iris Setosa')
    
    setosa_sepals_df['mean'] = setosa_sepals_df.mean(axis=1)
    
    # Creates linear regression of Setosa sepals.
    x = setosa_sepals_df.Sepal_W.values
    X = sm.add_constant(x)
    model = sm.OLS(setosa_sepals_df.Sepal_L, X)
    line = model.fit()
    line.summary()
    y = line.params['x1'] * x + line.params['const']
    plt.plot(x, y, linewidth=4)
    
    # Plots the lengths and widths of Versicolor sepals.
    versicolor_sepals_df = pd.DataFrame({"Sepal_W": df["Sepal_Width_cm"].loc[50:99], 
                              "Sepal_L": df["Sepal_Length_cm"].loc[50:99]},
                          dtype = np.float64)
    
    plt.scatter(x = versicolor_sepals_df.Sepal_W, y = versicolor_sepals_df.Sepal_L,
                                   label='Iris Versicolor')
    
    # Creates linear regression of Versicolor sepals.
    x = versicolor_sepals_df.Sepal_W.values
    X = sm.add_constant(x)
    model = sm.OLS(versicolor_sepals_df.Sepal_L, X)
    line = model.fit()
    line.summary()
    y = line.params['x1'] * x + line.params['const']
    plt.plot(x, y, linewidth=4)
    
    # Plots the lengths and widths of Virginica sepals.
    virginica_sepals_df = pd.DataFrame({"Sepal_W": df["Sepal_Width_cm"].loc[100:], 
                              "Sepal_L": df["Sepal_Length_cm"].loc[100:]},
                          dtype = np.float64)
    
    plt.scatter(x = virginica_sepals_df.Sepal_W, y = virginica_sepals_df.Sepal_L,
                                   label='Iris Virginica')
    
    # Creates linear regression of Virginica sepals
    x = virginica_sepals_df.Sepal_W.values
    X = sm.add_constant(x)
    model = sm.OLS(virginica_sepals_df.Sepal_L, X)
    line = model.fit()
    line.summary()
    y = line.params['x1'] * x + line.params['const']
    plt.plot(x, y, linewidth=4)
    
    plt.legend()

def make_fig3(df):
    """
    This function takes an iris DataFrame and creates a scatter plot with the
    linear regressions for each iris species. The scatter plot records the
    petal widths and lengths for each flower species in cm.
    
    df: An iris DataFrame table.

    Returns: Nothing.
    """
    
    plt.title("Measurement of Petals in cm", fontsize=20)
    plt.ylabel("Petal Length", fontsize=20)
    plt.xlabel("Petal Width", fontsize=20)
    
    # Plots the lengths and widths of Setosa petals.
    setosa_petals_df = pd.DataFrame({"Petal_W": df["Petal_Width_cm"].loc[0:49], 
                              "Petal_L": df["Petal_Length_cm"].loc[0:49]},
                          dtype = np.float64)
    
    plt.scatter(x = setosa_petals_df.Petal_W, y = setosa_petals_df.Petal_L,
                                   label='Iris Setosa')
    
    setosa_petals_df['mean'] = setosa_petals_df.mean(axis=1)
    
    # Creates linear regression of Setosa petals.
    x = setosa_petals_df.Petal_W.values
    X = sm.add_constant(x)
    model = sm.OLS(setosa_petals_df.Petal_L, X)
    line = model.fit()
    line.summary()
    y = line.params['x1'] * x + line.params['const']
    plt.plot(x, y, linewidth=4)
    
    # Plots the lengths and widths of Versicolor petals.
    versicolor_petals_df = pd.DataFrame({"Petal_W": df["Petal_Width_cm"].loc[50:99], 
                              "Petal_L": df["Petal_Length_cm"].loc[50:99]},
                          dtype = np.float64)
    
    plt.scatter(x = versicolor_petals_df.Petal_W, y = versicolor_petals_df.Petal_L,
                                   label='Iris Versicolor')
    
    # Creates linear regression of Versicolor petals.
    x = versicolor_petals_df.Petal_W.values
    X = sm.add_constant(x)
    model = sm.OLS(versicolor_petals_df.Petal_L, X)
    line = model.fit()
    line.summary()
    y = line.params['x1'] * x + line.params['const']
    plt.plot(x, y, linewidth=4)
    
    # Plots the lengths and widths of Virginica petals.
    virginica_petals_df = pd.DataFrame({"Petal_W": df["Petal_Width_cm"].loc[100:], 
                              "Petal_L": df["Petal_Length_cm"].loc[100:]},
                          dtype = np.float64)
    
    plt.scatter(x = virginica_petals_df.Petal_W, y = virginica_petals_df.Petal_L,
                                   label='Iris Virginica')
    
    # Creates linear regression of Virginica petals
    x = virginica_petals_df.Petal_W.values
    X = sm.add_constant(x)
    model = sm.OLS(virginica_petals_df.Petal_L, X)
    line = model.fit()
    line.summary()
    y = line.params['x1'] * x + line.params['const']
    plt.plot(x, y, linewidth=4)
    
    plt.legend()

def main():
    df = get_data()
    figure1 = get_data_per_iris(df)
    make_fig1(figure1)
    plt.figure()
    
    # Plots the measurements of sepals and petals of irises.
    make_fig2(df)
    plt.figure()
    
    make_fig3(df)
    plt.show()

main()