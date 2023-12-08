import pymysql
import tkinter as tk
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkFrame, CTkImage
from PIL import ImageTk, Image
from tkinter import messagebox
import subprocess

app = CTk()
app.geometry("600x440")
app.title('Login')


# Function to handle button click
def login_button():
    # Get username and password from the entry fields
    username = entry1.get()
    password = entry2.get()

    # Check if the user has signed up
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password='',
            database="login_db"
        )

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cursor.fetchone()

        if user:
            if len(password) <= 8 and user[2] == password:
                # Successful login
                messagebox.showinfo("Success", "Login successful!")
                app.destroy()
                subprocess.run(["python", "final.py"])
            else:
                messagebox.showerror("Error", "Invalid password! Password should be up to 8 characters.")
        else:
            messagebox.showerror("Error", "User not found.")
    except pymysql.connect.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        conn.close()

# Resize img1
original_img1 = Image.open("loginbackground.png")
resized_img1 = original_img1.resize((1950, 1000))
img1 = ImageTk.PhotoImage(resized_img1)

l1 = CTkLabel(master=app, image=img1)
l1.pack()

frame = CTkFrame(master=l1, width=350, height=500, corner_radius=20, bg_color='#1a1a1a', fg_color="#eeeeee")
frame.place(relx=0.5, rely=0.45, anchor="center")

logo_img = Image.open("logo.png") 
resized_logo_img = logo_img.resize((150, 150)) 
ctk_logo_img = ImageTk.PhotoImage(resized_logo_img) 

logo_label = CTkLabel(master=app, image=ctk_logo_img, text="", fg_color="#eeeeee")
logo_label.place(relx=0.5, rely=0.25, anchor="center")

logo_title = CTkLabel(master=frame, text="Burial Assistance System", font=('Century Gothic', 15), text_color='#1a1a1a')
logo_title.place(x=90, y=150)

login = CTkLabel(master=frame, text="Log in to your account", font=('Century Gothic', 12 ), text_color='#1a1a1a')
login.place(x=50, y=180)

username_label = CTkLabel(master=frame, text="Username", font=('Century Gothic', 15))
username_label.place(x=50, y=210)

password_label = CTkLabel(master=frame, text="Password", font=('Century Gothic', 15))
password_label.place(x=50, y=270)

entry1 = CTkEntry(master=frame, width=250)
entry1.place(x=50, y=240)

entry2 = CTkEntry(master=frame, width=250, show="*")
entry2.place(x=50, y=300)


button1 = CTkButton(master=frame, width=250, height=30, text="Login", text_color = '#0ddb02', command=login_button, corner_radius=6, fg_color='#383838')
button1.place(x=50, y=370)

app.mainloop()
