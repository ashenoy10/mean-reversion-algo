import os
import yfinance as yf
import pandas as pd
import logging
from datetime import datetime, timedelta

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Constants
DATA_DIR = "/Users/ashenoy/git-repos/mean-reversion-algo/data/raw"  # Directory to save raw data
STOCKS_LIST = ["AAPL", "MSFT", "GOOG", "NVDA", "AMZN"]  # List of tech stocks
START_DATE = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")  # 1 year back
END_DATE = datetime.now().strftime("%Y-%m-%d")

def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch historical stock data using yfinance.
    
    Args:
        ticker (str): Stock ticker symbol.
        start_date (str): Start date for historical data (YYYY-MM-DD).
        end_date (str): End date for historical data (YYYY-MM-DD).
    
    Returns:
        DataFrame: Stock data.
    """
    logging.info(f"Fetching data for {ticker} from {start_date} to {end_date}")
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        if stock_data.empty:
            logging.warning(f"No data found for {ticker}.")
            return None
        stock_data.reset_index(inplace=True)
        stock_data["Ticker"] = ticker  # Add ticker column
        return stock_data
    except Exception as e:
        logging.error(f"Error fetching data for {ticker}: {e}")
        return None

def save_to_csv(data, filename):
    """
    Save DataFrame to a CSV file.
    
    Args:
        data (DataFrame): Data to save.
        filename (str): Filename to save the data.
    """
    try:
        os.makedirs(DATA_DIR, exist_ok=True)  # Create directory if not exists
        file_path = os.path.join(DATA_DIR, filename)
        data.to_csv(file_path, index=False)
        logging.info(f"Data saved to {file_path}")
    except Exception as e:
        logging.error(f"Error saving data to {filename}: {e}")

def main():
    """
    Main pipeline to fetch and save stock data.
    """
    all_data = []
    for ticker in STOCKS_LIST:
        stock_data = fetch_stock_data(ticker, START_DATE, END_DATE)
        if stock_data is not None:
            all_data.append(stock_data)
    
    # Combine all data and save
    if all_data:
        combined_data = pd.concat(all_data)
        save_to_csv(combined_data, "tech_stocks_data.csv")
    else:
        logging.error("No data fetched. Exiting pipeline.")

if __name__ == "__main__":
    main()
