#
# Google stock price 
#

import numpy as np
import pandas as pd
import pylab as pl
from pandas_datareader import data as web  

goog=web.DataReader('AAPL',data_source='google',start='3/14/2009',end='4/14/2014')

goog['Log_Ret'] = np.log(goog['Close']/goog['Close'].shift(1))
goog['Vol']= pd.rolling_std(goog['Log_Ret'], window=252) * np.sqrt(252)

pl.plot(goog[['Close','Vol']])
pl.show()

