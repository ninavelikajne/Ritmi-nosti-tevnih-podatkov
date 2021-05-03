from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import calendar



def get_weekend(row):
    day = row['day']
    if day == 'Sunday' or day == 'Saturday':
        return 'weekend'
    else:
        return 'weekday'


def get_day(row):
    row['day_name']=calendar.day_name[row['date'].weekday()]
    row['day']=row['date'].weekday()
    return row



df = pd.read_csv(r'data.csv')
df['date']=pd.to_datetime(df['date'], format='%Y-%m-%d', errors='ignore')
df=df.apply(lambda row: get_day(row),axis=1)

df_first=df[(df['date'] >= '2020-10-20') & (df['date'] <= '2021-02-10')]
df_first.to_csv(r'data_first.csv')

df_second=df[(df['date'] >= '2021-02-11') & (df['date'] <= '2021-04-26')]
df_second.to_csv(r'data_second.csv')

df_third=df[(df['date'] >= '2020-10-20') & (df['date'] <= '2021-04-26')]
df_third.to_csv(r'data_third.csv')