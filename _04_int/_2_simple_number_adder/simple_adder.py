"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
from tkinter import simpledialog
import math
if __name__ == '__main__':

    number=simpledialog.askinteger(title="number", prompt="type any number")
    numbere=simpledialog.askinteger(title="number", prompt= "put another number you want to add")
    number+numbere
