from tkinter import *
from EandG import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3 as lite
import sys

import PIL.Image
import PIL.ImageTk

states=['andhraPradesh','gujarat','haryana','karnataka','kerala','tamilNadu','westBengal']
states2=['andhraPradesh','karnataka','tamilNadu','westBengal']
years=[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]

def func():
    def f1():
        fig = plt.figure(figsize=(7,7))
        #X,y=plotBar(v1.get())
        dataset=pd.read_excel('EandGstateWise.xlsx',sheetname=v1.get())
        X=dataset.iloc[:,0].values.reshape(11,1)
        y=dataset.iloc[:,1].values.reshape(11,1)
        plt.bar(X,y,align='center',alpha=1)
        plt.xticks(X)
        plt.xlabel('year')
        plt.ylabel('number of graduates')
        plt.title(v1.get()+' state')
        plt.close('all')
        canvas = FigureCanvasTkAgg(fig, master=branch)
        canvas.get_tk_widget().place(x=330,y=0)
        canvas.draw() 
        
    """def f2():
        ye=v2.get()
        ye=str(ye)
        fig = plt.figure(figsize=(7,7))
        #X,y=plotBar(v1.get())
        #dataset=pd.read_excel('EandGstateWise.xlsx',sheetname=v1.get())
        #X=dataset.iloc[:,0].values.reshape(11,1)
        #y=dataset.iloc[:,1].values.reshape(11,1)
        
        con = lite.connect('EandGstateWise.db')

        with con:    
            cur = con.cursor()    
            cur.execute("select a.graduates,g.graduates,h.graduates,k.graduates,ke.graduates,t.graduates,w.graduates from andhraPradesh a,gujarat g,haryana h,karnataka k,kerala ke,tamilNadu t,westBengal w where a.year="+ye+" and g.year="+ye+" and h.year="+ye+" and k.year="+ye+" and ke.year="+ye+" and t.year="+ye+" and w.year="+ye+";")
            rows = cur.fetchall()
        
        list=[]
        for c in rows:
            list.append(c)  
        
        y=[]
        for i in range(0,6):
            y.append([list[0][i-1]])
    
        y=np.array(y)    
        
        X=[]
        for i in states:
            X.append([i])
    
        X=np.array(X)
    
        h=len(states)
        he=np.arange(h)
        
        
        plt.bar(he,y,align='center',alpha=1)
        plt.xticks(X)
        plt.xlabel('states')
        plt.ylabel('number of graduates')
        plt.title(v2.get())
        plt.close('all')
        canvas = FigureCanvasTkAgg(fig, master=branch)
        canvas.get_tk_widget().place(x=330,y=0)
        canvas.draw()"""    
     
    def f3():
        fig = plt.figure(figsize=(7,7))
        #X,y=plotBar(v1.get())
        dataset=pd.read_excel('EandGstateWise.xlsx',sheetname=v1.get())
        X=dataset.iloc[:,0].values.reshape(11,1)
        y=dataset.iloc[:,2].values.reshape(11,1)
        plt.bar(X,y,align='center',alpha=1)
        plt.xticks(X)
        plt.xlabel('year')
        plt.ylabel('employment rate in %')
        plt.title(v1.get()+' state')
        plt.close('all')
        canvas = FigureCanvasTkAgg(fig, master=branch)
        canvas.get_tk_widget().place(x=330,y=0)
        canvas.draw()
    
    def f5():
        predG=predGrads(v1.get(),v2.get())
        gEP.delete(0,END)
        gEP.insert(INSERT,round(predG[0][0]))
        canvas = FigureCanvasTkAgg(predG[1], master=branch)
        canvas.get_tk_widget().place(x=330,y=0)
        canvas.draw()   

    def f6():
        predE=predEmp(v1.get(),v2.get())
        gEP.delete(0,END)
        gEP.insert(INSERT,round(predE[0][0]))
        canvas = FigureCanvasTkAgg(predE[1], master=branch)
        canvas.get_tk_widget().place(x=330,y=0)
        canvas.draw()   
    def dest():
        branch.destroy()
        
    val=v.get()
    if (val!=0):    
        branch=Toplevel()
        #branch.geometry('1920x1080')
        branch.attributes('-zoomed', True)
        v1=StringVar()
        v2=IntVar()
        
        if(val==1):
            Label(branch,text="Choose state:").grid(row=100,column=0)
            OptionMenu(branch,v1,*states).grid(row=100,column=1)
            Button(branch, text="graph",command=f1,font=('Times',16)).grid(row=140,column=1)
            #Button(root, text="Exit", command=branch.destroy,font=('Times',16)).grid(row=300,column=1)
        
        elif(val==3):
            Label(branch,text="Choose state:").grid(row=100,column=0)
            OptionMenu(branch,v1,*states2).grid(row=100,column=1)
            Button(branch, text="graph",command=f3,font=('Times',16)).grid(row=140,column=1)
            #Button(root, text="Exit", command=branch.destroy,font=('Times',16)).grid(row=300,column=1)

        elif (val==5):
            Label(branch,text="Choose state:").grid(row=100,column=0)
            OptionMenu(branch,v1,*states).grid(row=100,column=1)
            Label(branch,text="Choose year:").grid(row=120,column=0)
            OptionMenu(branch,v2,*years).grid(row=120,column=1)
            Label(branch,text="Predicted Graduates:").grid(row=130,column=0)
            gEP=Entry(branch,justify='center')
            gEP.grid(row=130,column=1)
            Button(branch, text="Predict",command=f5,font=('Times',16)).grid(row=140,column=1)
            #Button(root, text="Exit", command=dest,font=('Times',16)).grid(row=10,column=1)

        elif(val==6):
            Label(branch,text="Choose state:").grid(row=100,column=0)
            OptionMenu(branch,v1,*states2).grid(row=100,column=1)
            Label(branch,text="Choose year:").grid(row=120,column=0)
            OptionMenu(branch,v2,*years).grid(row=120,column=1)
            Label(branch,text="Predicted Employment rate:").grid(row=130,column=0)
            gEP=Entry(branch,justify='center')
            gEP.grid(row=130,column=1)
            Button(branch, text="Predict",command=f6,font=('Times',16)).grid(row=140,column=1)
            #Button(root, text="Exit", command=branch.destroy,font=('Times',16)).grid(row=300,column=1)
    	
    
