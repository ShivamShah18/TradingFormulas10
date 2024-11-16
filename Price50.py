import pandas as pd
from pandas import DataFrame

def Price50(data: DataFrame) -> float:

  if len(data) < 50:
        raise ValueError("Number of rows in DataFrame is lower than 50.")

  SMA_50 = data['Close'].rolling(window=50).mean().iloc[-1]
  points = (SMA_50 - data['Close'].iloc[-1]) / 0.00001

  return points
