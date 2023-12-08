import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to connect to the database
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='burialassistance_db',
    )
    return conn

# Function to execute a SELECT query
def execute_select_query(query, params=None):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result

# Function to execute INSERT, UPDATE, DELETE, DISPLAY, SEARCH queries
def execute_query(query, params=None):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

def search_function(value):
    query = "SELECT * FROM burial WHERE APPLICANTID=%s OR APPLICANTNAME=%s OR AGE=%s OR GENDER=%s OR ADDRESS=%s OR FAMILYINCOME=%s OR EMAILADDRESS=%s OR PHONENUMBER=%s OR DECEASEDNAME=%s OR CAUSEOFDEATH=%s OR GENDER=%s"
    params = (value, value, value, value, value, value, value, value, value, value, value)
    result = execute_select_query(query, params)
    display_result(result)

def add_function():
    try:
        applicantname = ph1.get()
        age = int(ph2.get()) 
        address = ph3.get()
        email = ph4.get()
        number = int(ph5.get())
        deceasedname = ph6.get()
        causeofdeath = ph7.get()
        gender = gender_var.get()
        familyincome = familyincome_var.get()

        if not (applicantname and age and gender and address and email and number and deceasedname and causeofdeath):
            messagebox.showinfo("Error", "Please fill up the blank entry.")
            return

        query = "INSERT INTO burial (APPLICANTNAME, AGE, GENDER, ADDRESS, FAMILYINCOME, EMAILADDRESS, PHONENUMBER, DECEASEDNAME, CAUSEOFDEATH) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params = (applicantname, age, gender, address, familyincome, email, number, deceasedname, causeofdeath)
        execute_query(query, params)
        refresh_table()

    except ValueError:
        messagebox.showinfo("Error", "Please enter valid age and phone number as integers.")
        return


def update_function():
    try:
        selected_item = my_tree.selection()
        if not selected_item:
            messagebox.showinfo("Error", "Please select a data row.")
            return

        selectedApplicantID = my_tree.item(selected_item)['values'][0]
        applicantname = ph1.get()
        age = int(ph2.get())
        address = ph3.get()
        email = ph4.get()
        number = int(ph5.get())
        deceasedname = ph6.get()
        causeofdeath = ph7.get()
        gender = gender_var.get()
        familyincome = familyincome_var.get()
    
    
        if not (applicantname and age and address and deceasedname and causeofdeath and gender and familyincome):
            messagebox.showinfo("Error", "Please fill up all the fields.")
            return

        query = "UPDATE burial SET APPLICANTNAME=%s, AGE=%s, GENDER=%s, ADDRESS=%s, FAMILYINCOME=%s, EMAILADDRESS=%s, PHONENUMBER=%s, DECEASEDNAME=%s, CAUSEOFDEATH=%s WHERE APPLICANTID=%s"
        params = (applicantname, age, gender, address, familyincome, email, number, deceasedname, causeofdeath, selectedApplicantID)  # Corrected the order and added missing parameter
        execute_query(query, params)
        refresh_table()
    
    except ValueError:
        messagebox.showinfo("Error", "Please enter valid age and phone number as integers.")
        return    
    

def delete_function():
    decision = messagebox.askquestion("Warning!!", "Delete the selected data?")
    if decision != "yes":
        return

    selected_item = my_tree.selection()
    if not selected_item:
        messagebox.showinfo("Error", "Please select a data row.")
        return

    selectedApplicantID = my_tree.item(selected_item)['values'][0]
    query = "DELETE FROM burial WHERE APPLICANTID=%s"
    params = (selectedApplicantID,)
    execute_query(query, params)
    refresh_table()

def sort_by_applicant_name():
    query = "SELECT * FROM burial ORDER BY APPLICANTNAME"
    result = execute_select_query(query)
    display_result(result)

def display_function():
    query = "SELECT * FROM burial"
    result = execute_select_query(query)
    display_result(result)
    clear_entries()

def refresh_table():
    query = "SELECT * FROM burial"
    result = execute_select_query(query)
    display_result(result)

def display_result(result):
    my_tree.delete(*my_tree.get_children())
    for row in result:
        my_tree.insert("", "end", values=row)

def on_tree_double_click(event):
    item = my_tree.selection()
    if item:
        selectedApplicantID = my_tree.item(item)['values'][0]
        query = "SELECT * FROM burial WHERE APPLICANTID=%s"
        params = (selectedApplicantID,)
        result = execute_select_query(query, params)
        set_placeholder(result[0])

def set_placeholder(values):
    ph1.set(values[1])  # APPLICANTNAME
    ph2.set(values[2])  # AGE
    ph3.set(values[4])  # ADDRESS
    ph4.set(values[6])  # EMAILADDRESS
    ph5.set(values[7])  # PHONENUMBER
    ph6.set(values[8])  # DECEASEDNAME
    ph7.set(values[9])  # CAUSEOFDEATH
    familyincome_var.set(values[5])
    gender_var.set(values[3])  # GENDER

