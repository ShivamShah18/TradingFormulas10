import pandas as pd
import numpy as np

def price_50_directional(data: pd.DataFrame, ma_period: int = 50):
    if len(data) < ma_period:
        raise ValueError(f"Number of rows in DataFrame is lower than {ma_period}.")

    data['SMA_50'] = data['Close'].rolling(window=ma_period).mean()
    data['Cross'] = np.where(data['Close'] > data['SMA_50'], 1, -1)
    data['Cross'] = data['Cross'].diff()
    data['Directional_Count'] = 0
    active = False
    direction = 0
    count = 0

    for i in range(1, len(data)):
        if data.loc[i, 'Cross'] != 0:
            direction = 1 if data.loc[i, 'Cross'] > 0 else -1
            active = True
            count = 1
        elif active and direction != 0:
            if (direction == 1 and data.loc[i, 'Close'] > data.loc[i, 'SMA_50']) or \
               (direction == -1 and data.loc[i, 'Close'] < data.loc[i, 'SMA_50']):
                count += 1
            else:
                active = False
        data.loc[i, 'Directional_Count'] = count if active else 0
    return data
