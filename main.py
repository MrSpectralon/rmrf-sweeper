import tkinter as tk

def print_entered_value(e):
    value = e.get()
    print("You entered :", value)

def make_text_field(window, lable_text, default_value) ->tk.Entry:
    label = tk.Label(window, text=lable_text)
    label.pack()
    entry = tk.Entry(conf_window)
    entry.insert(0, default_value)
    entry.pack()
    return entry


if __name__ == "__main__":
    conf_window = tk.Tk()
    conf_window.title("PythonExamples.org")
    conf_window.geometry("300x200")
    size_x = make_text_field(conf_window, "Size X: ", "1337")
    button = tk.Button(conf_window, text="Submit", command=lambda: print_entered_value(size_x))
    button.pack(side=tk.LEFT)
    exit_button = tk.Button(conf_window, text="EXIT", command=conf_window.quit)
    exit_button.pack(side=tk.RIGHT)

    conf_window.mainloop()
