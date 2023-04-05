# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:06:51 2023

@author: Nimasha
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


def read_data(filename):
    """
    Reads data and return.
    """
    # Reads data from csv file
    dataframe = pd.read_csv(filename, skiprows=4)
    # Returns the dataframe
    return dataframe


def climate_data(dataframe, column, value, countries, years):
    """
    Filter data and transpose of the dataframe.
    """
    # Groups data with column value
    clim_data = dataframe.groupby(column, group_keys=True)
    clim_data = clim_data.get_group(value)
    # Resets the index
    clim_data = clim_data.reset_index()

    clim_data.set_index('Country Name', inplace=True)
    clim_data = clim_data.loc[:, years]
    clim_data = clim_data.loc[countries, :]
    # clean the dataframe
    clim_data = clim_data.dropna(axis=1)
    # Resets the index
    clim_data = clim_data.reset_index()
    # Transposing the index of the dataframe
    transposed_data = clim_data.set_index('Country Name')
    transposed_data = transposed_data.transpose()
    # Returns normal dataframe and transposed dataframe
    return clim_data, transposed_data


def bar_plot(dataset, title, xlabel, ylabel):
    """ 
    polt a bar plot
    """

    dataset.plot.bar(x='Country Name', rot=0, figsize=(50, 25), fontsize=50)
    plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
    plt.legend(fontsize=50)
    plt.title(title.upper(), fontsize=60, fontweight='bold')
    plt.xlabel(xlabel, fontsize=60)
    plt.ylabel(ylabel, fontsize=60)
    plt.savefig(title + '.png')
    plt.show()
    return


def line_plot(dataset, title, xlabel, ylabel):
    """ 
    plot a line plot.
    """

    dataset.plot.line(figsize=(50, 30), fontsize=60, linewidth=6.0)
    plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    plt.title(title.upper(), fontsize=70, fontweight='bold')
    plt.xlabel(xlabel, fontsize=70)
    plt.ylabel(ylabel, fontsize=70)
    plt.legend(fontsize=60)
    plt.savefig(title + '.png')
    plt.show()
    return


def stat_data(dataframe, col, value, yr, a):

    df_stat = dataframe.groupby(col, group_keys=True)
    df_stat = df_stat.get_group(value)
    df_stat = df_stat.reset_index()
    df_stat.set_index('Indicator Name', inplace=True)
    df_stat = df_stat.loc[:, yr]
    df_stat = df_stat.transpose()
    df_stat = df_stat.loc[:, a]
    return df_stat


def heat_map(data):

    plt.figure(figsize=(80, 40))
    sns.heatmap(data.corr(), annot=True, annot_kws={"size": 32})
    plt.title("Brazil's Heatmap".upper(), size=40, fontweight='bold')
    plt.xticks(rotation=90, horizontalalignment="center", fontsize=50)
    plt.yticks(rotation=0, fontsize=50)
    plt.savefig('Heatmap.png', dpi=300, bbox_inches='tight')
    plt.show()
    return data


# Creating list of countries and years for plotting bar plot
country1 = ['Canada', 'China', 'India', 'Nigeria']
year1 = ['2000', '2005', '2010', '2015', '2020']

# Reads data from csv file
world_data = read_data("climate_change.csv")
world_data1, transdata1 = climate_data(
    world_data, 'Indicator Name', 'Population growth (annual %)', country1, year1)
# Prints filtered data and transposed data
print(world_data1)
print(transdata1)
# Calling bar plot function with indicator as Population growth
bar_plot(world_data1, 'Population growth (annual %)',
         'Countries', 'Percentage of Population Growth')

world_data2, transdata2 = climate_data(
    world_data, 'Indicator Name', 'Forest area (% of land area)', country1, year1)
# Prints filtered data and transposed data
print(world_data2)
print(transdata2)

# Calling another bar plot function with indicator as Access to electricity
bar_plot(world_data2, 'Forest area (% of land area)',
         'Countries', 'Percentage of Forest area of land are')
# Creating list of countries and years for plotting line plot
country2 = ['Afghanistan', 'Argentina', 'Pakistan', 'Greece', 'Cuba']
year2 = ['2010', '2012', '2014', '2016', '2018', '2020']
world_data3, transdata3 = climate_data(
    world_data, 'Indicator Name', 'Agricultural land (% of land area)', country2, year2)
# Prints filtered data and transposed data
print(world_data3)
print(transdata3)

# Calling line plot function with indicator as Agricultural land
line_plot(transdata3, 'Agricultural land (% of land area)',
          'Year', 'Agricultural land (% of land area)')

world_data4, transdata4 = climate_data(
    world_data, 'Indicator Name', 'Forest area (% of land area)', country2, year2)
# Prints filtered data and transposed data
print(world_data4)
print(transdata4)

# Calling another line plot function with indicator as Forest land
line_plot(transdata4, 'Forest area (% of land area)',
          'Year', 'Forest area (% of land area)')

# Creating a variable with years
year_heat = ['2000', '2004', '2008', '2012', '2016']
# creating a variable indicators for HeatMap
indicators = ['Forest area (% of land area)', 'Agricultural land (% of land area)',
              'Urban population (% of total population)', 'Access to electricity (% of population)', 'Cereal yield (kg per hectare)', 'Annual freshwater withdrawals, total (% of internal resources)']
data_heat = stat_data(world_data, 'Country Name',
                      'Brazil', year_heat, indicators)
print(data_heat.head())
# Calling a function to create heatmap
heat_map(data_heat)

start = 2000
end = 2020
yeardes = [str(i) for i in range(start, end+1)]
indicator2 = ['Population growth (annual %)', 'Electricity production from oil sources (% of total)',
              'Electricity production from nuclear sources (% of total)', 'Electricity production from natural gas sources (% of total)']
descr = stat_data(world_data, 'Country Name',
                  'Iraq', yeardes, indicator2)
# returns a summary of descriptive statistics for a dataset

stats_summary = descr.describe()
print(stats_summary)
skewness = stats.skew(descr['Population growth (annual %)'])
kurtosis = descr['Electricity production from oil sources (% of total)'].kurtosis(
)
print('Skewness of Population growth in Iraq : ', skewness)
print('Kurtosis of Electricity production from natural gas in Iraq : ', kurtosis)
