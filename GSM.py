import numpy as np
import math
import pandas as pd

# model parameters
S0 = 100.0 # initial index level
T = 10.0 # time horizon
r = 0.05 # risk-less short rate
vol = 0.2 # instantaneous volatility
# simulation parameters
np.random.seed(250000)

gbm_dates = pd.DatetimeIndex(start='30-09-2004',
                             end='31-08-2015',
freq='B') M = len(gbm_dates) # time steps
dt = 1 / 252. # fixed for simplicity
df = math.exp(-r * dt) # discount factor
def simulate_gbm():
# stock price paths
rand = np.random.standard_normal((M, I)) # random numbers
S = np.zeros_like(rand) # stock matrix
S[0] = S0 # initial values
for t in range(1, M): # stock price paths
        S[t] = S[t - 1] * np.exp((r - vol ** 2 / 2) * dt
                        + vol * rand[t] * math.sqrt(dt))
    gbm = pd.DataFrame(S[:, 0], index=gbm_dates, columns=['index'])
    gbm['returns'] = np.log(gbm['index'] / gbm['index'].shift(1))
    # Realized Volatility (eg. as defined for variance swaps)
gbm['rea_var'] = 252 * np.cumsum(gbm['returns'] ** 2) / np.arange(len(gbm)) gbm['rea_vol'] = np.sqrt(gbm['rea_var'])
gbm = gbm.dropna()
return gbm

from gbm_helper import *
I = 1 # index level paths
gbm = simulate_gbm() print_statistics(gbm)