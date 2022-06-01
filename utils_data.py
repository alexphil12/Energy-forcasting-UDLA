# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:53:49 2022

@author: alexa
"""
import pandas as pd
import copy as cp
import numpy as np
import matplotlib.pyplot as plt
def extractl(X):
    H=list(X["Voltaje_(R)_[v]"])
    h1=pd.DataFrame(cp.deepcopy(X["Voltaje_(R)_[v]"]))
    N=len(H)
    ind=0;
    index_util=[]
    long_nan=[]
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
    k=0
    for k in range(0,len(index_util)-1,2):
        long.append(abs(index_util[k]-index_util[k+1]))
    if (long==[]):
        l=[]
        l.append(np.nan)
        l.append(np.nan)
        long.append(0)
        return(l)
    else:
        rang_max=long.index(max(long))
        h1["index1"]=h1.index
        h2=h1.reset_index(drop=True,inplace=True)
        l=[]
        l.append(h1.iloc[index_util[rang_max*2],1])
        l.append(h1.iloc[index_util[rang_max*2+1],1])
        return(l)
def verif_dataframe_mois(L):
    H=[]
    verif=2
    data=[]
    for k in range(len(L)):
        H.append(list(L[k]["Voltaje_(R)_[v]"]))
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
def trace_data(dates,dataframe,mesure):
    serie=dataframe.loc[dates[0]:dates[1],mesure]
    serie.plot(kind='line',visible=True)
    plt.show()
    return(1)
def trace_histo_longueur_donnee(X,nombre_intervalle,dates,mesure):
    H=list(X.loc[dates[0]:dates[1],mesure])
    h1=pd.DataFrame(cp.deepcopy(X[mesure]))
    N=len(H)
    ind=0;
    index_util=[]
    long_nan=[]
    long=[]
    is_nan=[]
    for j in range(N):
        is_nan.append(pd.isna(H[j]))
        if pd.isna(H[j])==False and ind==0:
            index_util.append(j)
            ind=1;
        elif pd.isna(H[j])==True and ind==1:
            index_util.append(j-1)
            ind=0
    index_util.append(N-1)
    long_nan.append(index_util[0])
    
    for j in range(N):
        if is_nan[j]==True:
            is_nan[j]=0
        else:
            is_nan[j]=1
    for j in range(0,len(index_util)-1,2):
        long.append(abs(index_util[j]-index_util[j+1]))
    for j in range(0,len(index_util)-2,2):
        long_nan.append(abs(index_util[j+1]-index_util[j+2]))
    plt.hist(long, range = (0, max(long)), bins = np.linspace(0,max(long),nombre_intervalle), color = 'blue',edgecolor = 'black')
    plt.xlabel('length of the interval')
    plt.ylabel('occurency')
    plt.title("Histogram continues data")
    plt.show()
    plt.hist(long_nan, range = (0, max(long_nan)), bins = np.linspace(0,max(long_nan),nombre_intervalle), color = 'blue',edgecolor = 'black')
    plt.xlabel('length of the NaN')
    plt.ylabel('occurency')
    plt.title("Histogram continues NaN")
    plt.show()
    # plot
    index3=list(h1.index)
    h1=index3.index(dates[0])
    h2=index3.index(dates[1])
    plt.scatter(range(len(is_nan)),is_nan,c="blue",s=0.1)
    plt.xlabel("parcour du dataframe")
    plt.ylabel("nan ou non")
    plt.show()
    return(0)
        
    