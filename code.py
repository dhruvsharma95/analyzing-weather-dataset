# --------------
import numpy as np
import pandas as pd

# Step - 1
weather = pd.read_csv(path)
print(weather.head())
print(weather.shape)
print(weather.dtypes)


# Step - 2
def categorical(df):
    for col in df.columns:
        if df[col].dtypes == 'object':
            print(f"{col} is a categorical variable")

def numerical(df):
    for col in df.columns:
        if df[col].dtypes != 'object':
            print(f"{col} is a numerical variable")
    
categorical(weather)
numerical(weather)


# Step - 3
print(weather.columns)

def clear(col, value):
    out = weather[weather[col] == value]
    print(f'No. of times {col} is {value}: ', out.shape[0])

clear('Weather', 'Cloudy')
clear('Visibility (km)', 8)
clear('Rel Hum (%)', 80)
clear('Wind Spd (km/h)', 6)


# Step - 4
def instances_based_condition(col_1, col_2, val_1, val_2):
    return weather[(weather[col_1] > val_1) & (weather[col_2] == val_2)]

wind_speed_35_vis_25 = instances_based_condition('Wind Spd (km/h)', 'Visibility (km)', 35, 25)
print(wind_speed_35_vis_25.head())


# Step - 5
weather['Month'] =  pd.DatetimeIndex(weather['Date/Time']).month

def agg_values_ina_month(val, ind):
    print(weather.pivot_table(values = val, index = ind, aggfunc = {sum, min, max, len, np.mean}))

agg_values_ina_month('Temp (C)', 'Month')


# Step - 6
weather.drop(columns = 'Month', inplace = True)
def group_values(col):
    return weather.groupby(col).mean()

mean_weather = group_values('Weather')
print(mean_weather.head())


# Step - 7
def convert():
    weather['Temp (C)'] = (weather['Temp (C)']*1.8)+32
    print(weather['Temp (C)'])
        
convert()



