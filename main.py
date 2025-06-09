from tkinter import *
from tkinter import messagebox
from password_generator import PasswordGenerator
import pyperclip

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
    password_details = f"{website_str} | {email_str} | {password_str}\n"

    if len(website_str)==0 or len(email_str)==0 or len(password_str)==0:
        messagebox.showinfo(title="Empty", message="Please fill in all the entries")

    else:
        ok_to_save = messagebox.askokcancel(title="Website", message=f"These are the details entered:\n"
                                                        f"Website: {website_str}\n"
                                                        f"Email: {email_str}\n"
                                                        f"Password: {password_str}")
        if ok_to_save:
            with open("password.txt", "a") as password_file:
                password_file.write(password_details)
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

website_entry = Entry(width=48)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=48)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(END, "skylar@signaturecomputer.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

generate_password_button = Button(text="Generate Password", width=21, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=40, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
