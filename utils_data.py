# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:53:49 2022

@author: alexa
"""
import pandas as pd
import copy as cp
import numpy as np
def extractl(X):
    H=list(X["M1"])
    h1=pd.DataFrame(cp.deepcopy(X["M1"]))
    N=len(H)
    ind=0;
    index_util=[]
    long=[]
    for j in range(N):
        if pd.isna(H[j])==False and ind==0:
            index_util.append(j)
            ind=1;
        elif pd.isna(H[j])==True and ind==1:
            index_util.append(j-1)
            ind=0
    if len(index_util)%2==1:
            index_util.append(N-1)
    for j in range(0,len(index_util),2):
        long.append(abs(index_util[j]-index_util[j+1]))
    if long==[]:
        l=[]
        l.append(np.nan)
        l.append(np.nan)
        return(l)
    else:
        rang_max=long.index(max(long))
        h1["index1"]=h1.index
        h2=h1.reset_index(drop=True,inplace=True)
        l=[]
        l.append(h1.iloc[index_util[rang_max*2],1])
        l.append(h1.iloc[index_util[rang_max*2+1],1])
        return(l)
def verif_dataframe_mois(L,mois):
    H=[]
    verif=2
    data=[]
    for k in range(len(L)):
        H.append(list(L[k]["M1"]))
    for k in range(len(H)):
        verif=2
        for i in range(len(H[k])):
            if pd.isna(H[k][i])==True and verif!=1:
                verif=0
            if pd.isna(H[k][i])==False and verif==0:
                verif=1
        data.append(verif)
        verif=2
    return(data)     
    
    