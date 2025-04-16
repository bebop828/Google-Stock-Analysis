
import pandas as pd
import os

df= pd.read_csv('Convert file/Google Dataset.csv')
df['Date'] = pd.to_datetime(df['Date'])

google_04 = df[df['Date'].dt.year == 2004]
google_05 = df[df['Date'].dt.year == 2005]
google_06 = df[df['Date'].dt.year == 2006]
google_07 = df[df['Date'].dt.year == 2007]
google_08 = df[df['Date'].dt.year == 2008]
google_09 = df[df['Date'].dt.year == 2009]
google_10 = df[df['Date'].dt.year == 2010]
google_11 = df[df['Date'].dt.year == 2011]
google_12 = df[df['Date'].dt.year == 2012]
google_13 = df[df['Date'].dt.year == 2013]
google_14 = df[df['Date'].dt.year == 2014]
google_15 = df[df['Date'].dt.year == 2015]
google_16 = df[df['Date'].dt.year == 2016]
google_17 = df[df['Date'].dt.year == 2017]
google_18 = df[df['Date'].dt.year == 2018]
google_19 = df[df['Date'].dt.year == 2019]
google_20 = df[df['Date'].dt.year == 2020]
google_21 = df[df['Date'].dt.year == 2021]
google_22 = df[df['Date'].dt.year == 2022]
google_23 = df[df['Date'].dt.year == 2023]
google_24 = df[df['Date'].dt.year == 2024]

google_data = {
    2004: google_04,
    2005: google_05,
    2006: google_06,
    2007: google_07,
    2008: google_08,
    2009: google_09,
    2010: google_10,
    2011: google_11,
    2012: google_12,
    2013: google_13,
    2014: google_14,
    2015: google_15,
    2016: google_16,
    2017: google_17,
    2018: google_18,
    2019: google_19,
    2020: google_20,
    2021: google_21,
    2022: google_22,
    2023: google_23,
    2024: google_24
}

for year, df in google_data.items():
    folder_path = f'Google {year}'  
    os.makedirs(folder_path, exist_ok=True)  
    
    file_path = os.path.join(folder_path, f'Google_Data_{year}.csv')  
    df.to_csv(file_path, index=False)

