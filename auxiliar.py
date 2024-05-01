import pandas as pd

def df_tratar(df):
    df['Date'] = pd.to_datetime(df['Date'])

    return df