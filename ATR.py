import pandas as pd
from pandas import DataFrame

def ATR(period: int, data: DataFrame) -> float: 
    """
    Calculate Average True Range (ATR).

    Parameters:
    - period (int): The lookback period for calculating the ATR.
    - data (DataFrame): The DataFrame containing the data feed.

    Returns:
    - float: The ATR value.

    Raises:
    - ValueError: If the number of rows in the DataFrame is lower than the specified period.
    """
    if len(data) < period:
        raise ValueError("Number of rows in DataFrame is lower than the specified period.")

    data['High-Low'] = data['High'] - data['Low']
    data['High-PrevClose'] = abs(data['High'] - data['Close'].shift(1))
    data['Low-PrevClose'] = abs(data['Low'] - data['Close'].shift(1))
    data['TrueRange'] = data[['High-Low', 'High-PrevClose', 'Low-PrevClose']].max(axis=1)

    atr = data['TrueRange'].rolling(window=period).mean().iloc[-1]

    return atr.iloc[-1]
