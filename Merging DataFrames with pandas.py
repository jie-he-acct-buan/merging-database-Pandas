import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 10000)
pd.set_option('display.max_columns', 10000)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.width', None)

###############################################################################
# Read 'Bronze.csv' into a DataFrame: bronze
bronze = pd.read_csv('Bronze.csv')

# Read 'Silver.csv' into a DataFrame: silver
silver = pd.read_csv('Silver.csv')

# Read 'Gold.csv' into a DataFrame: gold
gold = pd.read_csv('Gold.csv')

# Print the first five rows of gold
print(gold.head())
###############################################################################
# Create the list of file names: filenames
filenames = ['Gold.csv', 
             'Silver.csv', 
             'Bronze.csv']

# Create the list of three DataFrames: dataframes
dataframes = []
for filename in filenames:
    dataframes.append(pd.read_csv(filename))

# Print top 5 rows of 1st DataFrame in dataframes
print(dataframes[0].head())
###############################################################################
# Make a copy of gold: medals
medals = gold.copy()

# Create list of new column labels: new_labels
new_labels = ['NOC', 'Country', 'Gold']

# Rename the columns of medals using new_labels
medals.columns = new_labels

# Add columns 'Silver' & 'Bronze' to medals
medals['Silver'] = silver.Total
medals['Bronze'] = bronze.Total

# Print the head of medals
print(medals.head())
###############################################################################
# Read 'monthly_max_temp.csv' into a DataFrame: weather1
weather1 = pd.read_csv('monthly_max_temp.csv', index_col='Month')

# Print the head of weather1
print(weather1.head())

# Sort the index of weather1 in alphabetical order: weather2
weather2 = weather1.sort_index()

# Print the head of weather2
print(weather2.head())

# Sort the index of weather1 in reverse alphabetical order: weather3
weather3 = weather1.sort_index(ascending=False)

# Print the head of weather3
print(weather3.head())

# Sort weather1 numerically using the values of 'Max TemperatureF': weather4
weather4 = weather1.sort_values('Max TemperatureF')

# Print the head of weather4
print(weather4.head())
###############################################################################
# Reindex weather1 using the list year: weather2
weather2 = weather1.reindex(year)

# Print weather2
print(weather2)

# Reindex weather1 using the list year with forward-fill: weather3
weather3 = weather1.reindex(year).ffill()

# Print weather3
print(weather3)
###############################################################################
names_1881 = pd.read_csv('names1881.csv', header=None)
names_1881.columns=['name', 'gender', 'count']
names_1881 = names_1881.set_index(['name', 'gender'])
names_1981 = pd.read_csv('names1981.csv', header=None)
names_1981.columns=['name', 'gender', 'count']
names_1981 = names_1981.set_index(['name', 'gender'])
# Reindex names_1981 with index of names_1881: common_names
common_names = names_1981.reindex(names_1881.index)

# Print shape of common_names
print(common_names.shape)

# Drop rows with null counts: common_names
common_names = common_names.dropna()

# Print shape of new common_names
print(common_names.shape)
###############################################################################
weather = pd.read_csv('pittsburgh2013.csv', index_col='Date')

# Extract selected columns from weather as new DataFrame: temps_f
temps_f = weather[['Min TemperatureF', 'Mean TemperatureF', 'Max TemperatureF']]

# Convert temps_f to celsius: temps_c
temps_c = (temps_f - 32) * 5/9

# Rename 'F' in column names with 'C': temps_c.columns
temps_c.columns = temps_c.columns.str.replace('F', 'C')

# Print first 5 rows of temps_c
print(temps_c.head())
###############################################################################
gdp = pd.read_csv('gdp_usa.csv', parse_dates=True, index_col='DATE')

# Slice all the gdp data from 2008 onward: post2008
post2008 = gdp.loc['2008-01-01':,:]

# Print the last 8 rows of post2008
print(post2008.tail(8))

