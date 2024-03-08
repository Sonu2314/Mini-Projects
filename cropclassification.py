
import pandas as pd
import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pickle

dataset=pd.read_csv('cpdata.csv')
print(type(dataset))
x=dataset.iloc[:,[0,1,2,3]].values  #iloc=ilocation
#print(x)
y=dataset.iloc[:,[4]].values
#print(y)

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.25,random_state=1000)

classifier=KNeighborsClassifier(n_neighbors=3) #neighbor selection
ytrain=np.ravel(ytrain)
classifier.fit(xtrain,ytrain)  #training is done #clsfir means obj

model=open("knnmodel.pkl",'wb')    #wb means writebite
pickle.dump(classifier,model)
model.close()

'''
tdata=np.array([[35,100,6.0,122]])
prediction=classifier.predict(tdata)
print(prediction)
'''



