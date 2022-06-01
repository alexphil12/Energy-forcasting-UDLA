# -*- coding: utf-8 -*-
"""
Created on Wed May 25 16:01:08 2022

@author: alexa
"""
import pandas as pd
import numpy as np
import datetime
from utils_data import trace_data,extractl,trace_histo_longueur_donnee
from numpy.fft import fft,ifft
import matplotlib.pyplot as plt
import statistics 
l_P0_cov=[];
l_ASC_cov=[];
l_P1_cov=[];
l_P2_cov=[];
l_P3_cov=[];
l_P4_cov=[];
l_P5_cov=[];
l_P6_cov=[];
l_S1_cov=[];
l_S2_cov=[];
l_S3_cov=[];
l_S4_cov=[];
l_S5_cov=[];
l_UPS1_cov=[];
l_UPS2_cov=[];
l_UPS3_cov=[];
l_CUB1_cov=[];
l_CUB2_cov=[];
l_CUB_cov=[];
l_bombas_cov=[];
l_data_center_cov=[];
mesure=["Fecha","Hora"];
  
start = datetime.datetime.strptime("22-07-2015", "%d-%m-%Y")
end = datetime.datetime.strptime("31-12-2021", "%d-%m-%Y")
dates = list(pd.date_range(start, end).strftime("%d-%m-%Y"))
N=len(dates)

index_fin=24*30*N;#number of mesure in the data set(1990 days between 22-07-2015 and 31-12-2020 24 hours a day and 30 mesure in one hour)
tab_array_P1=np.empty((index_fin,29))
tab_array_P1[:]= np.nan

tab_array_P2=np.empty((index_fin,29))
tab_array_P2[:]= np.nan

dates_fin=[];
hour=[]
for i in range(24):
    for j in range(0,60,2):
        if j<10:
            hour.append(str(i) +":"+"0"+str(j))
        else:
           hour.append(str(i) +":"+str(j)) 
hour_final=hour*N   

#creation of the "date" datas
for i in range(len(dates)):
    dates_fin=dates_fin + 24*30*[dates[i]]
    
#creation of the litteral index by concatenating date and hour     
index_lit=[]
for j in range(24*30*N):
    index_lit.append(dates_fin[j] +"-"+ hour_final[j])


#creation of the columns names
mesure.append("Voltaje_(R)_[v]")	
mesure.append("Voltaje_(S)_[v]")	
mesure.append("Voltaje_(T)_[v]")	
mesure.append("Voltaje_(RS)_[v]")	
mesure.append("Voltaje_(ST)_[v]")	
mesure.append("Voltaje_(TR)_[V]")	
mesure.append("Corriente_R_[A]")	
mesure.append("Corriente_S_[A]")	
mesure.append("Corriente_T_[A]")	
mesure.append("Potencia_R_[VA]")	
mesure.append("Potencia_S_[VA]")	
mesure.append("Potencia_T_[VA]")	
mesure.append("Potencia_R_[W]")	
mesure.append("Potencia_S_[W]")	
mesure.append("Potencia_T_[W]")	
mesure.append("Potencia_R_[VAR]")	
mesure.append("Potencia_S_[VAR]")	
mesure.append("Potencia_T_[VAR]")	
mesure.append("Corriente_N_[A]")	
mesure.append("Frecuencia_[Hz]")	
mesure.append("not_sure_1")	
mesure.append("not_sure_2")	
mesure.append("not_sure_3")	
mesure.append("Potencia_3F_[KVA]")	
mesure.append("Potencia_3F_[W]")	
mesure.append("Potencia_3F_[VAR]")	
mesure.append("Factor de Potencia")


#%%

Nom1="C:/Users/alexa/OneDrive/Documents/Code en tout genre/Python Scripts/df_continu/df_cov_continu_1_";
Nom2="C:/Users/alexa/OneDrive/Documents/Code en tout genre/Python Scripts/df_continu/df_cov_continu_2_";
continu_mois_p1=[]
continu_mois_p2=[]
for i in range(29):
    h=list(Nom1)
    h.append(str(i))
    h.append(".txt")
    h="".join(h)
    continu_mois_p1.append(pd.read_csv(h,sep=",",header=0,names=mesure))
for j in range(30):
    h=list(Nom2)
    h.append(str(i))
    h.append(".txt")
    h="".join(h)
    continu_mois_p2.append(pd.read_csv(h,sep=",",header=0,names=mesure))
    
    
