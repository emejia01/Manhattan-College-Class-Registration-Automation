"""
This file contains the main python code for the GUI that the user will be presented with.
The file brings all the other files together by importing the modules and using them collectively
to build the application.

Created by: Erik Mejia
"""

from GUI_classes_and_functions import *
import Program_text
import web_automator
# webbrowser package is used to open hyperlink window
import webbrowser

# Function used for hyperlinks in GUI
def hyperlink_callback(url):
    webbrowser.open_new(url)

# Function assigned to 'Run Bot' button to begin automation process
def run_bot():
    class_list = []

    # Displays updated status bar
    GUI_fields.status_label.config(text='Status: STARTING UP. PLEASE WAIT...', bg='#FFFF00', fg='#FF0000')
    master.after(300, GUI_fields.status_label.grid(row=11))
    master.update()

    if len(CRN_fields.crn1_entry_box.get()) > 0:
        class_list.append(CRN_fields.crn1_entry_box.get())
    if len(CRN_fields.crn2_entry_box.get()) > 0:
        class_list.append(CRN_fields.crn2_entry_box.get())
    if len(CRN_fields.crn3_entry_box.get()) > 0:
        class_list.append(CRN_fields.crn3_entry_box.get())
    if len(CRN_fields.crn4_entry_box.get()) > 0:
        class_list.append(CRN_fields.crn4_entry_box.get())

    username = GUI_fields.username_entry_field.get()
    password = GUI_fields.password_entry_field.get()
    path = GUI_fields.file_path_entry_field.get()

    # Calls function to run automation bot
    status = web_automator.bot(username, password, class_list, path)

    # Updates status bar; Notifies user of errors, successful execution, or invalid credentials.
    if status == 'invalid':
        GUI_fields.status_label.config(text='INVALID USERNAME OR PASSWORD. Please restart program and try again.', fg='#FF0000')
        master.update()
    elif status == 'success':
        GUI_fields.status_label.config(text='AUTOMATION SUCCESSFULLY EXECUTED!', fg='#FF0000')
        master.update()
    else:
        GUI_fields.status_label.config(text='ERROR OCCURRED. Please try again.', fg='#FF0000')


# Create the main GUI window; Will also align GUI objects and elements
master = Tk()

# Configure main window attributes
master.title('MANHATTAN COLLEGE Class Registration Automation')
master.geometry('1000x800')
master.config(bg='#336e7b')

# Creates and configures title label
title = Label(master, text=Program_text.title, bg='#336e7b')
title.config(font=('Helvetica', 24))
title.grid(row=0)

# Creates and aligns direction label
directions = Label(master, text=Program_text.directions, bg='#336e7b')
directions.grid(row=1)

# Creates Login label
login_label = Label(master, text='LOGIN:', bg='#336e7b')
login_label.config(font=('Helvetica', 18))
login_label.grid(row=2)

# Creates GUI objects for entry fields and buttons
GUI_fields = EntryFields(master)
GUI_buttons = ProgramButtons(master)
CRN_fields = CRN(master)

# Aligns Username and Password entry fields
GUI_fields.username_entry_field.grid(row=3, column=0)
GUI_fields.password_entry_field.grid(row=4, column=0)

# Creates and aligns email label
email_label = Label(master, text='@manhattan.edu', bg='#336e7b')
email_label.grid(row=3, sticky='E', padx=250)

# Align CRN entry fields
CRN_fields.crn1_entry_box.grid(row=5)
CRN_fields.crn2_entry_box.grid(row=6)
CRN_fields.crn3_entry_box.grid(row=7)
CRN_fields.crn4_entry_box.grid(row=8)

# Aligns GUI buttons and sets 'Run Button' to trigger function call
GUI_buttons.run_button.grid(row=9)
GUI_buttons.run_button.config(command=run_bot)
GUI_buttons.quit_button.grid(row=10)

# Aligns status label filepath entry field
GUI_fields.status_label.grid(row=11)
GUI_fields.file_path_entry_field.grid(row=12)

# Creates and aligns disclaimer label
disclaimer_label = Label(master, text=Program_text.disclaimer, bg='#336e7b')
disclaimer_label.grid(row=13)

# Creates hyperlink to download ChromeDriver
chrome_driver_link = Label(master, text='Click here to download ChromeDriver', fg='blue', bg='#A9A9A9')
chrome_driver_link.grid(row=14, sticky='E', padx=200)
chrome_driver_link.bind('<Button-1>', lambda e: hyperlink_callback('https://chromedriver.chromium.org/downloads'))

# Creates hyperlink to read more in-depth instructions
instructions_link = Label(master, text='Click here for in-depth instructions', fg='blue', bg='#A9A9A9')
instructions_link.grid(row=14, sticky='W', padx=200)
instructions_link.bind('<Button-1>', lambda e: hyperlink_callback('https://github.com/emejia01/Manhattan-College-Class-Registration-Automation/blob/master/README.md'))

master.mainloop()