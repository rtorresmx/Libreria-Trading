#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 14:03:52 2018

@author: Mr.Yellow
"""

import numpy as np
import pandas as pd
from DataAnalysis import DailyVolatility
from DataAnalysis import CusumFilter
from DataAnalysis import Side
from DataAnalysis import T1
from DataAnalysis import SampleWeights
from DataAnalysis import BetSizing
close = pd.read_csv('/home/rodolfo/Downloads/BA-master.csv',
	parse_dates=[['Date', 'Timestamp']], index_col='Date_Timestamp')
close.drop(['OpenPrice','HighPrice','LowPrice','TotalVolume',
          'TotalQuantity','TotalTradeCount','Ticker'], axis =1, inplace=True)
span0 = 420
dfv = DailyVolatility.getDailyVol(close,span0)
h = dfv['ClosePrice'].std()/100
#h=.0001
tEvents = CusumFilter.getTEventsCusum(dfv,h=h)
trgt = pd.Series()
trgt= close['ClosePrice']/close['ClosePrice'].iloc[0]
side = Side.side(close, trgt)
t1 = T1.t1(dfv,tEvents)
pstl=[1,1] # A list of two non-negative values that sets the width of the two barriers
minRet = .05 #The minimum target return required for running a triple barrier search
numThreads = 2 # The number of threads concurrently used by the function
#dfs = close['Adj Close']
##dfout = Metalabelling.testMetalabel(close=dfs,tEvents=tEvents,trgt=trgt,
##                                    pstl=pstl,minRet=minRet,
##                                    numThreads=numThreads,t1=t1,side=side)
#dfout,events = SampleWeights.SampleWeights(close=dfs,tEvents=tEvents,trgt=trgt,pstl=pstl,minRet=minRet,
#                                  numThreads=numThreads,t1=t1,side=side)
#dfout.drop('ret',axis=1,inplace=True)
#'''
#El segmento de código que sigue a continuación,
#se incluye sólo para ejecutar el algoritmo.
#En la implementación en el pipeline los datos de predicción y
#de probabilidad provienen del machine learning
#secundario
#'''
#p=[]
#i=0
#while i < events.shape[0]:
#    p.append(np.random.random())
#    i +=1
#prob= pd.Series(p, index=events.index)
#i=0
#pr=[]
#while i < events.shape[0]:
#    r = np.random.randint(0,2)
#    if r == 0:
#        r = -1
#    pr.append(r)
#    i = i+1
#pred = pd.Series(pr, index= events.index)
#
#'''
#Termina segmento de código
#'''
#
#stepSize = .01
#numClasses = 2
#numThreads = 16
#m = BetSizing.getSignal(events=events,stepSize=stepSize,prob=prob,pred=pred,
#                        numClasses=numClasses,numThreads=numThreads)