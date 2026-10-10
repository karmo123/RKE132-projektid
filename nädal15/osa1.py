import tkinter as tk

root = tk.Tk()
root.title("Greeting")
root.geometry("500x300")
root.grid_columnconfigure(0, weight=1)


def say_hello():
    greeting_label.config(text="Hello, world!")


greeting_label = tk.Label(root, text="nothing to see here yet")
greeting_label.grid(row=0, column=0, pady=10)

hello_button = tk.Button(root, text="Click me", command=say_hello)
hello_button.grid(row=1, column=0, pady=10)

root.mainloop()