import pandas as pd
def BollingerBands(dataset:pd.DataFrame, column_name='Close', window=20, num_std_dev=2):
    """
    Calculate Bollinger Band distance and Bollinger Band ratio for each row in the Dataset.

    Parameters:
    - dataset (Dataset): Dataset object containing price data.
    - column_name (str): Name of the column to use for Bollinger Band calculation.
    - window (int): Moving average window size.
    - num_std_dev (int): Number of standard deviations for Bollinger Bands.

    Returns:
    - Dataset: Dataset object with appended columns for Bollinger Band distance and ratio.
    """
    if column_name not in dataset.columns:
        raise ValueError(f"Column '{column_name}' not found in the dataset")

    # Calculate the rolling mean and standard deviation
    rolling_mean = dataset[column_name].rolling(window=window).mean()
    rolling_std = dataset[column_name].rolling(window=window).std()

    # Calculate upper and lower Bollinger Bands
    upper_band = rolling_mean + (rolling_std * num_std_dev)
    lower_band = rolling_mean - (rolling_std * num_std_dev)

    # Calculate Bollinger Band distance
    dataset['Bollinger_Band_Distance'] = (upper_band - lower_band) * 1000

    # Calculate Bollinger Band ratio for each row
    def calculate_ratio(row):
        price = row[column_name]
        upper_distance = row[column_name + '_upper_dist']
        lower_distance = row[column_name + '_lower_dist']

        if upper_distance == 0:
            return float('inf')  # Handle division by zero

        ratio1 = abs(price - upper_distance) / upper_distance
        ratio2 = abs(price - lower_distance) / lower_distance

        return max(ratio1, ratio2)

    # Calculate upper and lower Bollinger Band distances
    dataset[column_name + '_upper_dist'] = dataset[column_name] - upper_band
    dataset[column_name + '_lower_dist'] = lower_band - dataset[column_name]

    # Apply the ratio calculation function row-wise
    dataset['BollingerBandRatio'] = dataset.apply(calculate_ratio, axis=1)

    return dataset
