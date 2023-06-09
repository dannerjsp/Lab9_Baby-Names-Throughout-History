# ******************************************************************************
# Author:           Danner Peter
# Lab:              Lab 8
# Date:             04 June 2023
# Description:      Progress update for final program project. Developed a UI
#                   which asks the user to enter a name and a gender (M/F).
#                   After which, a query is run through a database that was
#                   provided. The results of which are list of how many
#                   babies, throughout the years, that the name and gender
#                   matched.
# Input:            User inputs a name and a gender via a UI window.
# Output:           A list of tuples that are the result of a query that is
#                   run within the parameters asked by the user's input.
#
# ******************************************************************************

import tkinter as tk
from tkinter import ttk
from name import Name
from tkinter.messagebox import showinfo


def button_1_click():
    """
    Assigns a function for when the user clicks button_1.
    :return: list: lst_names. A list of names that have been pulled from the
    user's query via the getNamesByNameAndGender method from the Name class
    in name.py.
    """
    lst_names = Name.getNamesByNameAndGender(str_Name.get(), str_Gender.get())

    for name in lst_names:
        print(name.Name, name.Gender, name.Year, name.Births)
        tpl = (name.Name, name.Gender, name.Year, name.Births)

        tree.insert('', tk.END, values=tpl)


def button_2_click():
    """
    Assigns a function for when the user clicks button_2, which kills the
    program.
    :return: None.
    """
    root.destroy()


# Uses tkinter to creates the root window.
root = tk.Tk()
root.title("Baby Names Throughout History")
root.geometry("838x353")
# root.resizable(False, False)    # Keeps window from entering full screen


# Sets up Frame 1
frame_1 = ttk.Frame(root, padding="10 10 10 10")
frame_1.grid(column=0, row=0)

# Bind a text entry field to a StringVar object.
str_Name = tk.StringVar()

# Constructors for labels and text entry fields for Name.
label_name = ttk.Label(frame_1, text="Please Enter a First Name: ")
label_name.grid(column=0, row=0, sticky=tk.W)
text_name = ttk.Entry(frame_1, width=30, textvariable=str_Name)
text_name.grid(column=1, row=0, sticky=tk.W)



# # # # # # # # # # # # # # # # # # # #


# # Constructors for labels and text entry fields for Gender.
# label_gender = ttk.Label(frame_1, text="Enter Gender (M/F): ")
# label_gender.grid(column=0, row=1, sticky=tk.W)
# text_gender = ttk.Entry(frame_1, width=2, textvariable=str_Gender)
# str_Gender.set("?")
# text_gender.grid(column=1, row=1, sticky=tk.W)


# Sets up Frame 2
frame_2 = ttk.Frame(root, padding="10 10 10")
frame_2.grid(column=0, row=1)

selected_gender = ttk.Label(frame_2, text="Select a Gender: ")
selected_gender.grid(column=0, row=1, sticky=tk.W)

# Bind the radiobutton field to a StringVar object.
str_Gender = tk.StringVar()

# Male radiobutton
ttk.Radiobutton(frame_2, text='Male', variable=str_Gender, value='M').grid(
    column=1, row=1, sticky=tk.W)

# Female radiobutton
ttk.Radiobutton(frame_2, text='Female', variable=str_Gender,
                value='F').grid(
    column=2, row=1, sticky=tk.W)

# Trans radiobutton
# ttk.Radiobutton(frame_2, text='Transgender', variable=gendr,
# value='Transgender').grid(
# column=3, row=1, sticky=tk.W)


# Assigning buttons 1 & 2 a command once pressed.
button_1 = ttk.Button(frame_2, text="Run Query", command=button_1_click)
button_2 = ttk.Button(frame_2, text="End Query", command=button_2_click)

# Positions the buttons in the frame.
button_1.grid(column=1, row=3, sticky=tk.W)
button_2.grid(column=2, row=3, sticky=tk.W)

# # # # # # # # # # # # # # # # # # # #

# Sets up Frame 3
frame_3 = ttk.Frame(root, padding="10 10 10")
frame_3.grid(column=0, row=2)


# The beginning of the Treeview that we've developed in Module 8.
columns = ('Name', 'Gender', 'Year', 'Babies')
tree = ttk.Treeview(frame_3, columns=columns, show='headings')
tree.heading('Name', text='Name')
tree.heading('Gender', text='Gender')
tree.heading('Year', text='Year')
tree.heading('Babies', text='Births')
tree.grid(column=1, row=4, sticky=tk.NSEW)

scrollbar = ttk.Scrollbar(frame_3, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(column=2, row=4, sticky=tk.NSEW)

root.mainloop()