root=Tk()
#root.geometry('1920x1080')
root.attributes('-fullscreen', True)
root.title('Graduates and employability')

image = PIL.Image.open('background.jpg')
photo_image = PIL.ImageTk.PhotoImage(image)
Label(root, image = photo_image).pack()

Label(root,text="IT Graduates estimation and employabilty prediction",font=('Papyrus',20)).place(x=300,y=20)
v=IntVar()
Label(root,text="Access existing data:",font=('Perpetua',18)).place(x=20,y=100)
Radiobutton(root,text="Number of graduates of a particular state over all years",variable=v,value=1,font=('Garamond',16)).place(x=20,y=160,anchor=W)
#Radiobutton(root,text="Number of graduates of all states in a particular year",variable=v,value=2,font=('Garamond',16)).place(x=20,y=210,anchor=W)
Radiobutton(root,text="Employment rate of a particular state over all years",variable=v,value=3,font=('Garamond',16)).place(x=20,y=210,anchor=W)
#Radiobutton(root,text="Employment rate of all states in a particular year",variable=v,value=4,font=('Garamond',16)).place(x=20,y=310,anchor=W)
Label(root,text="Predict future data:",font=('Perpetua',18)).place(x=20,y=380)
Radiobutton(root,text="Predict the number of graduates",variable=v,value=5,font=('Garamond',16)).place(x=20,y=440,anchor=W)
Radiobutton(root,text="Predict the employment rate",variable=v,value=6,font=('Garamond',16)).place(x=20,y=490,anchor=W)
Button(root, text="Next", command=func,font=('Times',16)).place(x=300,y=650)
Button(root, text="Exit", command=root.destroy,font=('Times',16)).place(x=400,y=650)

root.mainloop()