def clear_entries():
    ph1.set("")  # APPLICANTNAME
    ph2.set("")  # AGE
    ph3.set("")  # ADDRESS
    ph4.set("")  # EMAILADDRESS
    ph5.set("")  # PHONENUMBER
    ph6.set("")  # DECEASEDNAME
    ph7.set("")  # CAUSEOFDEATH
    familyincome_var.set("0 - 10 000")
    gender_var.set("Male")  # Reset the combobox

root = Tk()
root.title("Burial Assistance System")
root.geometry("1100x600")
# Load the background image using PIL (Pillow)
bg_image = Image.open("basbg.jpg")
bg_image = bg_image.resize((1550, 800))
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a Label widget to display the background image
bg_label = Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# GUI label
label = Label(root, text="Burial Assistance System", bg='black', fg='#0ddb02', font=('Cooper Black', 40))
label.place(relx=0.5, rely=0.1, anchor='e')

# Function to create a rounded rectangle
def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]
    canvas.create_polygon(points, **kwargs, smooth=True)

# Function to create text inside the rectangle
def create_text_inside_rectangle(canvas, x, y, text, **kwargs):
    return canvas.create_text(x, y, text=text, **kwargs)

# Create a Canvas widget for the rounded rectangle
canvas_width = 550  # Adjust the width of the Canvas
canvas_height = 650  # Adjust the height of the Canvas
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='black', highlightthickness=0)
canvas.grid(row=1, column=0, padx=0, pady=100, sticky='w')

# Create a rounded rectangle on the canvas
rounded_rect = create_rounded_rectangle(canvas, 50, 70, canvas_width, canvas_height, 50, fill='#1f1f1f')

# Create text inside the rectangle
create_text_inside_rectangle(canvas, 150, 200, "Applicant Name", font=('Bookman Old Style', 14), fill='#0ddb02')
create_text_inside_rectangle(canvas, 166, 240, "Age", font=('Bookman Old Style', 14), fill='#0ddb02')
create_text_inside_rectangle(canvas, 380, 240, "Gender", font=('Bookman Old Style', 14), fill='#0ddb02')
create_text_inside_rectangle(canvas, 187, 280, "Address", font=('Bookman Old Style', 14), fill='#0ddb02')
create_text_inside_rectangle(canvas, 150, 320, "Family Income", font=('Bookman Old Style', 14), fill='#0ddb02')
create_text_inside_rectangle(canvas, 150, 360, "E-Mail Address", font=('Bookman Old Style', 14), fill='#0ddb02')
create_text_inside_rectangle(canvas, 150, 400, "Phone Number", font=('Bookman Old Style', 14), fill='#0ddb02')
create_text_inside_rectangle(canvas, 150, 440, "Deceased Name", font=('Bookman Old Style', 14), fill='#0ddb02')
create_text_inside_rectangle(canvas, 150, 480, "Cause of Death", font=('Bookman Old Style', 14), fill='#0ddb02')

# Entry widgets
ph1 = StringVar()
ph2 = StringVar()
ph3 = StringVar()
ph4 = StringVar()
ph5 = StringVar()
ph6 = StringVar()
ph7 = StringVar()
entry_x = 250  # Adjust the x-coordinate for the entry widgets

# Gender and Family Income Combobox
gender_var = StringVar()
gender_combobox = ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female"], state="readonly", font=('Arial', 13), width=4)
gender_combobox.set("Male")

familyincome_var = StringVar()
familyincome_combobox = ttk.Combobox(root, textvariable=familyincome_var, values=["0 - 10 000", "10 000 - 20 000", "20 000 - 30 000", "30 000 - 40 000", "40 000 - 50 000", "50 000 - 60 000", "60 000 - 70 000", "80 000 - 90 000" , "90 000 - 100 000"], state="readonly", font=('Arial', 13), width=18)
familyincome_combobox.set("0 - 10 000")

# entry
search_entry = Entry(root, width=31, bd=2, font=('Arial', 10))
applicantnameEntry = Entry(root, width=25, bd=3, font=('Arial', 12), textvariable=ph1)
ageEntry = Entry(root, width=6, bd=3, font=('Arial', 12), textvariable=ph2)
addressEntry = Entry(root, width=25, bd=3, font=('Arial', 12), textvariable=ph3)
emailEntry = Entry(root, width=25, bd=3, font=('Arial', 12), textvariable=ph4)
numberEntry = Entry(root, width=25, bd=3, font=('Arial', 12), textvariable=ph5)
deceasednameEntry = Entry(root, width=25, bd=3, font=('Arial', 12), textvariable=ph6)
causeofdeathEntry = Entry(root, width=25, bd=3, font=('Arial', 12), textvariable=ph7)

