import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3 as lite
import sys

#state=input("Enter the state:")
#year=int(input("Enter the year:"))


def regressionGrad(X,y,year):
    #feature scaling
    from sklearn.preprocessing import StandardScaler
    sc_X=StandardScaler()
    sc_y=StandardScaler()
    X=sc_X.fit_transform(X)
    y=sc_y.fit_transform(y)
    
    #svr fit
    from sklearn.svm import SVR
    regressor=SVR(kernel='rbf')
    regressor.fit(X,y)
    y_pred=sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([[year]]))))
    
    #plot svr
    X_grid=np.arange(min(X),max(X),0.1)
    X_grid=X_grid.reshape((len(X_grid),1))
    y_grid=regressor.predict(X_grid)
    X=sc_X.inverse_transform(X)
    y=sc_y.inverse_transform(y)
    X_grid=sc_X.inverse_transform(X_grid)
    y_grid=sc_y.inverse_transform(y_grid)
    fig = plt.figure(figsize=(7,7))
    plt.scatter(X,y,color='red',label='Input Data')
    plt.plot(X_grid,y_grid,color="blue",label='best fit curve')
    plt.xticks(X)
    plt.legend(loc=0)
    plt.title("Number of graduates")
    plt.xlabel('Year')
    plt.ylabel("Number of graduates")
    plt.close('all')
    
    return ([y_pred,fig])
    
def regressionEmp(X,y,year):
    #feature scaling
    from sklearn.preprocessing import StandardScaler
    sc_X=StandardScaler()
    sc_y=StandardScaler()
    X=sc_X.fit_transform(X)
    y=sc_y.fit_transform(y)
    
    #svr fit
    from sklearn.svm import SVR
    regressor=SVR(kernel='rbf')
    regressor.fit(X,y)
    y_pred=sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([[year]]))))

    #plot svr
    X_grid=np.arange(min(X),max(X),0.1)
    X_grid=X_grid.reshape((len(X_grid),1))
    y_grid=regressor.predict(X_grid)
    X=sc_X.inverse_transform(X)
    y=sc_y.inverse_transform(y)
    X_grid=sc_X.inverse_transform(X_grid)
    y_grid=sc_y.inverse_transform(y_grid)
    fig = plt.figure(figsize=(7,7))
    plt.scatter(X,y,color='red',label='Input Data')
    plt.plot(X_grid,y_grid,color="blue",label='best fit curve')
    plt.xticks(X)
    plt.legend(loc=0)
    plt.title("Employment rate")
    plt.xlabel('Year')
    plt.ylabel("Employment percent")
    plt.close('all')
    
    return ([y_pred,fig])
    
def predGrads(state,year):
    #importing data
    #dataset=pd.read_excel('EandGstateWise.xlsx',sheetname=state)
    #X=dataset.iloc[:,0].values.reshape(11,1)
    #y=dataset.iloc[:,1].values.reshape(11,1)
    
    
    con = lite.connect('EandGstateWise.db')

    with con:    
        cur = con.cursor()    
        cur.execute("SELECT * FROM "+state)
        rows = cur.fetchall()
        
    list=[]
    for c in rows:
        list.append(c)    
        
    X=[]
    for i in range(0,11):
        X.append([list[i][0]])
    
    X=np.array(X)
    
    y=[]
    for i in range(0,11):
        y.append([list[i][1]])
    
    y=np.array(y)
    
    predG=regressionGrad(X,y,year)
    return predG
    #print("Predicted value of number of graduates:",predG)
    
def predEmp(state,year):
    #importing data
    #dataset=pd.read_excel('EandGstateWise.xlsx',sheetname=state)
    #X=dataset.iloc[:,0].values.reshape(11,1)
    #y=dataset.iloc[:,2].values.reshape(11,1)
   
    con = lite.connect('EandGstateWise.db')

    with con:    
        cur = con.cursor()    
        cur.execute("SELECT * FROM "+state)
        rows = cur.fetchall()
        
    list=[]
    for c in rows:
        list.append(c)    
        
    X=[]
    for i in range(0,11):
        X.append([list[i][0]])
    
    X=np.array(X)
    
    y=[]
    for i in range(0,11):
        y.append([list[i][2]])
    
    y=np.array(y)
    
    predE=regressionEmp(X,y,year)
    return predE
    #print("Predicted value of employment percent:",predE)
    
#predGrads(year)
#predEmp(year)
"""def plotBar(state):
    dataset=pd.read_excel('EandGstateWise.xlsx',sheetname=state)
    X=dataset.iloc[:,0].values.reshape(11,1)
    y=dataset.iloc[:,1].values.reshape(11,1)
"""    
