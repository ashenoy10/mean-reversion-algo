# mean-reversion-algo

mean-reversion-algo/
│
├── data/                  # For raw and processed data
│   ├── raw/               # Raw CSV/JSON data from APIs
│   ├── processed/         # Cleaned and feature-engineered datasets
│   └── stocks_list.json   # List of selected tech stocks
│
├── notebooks/             # Jupyter notebooks for exploration and prototyping
│   └── data_exploration.ipynb
│
├── scripts/               # Standalone scripts for running tasks
│   ├── data_pipeline.py   # Collects, cleans, and stores data
│   ├── backtest.py        # Runs backtests on strategies
│   ├── trade_executor.py  # Executes live trades using API
│   └── monitor.py         # Monitors live strategy performance
│
├── src/                   # Source code for the project
│   ├── data/              # Data-related modules
│   │   ├── fetch.py       # Fetch stock data from APIs
│   │   ├── clean.py       # Data cleaning and transformation
│   │   └── store.py       # Save and load data (e.g., to/from database)
│   │
│   ├── strategy/          # Strategy-related modules
│   │   ├── indicators.py  # Compute Bollinger Bands, RSI, Z-scores, etc.
│   │   └── strategy.py    # Define the mean-reversion trading strategy
│   │
│   ├── execution/         # Trade execution and risk management
│   │   ├── broker_api.py  # Interact with broker's API (e.g., Alpaca)
│   │   └── risk.py        # Risk management functions
│   │
│   ├── utils/             # Utility functions and helpers
│   │   ├── config.py      # Configuration for API keys, paths, etc.
│   │   └── logging.py     # Set up logging for the project
│   │
│   └── __init__.py        # Makes `src` a package
│
├── tests/                 # Unit and integration tests
│   ├── test_fetch.py      # Tests for data fetching
│   ├── test_strategy.py   # Tests for strategy logic
│   └── test_execution.py  # Tests for trade execution
│
├── dashboard/             # Dashboard to visualize performance
│   ├── app.py             # Main dashboard app (e.g., Streamlit or Flask)
│   └── templates/         # HTML templates (if needed)
│
├── .gitignore             # Ignore unnecessary files (e.g., API keys, data files)
├── requirements.txt       # List of Python dependencies
├── README.md              # Project overview and setup instructions
└── LICENSE                # License for the project (optional)
