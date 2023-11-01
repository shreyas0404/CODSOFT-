import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
import json

class TodoListApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Todo List Application")
        self.geometry("400x400")
        style = Style(theme="flatly")
        style.configure("Custon.TEntry", foreground="magenta")

        
        self.todo_input = ttk.Entry(self, font=("Times New Roman", 16), width=30, style="Custon.TEntry")
            
        self.todo_input.pack(pady=10)

        
        self.todo_input.insert(0, "Enter your tasks here...")

    
        self.todo_input.bind("<FocusIn>", self.empty_placeholder)

        self.todo_input.bind("<FocusOut>", self.fill_placeholder)

        ttk.Button(self, text="Add", command=self.add_task).pack(pady=5)


        self.todo_list = tk.Listbox(self, font=("Times New Roman", 16), height=10, selectmode=tk.NONE)
        self.todo_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        ttk.Button(self, text="Done", style="success.TButton",command=self.task_done).pack(side=tk.LEFT, padx=10, pady=10)
                   
        ttk.Button(self, text="Delete", style="danger.TButton",command=self.remove_task).pack(side=tk.RIGHT, padx=10, pady=10)
                   
        ttk.Button(self, text="View Stats", style="info.TButton",command=self.track_stats).pack(side=tk.BOTTOM, pady=10)
                   
        
        self.load_tasks()
    
    def track_stats(self):
        done_count = 0
        total_count = self.todo_list.size()
        for i in range(total_count):
            if self.todo_list.itemcget(i, "fg") == "green":
                done_count += 1
        messagebox.showinfo("Task Statistics", f"Total tasks: {total_count}\nCompleted tasks: {done_count}")

    def add_task(self):
        task = self.todo_input.get()
        if task != "Enter your tasks here...":
            self.todo_list.insert(tk.END, task)
            self.todo_list.itemconfig(tk.END, fg="darkblue")
            self.todo_input.delete(0, tk.END)
            self.save_tasks()

    def task_done(self):
        todo_index = self.todo_list.curselection()
        if todo_index:
            self.todo_list.itemconfig(todo_index, fg="green")
            self.save_tasks()
    
    def remove_task(self):
        todo_index = self.todo_list.curselection()
        if todo_index:
            self.todo_list.delete(todo_index)
            self.save_tasks()
    
    def empty_placeholder(self, event):
        if self.todo_input.get() == "Enter your tasks here...":
            self.todo_input.delete(0, tk.END)
            self.todo_input.configure(style="TEntry")

    def fill_placeholder(self, event):
        if self.todo_input.get() == "":
            self.todo_input.insert(0, "Enter your tasks here...")
            self.todo_input.configure(style="Custom.TEntry")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
                for task in data:
                    self.todo_list.insert(tk.END, task["text"])
                    self.todo_list.itemconfig(tk.END, fg=task["color"])
        except FileNotFoundError:
            pass
    
    def save_tasks(self):
        data = []
        for i in range(self.todo_list.size()):
            text = self.todo_list.get(i)
            color = self.todo_list.itemcget(i, "fg")
            data.append({"text": text, "color": color})
        with open("tasks.json", "w") as f:
            json.dump(data, f)

if __name__ == '__main__':
    app = TodoListApp()

    app.mainloop()
