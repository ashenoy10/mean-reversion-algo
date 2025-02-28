import pandas as pd

def calculate_bollinger_bands(data, window=20, num_std_dev=2):
    """
    Calculate Bollinger Bands for a given data series.
    
    Args:
        data (DataFrame): Stock data with a 'Close' column.
        window (int): Rolling window for the moving average.
        num_std_dev (int): Number of standard deviations for the bands.
    
    Returns:
        DataFrame: Data with added Bollinger Bands.
    """
    data["MA"] = data["Close"].rolling(window=window).mean()
    data["STD"] = data["Close"].rolling(window=window).std()
    data["Upper_Band"] = data["MA"] + (num_std_dev * data["STD"])
    data["Lower_Band"] = data["MA"] - (num_std_dev * data["STD"])
    return data

def calculate_z_score(data, window=20):
    """
    Calculate Z-score for the 'Close' price.
    
    Args:
        data (DataFrame): Stock data with a 'Close' column.
        window (int): Rolling window for the mean and std deviation.
    
    Returns:
        Series: Z-scores of the closing prices.
    """
    rolling_mean = data["Close"].rolling(window=window).mean()
    rolling_std = data["Close"].rolling(window=window).std()
    z_scores = (data["Close"] - rolling_mean) / rolling_std
    return z_scores
