from tkinter import *

contact = Tk()
contact.geometry('400x400')
contact.config(bg = 'khaki')
contact.resizable(0,0)
contact.title('CONTACT BOOK')

contactList = []
Name = StringVar()
Number = StringVar()

frame = Frame(contact)
frame.pack(side = RIGHT)

scroll = Scrollbar(frame,orient=VERTICAL)
select = Listbox(frame,yscrollcommand=scroll.set,height=12)
scroll.config(command=select.yview)
scroll.pack(side = RIGHT,fill=Y)
select.pack(side=LEFT,fill = BOTH,expand=1)

def Selected():
    return int(select.curselection() [0])

def AddContact():
    contactList.append([Name.get(),Number.get()])
    Select_set()

def EDIT():
    contactList[Selected()] = [Name.get(),Number.get()]
    Select_set()

def DELETE():
    del contactList[Selected()]
    Select_set()

def VIEW():
    NAME,NUMBER = contactList[Selected()]
    Name.set(NAME)
    Number.set(NUMBER)

def EXIT():
    contact.destroy()

def Select_set():
    contactList.sort()
    select.delete(0,END)
    for name,phone in contactList:
        select.insert(END,name)
Select_set()
Label(contact,text = 'NAME',font=('Times New Roman', '12', 'bold'),bg='aqua',fg='navy').place(x=30,y=20)
Entry(contact,textvariable= Name).place(x=100,y=20)

Label(contact,text = 'PHONE NO',font=('Times New Roman', '12', 'bold'),bg='aqua',fg='navy').place(x=30,y=70)
Entry(contact,textvariable= Number).place(x=130,y=70)

Button(contact,text='ADD',font=('Times New Roman', '12', 'bold'),bg='aqua',fg='navy',command=AddContact).place(x=30,y=150)
Button(contact,text='EDIT',font=('Times New Roman', '12', 'bold'),bg='aqua',fg='navy',command=EDIT).place(x=30,y=300)

Button(contact,text='DELETE',font=('Times New Roman', '12', 'bold'),bg='aqua',fg='navy',command=DELETE).place(x=30,y=250)
Button(contact,text='VIEW',font=('Times New Roman', '12', 'bold'),bg='aqua',fg='navy',command=VIEW).place(x=30,y=200)

Button(contact,text='EXIT',font=('Times New Roman', '12', 'bold'),bg='aqua',fg='navy',command=EXIT).place(x=30,y=350)

contact.mainloop()
