#########################################
#
#  Bloomberg Data Feed
#
#  Initial: Feb 28 2018
#  Author: Jim Tai
#
#########################################

import backtrader.feeds as bt
import QuantLib.Utils.genericDatafeed as gdf

class backtestDatafeed():
    def __init__(self):
        pass

    def GetBbgData(self, ticker, start_date, end_date):
        tmp_df = gdf.bbgDataWrapper().getBloombergData(ticker=ticker, fields=['PX_OPEN', 'PX_HIGH', 'PX_LOW', 'PX_LAST'],
                                                       start_date=start_date, end_date=end_date)
        tmp_df.columns = ['OPEN', 'HIGH', 'LOW', 'CLOSE']

        return bt.PandasData(dataname=tmp_df)

    def GetBbgClose(self, ticker, start_date, end_date):
        tmp_df = gdf.bbgDataWrapper().getBloombergData(ticker=ticker, fields=['PX_LAST'],
                                                       start_date=start_date, end_date=end_date)
        tmp_df.columns = ['CLOSE']

        return bt.PandasData(dataname=tmp_df)
