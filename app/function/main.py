from tkinter import *


# Начало программы
def main():
  # tkinter
  root = Tk()

  def donothing():
    window = Toplevel(root)
    window.title("Программа по обработке изображений")
    window.geometry('1080x600')

  def help_about():
    window = Toplevel(root)
    window.title("About")
    window.geometry('300x300')

  # Menu
  # https://www.tutorialspoint.com/python/tk_menu.htm | https://younglinux.info/tkinter/menu.php
  menubar = Menu(root)

  filemenu = Menu(menubar, tearoff=0)
  # filemenu.add_command(label="New")
  # filemenu.add_command(label="Open", command=donothing)
  # filemenu.add_command(label="Save", command=donothing)
  # filemenu.add_command(label="Save as...", command=donothing)
  # filemenu.add_command(label="Close", command=root.quit)

  filemenu.add_separator()

  filemenu.add_command(label="Выход", command=root.quit)
  menubar.add_cascade(label="Файл", menu=filemenu)

  helpmenu = Menu(menubar, tearoff=0)
  # helpmenu.add_command(label="Help Index", command=donothing)
  helpmenu.add_command(label="О программе", command=help_about)
  menubar.add_cascade(label="Справка", menu=helpmenu)

  root.config(menu=menubar)

  root.title("Программа по обработке изображений")
  root.geometry('1080x600')
  root.config(bg='#FFE4B5')  # цвет поля
  root.resizable(False, False) # отмена ресайза окна
  print("Program run \n\n")

  return root
