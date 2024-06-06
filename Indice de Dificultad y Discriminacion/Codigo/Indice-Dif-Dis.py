# -*- coding: utf-8 -*-
"""
Created on Fri May 31 15:38:59 2024

@author: USER
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import ceil
alumnos = pd.read_csv("EP1.csv")
# list(enumerate(nomcol))
nomcol = alumnos.columns
#nomcol

indices = [i for i , s in enumerate(nomcol) if 'item' in s]

#obteniendo el puntaje 
puntaje = []
for i in indices:
    valor = int(alumnos[nomcol[i]].name[-8])+int(alumnos[nomcol[i]].name[-6])/10
    puntaje.append(valor)

#puntaje

n = len(indices)
alumnos["Total Score"] = alumnos["Total Score"].replace(",",".",regex = True).astype(float)
order = alumnos.sort_values('Total Score',ascending=False)
order = order.reset_index(drop=True)

order=order.iloc[0:(len(order)-(order['Total Score'].isnull().sum())),:] # elimina a los alumnos que no dieron el examen 


suma=[]
for j in range(n):
    valor = order.iloc[:,indices[j]]
    valorNumero = valor.replace(',', '.',regex=True).astype(float).sum()
    suma.append(valorNumero)


######### indice de dificultad #######
Ind_dif=[]
for j in range(n):
    valor=1-(suma[j]/(puntaje[j]*len(order)))
    Ind_dif.append(valor)
#print(Ind_dif)

############ Separamos grupos superior y inferior ###########

q1=round(0.27*(len(order)))
q2=len(order)-q1
#print(q1)
#print(q2)
num_Gs=len(order[0:q1])
num_Gi=len(order[(q2):(len(order))])
#print(num_Gs)
#print(num_Gi)

Grupo1=order[0:q1];Grupo2=order[q2:(len(order))]
#Grupo1
#Grupo2
###########################################
Cs=[]
for j in range(n):
    valor = Grupo1.iloc[:,indices[j]].replace(',', '.',regex=True).astype(float).sum()
    Cs.append(valor)
#print(Cs)

Ci=[]
for j in range(n):
    valor = Grupo2.iloc[:,indices[j]].replace(',', '.',regex=True).astype(float).sum()
    Ci.append(valor)
#print(Ci)
#################indice de discriminación################
Ind_dis=[]
for j in range(n):
    valor=(Cs[j]/(puntaje[j]*num_Gs))-(Ci[j]/(puntaje[j]*num_Gi))
    Ind_dis.append(valor)
#print(Ind_dis)

pregunta=[]
for i in indices:
    valor='P' + ' ' + alumnos[nomcol[i]].name[0]+ alumnos[nomcol[i]].name[10]+alumnos[nomcol[i]].name[11]
    valor = valor.replace(" ","")
    pregunta.append(valor)

#pregunta

mapeado=range(len(pregunta))

plt.plot(Ind_dif,marker="*",linestyle='--',label = "Indice de dificultad")
#plt.xticks(rotation=60 )
plt.xticks(mapeado, pregunta)
plt.plot(Ind_dis,color='red',linestyle='--' ,marker="*",label = "Indice de discriminación")
plt.yticks(np.arange(0, 1.1, step=0.1))
plt.title("INDICES")
plt.legend(loc="best")##https://matplotlib.org/3.1.1/api/legend_api.html
plt.xlabel("Preguntas")
plt.ylabel("Indices") 
plt.grid(color='black', linestyle='-', linewidth=0.1)
plt.show()