# Resample post2008 by year, keeping last(): yearly
yearly = post2008.resample('A').last()

# Print yearly
print(yearly)

# Compute percentage growth of yearly: yearly['growth']
yearly['growth'] = yearly.pct_change()*100

# Print yearly again
print(yearly)

###############################################################################
sp500 = pd.read_csv('sp500.csv', parse_dates=True, index_col='Date')
exchange = pd.read_csv('exchange.csv', parse_dates=True, index_col='Date')

# Subset 'Open' & 'Close' columns from sp500: dollars
dollars = sp500[['Open', 'Close']]

# Print the head of dollars
print(dollars.head())

# Convert dollars to pounds: pounds
pounds = dollars.multiply(exchange['GBP/USD'], axis=0)

# Print the head of pounds
print(pounds.head())
###############################################################################
jan = pd.read_csv('sales-feb-2015.csv', parse_dates=True, index_col='Date')
mar = pd.read_csv('sales-mar-2015.csv', parse_dates=True, index_col='Date')
# Extract the 'Units' column from jan: jan_units
jan_units = jan['Units']

# Extract the 'Units' column from feb: feb_units
feb_units = feb['Units']

# Extract the 'Units' column from mar: mar_units
mar_units = mar['Units']

# Append feb_units and then mar_units to jan_units: quarter1
quarter1 = jan_units.append(feb_units).append(mar_units)

# Print the first slice from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])

# Print the second slice from quarter1
print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])

# Compute & print total sales in quarter1
print(quarter1.sum())
###############################################################################
# Initialize empty list: units
units = []

# Build the list of Series
for month in [jan, feb, mar]:
    units.append(month['Units'])

# Concatenate the list: quarter1
quarter1 = pd.concat(units, axis=0)

# Print slices from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])
print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])
###############################################################################
names_1881 = pd.read_csv('names1881.csv', header=None, names=['name', 'gender', 'count'])
names_1981 = pd.read_csv('names1981.csv', header=None, names=['name', 'gender', 'count'])

# Add 'year' column to names_1881 and names_1981
names_1881['year'] = 1881
names_1981['year'] = 1981

# Append names_1981 after names_1881 with ignore_index=True: combined_names
combined_names = names_1881.append((names_1981), ignore_index=True)

# Print shapes of names_1981, names_1881, and combined_names
print(names_1981.shape)
print(names_1881.shape)
print(combined_names.shape)

# Print all rows that contain the name 'Morgan'
print(combined_names.loc[combined_names['name']=='Morgan'])
###############################################################################
medals=[]
medal_types=['gold', 'silver', 'bronze']
for medal in medal_types:

    # Create the file name: file_name
    file_name = '%s_top5.csv' % medal
    
    # Create list of column names: columns
    columns = ['Country', medal]
    
    # Read file_name into a DataFrame: df
    medal_df = pd.read_csv(file_name, header=0, index_col='Country', names=columns)

    # Append medal_df to medals
    medals.append(medal_df)

# Concatenate medals horizontally: medals
medals = pd.concat(medals, axis=1, sort=True)

# Print medals
print(medals)
###############################################################################
medals=[]
medal_types=['gold', 'silver', 'bronze']
for medal in medal_types:

    file_name = '%s_top5.csv' % medal
    
    # Read file_name into a DataFrame: medal_df
    medal_df = pd.read_csv(file_name, index_col='Country')
    
    # Append medal_df to medals
    medals.append(medal_df)
    
# Concatenate medals: medals
medals = pd.concat(medals, keys=['gold', 'silver', 'bronze'], axis=0)

# Print medals in entirety
print(medals)
###############################################################################
# Sort the entries of medals: medals_sorted
medals_sorted = medals.sort_index(level=0)

# Print the number of Bronze medals won by Germany
print(medals_sorted.loc[('bronze','Germany')])

# Print data about silver medals
print(medals_sorted.loc['silver'])

# Create alias for pd.IndexSlice: idx
idx = pd.IndexSlice

