import turtle
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    q=simpledialog.askstring(title="prompt", prompt="is your birthday today?")
    if q=="yes":
        messagebox.showinfo(title="", message= "Happy birthday")

    if q=="no":
        messagebox.showinfo(title= "", message= "Happy Unbirthday")
    else:
        messagebox.showinfo(title="", message="You suck, put yes or no")
