import backtrader as bt

class MeanReversionStrategy(bt.Strategy):
    params = (("window", 20), ("num_std_dev", 2))

    def __init__(self):
        self.ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.window)
        self.std = bt.indicators.StandardDeviation(self.data.close, period=self.params.window)
        self.upper_band = self.ma + (self.params.num_std_dev * self.std)
        self.lower_band = self.ma - (self.params.num_std_dev * self.std)

    def next(self):
        if self.data.close[0] < self.lower_band[0]:  # Buy signal
            self.buy()
        elif self.data.close[0] > self.upper_band[0]:  # Sell signal
            self.sell()

# Backtesting setup
def run_backtest(data_file):
    cerebro = bt.Cerebro()
    data = bt.feeds.GenericCSVData(
        dataname=data_file,
        dtformat="%Y-%m-%d",
        timeframe=bt.TimeFrame.Days,
        compression=1,
        openinterest=-1
    )
    cerebro.adddata(data)
    cerebro.addstrategy(MeanReversionStrategy)
    cerebro.run()
    cerebro.plot()

if __name__ == "__main__":
    run_backtest("../data/raw/tech_stocks_data.csv")
