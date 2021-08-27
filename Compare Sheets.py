import pandas as pd
from tkinter import *
from tkinter import messagebox
import tkinter as t
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import re
root = Tk()
global fileDataA
global fileDataB

# Functions
def openFileFunA():
    global fileDataA
    fileTypeA = rAValue.get()
    if (fileTypeA == 1):
        fileAName = askopenfilename()
        fileDataA = pd.read_csv(fileAName)
        result = []
        for i in fileDataA.columns:
            colChange = re.sub(r' ', '_', i)
            fileDataA.rename(columns={i: colChange},inplace=True)
            result.append(colChange)
        boxA['values'] = result
    elif (fileTypeA == 2):
        fileAName = askopenfilename()
        fileDataA = pd.read_excel(fileAName)
        result = []
        for i in fileDataA.columns:
            colChange = re.sub(r' ', '_', i)
            fileDataA.rename(columns={i: colChange}, inplace=True)
            result.append(colChange)
        boxA['values'] = result
    else:
        messagebox.showwarning("No Format Selected", "Kindly Select Any Format First.")



def openFileFunB():
    global fileDataB
    fileTypeB = rBValue.get()
    if(fileTypeB == 1):
        fileBName = askopenfilename()
        fileDataB = pd.read_csv(fileBName)
        result = []
        for i in fileDataB.columns:
            colChange = re.sub(r' ', '_', i)
            fileDataB.rename(columns={i: colChange}, inplace=True)
            result.append(colChange)
        boxB['values'] = result
    elif(fileTypeB == 2):
        fileBName = askopenfilename()
        fileDataB = pd.read_excel(fileBName)
        result = []
        for i in fileDataB.columns:
            colChange = re.sub(r' ', '_', i)
            fileDataB.rename(columns={i: colChange}, inplace=True)
            result.append(colChange)
        boxB['values'] = result
    else:
        messagebox.showwarning("No Format Selected", "Kindly Select Any Format First.")

def deleteResult():
    x = tree.get_children()
    if(x != '()'):
        for child in x:
            tree.delete(child)

def finalResult():
    global fileDataA
    global fileDataB
    colAValue = colA.get()
    colBValue = colB.get()
    cSeriesA = pd.Series(data = fileDataA[colAValue])
    cSeriesB = pd.Series(data = fileDataB[colBValue])
    for num in fileDataA.index:
        if( cSeriesA.iloc[num] != cSeriesB.iloc[num]):
            tree.insert("", index=num, values=(num+1, cSeriesA.iloc[num], cSeriesB.iloc[num]))


# About root
windowWidth = root.winfo_screenwidth()
windowHeight = root.winfo_screenheight()
root.geometry("%dx%d+%d+%d"%(windowWidth/2, windowHeight/2, windowWidth/4, windowHeight/4))
root.minsize(int(windowWidth/2) + 85, int(windowHeight/2))
root.maxsize(windowWidth, windowHeight)
root.title("Compare Sheets By Pardeep Grewal")
root.iconbitmap(r"MY.ico")

# Frame on Top
ft = Frame(root, bg = "black", borderwidth=4)
ft.pack(side="top", pady=3, padx=4, fill="x")
ftLabel = Label(ft, text="Compare Sheets", font="comicsansms 13 bold")
ftLabel.pack()

# Frame in Middle
fm = Frame(root, bg = "black", borderwidth=5)
fm.pack(pady=1, padx=4, fill="x")

# Left Frame in Middle Frame
fmm1 = Frame(fm, bg="black", borderwidth=2)
fmm1.pack(side="left")
f1 = Frame(fmm1, bg = "white", borderwidth=2)
f1.pack(padx=112, pady=4, anchor="center")

f1Label = Label(f1, text="Select File Format", padx=3)
f1Label.grid(row=0, column=0, columnspan=2, pady=1, padx=1, sticky=E+W)
rAValue = t.IntVar()
rA1 = t.Radiobutton(f1, text = "CSV", variable = rAValue, value = 1)
rA1.grid(row=1, column=0, pady=1, sticky=E+W)
rA2 = t.Radiobutton(f1, text = "Excel", variable = rAValue, value = 2)
rA2.grid(row=1, column=1, pady=1, sticky=E+W)
button1 = t.Button(f1, text="Open File A", command=openFileFunA)
button1.grid(row=2, column=0, columnspan=2, pady=1, sticky=E+W)
colA = t.StringVar()
boxA = ttk.Combobox(f1, textvariable=colA, state="readonly")
boxA['values'] = 'Select-Column'
boxA.current(0)
boxA.grid(row=3, column=0, columnspan=2)
button4 = t.Button(f1, text="Clear Table", command=deleteResult)
button4.grid(row=4, column=0, columnspan=2, pady=1, sticky=E+W)

# Right Frame in Middle
fmm2 = Frame(fm, bg="black", borderwidth=2)
fmm2.pack(side="right")
f2 = Frame(fmm2, bg = "white", borderwidth=2)
f2.pack(padx=112, pady=4, anchor="center")

f2Label = Label(f2, text="Select File Format", padx=3)
f2Label.grid(row=0, column=0, columnspan=2, pady=1, padx=1, sticky=E+W)
rBValue = t.IntVar()
rB1 = t.Radiobutton(f2, text = "CSV", variable = rBValue, value = 1)
rB1.grid(row=1, column=0, pady=1, sticky=W+E)
rB2 = t.Radiobutton(f2, text = "Excel", variable = rBValue, value = 2)
rB2.grid(row=1, column=1, pady=1, sticky=E+W)
button2 = t.Button(f2, text="Open File B", command=openFileFunB)
button2.grid(row=2, column=0, columnspan=2, pady=1, sticky=E+W)
colB = t.StringVar()
boxB = ttk.Combobox(f2, textvariable=colB, state="readonly")
boxB['values'] = "Select-Column"
boxB.current(0)
boxB.grid(row=3, column=0, columnspan=2)
button3 = t.Button(f2, text="Compare", command=finalResult)
button3.grid(row=4, column=0, columnspan=2, pady=1, sticky=E+W)

# Frame in Bottom
fb = Frame(root, bg="black", borderwidth=4)
fb.pack(side="bottom", pady=1, padx=4, fill="x")

tree = ttk.Treeview(fb)
tree["columns"]=("one","two","three")
tree.column("one", width=10)
tree.column("two")
tree.column("three")
tree.heading("one", text="Serial Number")
tree.heading("two", text="Value in file A")
tree.heading("three", text="Value in file B")
tree['show'] = 'headings'
tree.pack(side="right", ipadx=windowWidth, ipady=windowHeight)

scroll = t.Scrollbar(tree)
scroll.pack(side="right", fill="y", pady=2)
scroll.configure(command=tree.yview)
tree.configure(yscrollcommand=scroll.set)



root.mainloop()
