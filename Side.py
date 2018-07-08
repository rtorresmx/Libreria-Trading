#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 16:48:48 2018

@author: rodolfo
"""
import numpy as np
import pandas as pd
from sklearn import mixture as mix
#  ----------------------------------------------------------------------------
def side(close,trgt):
    df = close[['Open','High','Low','Adj Close']]
    df['open']=df['Open'].shift(1)
    df['high']=df['High'].shift(1)
    df['low']=df['Low'].shift(1)
    df['close']=df['Adj Close'].shift(1)
    df = df[['open','high','low','close']]
    df = df.dropna()
    unsup = mix.GaussianMixture(n_components=3,
                                covariance_type="spherical",
                                n_init=100,
                                random_state=42)
    unsup.fit(np.reshape(df,(-1,df.shape[1])))
    regime = unsup.predict(np.reshape(df,(-1,df.shape[1])))
    df["Return"]=np.log(df['close']/df['close'].shift(1))
#    Regimes = pd.DataFrame(regime,columns=['Regime'],index=df.index)\
#    .join(df,how='inner')\
#    .assign(market_cu_return=df.Return.cumsum())\
#    .reset_index(drop=False)\
#    .rename(columns={'index':'Date'})
    #trgt = trgt[1:]
    #side = pd.DataFrame(regime, index=trgt[1:].index)
    side = pd.Series(regime, index=trgt[1:].index)
#    side = trgt.copy(deep=True)
#    i = 0
#    while i < side.shape[0]:
#        side.iloc[i]= regime[i]
#        i = i+1
    return side