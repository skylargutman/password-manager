from tkinter import *
from tkinter import messagebox
from password_generator import PasswordGenerator
import pyperclip
import json

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    if website_entry.get() == "":
        messagebox.showinfo("Empty", "Please enter a website name")
    else:
        try:
            with open("password.json") as password_file:
                pw_s = json.load(password_file)
        except FileNotFoundError:
            messagebox.showinfo("No Passwords", "No password file found")
            website_entry.focus()
        else:
            try:
                email = pw_s[website_entry.get().lower()]["email"]
                password = pw_s[website_entry.get().lower()]["password"]
            except KeyError:
                messagebox.showinfo("No record", "There is no record of this website")
            else:
                messagebox.showinfo(f"Your {website_entry.get()} Credentials:", f"Email: {email}\n"
                                                     f"Password: {password}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_str = PasswordGenerator().password
    password_entry.delete(0,END)
    password_entry.insert(0,password_str)
    pyperclip.copy(password_str)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website_str = website_entry.get()
    email_str = email_entry.get()
    password_str = password_entry.get()
    # password_details = f"{website_str} | {email_str} | {password_str}\n"
    new_password = {
        website_str.lower():{
            "email": email_str,
            "password": password_str
        }
    }

    if len(website_str)==0 or len(email_str)==0 or len(password_str)==0:
        messagebox.showinfo(title="Empty", message="Please fill in all the entries")

    else:
        ok_to_save = messagebox.askokcancel(title="Website", message=f"These are the details entered:\n"
                                                        f"Website: {website_str}\n"
                                                        f"Email: {email_str}\n"
                                                        f"Password: {password_str}")
        if ok_to_save:
            try:
                with open("password.json", "r") as password_file:
                    pw_s = json.load(password_file)

            except FileNotFoundError:
                with open("password.json","w") as password_file:
                    # noinspection PyTypeChecker
                    json.dump(new_password, password_file, indent=4)
            else:
                pw_s.update(new_password)
                with open("password.json", "w") as password_file:
                    # noinspection PyTypeChecker
                    json.dump(pw_s, password_file, indent=4)
            finally:
                    website_entry.delete(0,END)
                    password_entry.delete(0,END)
        else:
            website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=30)
website_entry.grid(column=1,row=1,)
website_entry.focus()

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=50)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(END, "skylar@signaturecomputer.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=30)
password_entry.grid(column=1,row=3)

generate_password_button = Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=42, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
