import numpy as np
import pandas as pd

df=pd.read_csv('Countries.csv')
# print(df)

##1)first do data preprocssing like see null values etc
# print(df.shape)#194 rows and 64 columns
#print(df.info())#bohat si null values hain
#print(df.describe())##only 3 columns have numerical values rest are categorical
            
            ## Which country has highestPopulation#
# print(df.loc[1].to_string())
largest_population=df[df['population']==df['population'].max()]['country']
print(largest_population)

        # #What is capital of country with highest population
# print(df.columns)
print(df[df['population']==df['population'].max()]['capital_city'])

    ## Which country has least population
least_population=df[df['population']==df['population'].min()]['country']
print('Country with least Population is',least_population)

    ## What is capital of country with least population
least_population_capital=df[df['population']==df['population'].min()]['capital_city']
print(f'Capital With Least Population : {least_population_capital}')


    ## give me top5 countries with highest democratic score
df.sort_values(by='democracy_score',ascending=False,inplace=True)
# by default ascending is true
print(df['country'].head())

  ## how many total regions are there in data sets
print(df['region'].value_counts().count())
# total 22 regions hai jinky samany bohat si countries hain
    ## how many countries are there in estern europe region
print(df[df['region']=='Eastern Europe']['country'])
print(df[df['region']=='Eastern Europe']['country'].count())
    # Who is political region of 2nd highest population country
print(df[df['population']==df['population'].nlargest(2).iloc[1]]['political_leader'])

    #    how many countries are there whose political leader are unknown
print(df[df['political_leader'].isna()]['country'].count())

#  how many countries country_long have Republic in their name
count=0
def counting(txt):
    global count # ab count function k ander bhi use kr skty hain
    if 'republic' in txt.lower():
        count+=1
    return txt      #data mein koi change nhi krna chahte is function sy sirf count krna chahta hu
df['country_long']=df['country_long'].apply(counting)
print(count)
# total 125 countries hain jinka long name mein republic hai
    ## which country in African region has highest population
africa_df=df[df['continent']=='Africa']
print(africa_df[africa_df['population']==africa_df['population'].max()]['country'])