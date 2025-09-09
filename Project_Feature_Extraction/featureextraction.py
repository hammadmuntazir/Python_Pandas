import numpy as np
import pandas as pd
from datetime import datetime

df=pd.read_csv('anime.csv')
# print(df.head())
             #### # make a new column for episode count

# print(df.loc[1]['Title'])
# Steins;GateTV (24 eps)Apr 2011 - Sep 20112,473,707 members


# everytitle has there episode count but separate column nai bana hua
txt=(df.loc[3]['Title'])
# Gintama°TV (51 eps)Apr 2015 - Mar 2016605,113 members
# episode count nikalna hai title se jo ky bracket mein araha hai haar baar

def extract_episode_count(txt):
    check =False
    data=''
    for i in txt:
        if i==')':
            break
        if check == True:
             data+=i
        if i=='(':
            check=True
    return data

# print(df['Title'].apply(extract_episode_count))
df['Episodes']=df['Title'].apply(extract_episode_count)
df['Episodes']=df['Episodes'].str.replace('eps','')
# print(df.head().to_string()) 
# convert episode column which are string to numeric
df['Episodes']=df['Episodes'].astype(int)
# data ta us mein title tha title mein sy episode ko extract kia phir kuch cheezo ko replace kia jo important nai thi 
 
   ### make a new column for timestamp
# df.loc[3]['Title']
def extract_timestamp(txt):
    check=False
    data=''
    for i in range(len(txt)):
        if txt[i]==')':
            for j in range(i+1,i+20):
                data+=txt[j]

            return data
# print(df['Title'].apply(extract_timestamp))
# Extract the timestamp first
df['TimeRange'] = df['Title'].apply(extract_timestamp)
# print(df['TimeRange'])
def calculate_months(date_range):
    try:
        if pd.isna(date_range):
            return None
            
        # Split the date range into start and end parts
        start_str, end_str = date_range.split(' - ')
        
        # Parse the dates
        start_date = datetime.strptime(start_str, '%b %Y')
        end_date = datetime.strptime(end_str, '%b %Y')
        
        # Calculate total months
        total_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month) + 1
        
        return total_months
        
    except:
        return None

# Apply to the extracted TimeRange column, not the full Title
df['TotalMonths'] = df['TimeRange'].apply(calculate_months)
# print(df[['Title', 'TimeRange', 'TotalMonths']].head())
 
    # # which anime has highest score

# print(df[df['Score']==df['Score'].max()])

  ## give me top 5 highest scoring anime
top5=df['Score'].value_counts()
# print(top5)
unique_scores=df['Score'].unique()
# print(unique_scores)
# since data is sorted in descending order
# print(df['Title'].head())
   ### which anime has highest episode count

highest_episode=df['Episodes']==df['Episodes'].max()
# print(df[highest_episode])
           ## animes with top 5 episode count
top5_episode_count=df['Episodes'].value_counts().head()
print(top5_episode_count)
print(df[df['Episodes'].isin(top5_episode_count.index)])

   # which is largest running anime
longest_running_anime=df['TotalMonths'].max()
print(df[df['TotalMonths']==longest_running_anime])