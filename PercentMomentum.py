import pandas as pd
from pandas import DataFrame

def PercentMomentum(data: DataFrame) -> float:

  if len(data) < 5:
        raise ValueError("Number of rows in DataFrame is lower than 5.")

  open = data['Open'].iloc[4:].dropna()
  open.reset_index(drop=True, inplace=True)
  close = data['Close']
  close.reset_index(drop=True, inplace=True)

  df_open_close = (abs(open - close)).dropna()
  df_vol = ((data['High']-data['Low']).rolling(window=5).sum()).dropna()
  df_vol.reset_index(drop=True, inplace=True)
  percent_momemtum = (df_open_close/df_vol*100).iloc[-1]

  return percent_momemtum
