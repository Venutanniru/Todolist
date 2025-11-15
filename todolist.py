"""
author, pythonplayground, 

help us grow our yt channel :) :  
https://www.youtube.com/@PythonPlayground-rbh

A small application that is a to do list

The user can add/remove tasks from the to do list. 

The app is in OOP (objected oritented programming) 

The tasks will be saved in a file named "tasks.txt" 

First run "pip install tkinter" 
"""

import tkinter as tk #pip install tkinter :) 
from tkinter import messagebox
import os

# default file to store tasks within it will be updated in real time
TASKS_FILE = "tasks.txt"

class ToDoApp:

    # Constructor
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("To do List")
        self.root.geometry("400x500") #400 by 500 px 
        self.root.configure(bg="#2C2F33") # darkish color 

        self.tasks = [] # contains list of tasks 
        self.load_tasks() # loads existing tasks from the tasks file :)

        self.create_widgets() # creates everything within the app
        self.root.mainloop() # for the app to keep running

    def create_widgets(self):
        """Create elements for the to do list application"""

        # the to do list label
        tk.Label(self.root, text="To do List", 
                 font=("Arial", 18, "bold"), 
                 fg="white", bg="#2C2F33").pack(pady=10)

        # entry to add the labels 
        self.task_entry = tk.Entry(self.root, font=("Arial", 14), width=25, bg="#23272A", fg="white")
        self.task_entry.pack(pady=10) # add a small padding from the top

        self.add_btn = tk.Button(self.root, text="Add Task", font=("Arial", 12, "bold"),
                                 command=self.add_task, bg="green", fg="white")
        self.add_btn.pack(pady=5) # add a small padding from the top 

        self.task_listbox = tk.Listbox(self.root, font=("Arial", 12), width=40, height=10,
                                       bg="#23272A", fg="white", selectbackground="#7289DA")
        self.task_listbox.pack(pady=10)
        self.update_listbox() # to add elements to the list box 

        self.delete_btn = tk.Button(self.root, text="Delete Task", font=("Arial", 12, "bold"),
                                    command=self.delete_task, bg="red", fg="white")
        self.delete_btn.pack(pady=5)

        self.clear_btn = tk.Button(self.root, text="Clear", font=("Arial", 12, "bold"),
                                   command=self.clear_tasks, bg="#99AAB5", fg="black")
        self.clear_btn.pack(pady=5)

    def add_task(self):
        """A function to add a new task to the list."""
        task = self.task_entry.get().strip() #strip is to remove spaces from start/end
        if task: # if task not empty
            self.tasks.append(task)
            self.update_listbox() # add th enew task to the textbox 
            self.task_entry.delete(0, tk.END) #after adding the task, clear the entry. 
            self.save_tasks()# save to the file.txt  
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        """Deletes the selected task."""
        try:
            selected_task = self.task_listbox.curselection()[0] # curselection()[0] will give the selected task :) 
            del self.tasks[selected_task] # remove the selected task from the list tasks 
            self.update_listbox() 
            self.save_tasks() # update and save the txt file
        except IndexError:
            messagebox.showwarning("Warning", "Please first select a task to delete.")

    def clear_tasks(self):
        """clears all tasks from the list."""
        if messagebox.askyesno("Confirm", "You are going to delete all tasks, confirm?"):
            self.tasks = []
            self.update_listbox()
            self.save_tasks()

    def update_listbox(self):
        """Updates the Listbox with tasks."""
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def save_tasks(self):
        """Saves tasks to a file."""
        with open(TASKS_FILE, "w") as file: #opens file in write mode (w) 
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        """Loads tasks from a file."""
        if os.path.exists(TASKS_FILE): #check if it exists 
            with open(TASKS_FILE, "r") as file: #opens file in read mode(r) 
                self.tasks = [line.strip() for line in file.readlines()]

if __name__ == "__main__": #ensures that the script runs only when executed directly, not when imported as a module in another script
    ToDoApp()
