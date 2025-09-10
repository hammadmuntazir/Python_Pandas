import pandas as pd
import numpy as np
df1=pd.read_csv('airlines_flights_data.csv')
# print(df1.head())

#    index   airline   flight source_city departure_time stops   arrival_time destination_city    class  duration  days_left  price
# 0      0  SpiceJet  SG-8709       Delhi        Evening  zero          Night           Mumbai  Economy      2.17          1   5953
# 1      1  SpiceJet  SG-8157       Delhi  Early_Morning  zero        Morning           Mumbai  Economy      2.33          1   5953
# 2      2   AirAsia   I5-764       Delhi  Early_Morning  zero  Early_Morning           Mumbai  Economy      2.17          1   5956
# 3      3   Vistara   UK-995       Delhi        Morning  zero      Afternoon           Mumbai  Economy      2.25          1   5955
# 4      4   Vistara   UK-963       Delhi        Morning  zero        Morning           Mumbai  Economy      2.33          1   5955

# print(df1.info())
# no need for filtration as data is already clean
# print(df1.isnull().sum()) ## no null values
airline_frequencies=df1['airline'].value_counts().count()
print("Number of airlines in the dataset:", airline_frequencies)

Airline_having_maximum_frequency=df1['airline'].value_counts().idxmax()
print('Airline having maximum flight is : ',Airline_having_maximum_frequency)
# Airline having maximum flight is :  Vistara

average_price_of_flights_for_each_airline=df1.groupby('airline')['price'].mean()
print(f'Average Price of flights of each Airline is : {average_price_of_flights_for_each_airline}')

# Average Price of flights of each Airline is : airline
# AirAsia       4091.072742
# Air_India    23507.019112
# GO_FIRST      5652.007595
# Indigo        5324.216303
# SpiceJet      6179.278881
# Vistara      30396.536302
# Name: price

route_having_highest_average_price=df1.groupby(['source_city','destination_city'])['price'].mean().idxmax()
print(f'Route having highest price is : {route_having_highest_average_price}')
# route having highest price is : ('Chennai', 'Bangalore')

average_duration_for_flight_for_each_airline=df1.groupby('airline')['duration'].mean()
print(f'average durations of flights of air lines are : {average_duration_for_flight_for_each_airline}')

# average durations of flights of air lines are : airline
# AirAsia       8.941714
# Air_India    15.504235
# GO_FIRST      8.755380
# Indigo        5.795197
# SpiceJet     12.579767
# Vistara      13.326634
# Name: duration,

airline_having_shortest_flight_duration=df1.groupby('airline')['duration'].min().idxmin()
print(f'Airline having shortest Flight duration is :{airline_having_shortest_flight_duration}')
# Airline having shortest Flight duration is :Indigo

correlation_duration_price=df1['duration'].corr(df1['price'])
print(f'correlation between duration and price is : {correlation_duration_price}' )
# correlation between duration and price is : 0.20422236784542708# #it means as duration increases price also increases but not strongly

average_price_per_stops=df1.groupby('stops')['price'].mean()
print(average_price_per_stops)

most_frequent_source_city=df1['source_city'].value_counts().idxmax()
print(most_frequent_source_city)

most_frequent_destination_city=df1['destination_city'].value_counts().idxmax()
print(most_frequent_destination_city)