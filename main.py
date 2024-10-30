from trading_system import TradingSystem
from strategy import Strategy1
from data import get_data
from datetime import datetime
import pandas as pd


if __name__ == "__main__":

    # Get data, end_date defaults to today's date
    print('Fetching data')
    data : pd.DataFrame = get_data(start_date='2015-01-01')
    print('Data fetched')

    risk_target = 0.30 # Risky
    capital = 1000 # USD

    trading_system = TradingSystem(
        strategies=[
            #(Proportion of capital for strategy, Strategy Class)
            (1.0, Strategy1(data, risk_target=risk_target, capital=capital, num_stocks=100)),
        ]
    )

    trading_system.backtest()
    trading_system.graph()
    trading_system.metrics()
    trading_system.plot_pnl(save_path='pnl_plot.png', log_scale=True)

    '''
    # TODO: Define the TradingSystem class
    Some strategies can include trend following, indicators & AI (beware of overfitting)

    This class will have helper functions that assist in returning risk and PnL
    metrics as well as graphs to help simulate trading strategy


    #! Time Horizon
    Set up backtests until a successful Strategy is found
    Weigh risks of strategy

    Paper Trade on Alpaca for a few months

    Set up Systematic live trader
    '''
