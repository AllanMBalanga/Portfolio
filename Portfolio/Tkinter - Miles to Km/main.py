from tkinter import *

window = Tk()
window.title("GUI Project")
window.minsize(300,150)
window.config(padx=10,pady=10)


entry = Entry(width=15)
entry.grid(column=1,row=0)


my_label3 = Label(text="Miles", font = ("Arial", 15,))
my_label3.grid(column = 2, row=0)
my_label3.config(padx=5,pady=5)


my_label4 = Label(text="is equal to", font = ("Arial", 15,))
my_label4.grid(column = 0, row=1)
my_label4.config(padx=5,pady=5)


my_label5 = Label(text="Km", font = ("Arial", 15,))
my_label5.grid(column = 2, row=1)
my_label5.config(padx=5,pady=5)


my_label2 = Label(text="0", font = ("Arial", 15,))
my_label2.config(padx=5,pady=5)
my_label2.grid(column = 1, row=1)


#BUTTON
def button_clicked():
    my_label2.config(text = round(int(entry.get())*1.60934))


button = Button(text="calculate", command=button_clicked)
button.grid(column=1,row=2)
button.config(padx=5,pady=5)



window.mainloop()