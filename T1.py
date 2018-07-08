#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 17:06:49 2018

@author: rodolfo
"""
import numpy as np
import pandas as pd

def t1(close,tEvents):
    t1=close.index.searchsorted(tEvents+pd.Timedelta(days=1))
    t1=t1[t1<close.shape[0]]
    t1=pd.Series(close.index[t1],index=tEvents[:t1.shape[0]]) # NaNs at end
    return t1