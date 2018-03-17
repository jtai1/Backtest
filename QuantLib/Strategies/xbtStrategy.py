# Import the backtrader platform
import backtrader.indicators as btind
import backtrader as bt
import QuantLib.Strategies as strats

# Create a Strategy
class bitcoinStrategy(strats.baseStrategyAbstract):
    params = (
        ('STMAperiod', 5),
        ('LTMAperiod', 10),
    )

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close

        # To keep track of pending orders
        self.order = None

        smaFast = btind.MovingAverageSimple(period=self.params.STMAperiod)
        smaSlow = btind.MovingAverageSimple(period=self.params.LTMAperiod)

        self.buysig = btind.CrossOver(smaFast, smaSlow)

    def next(self):
        # Simply log the closing price of the series from the reference
        self.log('Close, %.2f' % self.dataclose[0])

        if self.position.size:
            if self.buysig < 0:
                self.sell()
        elif self.buysig > 0:
            self.buy()