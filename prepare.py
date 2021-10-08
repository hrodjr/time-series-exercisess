import pandas as pd


def prepare(df):
#Filters Springfield, US temps    
    df = df[df['City']=='Springfield']
#converts uppercase to lowercase in columns
    df = df.rename(str.lower, axis='columns')
#rename columns
    df = df.rename(columns = {'dt':'date', 'averagetemperature':'avg_temp',
                          'averagetemperatureuncertainty':'avgtemp_uncertainty'})
#fills NaN's with the corresponding column average
    df.avg_temp.fillna(df.avg_temp.mean(), inplace = True)
    df.avgtemp_uncertainty.fillna(df.avgtemp_uncertainty.mean(), inplace = True)
#drop alpha characters from lat/long
    df['longitude'] = df.longitude.str.strip('W')
    df['latitude'] = df.latitude.str.strip('N')
#convert dtypes for lat/long
    convert_dict_int = {'latitude': float, 'longitude': float}
    df = df.astype(convert_dict_int)   
#Reassign the sale_date column to be a datetime type
    df.date = pd.to_datetime(df.date)
#sort rows by the date and then set the index as that date
    df = df.set_index('date').sort_index()
#filters 50 years
    df = df.loc['1963-09-01':'2013-09-01']
#converting celcius to fahrenheit
    df.avg_temp = df.avg_temp * 1.800 + 32.00
    df.avgtemp_uncertainty = df.avgtemp_uncertainty * 1.800 + 32.00
    
    return df

#new df summarization
def summarize(df):
    print(df.shape)
    print(f'___________________________')
    print(df.info())
    print(f'___________________________')      
    print(df.isnull().sum())