# Print all the data on medals won by the United Kingdom
print(medals_sorted.loc[idx[:, 'United Kingdom'],:])
###############################################################################
df1 = pd.read_csv('feb-sales-Hardware.csv', parse_dates=True, index_col='Date')
df2 = pd.read_csv('feb-sales-Software.csv', parse_dates=True, index_col='Date')
df3 = pd.read_csv('feb-sales-Service.csv', parse_dates=True, index_col='Date')
february = pd.concat((df1,df2,df3), axis=1, keys=['Hardware', 'Software', 'Service'])

# Print february.info()
print(february.info())

# Assign pd.IndexSlice: idx
idx = pd.IndexSlice

# Create the slice: slice_2_8
slice_2_8 = february.loc['2015-02-02':'2015-02-08', idx[:, 'Company']]

# Print slice_2_8
print(slice_2_8)
###############################################################################
jan = pd.read_csv('sales-jan-2015.csv', parse_dates=True)
feb = pd.read_csv('sales-feb-2015.csv', parse_dates=True)
mar = pd.read_csv('sales-mar-2015.csv', parse_dates=True)

# Make the list of tuples: month_list
month_list = [('january', jan), ('february', feb), ('march', mar)]

# Create an empty dictionary: month_dict
month_dict = {}

for month_name, month_data in month_list:

    # Group month_data: month_dict[month_name]
    month_dict[month_name] = month_data.groupby('Company').sum()

# Concatenate data in month_dict: sales
sales = pd.concat(month_dict)

# Print sales
print(sales)

# Print all sales by Mediacore
idx = pd.IndexSlice
print(sales.loc[idx[:, 'Mediacore'], :])
###############################################################################
# Read 'Bronze.csv' into a DataFrame: bronze
bronze = pd.read_csv('Bronze.csv', nrows=5)

# Read 'Silver.csv' into a DataFrame: silver
silver = pd.read_csv('Silver.csv', nrows=5)

# Read 'Gold.csv' into a DataFrame: gold
gold = pd.read_csv('Gold.csv', nrows=5)

# Create the list of DataFrames: medal_list
medal_list = ['bronze', 'silver', 'gold']

# Concatenate medal_list horizontally using an inner join: medals
medals = pd.concat((bronze, silver, gold), keys=medal_list, axis=1, join='inner')

# Print medals
print(medals)

###############################################################################
china = pd.read_csv('gdp_china.csv', parse_dates=True, index_col='Year')
china = china.rename(columns={'GDP':'China'})
usa = pd.read_csv('gdp_usa.csv', parse_dates=True, index_col='DATE')
us = usa.rename(columns={'VALUE':'USA'})
us.index.name = 'Year'

# Resample and tidy china: china_annual
china_annual = china.resample('A').last()
china_annual = china_annual.pct_change(10)
china_annual = china_annual.dropna()
# Resample and tidy us: us_annual
us_annual = us.resample('A').last()
us_annual = us_annual.pct_change(10)
us_annual = us_annual.dropna()

# Concatenate china_annual and us_annual: gdp
gdp = pd.concat((china_annual, us_annual), axis=1, join='inner')

# Resample gdp and print
print(gdp.resample('10A').last())

###############################################################################
oil = pd.read_csv('oil_price.csv', parse_dates=True)
auto = pd.read_csv('automobiles.csv')
oil.Date = pd.to_datetime(oil.Date)
auto.yr = pd.to_datetime(auto.yr)
# Merge auto and oil: merged
merged = pd.merge_asof(auto, oil, left_on='yr', right_on='Date')

# Print the tail of merged
print(merged.tail())

# Resample merged: yearly
yearly = merged.resample('A', on='Date')[['mpg', 'Price']].mean()

# Print yearly
print(yearly)

# print yearly.corr()
print(yearly.corr())
###############################################################################
# Create file path: file_path
file_path = 'Summer Olympic medalists 1896 to 2008 - EDITIONS.tsv'

