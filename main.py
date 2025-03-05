# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
import json
from tkinter import messagebox
#Password Generator Project
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    #
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_list1 = [random.choice(letters) for _ in range(nr_letters)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_list2 = [random.choice(symbols) for _ in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list3 = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_list1 + password_list2 + password_list3
    random.shuffle(password_list)

    password = "".join(password_list)

    # for char in password_list:
    #   password += char

    input_pwd.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_web.get()

    email = input_mail.get()
    password = input_pwd.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title = "oops",message= "Please make sure you haven't left any fields empty!")
    else:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(data,data_file,indent = 4)
        finally:
            input_web.delete(0, END)
            input_pwd.delete(0, END)

def find_password():
    website = input_web.get()
    try:

        with open ("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title = "Error",message = "No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title= website,message = f"Email:{email}\n Password:{password}")
        else:
            messagebox.showinfo(title= "Error",message = f"No details for {website} exists")
# ---------------------------- UI SETUP ------------------------------- #

from holoviews.plotting.bokeh.util import pad_width

window = Tk()
window.config(padx = 50, pady = 50)
window.title("Password Manager")
lock_img = PhotoImage(file = "logo.png")
canvas = Canvas(width = 200, height = 200)
canvas.create_image(100,100,image = lock_img)
canvas.grid(column =1,row = 0)
label_web = Label(text = "website")


label_web.grid(column = 0,row = 1)
input_web = Entry(width = 35)
input_web.focus()
input_web.grid(column =1, row =1, columnspan = 2)



button_search = Button(text = "Search",width = 30,command = find_password)
button_search.grid(column =3,row =1)
label_2 =Label(text = "Email/Username")
label_2.grid(column =0,row =2)
input_mail = Entry(width = 35)
input_mail.insert(0,"a.selvam3e@gmail.com")
input_mail.grid(column =1,row=2,columnspan = 2)
label_3 = Label(text = "Password")
label_3.grid(column = 0,row = 3)
input_pwd = Entry(width = 21)

input_pwd.grid(column = 1, row =3)
button_genpwd = Button(text = "Generate Password",command = generate_password)
button_genpwd.grid(column = 2,row =3)
button_add = Button(text = "Add",width = 36,command = save)
button_add.grid(column =1,row = 4, columnspan = 2)










window.mainloop()