import pandas as pd
import numpy as np
#read files
arquivo=pd.read_csv('C:/Users/jvict/OneDrive/Documents/wine_dataset.csv')


#red=0 and white=1
arquivo['style']=arquivo['style'].replace('red',0)
arquivo['style']=arquivo['style'].replace('white',1)


#set the array
y=arquivo['style']
X=arquivo.drop('style',axis=1)


#split the arrays between train and test
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)


#set the tree to module and fit it
from  sklearn.ensemble import ExtraTreesClassifier
clt=ExtraTreesClassifier()
clt.fit(X_train,y_train)


#measure the accuracy of the IA
resultado=clt.score(X_test,y_test)
print(resultado)