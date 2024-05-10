#data entry in csv file

from csv import *
from tkinter import *

window=Tk()
window.title("Data Entry")
main_list=[]

def Clear():
    name.delete(0,END)
    age.delete(0,END)
    contact.delete(0,END)
    
def Add():
    lst=[name.get(),age.get(),contact.get()]
    main_list.append(lst)
    messagebox.showinfo("Information","The data has been added succesfully")
    
def Save():
    with open("data_entry.csv","a") as file:
        Writer=writer(file)
        #Writer.writerow(["Name","Age","Contact"])
        Writer.writerows(main_list)
        messagebox.showinfo("Information","The file has been saved succesfully")
    

label1=Label(window,text="Name: ",padx=20,pady=10)
label2=Label(window,text="Age: ",padx=20,pady=10)
label3=Label(window,text="Contact: ",padx=20,pady=10)
name=Entry(window,width=30,borderwidth=5)
age=Entry(window,width=30,borderwidth=5)
contact=Entry(window,width=30,borderwidth=5)
save=Button(window,text="Save",padx=20,pady=10,command=Save)
add=Button(window,text="Add",padx=20,pady=10,command=Add)
clear=Button(window,text="Clear",padx=20,pady=10,command=Clear)
Exit=Button(window,text="Exit",padx=20,pady=10,command=window.quit)

label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)
name.grid(row=0,column=1)
age.grid(row=1,column=1)
contact.grid(row=2,column=1)
save.grid(row=4,column=0,columnspan=2)
add.grid(row=3,column=0,columnspan=2)
clear.grid(row=5,column=0,columnspan=2)
Exit.grid(row=6,column=0,columnspan=2)

window.mainloop()






