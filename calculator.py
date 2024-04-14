from tkinter import *
Window = Tk()
Window.geometry("500x500")
Window.title("Calculator")
e =Entry(Window,width=76,bg="blue",fg="white",borderwidth=20,relief=SUNKEN)
e.place(x=0,y=0)
def click(num):
    result= e.get()
    e.delete(0,END)
    e.insert(0,str(result)+ str(num))
def div():
    n1=e.get()
    global math
    math = math = "division"
    global i
    i = int(n1)
    e.delete(0,END)
def mult():
    n1 = e.get()
    global math
    math= math ="multiplication"
    global i
    i = int(n1)
    e.delete(0,END)
def Sub():
    n1 = e.get()
    global math
    math = math="subtraction"
    global i
    i = int(n1)
    e.delete(0,END)
def add():
    n1 = e.get()
    global math
    math = math = "addition"
    global i
    i = int(n1)
    e.delete(0,END)
def modulas():
    n1 = e.get()
    global math
    math = math ="modular"
    global i
    i = int(n1)
    e.delete(0,END)
def dot():
    n1 = e.get()
    global math
    math = math = "dotoprator"
    global i
    i = int(n1)
    e.delete(0,END)

def clear():
    e.delete(0,END)
def crossbraket():
    n2 = e.get()
    e.delete(0,END)
def closebracket():
    n2 = e.get()
    e.delete(0,END)
def openbracket():
    n2 = e.get()
    e.delete(0,END)
def Equal():
    n2 = e.get()
    e.delete(0,END)
    if math == "division":
        e.insert(0,i /int(n2))
    elif math == "multiplication":
        e.insert(0,i * int(n2))
    elif math == "subtraction":
        e.insert(0,i- int(n2))
    elif math == "addition":
        e.insert(0,i+int(n2))
    elif math == "modular":
        e.insert(0,i%int(n2))
    elif math == "dotoprator":
        e.insert(0,i.int(n2))
b = Button(Window,text= '1',width=15,command=lambda:click(1))
b.place(x=20,y=70)
b = Button(Window,text= '2',width=15,command=lambda:click(2))
b.place(x=120,y=70)
b = Button(Window,text= '3',width=15,command=lambda:click(3))
b.place(x=230,y=70)
b = Button(Window,text= '/',width=15,command= div)
b.place(x=380,y=70)
b = Button(Window,text= '4',width=15,command=lambda:click(4))
b.place(x=20,y=120)
b = Button(Window,text= '5',width=15,command=lambda:click(5))
b.place(x=120,y=120)
b = Button(Window,text= '6',width=15,command=lambda:click(6))
b.place(x=230,y=120)
b = Button(Window,text= '*',width=15,command=mult)
b.place(x=380,y=120)
b = Button(Window,text= '7',width=15,command=lambda:click(7))
b.place(x=20,y=180)
b = Button(Window,text= '8',width=15,command=lambda:click(8))
b.place(x=120,y=180)
b = Button(Window,text= '9',width=15,command=lambda:click(9))
b.place(x=230,y=180)
b = Button(Window,text= '-',width=15,command=Sub)
b.place(x=380,y=180)
b = Button(Window,text= '0',width=15,command=lambda:click(0))
b.place(x=20,y=240)
b = Button(Window,text= '.',width=15 ,command = dot)
b.place(x=120,y=240)
b = Button(Window,text= '=',width=15 ,command = Equal)
b.place(x=230,y=240)
b = Button(Window,text= '+',width=15,command =add)
b.place(x=380,y=240)
b = Button(Window,text= '%',width=15,command = modulas)
b.place(x=20,y=300)
b = Button(Window,text= '(',width=15,command= openbracket)
b.place(x=120,y=300)
b = Button(Window,text= ')',width=15 ,command=closebracket)
b.place(x=230,y=300)
b = Button(Window,text= 'x',width=15,command= crossbraket)
b.place(x=380,y=300)
b = Button(Window,text= 'clear',width=15,command=clear)
b.place(x=20,y=360)

mainloop()
