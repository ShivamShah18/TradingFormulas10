# takes in a parameter for the lookback period and data feed with length > lookback period(otherwise throws error). returns an double for the SMA value.
import pandas as pd
from pandas import DataFrame

def SMA(period: int, data: DataFrame) -> float:
    
    if len(data) < period:
        raise ValueError("Number of rows in DataFrame is lower than the specified period.")

    sma = data['Close'].rolling(window=period).mean().iloc[-1]

    return sma.iloc[-1]


