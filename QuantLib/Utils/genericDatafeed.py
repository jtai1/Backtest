#########################################
#
#  Generic Data Feed
#
#  Initial: Feb 28 2018
#  Author: Jim Tai
#
#########################################

import pdblp

class bbgDataWrapper():
    def __init__(self):
        self.con = pdblp.BCon(debug=False, port=8194)
        pass

    def getBloombergData(self, ticker, fields, start_date, end_date):
        self.con.start()
        tmp_df = self.con.bdh(ticker, fields, start_date, end_date)
        self.con.stop()

        return tmp_df