from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = ([random.choice(letters) for _ in range(random.randint(8, 10))] +
                     [random.choice(symbols) for _ in range(random.randint(2, 4))]  +
                     [random.choice(numbers) for _ in range(random.randint(2, 4))])

    random.shuffle(password_list)

    password = "".join(password_list)

    p_entry.delete(0,END)
    p_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    web = w_entry.get()
    user = e_entry.get()
    pw = p_entry.get()
    new_data = {
        web: {
            "Email": user,
            "Password": pw
        }
    }

    if len(web) == 0 or len(pw) == 0:
        messagebox.showinfo(title="Missing Information", message="You've left some field/s empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reads the old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                #Writes a json.file using the new_data
                json.dump(new_data, data_file, indent=4)
        else:
            """Merges the old to the new data"""
            data.update(new_data)
            with open("data.json", "w") as data_file:
                """Writes the updated data to the json.file"""
                json.dump(data, data_file, indent=4)
        finally:
            w_entry.delete(0, END)
            p_entry.delete(0, END)

def find_password():
    webpage = w_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if webpage in data:
            messagebox.showinfo(title=f"{webpage}",
                                message=f"Email: {data[webpage]["Email"]} \n Password: {data[webpage]["Password"]}")
        else:
            messagebox.showinfo(title="Data Missing",message=f"No Data Provided For {webpage}.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50,pady=50)

#LABELS
website = Label(text="Website:")
website.grid(row=1, column=0)

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3,column=0)

#ENTRIES
w_entry = Entry(width=27)
w_entry.grid(row=1,column=1)
w_entry.focus()

e_entry = Entry(width=45)
e_entry.grid(row=2,column=1,columnspan=2)
e_entry.insert(0,"allanmbalangajr@gmail.com")

p_entry = Entry(width=27)
p_entry.grid(row=3,column=1)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

generate_pw = Button(text="Generate Password",command=password_generator)
generate_pw.grid(row=3,column=2)

add = Button(text="Add",width=38,command=save_password)
add.grid(row=4, column=1,columnspan=2)

search = Button(text="Search",width=15,command=find_password)
search.grid(row=1, column=2)
window.mainloop()