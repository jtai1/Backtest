import backtrader as bt

# This is the base class for all strategies
class baseStrategyAbstract(bt.Strategy):
    """
       Define the abstract base class, which only requires user implementation of the run method
       Only need to implement the __init__ and next methods!
    """
    def __init__(self):
        pass

    def next(self):
        pass

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXECUTED, %.2f' % order.executed.price)
            elif order.issell():
                self.log('SELL EXECUTED, %.2f' % order.executed.price)

            self.log('Port Value:, %.2f' % self.broker.get_value())
            self.log('Cash Value:, %.2f' % self.broker.get_cash())

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        # Write down: no pending order
        self.order = None
