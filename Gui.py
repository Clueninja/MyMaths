from Function import Function, ListOfFunctions
import matplotlib.pyplot as plt

import tkinter as tk
alist = ListOfFunctions()


# configure workspace
ws = tk.Tk()
ws.title("Gui For Graphing")
ws.geometry('300x400')
ws.configure(bg="#567")

# function territory
def outputFunction():
    poly = polyEn.get()
    imin = int(minEn.get())
    imax=int(maxEn.get())
    alist.addfunction(Function((imin,imax), Function.parser(poly)))
    return tk.Label(ws, text=f'Entered', pady=15, bg='#567').grid(row=4, columnspan=2)

def plot():
    imin = float(plotminEn.get())
    imax=float(plotmaxEn.get())
    alist.plot(imin,imax)
    plt.show()


# label & Entry boxes territory
polyLb = tk.Label(ws, text="Enter Polynomial", pady=15, padx=10, bg='#567')
polyEn = tk.Entry(ws)

minLb = tk.Label(ws, text="Enter Min Range", pady=15, padx=10, bg='#567')
minEn = tk.Entry(ws)

maxLb = tk.Label(ws, text="Enter Max Range", pady=15, padx=10, bg='#567')
maxEn = tk.Entry(ws)

plotminLb = tk.Label(ws, text="Enter Plot Min", pady=15, padx=10, bg='#567')
plotminEn = tk.Entry(ws)

plotmaxLb = tk.Label(ws, text="Enter Plot Max", pady=15, padx=10, bg='#567')
plotmaxEn = tk.Entry(ws)



# button territory
enterBtn = tk.Button(ws, text="Enter Function", command=outputFunction)

plotBtn = tk.Button(ws, text="Plot", command=plot)


# Position Provide territory
polyLb.grid(row=0, column=0); polyEn.grid(row=0, column=1)
minLb.grid(row=1, column=0); minEn.grid(row=1, column=1)
maxLb.grid(row=2, column=0); maxEn.grid(row=2, column=1)

enterBtn.grid(row=3, columnspan=2)

plotminLb.grid(row=5, column=0); plotminEn.grid(row=5, column=1)
plotmaxLb.grid(row=6, column=0); plotmaxEn.grid(row=6, column=1)


plotBtn.grid(row=7, columnspan=2)


# infinite loop 
ws.mainloop()