# Create Entry widgets inside the blue rectangle
canvas.create_window(entry_x, 200, window=applicantnameEntry, anchor='w')
canvas.create_window(entry_x, 240, window=ageEntry, anchor='w')
canvas.create_window(entry_x, 280, window=addressEntry, anchor='w')
canvas.create_window(entry_x, 320, window=familyincome_combobox, anchor='w')
canvas.create_window(entry_x, 360, window=emailEntry, anchor='w')
canvas.create_window(entry_x, 400, window=numberEntry, anchor='w')
canvas.create_window(entry_x, 440, window=deceasednameEntry, anchor='w')
canvas.create_window(entry_x, 480, window=causeofdeathEntry, anchor='w')
canvas.create_window(entry_x + 203, 228, window=gender_combobox, anchor='n')

# Buttons for Add, Update, Delete, and Display
search_button = Button(root, text="Search", command=lambda: search_function(search_entry.get()), bd=3, font=('Arial', 10), bg='#0ddb02')
sort_button = Button(root, text="A - Z", command=sort_by_applicant_name, bd=3, font=('Arial', 9), bg='#0ddb02', width=6, height=1)
add_button = Button(root, text="ADD", command=add_function, bd=3, font=('Arial Bold', 10), bg='#0ddb02', width=10, height=2)
update_button = Button(root, text="UPDATE", command=update_function, bd=3, font=('Arial Bold', 10), bg='#0ddb02', width=10, height=2)
delete_button = Button(root, text="DELETE", command=delete_function, bd=3, font=('Arial Bold', 10), bg='#0ddb02', width=10, height=2)
display_button = Button(root, text="DISPLAY", command=display_function, bd=3, font=('Arial Bold', 10), bg='#0ddb02', width=10, height=2)

# Create buttons inside the blue rectangle
button_y = 570  # Adjust the y-coordinate for the buttons
canvas.create_window(150, button_y, window=add_button, anchor='center')
canvas.create_window(250, button_y, window=update_button, anchor='center')
canvas.create_window(450, button_y, window=delete_button, anchor='center')
canvas.create_window(350, button_y, window=display_button, anchor='center')
canvas.create_window(entry_x + 110, 90, window=search_entry, anchor='n')
canvas.create_window(entry_x + 260, 87, window=search_button, anchor='n')
canvas.create_window(entry_x + 260, 125, window=sort_button, anchor='n')

def configure_treeview():
    style = ttk.Style()
    font_size = 10

    style.configure('Treeview.Heading', font=('Garuda', font_size ))
    style.configure('Treeview', font=('Garuda', font_size))
    style.map('Treeview', background=[('selected', '#6b6b6b')], foreground=[('selected', '#0ddb02')])
    
def display_result(result):
    my_tree.delete(*my_tree.get_children())
    for row in result:
        # Extract relevant values
        family_income = row

        # Check if monthly family income is 20,000 or above
        if "20 000 - 30 000" in family_income or "30 000 - 40 000" in family_income or "40 000 - 50 000" in family_income or "50 000 - 60 000" in family_income or "60 000 - 70 000" in family_income or "70 000 - 80 000" in family_income or "80 000 - 90 000" in family_income or "90 000 - 100 000" in family_income:
            my_tree.insert("", "end", values=row, tags='rejected')  # Use a tag for rejected rows
        else: 
            my_tree.insert("", "end", values=row)

    # Apply red highlighting for rejected rows
    my_tree.tag_configure('rejected', background='red', foreground='white')


my_tree = ttk.Treeview(root)
my_tree['columns'] = ("Applicant ID", "Applicant Name", "Age", "Gender", "Address", "Family Income", "E-Mail Address", "Phone Number", "Deceased Name", "Cause of Death")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Applicant ID", anchor=W, width=80)
my_tree.column("Applicant Name", anchor=W, width=120)
my_tree.column("Age", anchor=W, width=32)
my_tree.column("Gender", anchor=W, width=52)
my_tree.column("Address", anchor=W, width=65)
my_tree.column("Family Income", anchor=W, width=155)
my_tree.column("E-Mail Address", anchor=W, width=120)
my_tree.column("Phone Number", anchor=W, width=105)
my_tree.column("Deceased Name", anchor=W, width=120)
my_tree.column("Cause of Death", anchor=W, width=120)

my_tree.heading("Applicant ID", text="Applicant ID", anchor=W)
my_tree.heading("Applicant Name", text="Applicant Name", anchor=W)
my_tree.heading("Age", text="Age", anchor=W)
my_tree.heading("Gender", text="Gender", anchor=W)
my_tree.heading("Address", text="Address", anchor=W)
my_tree.heading("Family Income", text="Monthly Family Income", anchor=W)
my_tree.heading("E-Mail Address", text="E-Mail Address", anchor=W)
my_tree.heading("Phone Number", text="Phone Number", anchor=W)
my_tree.heading("Deceased Name", text="Deceased Name", anchor=W)
my_tree.heading("Cause of Death", text="Cause of Death", anchor=W)
my_tree.grid(row=1, column=1, padx=10, pady=250, sticky='s', ipady=70)

configure_treeview()

my_tree.bind("<Double-1>", on_tree_double_click)

root.mainloop()
