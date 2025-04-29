# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
import json
from tkinter import messagebox
import random
import pyperclip



#----------------------GENERATE PASSWORD----------------------------------------------------------------------------#
#function to generate the password once the generate password button is clicked
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#list comprehension to create new list which contain random letters from letters list in range of 8 to 10
    password_list1 = [random.choice(letters) for _ in range(random.randint(8, 10))]


#list comprehension to create new list which contain random symbols from symbols list in range of 2 to 4
    password_list2 = [random.choice(symbols) for _ in range(random.randint(2, 4))]

#list comprehension to create new list which contain random numbers from numbers list in range of 2 to 4
    password_list3 = [random.choice(numbers) for _ in range(random.randint(2, 4))]

#new list created to concatenate all the letters, symbols and numbers together
    password_list = password_list1 + password_list2 + password_list3

#the contents of the list is shuffled to create hard password
    random.shuffle(password_list)

#list is converted to string by using join function which joins the contents of the list into a string
    password = "".join(password_list)

#Once the password is ready, it gets entered into the password field at the start by this insert function
    password_entry.insert(0, password)

#copies the password generated into the clipboard and its ready to paste in the site needed
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()

    email = email_entry.get()
    password = password_entry.get()

#dictionary created to pass it to json so that it gets stored in accessible format.
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
            website_entry .delete(0, END)
            password_entry.delete(0, END)

#--------------------------FIND PASSWORD---------------------------------------------------#
def find_password():
    website = website_entry .get()
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

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0,sticky = 'w')
email_label = Label(text="Email:")
email_label.grid(row=2, column=0,sticky = 'w')
password_label = Label(text="Password:")
password_label.grid(row=3, column=0,sticky = 'w')

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "a.selvam3e@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