df_p1=pd.read_csv("C:/Users/alexa/OneDrive/Documents/Code en tout genre/Python Scripts/df_entier_année_mois/df_p1_full.txt",sep=",",header=0,names=mesure)
df_p1.insert(29,"index2",index_lit)       
df_p1.set_index("index2",inplace=True)
df_p2=pd.read_csv("C:/Users/alexa/OneDrive/Documents/Code en tout genre/Python Scripts/df_entier_année_mois/df_p2_full.txt",sep=",",header=0,names=mesure)    
df_p2.insert(29,"index2",index_lit)       
df_p2.set_index("index2",inplace=True)
L_annee_P1=[]
L_mois_P1=[]
start1 = datetime.datetime.strptime("07-2015", "%m-%Y")
end1=datetime.datetime.strptime("01-2022", "%m-%Y")
mois = list(pd.date_range(start1,end1,freq='M').strftime("%m-%Y"))
annee=["2015","2016","2017","2018","2019","2020","2021"]
booll=[]
for j in range(len(mois)):
    L_mois_P1.append(pd.read_csv("C:/Users/alexa/OneDrive/Documents/Code en tout genre/Python Scripts/df_entier_année_mois/df_p1-"+mois[j]+".txt",sep=",",header=0,names=mesure))
    f=str(len(mois)-j)
    print("dataset-suivants1-mois"+" "+f)
for j in range(len(annee)):
    L_annee_P1.append(pd.read_csv("C:/Users/alexa/OneDrive/Documents/Code en tout genre/Python Scripts/df_entier_année_mois/df_p1-"+annee[j]+".txt",sep=",",header=0,names=mesure))
    f=str(len(annee)-j)
    print("dataset-suivants1-année"+" "+f)    
L_annee_P2=[]
L_mois_P2=[]
booll=[]
for j in range(len(mois)): 
    L_mois_P2.append(pd.read_csv("C:/Users/alexa/OneDrive/Documents/Code en tout genre/Python Scripts/df_entier_année_mois/df_p2-"+mois[j]+".txt",sep=",",header=0,names=mesure))
    f=str(len(mois)-j)
    print("dataset-suivants2-mois"+" "+f)    
for j in range(len(annee)):
    L_annee_P2.append(pd.read_csv("C:/Users/alexa/OneDrive/Documents/Code en tout genre/Python Scripts/df_entier_année_mois/df_p2-"+annee[j]+".txt",sep=",",header=0,names=mesure))
    f=str(len(annee)-j)
    print("dataset-suivants2-année"+" "+f)        
print("Dataframe of month and years written")
#%%
names=["ASC","P0","P1","P2","P3","P4","P5","P6","TDP-S1","TDP-S2","TDP-S3","TDP-S4","TDP-S5","UPS1","UPS2","UPS3","CUB1","CUB2","TV-CUB","Bombas","Data-center"]
l_cov=[]
cols=cols=mesure[2:29]
for j in range(len(names)):
    l_cov.append(pd.read_csv("C:/Users/alexa/OneDrive/Documents/Code en tout genre/Python Scripts/df_cov_(2019-2021)/df_cov-"+names[j]+".txt",sep=",",header=0,names=mesure))
    l_cov[j][cols]=l_cov[j][cols].replace(',','.',regex=True).astype(float)
    f=str(len(names)-j)
    print("dataset-suivants-cov"+" "+f)  
l_ASC_cov=l_cov[0]
l_P0_cov=l_cov[1]
l_P1_cov=l_cov[2]
l_P2_cov=l_cov[3]
l_P3_cov=l_cov[4]
l_P4_cov=l_cov[5]
l_P5_cov=l_cov[6]
l_P6_cov=l_cov[7]
l_S1_cov=l_cov[8]
l_S2_cov=l_cov[9]
l_S3_cov=l_cov[10]
l_S4_cov=l_cov[11]
l_S5_cov=l_cov[12]
l_UPS1_cov=l_cov[13]
l_UPS2_cov=l_cov[14]
l_UPS3_cov=l_cov[15]
l_CUB1_cov=l_cov[16]
l_CUB2_cov=l_cov[17]
l_CUB_cov=l_cov[18]
l_bombas_cov=l_cov[19]
l_data_center_cov=l_cov[20]
del l_cov
#%%
dates=["30-12-2016-0:00","31-12-2016-23:58"]
trace_data(dates,df_p1,"M19")
trace_histo_longueur_donnee(df_p1,100,dates,"M20")
#%%
df_fourrier=continu_mois_p1[12]
N=len(df_fourrier.index)
nu=np.linspace(0,30,N)
for j in range(len(mesure)-2):
    inter=list(df_fourrier[mesure[j+2]])
    # mean=statistics.mean(inter)
    # inter=[i-mean for i in inter]
    spectre=np.abs(np.fft.fft(inter))
    spectre=20*np.log10(spectre/(max(spectre)))
    plt.plot(range(len(inter)),inter)
    plt.title("Time representation of"+" "+mesure[j+2])
    plt.xlabel("sample")
    plt.ylabel("Ampl")
    plt.show()
    plt.plot(nu,spectre)
    plt.title("Spectrum of"+" "+mesure[j+2])
    plt.xlabel("freq event/hours")
    plt.ylabel("Ampl")
    plt.show()
    
    
    
    
    
    
    