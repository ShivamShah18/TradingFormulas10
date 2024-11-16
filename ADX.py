import pandas as pd
import numpy as np


def calculate_true_range(high, low, close):
    tr1 = high - low
    tr2 = (high - close.shift()).abs()
    tr3 = (low - close.shift()).abs()
    true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    return true_range

def calculate_dm(high, low):
    plus_dm = high.diff()
    minus_dm = -low.diff()
    plus_dm[plus_dm < 0] = 0
    minus_dm[minus_dm < 0] = 0
    return plus_dm, minus_dm

def ADX(dataset, high_column='High', low_column='Low', close_column='Close', window=14):
    """
    Appends an ADX column to the dataset.

    Parameters:
    - dataset: Dataset object
    - high_column: str, the name of the column for high prices
    - low_column: str, the name of the column for low prices
    - close_column: str, the name of the column for close prices
    - window: int, the window period for ADX calculation
    """
    if high_column not in dataset.columns or low_column not in dataset.columns or close_column not in dataset.columns:
        raise ValueError(f"One or more required columns ({high_column}, {low_column}, {close_column}) not found in the dataset")
    
    high = dataset[high_column]
    low = dataset[low_column]
    close = dataset[close_column]

    # Calculate True Range
    true_range = calculate_true_range(high, low, close)
    
    # Calculate +DM and -DM
    plus_dm, minus_dm = calculate_dm(high, low)
    
    # Calculate smoothed TR, +DM, and -DM
    atr = true_range.rolling(window=window).mean()
    plus_dm_smoothed = plus_dm.rolling(window=window).mean()
    minus_dm_smoothed = minus_dm.rolling(window=window).mean()

    # Calculate +DI and -DI
    plus_di = 100 * (plus_dm_smoothed / atr)
    minus_di = 100 * (minus_dm_smoothed / atr)

    # Calculate DX
    dx = 100 * ((plus_di - minus_di).abs() / (plus_di + minus_di))

    # Calculate ADX
    adx = dx.rolling(window=window).mean()

    dataset['ADX'] = adx

    return dataset
