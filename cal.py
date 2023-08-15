from tkinter import*

root = Tk()

input = Entry(root,width=50)
input.grid(row=0,column=0,columnspan=3,padx=15,pady=15)

def click(num):
  current=input.get()
  input.delete(0,END)
  input.insert(0,str(current)+str(num))
  return

def add():
   current=input.get()
   global fnum
   fnum=int(current)
   input.delete(0,END)
   return
def sub():
   current=input.get()
   global anum
   anum=int(current)
   input.delete(0,END)
def clear():
   input.delete(0,END)
   return
def mul():
   return
def equal():
   current= input.get()
   snum=int(current)
   input.delete(0,END)

   input.insert(0,str(fnum+snum))

   input.insert(0,str(anum-snum))

   return

    
button1 = Button(root,text="1",padx=50,pady=25,command= lambda:click(1))
button2 = Button(root,text="2",padx=50,pady=25,command=lambda:click(2))
button3 = Button(root,text="3",padx=50,pady=25,command=lambda:click(3))
button4=  Button(root,text="4",padx=50,pady=25,command=lambda:click(4))
button5 = Button(root,text="5",padx=50,pady=25,command=lambda:click(5))
button6 = Button(root,text="6",padx=50,pady=25,command=lambda:click(6))
button7 = Button(root,text="7",padx=50,pady=25,command=lambda:click(7))
button8 = Button(root,text="8",padx=50,pady=25,command=lambda:click(8))
button9 = Button(root,text="9",padx=50,pady=25,command=lambda:click(9))
button0 = Button(root,text="0",padx=50,pady=25,command=lambda:click(0))
button_add = Button(root,text="+",padx=105,pady=25,command=add)
button_sub=  Button(root,text="-",padx=50,pady=25,command=sub)




button_clear = Button(root,text="AC",padx=45,pady=25,command=clear)
button_equal = Button(root,text="=",padx=105,pady=25,command=equal)


button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button6.grid(row=2,column=0)
button5.grid(row=2,column=1)
button4.grid(row=2,column=2) 

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button0.grid(row=4,column=0,columnspan=1)
button_add.grid(row=4,column=1,columnspan=2)
button_sub.grid(row=5,column=0,columnspan=1)
button_clear.grid(row=6,column=0)
button_equal.grid(row=6,column=1,columnspan=2)












root.mainloop()