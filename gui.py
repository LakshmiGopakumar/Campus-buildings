import csv
import string
from tkinter import *
import tkinter as tk
import pandas as pd


#configure tkinter window
root = Tk()
root.title("XYZ UNIVERSITY")
root.geometry("800x450")

#get the csv file
csv_path = '/Users/buildings.csv'

#need label for the user to select their choice from building name, reference and classification
myLabel1 = Label(root, text="Please select your choice")
myLabel1.pack()


#if the user chooses 'Buildings' button
def button1():
    #The submit button after entering the building name
    def submit():
        search_building=building.get() 

        ref.configure(state=tk.NORMAL)
        clas.configure(state=tk.NORMAL)

        ref.delete(0,'end')
        clas.delete(0,'end')

        df = pd.read_csv("buildings.csv")
        row_count=df.shape[0] #gives the row count
        #print(row_count)


        #to open the csv file
        with open("buildings.csv") as file:
            csv_read = csv.reader(file)
            df=pd.DataFrame([csv_read], index = None) #converting the csv file into data frame format
        
            n=1
            while n<=row_count:
                for val in list(df[n]):

                    if (val[0]) == search_building:
                        ref.insert(0, val[1])
                        clas.insert(0, val[2])
                        ref.configure(state=tk.DISABLED)
                        clas.configure(state=tk.DISABLED)
                    n+=1
    frame= LabelFrame(root, text= "XYZ University").pack(expand= 'yes', fill='both')

    #final output in gui printed as
    Label(frame, text="Building Name: ").place(x=50, y=160 )
    Label(frame, text="Reference: ").place(x=50, y=200)
    Label(frame, text="Classification: ").place(x=50, y=230)
    building = Entry(frame)
    building.place(x=250, y=160)
    ref = Entry(frame)
    ref.place(x=250,y=200)
    clas = Entry(frame)
    clas.place(x=250,y=230)
    ref.configure(state=tk.DISABLED)
    clas.configure(state=tk.DISABLED)

    Button(frame, text = "Submit" , command=submit).place(x=200,y=300) #goes to submit function

#if the user chooses reference option
def button2():
    def submit():
        search_ref=ref.get()

        building.configure(state=tk.NORMAL)
        clas.configure(state=tk.NORMAL)

        building.delete(0,'end')
        clas.delete(0,'end')

        df = pd.read_csv("buildings.csv")
        row_count=df.shape[0]
    

        with open("buildings.csv") as file:
            csv_read = csv.reader(file)
            df=pd.DataFrame([csv_read], index = None)
        
            n=1
            while n<=row_count:
                for val in list(df[n]):

                    if (val[1]) == search_ref:
                        building.insert(0, val[0])
                        clas.insert(0, val[2])
                        building.configure(state=tk.DISABLED)
                        clas.configure(state=tk.DISABLED)
                    n+=1
    frame= LabelFrame(root, text= "XYZ University").pack(expand= 'yes', fill='both')

    Label(frame, text="Building Name: ").place(x=50, y=160 )
    Label(frame, text="Reference: ").place(x=50, y=200)
    Label(frame, text="Classification: ").place(x=50, y=230)
    building = Entry(frame)
    building.place(x=250, y=160)
    ref = Entry(frame)
    ref.place(x=250,y=200)
    clas = Entry(frame)
    clas.place(x=250,y=230)
    building.configure(state=tk.DISABLED)
    clas.configure(state=tk.DISABLED)

    Button(frame, text = "Submit" , command=submit).place(x=200,y=300) #goes to submit function

#if teh user chooses classification option
def button3():
    def submit():
        search_clas=clas.get()

        building.configure(state=tk.NORMAL)
        ref.configure(state=tk.NORMAL)

        building.delete(0,'end') #as there are multiple entries for classification column, 
                                 #either reference number or building name should also be given

        

        df = pd.read_csv("buildings.csv")
        row_count=df.shape[0]
    

        with open("buildings.csv") as file:
            csv_read = csv.reader(file)
            df=pd.DataFrame([csv_read], index = None)
        
            n=1
            while n<=row_count:
                for val in list(df[n]):

                    if (val[2]) == search_clas:
                        building.insert(0, val[0])
                        building.configure(state=tk.DISABLED)
                    n+=1
    frame= LabelFrame(root, text= "XYZ University").pack(expand= 'yes', fill='both')

    Label(frame, text="Building Name: ").place(x=50, y=160 )
    Label(frame, text="Reference: ").place(x=50, y=200)
    Label(frame, text="Classification: ").place(x=50, y=230)

    building = Entry(frame)
    building.place(x=250, y=160)
    ref = Entry(frame)
    ref.place(x=250,y=200)
    clas = Entry(frame)
    clas.place(x=250,y=230)
    building.configure(state=tk.DISABLED)
   

    Button(frame, text = "Submit" , command=submit).place(x=200,y=300) #goes to submit function

myButton1 = Button(root, text = "Building", command=button1)  #goes to button1 funtion
myButton2 = Button(root, text = "Reference", command=button2) #goes to button2 function
myButton3 = Button(root, text = "Classifications", command=button3) #goes to button3 function
myButton1.pack()
myButton2.pack()
myButton3.pack()

root.mainloop()
                 



