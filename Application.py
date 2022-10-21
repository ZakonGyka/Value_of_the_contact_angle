from app.function.program_square import program_square
from app.function.program_canny import program_canny
from tkinter import *


# Открытие окна 1
def square():
  program_square(start_window)


# Открытие окна 2
def canny():
  program_canny(start_window)


start_window = Tk()
start_window.title("Программа по обработке изображений")
start_window.geometry("420x200")
header = Label(text="Выберите программу для обработки изображений", padx=15, pady=10)
header.grid(row=0, column=0, sticky=W)

Canny_checkbutton = Button(start_window, text='Canny filter', command=canny)
Canny_checkbutton.config(width=17, height=2, bg='red', fg='black')
Canny_checkbutton.place(x=20, y=80)

Square_checkbutton = Button(start_window, text='Square filter', command=square)
Square_checkbutton.config(width=17, height=2, bg='#9ACD32', fg='black')
Square_checkbutton.place(x=220, y=80)

start_window.mainloop()
print("Program run!\n\n")
