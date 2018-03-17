import backtrader as bt
import QuantLib.Strategies as strats
import QuantLib.Backtests as backtests
import QuantLib.Utils as utils

class bitcoinBacktest(backtests.backtestAbstract):
    def run(self, startdate, enddate):
        cerebro = bt.Cerebro()

        # Add a strategy
        cerebro.addstrategy(strats.bitcoinStrategy)

        # Add the data, trading and indicators
        cerebro.adddata(utils.backtestDatafeed().GetBbgData("ES1 Index", start_date=startdate, end_date=enddate),
                        name="SPX")

        # Set our desired cash start
        cerebro.broker.setcash(self.portcash)

        # Set slippage assumptions
        cerebro.broker.set_slippage_perc(self.slippage)

        # Set the commission - 0.1% ... divide by 100 to remove the %
        cerebro.broker.setcommission(commission=self.commission, leverage=2.0)

        # Add analyzers
        cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='mysharpe', riskfreerate=0.0)
        cerebro.addanalyzer(bt.analyzers.DrawDown, _name='mydrawdown')
        cerebro.addanalyzer(bt.analyzers.PeriodStats, _name='myperiodstats')
        cerebro.addanalyzer(bt.analyzers.Transactions, _name='mytransactions')
        cerebro.addanalyzer(bt.analyzers.TimeReturn, _name='mytimereturns')

        cerebro.addwriter(bt.WriterFile, csv=True, out="testExample.csv")

        # Print out the starting portfolio value
        print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

        # cerebro.addobserver(bt.observers.Value)

        # Add writer for output
        cerebro.addwriter(bt.WriterFile, csv=True)

        # Run the strategy
        results = cerebro.run()

        # Print out the results
        print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

        return dict([('cerebro', cerebro), ('results', results)])
