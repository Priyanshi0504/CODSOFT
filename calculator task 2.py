from tkinter import*
root=Tk()
root.geometry('490x335')
root.title('calculator')
root.configure(bg='teal')

a=StringVar()
e1=Entry(root,font=('courier',20),fg='dark blue',bg='light blue',textvariable=a,justify='right')
e1.place(x=0,y=0,width=490,height=50)

def eql():
    exp=a.get()
    a.set(eval(exp))
def show(op):
    a.set(a.get()+op)
def clr():
    a.set('')
    
b10=Button(root,text='+',font=('courier',20),fg='white',bg='gray',activebackground='black',activeforeground='red')
b10.configure(command=lambda:show("+"))
b10.place(x=380,y=55,width=105,height=50)

b11=Button(root,text='-',font=('courier',20),fg='white',bg='gray',activebackground='black',activeforeground='red')
b11.configure(command=lambda:show("-"))
b11.place(x=380,y=130,width=105,height=50)

b12=Button(root,text='x',font=('courier',20),fg='white',bg='gray',activebackground='black',activeforeground='red')
b12.configure(command=lambda:show("*"))
b12.place(x=380,y=205,width=105,height=50)

b13=Button(root,text='=',font=('courier',20),fg='white',bg='gray',activebackground='black',activeforeground='red')
b13.configure(command=lambda:eql())
b13.place(x=5,y=280,width=105,height=50)

b14=Button(root,text='/',font=('courier',20),fg='white',bg='gray',activebackground='black',activeforeground='red')
b14.configure(command=lambda:show("/"))
b14.place(x=380,y=280,width=105,height=50)

b15=Button(root,text='0',font=('courier',20),fg='white',bg='gray',activebackground='black',activeforeground='red')
b15.configure(command=lambda:show("0"))
b15.place(x=130,y=280,width=105,height=50)

b16=Button(root,text='C',font=('courier',20),fg='white',bg='gray',activebackground='black',activeforeground='red')
b16.configure(command=lambda:clr())
b16.place(x=255,y=280,width=105,height=50)


b17=Button(root,text='%',font=('courier',20),fg='white',bg='gray',activebackground='black',activeforeground='red')
b17.configure(command=lambda:show("%"))
b17.place(x=255,y=355,width=105,height=50)

b17=Button(root,text='**',font=('courier',20),fg='white',bg='gray',activebackground='black',activeforeground='red')
b17.configure(command=lambda:show("**"))
b17.place(x=5,y=355,width=105,height=50)


b1=Button(root,text='1',font=('courier',20),fg='white',bg='gray',activebackground='black',activeforeground='red')
b1.configure(command=lambda:show("1"))
b1.place(x=5,y=55,width=105,height=50)


b2=Button(root,text='2',font=('courier',20),fg='white',bg='gray',activebackground='black',activeforeground='red')

b2.configure(command=lambda:show("2"))
b2.place(x=130,y=55,width=105,height=50)


b3=Button(root,text='3',font=('courier',20),fg='white',bg='gray',activebackground='black',activeforeground='red')

b3.configure(command=lambda:show("3"))
b3.place(x=255,y=55,width=105,height=50)


b4=Button(root,text='4',font=('courier',20),fg='white',bg='gray',activebackground='black',activeforeground='red')

b4.configure(command=lambda:show("4"))
b4.place(x=5,y=130,width=105,height=50)



b5=Button(root,text='5',font=('courier',20),fg='white',bg='gray',activebackground='black',activeforeground='red')

b5.configure(command=lambda:show("5"))
b5.place(x=130,y=130,width=105,height=50)


b6=Button(root,text='6',font=('courier',20),fg='white',bg='gray',activebackground='black',activeforeground='red')

b6.configure(command=lambda:show("6"))
b6.place(x=255,y=130,width=105,height=50)




b7=Button(root,text='7',font=('courier',20),fg='white',bg='gray',activebackground='black',activeforeground='red')

b7.configure(command=lambda:show("7"))
b7.place(x=5,y=205,width=105,height=50)



b8=Button(root,text='8',font=('courier',20),fg='white',bg='gray',activebackground='black',activeforeground='red')

b8.configure(command=lambda:show("8"))
b8.place(x=130,y=205,width=105,height=50)




b9=Button(root,text='9',font=('courier',20),fg='white',bg='gray',activebackground='black',activeforeground='red')

b9.configure(command=lambda:show("9"))
b9.place(x=255,y=205,width=105,height=50)





root.mainloop()