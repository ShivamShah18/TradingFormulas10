import pandas as pd

def calculate_vwap_sma_indicator(data, timeframes, sma_period=200):
    vwap_indicators = {}
    
    for timeframe in timeframes:
        # Calculate VWAP
        vwap = (data[timeframe]['Close'] * data[timeframe]['Volume']).cumsum() / data[timeframe]['Volume'].cumsum()
        
        # Use the pre-calculated SMA from the data
        sma_column = f'SMA_{sma_period}_{timeframe}'
        sma = data[timeframe][sma_column]
        
        # Calculate the absolute distance between VWAP and the SMA
        distance = abs(vwap - sma)
        
        # Store the distance as the X value
        vwap_indicators[f'VWAP {sma_period} Indicator_{timeframe}'] = distance

    return vwap_indicators
