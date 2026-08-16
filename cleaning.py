#script to import the data and clean it for analysis
import pandas as pd
import numpy as np

try:
    df = pd.read_csv("final project/gold_stock.csv")
    print("Dataset loaded successfully.")

except FileNotFoundError:
    print("Error: Could not find final gold_stock.csv")



def clean_data(df):
    #first two rows are not needed, so we will remove them
    df = df.iloc[2:].copy()
    return df

def fix_column(df):
    #fixing the column names
    df.columns = ['Date','close', 'High','Low','Open',  'Vol.']
    return df

def convert_data_types(df):
    #converting the data types of the columns to appropriate types
    df['Date'] = pd.to_datetime(df['Date'])
    df['close'] = df['close'].str.replace(',', '').astype(float)
    df['Open'] = df['Open'].str.replace(',', '').astype(float)
    df['High'] = df['High'].str.replace(',', '').astype(float)
    df['Low'] = df['Low'].str.replace(',', '').astype(float)
    df['Vol.'] = df['Vol.'].str.replace('K', 'e3').str.replace('M', 'e6').astype(float)
    
    return df
def to_numeric(df):
    #converting the data types of the columns to appropriate types
    
    df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
    df['High'] = pd.to_numeric(df['High'], errors='coerce')
    df['Low'] = pd.to_numeric(df['Low'], errors='coerce')
    df['Vol.'] = pd.to_numeric(df['Vol.'], errors='coerce')
    df['close'] = pd.to_numeric(df['close'], errors='coerce')
    return df

def drop_missing_values(df):
    #dropping the rows with missing values
    df = df.dropna()
    return df


#calling the functions to clean the data while using try and except to handle any errors that may occur
try:
    df = clean_data(df)
    df = fix_column(df)
    df = convert_data_types(df)
    df = to_numeric(df)
    df = drop_missing_values(df)
    print("Data cleaned successfully.")
except Exception as e:
    print(f"Error: {e}")
    print("Error: Could not clean the data. Please check the data and try again.")


#now that the data is cleaned, we will save it to a new csv file
try:
    df.to_csv("final project/gold_stock_cleaned.csv", index=False)
    print("Cleaned data saved to gold_stock_cleaned.csv")
except Exception as e:
    print(f"Error: {e}")
    print("Error: Could not save the cleaned data. Please check the data and try again.")