# Load DataFrame from file_path: editions
editions = pd.read_csv(file_path, sep='\t')

# Extract the relevant columns: editions
editions = editions[['Edition', 'Grand Total', 'City', 'Country']]

# Print editions DataFrame
print(editions)
###############################################################################
# Create the file path: file_path
file_path = 'Summer Olympic medalists 1896 to 2008 - IOC COUNTRY CODES.csv'

# Load DataFrame from file_path: ioc_codes
ioc_codes = pd.read_csv(file_path)

# Extract the relevant columns: ioc_codes
ioc_codes = ioc_codes[['Country', 'NOC']]

# Print first and last 5 rows of ioc_codes
print(ioc_codes.head())
print(ioc_codes.tail())
###############################################################################
df = pd.read_csv('Summer Olympic medalists 1896 to 2008 - ALL MEDALISTS.tsv', 
                 sep='\t', skiprows=range(4))

medals = df[['Athlete', 'NOC', 'Medal', 'Edition']]
# Print first and last 5 rows of medals
print(medals.head())
print(medals.tail())
###############################################################################
# Construct the pivot_table: medal_counts
medal_counts = medals.pivot_table(index='Edition', columns='NOC', values='Athlete', aggfunc='count')

# Print the first & last 5 rows of medal_counts
print(medal_counts.head())
print(medal_counts.tail())
###############################################################################
# Set Index of editions: totals
totals = editions.set_index('Edition')

# Reassign totals['Grand Total']: totals
totals = totals['Grand Total']

# Divide medal_counts by totals: fractions
fractions = medal_counts.divide(totals, axis=0)

# Print first & last 5 rows of fractions
print(fractions.head())
print(fractions.tail())
###############################################################################
# Apply the expanding mean: mean_fractions
mean_fractions = fractions.expanding().mean()

# Compute the percentage change: fractions_change
fractions_change = mean_fractions.pct_change()*100

# Reset the index of fractions_change: fractions_change
fractions_change = fractions_change.reset_index('Edition')

# Print first & last 5 rows of fractions_change
print(fractions_change.head())
print(fractions_change.tail())
###############################################################################
# Left join editions and ioc_codes: hosts
hosts = pd.merge(editions, ioc_codes, on='Country', how='left')

# Extract relevant columns and set index: hosts
hosts = hosts[['Edition', 'NOC']].set_index('Edition')

# Fix missing 'NOC' values of hosts
print(hosts.loc[hosts.NOC.isnull()])
hosts.loc[1972, 'NOC'] = 'FRG'
hosts.loc[1980, 'NOC'] = 'URS'
hosts.loc[1988, 'NOC'] = 'KOR'

# Reset Index of hosts: hosts
hosts = hosts.reset_index()

# Print hosts
print(hosts)
###############################################################################
# Reshape fractions_change: reshaped
reshaped = fractions_change.melt(id_vars='Edition', value_name='Change')

# Print reshaped.shape and fractions_change.shape
print(reshaped.shape, fractions_change.shape)

# Extract rows from reshaped where 'NOC' == 'CHN': chn
chn = reshaped[reshaped['NOC']=='CHN']

# Print last 5 rows of chn with .tail()
print(chn.tail())
###############################################################################
# Merge reshaped and hosts: merged
merged = pd.merge(reshaped, hosts, how='inner')

# Print first 5 rows of merged
print(merged.head())

# Set Index of merged and sort it: influence
influence = merged.set_index('Edition').sort_index()

# Print first 5 rows of influence
print(influence.head())
###############################################################################
# Extract influence['Change']: change
change = influence.Change

# Make bar plot of change: ax
ax = change.plot(kind='bar')

# Customize the plot to improve readability
ax.set_ylabel("% Change of Host Country Medal Count")
ax.set_title("Is there a Host Country Advantage?")
ax.set_xticklabels(editions['City'])

# Display the plot
plt.show()
###############################################################################
