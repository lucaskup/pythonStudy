#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:11:14 2017

@author: lucas
"""

import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import Imputer

from sklearn.model_selection import train_test_split

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout

import math
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

import matplotlib.pyplot as plt

import random


def read_dataset(filename):
    return pd.read_table(filepath_or_buffer=filename,
                        delim_whitespace = True,
                        skiprows = 4).iloc[:, -1]
# Importing the Blue dataset
dataset_blue = read_dataset("Orto_Canon_Mod_Blue.txt")


# Importing the Green dataset
dataset_green = read_dataset("Orto_Canon_Mod_Green.txt")

# Importing the NIR dataset
dataset_nir = read_dataset("Orto_Canon_Mod_NIR.txt")


# Importing the Sequoia Green dataset
dataset_sgreen = read_dataset("Sequoia_Green.txt")

# Importing the Sequoia NIR dataset
dataset_snir = read_dataset("Sequoia_NIR.txt")

# Importing the Sequoia Red Edge dataset
dataset_sredge = read_dataset("Sequoia_Red_Edge.txt")

# Importing the Sequoia Red Dataset
dataset_sred = read_dataset("Sequoia_Red.txt")


#Concatenates Dataframes to get X and Y
complete_set = pd.concat([dataset_blue,
                    dataset_green,
                    dataset_nir,
                    dataset_sgreen,
                    dataset_snir,
                    dataset_sredge,
                    dataset_sred],
                axis=1,
                ignore_index=True)


complete_set = complete_set.iloc[:,:].values

#complete_set = np.nan_to_num(complete_set)

#[(np.mean(complete_set[:,12]),np.std(complete_set[:,12])),
# (np.mean(complete_set[:,13]),np.std(complete_set[:,13])),
# (np.mean(complete_set[:,14]),np.std(complete_set[:,14]))]


#sc2 = MinMaxScaler()
#sc2.fit(complete_set)


set_navolta = np.roll(complete_set[:,0],1)
set_navolta = np.c_[ np.roll(complete_set[:,0],-1), set_navolta ]
set_navolta = np.c_[ np.roll(complete_set[:,0],2132), set_navolta ]
set_navolta = np.c_[ np.roll(complete_set[:,0],-2132), set_navolta ]


set_navolta = np.c_[ np.roll(complete_set[:,1],1), set_navolta ]
set_navolta = np.c_[ np.roll(complete_set[:,1],-1), set_navolta ]
set_navolta = np.c_[ np.roll(complete_set[:,1],2132), set_navolta ]
set_navolta = np.c_[ np.roll(complete_set[:,1],-2132), set_navolta ]

set_navolta = np.c_[ np.roll(complete_set[:,2],1), set_navolta ]
set_navolta = np.c_[ np.roll(complete_set[:,2],-1), set_navolta ]
set_navolta = np.c_[ np.roll(complete_set[:,2],2132), set_navolta ]
set_navolta = np.c_[ np.roll(complete_set[:,2],-2132), set_navolta ]

complete_set = np.c_[ set_navolta, complete_set ]
set_navolta = None

complete_set = complete_set[np.logical_not(np.isnan(complete_set[:,12]))]
complete_set = complete_set[np.logical_not(np.isnan(complete_set[:,13]))]
complete_set = complete_set[np.logical_not(np.isnan(complete_set[:,14]))]


complete_set = complete_set[
    np.logical_not(np.logical_and(
        np.logical_and(complete_set[:,12] == 255, 
                       np.logical_and(complete_set[:,13] == 255, complete_set[:,14] == 255)),
        np.logical_and(np.logical_and(complete_set[:,15] == 255, complete_set[:,16] == 255),
                       np.logical_and(complete_set[:,17] == 255, complete_set[:,18] == 255))
    ))
]



# Taking care of missing data

imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(complete_set)
complete_set = imputer.transform(complete_set)

# Feature Scaling

#sc = MinMaxScaler()

complete_set[:,0] = complete_set[:,0]
complete_set[:,1] = complete_set[:,1]
complete_set[:,2] = complete_set[:,2]
complete_set[:,3] = complete_set[:,3]

complete_set[:,4] = complete_set[:,4]
complete_set[:,5] = complete_set[:,5]
complete_set[:,6] = complete_set[:,6]
complete_set[:,7] = complete_set[:,7]

complete_set[:,8] = complete_set[:,8]
complete_set[:,9] = complete_set[:,9]
complete_set[:,10] = complete_set[:,10]
complete_set[:,11] = complete_set[:,11]

complete_set = complete_set/255
#complete_set = sc.fit_transform(complete_set)

X = complete_set[:,0:15]
Y = complete_set[:,15:]




# Splitting the dataset into the Training set and Test set

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2)


# Importing the Keras libraries and packages


# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 16, kernel_initializer = 'normal', activation = 'sigmoid', input_dim = 15))

# Adding the output layer
classifier.add(Dense(units = 277, kernel_initializer = 'normal', activation = 'sigmoid'))

classifier.add(Dense(units = 277, kernel_initializer = 'normal', activation = 'sigmoid'))

#classifier.add(Dense(units = 81, kernel_initializer = 'uniform', activation = 'sigmoid'))
#classifier.add(Dense(units = 81, kernel_initializer = 'uniform', activation = 'relu'))
#classifier.add(Dense(units = 81, kernel_initializer = 'uniform', activation = 'sigmoid'))
#classifier.add(Dense(units = 81, kernel_initializer = 'uniform', activation = 'relu'))
#classifier.add(Dense(units = 81, kernel_initializer = 'uniform', activation = 'sigmoid'))
#classifier.add(Dense(units = 81, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dense(units = 4, kernel_initializer = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'mean_squared_error', metrics = ['accuracy'])

#Just to free some memory
dataset_blue = None
dataset_green = None
dataset_nir = None
dataset_sred = None
dataset_sgreen = None
dataset_snir = None
dataset_sredge = None

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 64, epochs = 60)

y_pred = classifier.predict(X_test)


pred_rs = pd.concat([pd.DataFrame(X_test),
                    pd.DataFrame(y_pred)],
                axis=1,
                ignore_index=True)
pred_rs = pred_rs.iloc[:,:].values
pred_rs = pred_rs*255
pred_rs = pred_rs[:,15:]

pred_rs = pred_rs.round(decimals=0)



y_rs = pd.concat([pd.DataFrame(X_test),
                    pd.DataFrame(y_test)],
                axis=1,
                ignore_index=True)
y_rs = y_rs.iloc[:,:].values
y_rs = y_rs*255
y_rs = y_rs[:,15:]

y_rs = y_rs.round(decimals=0)





listaRMSE = []

rmse = math.sqrt(mean_squared_error(y_rs[:,0], pred_rs[:,0]))
listaRMSE.append((rmse/y_rs[:,0].mean(),r2_score(y_rs[:,0],pred_rs[:,0])))


rmse = math.sqrt(mean_squared_error(y_rs[:,1], pred_rs[:,1]))
listaRMSE.append((rmse/y_rs[:,1].mean(),r2_score(y_rs[:,1],pred_rs[:,1])))

rmse = math.sqrt(mean_squared_error(y_rs[:,2], pred_rs[:,2]))
listaRMSE.append((rmse/y_rs[:,2].mean(),r2_score(y_rs[:,2],pred_rs[:,2])))

rmse = math.sqrt(mean_squared_error(y_rs[:,3], pred_rs[:,3]))
listaRMSE.append((rmse/y_rs[:,3].mean(),r2_score(y_rs[:,3],pred_rs[:,3])))


##Code to save the classifier if it got good results 
#class_json = classifier.to_json()
#with open("experimento22.json", "w") as json_file:
#    json_file.write(class_json)
#classifier.save_weights("experimento22.h5")


##Load model from file
#from keras.models import model_from_json
#json_file = open('experimento17.json', 'r')
#loaded_model_json = json_file.read()
#json_file.close()
#classifier = model_from_json(loaded_model_json)
##load weights into new model
#classifier.load_weights("experimento17.h5")



#pred = classifier.predict(X)
#complete_set = pd.concat([pd.DataFrame(X),
#                    pd.DataFrame(pred)],
#                axis=1,
#                ignore_index=True)
#
#complete_set = sc.inverse_transform(complete_set)
#complete_set = complete_set.round(decimals=0)
#
##Gera as imagens novas conforme entrada da rede neural
#import cv2
#banda = complete_set[:,15]
#banda = np.reshape(banda, (3158, 2132))
#cv2.imwrite('neural_output/NeuralSequoiaGreen.jpg',banda)
#
#banda = complete_set[:,16]
#banda = np.reshape(banda, (3158, 2132))
#cv2.imwrite('neural_output/NeuralSequoiaNIR.jpg',banda)
#
#banda = complete_set[:,17]
#banda = np.reshape(banda, (3158, 2132))
#cv2.imwrite('neural_output/NeuralSequoiaREdge.jpg',banda)
#
#banda = complete_set[:,18]
#banda = np.reshape(banda, (3158, 2132))
#cv2.imwrite('neural_output/NeuralSequoiaRed.jpg',banda)


lista_y = [[],[],[],[]]
lista_ypred = [[],[],[],[]]
setProibido = set()
n = random.randint(0,721504)
for i in range(500):
    while n in setProibido:
        #print(i)
        n = random.randint(0,721504)
    setProibido.add(n)
    lista_y[0].append(y_rs[n,0])
    lista_ypred[0].append(pred_rs[n,0])
    lista_y[1].append(y_rs[n,1])
    lista_ypred[1].append(pred_rs[n,1])
    lista_y[2].append(y_rs[n,2])
    lista_ypred[2].append(pred_rs[n,2])
    lista_y[3].append(y_rs[n,3])
    lista_ypred[3].append(pred_rs[n,3])




#plt.plot(y_rs[:,1],pred_rs[:,1],'ro')
f, ax = plt.subplots()
ax.plot(lista_y[0],lista_ypred[0],'ro',markersize=1)
x_plot=np.linspace(100,255,256)
ax.plot(x_plot,x_plot,'k-')
ax.set_xlabel('Sequoia Green')
ax.set_ylabel('ANN Green')
ax.grid(True)
gridlines = ax.get_xgridlines() + ax.get_ygridlines()
for line in gridlines:
    line.set_linestyle('--')
f.savefig('GraphGreen.svg',format='svg',dpi=900)


f, ax = plt.subplots()
ax.plot(lista_y[1],lista_ypred[1],'ro',markersize=1)
x_plot=np.linspace(100,255,256)
ax.plot(x_plot,x_plot,'k-')
ax.set_xlabel('Sequoia NIR')
ax.set_ylabel('ANN NIR')
ax.grid(True)
gridlines = ax.get_xgridlines() + ax.get_ygridlines()
for line in gridlines:
    line.set_linestyle('--')
f.savefig('GraphNIR.svg',format='svg',dpi=900)

f, ax = plt.subplots()
ax.plot(lista_y[2],lista_ypred[2],'ro',markersize=1)
x_plot=np.linspace(100,255,256)
ax.plot(x_plot,x_plot,'k-')
ax.set_xlabel('Sequoia Red Edge')
ax.set_ylabel('ANN Red Edge')
ax.grid(True)
gridlines = ax.get_xgridlines() + ax.get_ygridlines()
for line in gridlines:
    line.set_linestyle('--')
f.savefig('GraphRedEdge.svg',format='svg',dpi=900)

f, ax = plt.subplots()
ax.plot(lista_y[3],lista_ypred[3],'ro',markersize=1)
x_plot=np.linspace(100,255,256)
ax.plot(x_plot,x_plot,'k-')
ax.set_xlabel('Sequoia Red')
ax.set_ylabel('ANN Red')
ax.grid(True)
gridlines = ax.get_xgridlines() + ax.get_ygridlines()
for line in gridlines:
    line.set_linestyle('--')
f.savefig('GraphRed.svg',format='svg',dpi=900)


#
##f.savefig('filename.eps', format='eps')
#
