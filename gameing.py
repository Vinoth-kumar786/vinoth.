from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("Tic tac Toe")

frame1=Frame(root)

titleLabel=Label(frame1,text="Tic Tac Toe",font="arial",bg="red")

titleLabel.pack()
frame2=Frame(root)
frame2.pack()


turn ="x"
def play(event):
  global turn
  button=event.widget
  if turn=="x":  
   button["text"]="x"
   turn="o"
  else:
    button["text"]="o"
    turn="x"


button1=Button(frame2,text="",width=16,height=8)
button1.grid(row=0,column=0)
button1.bind("<Button-1>",play)

button1=Button(frame2,text="",width=16,height=8)
button1.grid(row=0,column=1)

button1.bind("<Button-1>",play)


button1=Button(frame2,text="",width=16,height=8)
button1.grid(row=0,column=2)
button1.bind("<Button-1>",play)


button1=Button(frame2,text="",width=16,height=8)
button1.grid(row=1,column=0)
button1.bind("<Button-1>",play)


button1=Button(frame2,text="",width=16,height=8)
button1.grid(row=1,column=1)
button1.bind("<Button-1>",play)


button1=Button(frame2,text="",width=16,height=8)
button1.grid(row=1,column=2)
button1.bind("<Button-1>",play)




button1=Button(frame2,text="",width=16,height=8)
button1.grid(row=2,column=0)
button1.bind("<Button-1>",play)


  
button1=Button(frame2,text="",width=16,height=8)
button1.grid(row=2,column=1)
button1.bind("<Button-1>",play)


button1=Button(frame2,text="",width=16,height=8)
button1.grid(row=2,column=2)
button1.bind("<Button-1>",play)

root.mainloop()