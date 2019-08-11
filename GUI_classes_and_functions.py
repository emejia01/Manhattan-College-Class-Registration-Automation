'''
This file contains the code for the Tkinter classes and functions that will be used
in the GUI of the program. They will create the various labels, entry fields, and buttons
that will be present in the program.

Created by: Erik Mejia
'''

# Tkinter will be used to create the GUI
from tkinter import *


# Entry_Fields class creates all the entry fields in the GUI.
class EntryFields:
    def __init__(self, master):
        # Create Username entry field
        self.username_entry_field = Entry(master, fg='#555')
        self.username_entry_field.insert(0, 'Username')
        self.username_entry_field.bind('<FocusIn>', self.username_text)
        self.username_entry_field.bind('<FocusOut>', self.is_Empty)

        # Create Password entry field
        self.password_entry_field = Entry(master, fg='#555')
        self.password_entry_field.insert(0, 'Password')
        self.password_entry_field.bind('<FocusOut>', self.is_Empty)
        self.password_entry_field.bind('<FocusIn>', self.password_text)

        # Create ChromeDriver path entry field and label
        self.file_path_entry_field = Entry(master)
        self.file_path_entry_label = Label(master, text='ChromeDriver FilePath:', bg='#778899')

        # Creates Status Label
        self.status_label = Label(master, text='', bg='#336e7b')

    # Function/Method to delete default text in Username entry field
    def username_text(self, event):
        if self.username_entry_field.get() == 'Username':
            self.username_entry_field.delete(0, END)

    # Function/Method to delete default text in Password entry field
    def password_text(self, event):
        self.password_entry_field.delete(0, END)
        self.password_entry_field.config(show='\u2022')

    # Function/Method checks if Username or Password entry fields are empty
    def is_Empty(self, event):
        if len(self.username_entry_field.get()) == 0:
            self.username_entry_field.insert(0, 'Username')
        if len(self.password_entry_field.get()) == 0:
            self.password_entry_field.config(show='')
            self.password_entry_field.insert(0, 'Password')


# ProgramButtons class creates the buttons that will be displayed in the GUI
class ProgramButtons:
    def __init__(self, master):
        # Create 'Run Bot' button
        self.run_button = Button(master, text='Run Bot')
        # Create the 'Quit' button
        self.quit_button = Button(master, text='Quit', command=master.quit)


# CRN class creates the entry boxes and labels for the CRN (Class Registration Number) that will be displayed in the GUI
class CRN:
    def __init__(self, master):
        # Creates the entry box and label for CRN 1
        self.crn1_entry_box = Entry(master)
        self.crn1_entry_label = Label(master, text='CRN 1', bg='#778899')

        # Creates the entry box and label for CRN 2
        self.crn2_entry_box = Entry(master)
        self.crn2_entry_label = Label(master, text='CRN 2', bg='#778899')

        # Creates the entry box and label for CRN 3
        self.crn3_entry_box = Entry(master)
        self.crn3_entry_label = Label(master, text='CRN 3', bg='#778899')

        # Creates the entry box and label for CRN 4
        self.crn4_entry_box = Entry(master)
        self.crn4_entry_label = Label(master, text='CRN 4', bg='#778899')