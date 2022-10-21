from tkinter import *

"""
    Application
    ~~~~~~~
    тест
"""


class Application:
  def __init__(self):
    self.root = Tk()
    self.test = 'ddk'

  def title(self):
    self.test = '111'

  # Начало программы
  def start(self):
    self.root.title("Программа по обработке изображений")
    self.root.geometry('1080x600')
    self.root.config(bg='#FFE4B5')  # цвет поля
    print("Program run \n\n")

    return self.root
