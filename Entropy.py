import numpy as np
import pandas as pd

def entropy(close):
    dif = close.diff()
    dif['01'] = (dif['Adj Close'] > 0).astype(int)
    dif.drop(['Adj Close'], axis=1,inplace=True)
    dif = dif.reset_index()
    dif = dif['01'].values
    w = 252 # No de días de operación anual del stock market
    l = len(dif)
    matrix = [[0 for x in range(w)] for y in range(l)]
    i = 251
    j = 0
    while i < len(dif):
        matrix[i]=(dif[j:i])
        j +=1
        i +=1
    matrix2 = [['0' for x in range(w)] for y in range(l)]
    i = 0
    while(i<len(dif)):
        str1 = ''.join(str(e) for e in matrix[i])
        matrix2[i]= str1
        i = i + 1
    h = []
    i = 0
    while(i<len(dif)):
        h.append(konto(matrix2[i][::-1]))
        i = i + 1
    entropy = pd.DataFrame(index= close.index)
    entropy['h']= h
    return entropy


def matchLength(msg,i,n):
    # Maximum matched length+1, with overlap.
    # i>=n & len(msg)>=i+n
    subS=''
    for l in range(n):
        msg1=msg[i:i+l+1]
        for j in range(i-n,i):
            msg0=msg[j:j+l+1]
            if msg1==msg0:
                subS=msg1
                break # search for higher l.
    return len(subS)+1,subS # matched length + 1

def konto(msg,window=None):
    '''
    * Kontoyiannis’ LZ entropy estimate, 2013 version (centered window).
    * Inverse of the avg length of the shortest non-redundant substring.
    * If non-redundant substrings are short, the text is highly entropic.
    * window==None for expanding window, in which case len(msg)%2==0
    * If the end of msg is more relevant, try konto(msg[::-1])
    '''
    out={'num':0,'sum':0,'subS':[]}
    if not isinstance(msg,str):msg=''.join(map(str,msg))
    if window is None:
        points=range(1,int(len(msg)/2+1))
    else:
        window=min(window,len(msg)/2)
        points=range(window,len(msg)-window+1)
    for i in points:
        if window is None:
            l,msg_=matchLength(msg,i,i)
            out['sum']+=np.log2(i+1)/l # to avoid Doeblin condition
        else:
            l,msg_=matchLength(msg,i,window)
            out['sum']+=np.log2(window+1)/l # to avoid Doeblin condition
        out['subS'].append(msg_)
        out['num']+=1
    out['h']=out['sum']/out['num']
    out['r']=1-out['h']/np.log2(len(msg)) # redundancy, 0<=r<=1
    return out['h']