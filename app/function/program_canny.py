from tkinter import filedialog
from tkinter import *
from PIL import Image
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import array
import os
from app import Application
import numpy as np
import argparse
import glob
import cv2

# массив для списка фотографий
scan_photos = []


def program_canny(self_window=None):
    if self_window is not None:
        # закрываем передано окноX
        self_window.destroy()
        print("parent window is closed")

    def donothing():
        window = Toplevel(program2)
        window.title("Canny filter")
        window.geometry('1024x600')

    def help_about():
        window = Toplevel(program2)
        window.title("About")
        window.geometry('300x300')

    def P0r0g(c, g):
        for i in range(c.size[0]):
            for j in range(c.size[1]):
                if c.getpixel((i, j)) < g:
                    c.putpixel((i, j), 0)
        z = c.getbbox()
        c = c.crop(z)
        c.show()
        return z

    def auto_canny(image, sigma=0.33):
        # compute the median of the single channel pixel intensities
        v = np.median(image)

        # apply automatic Canny edge detection using the computed median
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        edged = cv2.Canny(image, lower, upper)

        # return the edged image
        return edged

    def Canny_filter():

        Canny_start()

    def Canny_start():
        global scan_photos

        if get_program_ready(show_error=True, output_in_console=False):
            sigma = float(field_threshold_filter.get())
            pic = []

            if len(scan_photos) > 0:
                for key, imagePath in enumerate(scan_photos):
                    image = cv2.imread(imagePath)
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

                    # apply Canny edge detection using a wide threshold, tight
                    # threshold, and automatically determined threshold
                    wide = cv2.Canny(blurred, 10, 200)
                    tight = cv2.Canny(blurred, 225, 250)
                    auto = auto_canny(blurred, sigma)

                    # show the images
                    # cv2.imshow("Original" + str(key), image)
                    # cv2.imshow("Edges" +  str(key), np.hstack([wide, tight, auto]))

                    cv2.imwrite("Images/Canny/" + str(key) + ".jpg", np.hstack([auto]))
                    # cv2.waitKey(0)
                    cv2.destroyAllWindows()

                    # if key == 0:
                    pic.insert(key, os.getcwd() + "/Images/Canny/" + str(key) + ".jpg")

            Video_Scan(pic)

    def is_float(value):
        try:
            float(value)
            return True
        except:
            return False

    def is_int(value):
        try:
            float(value)
            return True
        except:
            return False

    # Событие проверить все поля и показать ошибки
    def validation_required_values():
        get_program_ready(show_error=True, output_in_console=True)

    # Глобальная проверка параметров
    def get_program_ready(show_error=False, output_in_console=True):
        global scan_photos

        parameter_z = field_parameter_z.get()
        refractive_index = field_indicator_n.get()
        threshold_filter_value = field_threshold_filter.get()
        # amount_of_photos_scan = field_amount_scanned_photos.get()
        # amount_of_photos_camera = camera_photo_entry_field.get()
        amount_of_pixels = field_amount_of_pixels.get()
        droplet_radius = field_droplet_radius.get()
        error = False

        # Reset labels
        label_error_parameter_z.config(text='')
        label_error_indicator_n.config(text='')
        label_error_threshold_filter.config(text='')
        label_error_amount_scanned_photos.config(text='')
        # label_error_amount_camera_photo.config(text='')
        label_error_amount_pixels_per_millimeter.config(text='')
        label_error_laser_radius.config(text='')

        # Значение параметра Z
        if not is_float(parameter_z) or not is_int(parameter_z):
            if show_error:
                label_error_parameter_z.config(text='Некорректное значение')
            error = True

        # Показатель N
        if not is_float(refractive_index) or not is_int(refractive_index):
            if show_error:
                label_error_indicator_n.config(text='Некорректное значение')
            error = True

        # Значение порогового фильтра
        if not is_float(threshold_filter_value) or not is_int(threshold_filter_value):
            if show_error:
                label_error_threshold_filter.config(text='Некорректное значение')
            error = True

        # # Кол-во фотографий с видеоскана
        # if not is_float(amount_of_photos_scan) or not is_int(amount_of_photos_scan):
        #   if show_error:
        #     label_error_amount_scanned_photos.config(text='Некорректное значение')
        #   error = True

        # Кол-во фотографий с камеры
        # if not is_float(amount_of_photos_camera) or not is_int(amount_of_photos_camera):
        #   if show_error:
        #     label_error_amount_camera_photo.config(text='Некорректное значение')
        #   error = True

        # Кол-ва пикселей в одном мм
        if not is_float(amount_of_pixels) or not is_int(amount_of_pixels):
            if show_error:
                label_error_amount_pixels_per_millimeter.config(text='Некорректное значение')
            error = True

        # радиуса лазерного пучка
        if not is_float(droplet_radius) or not is_int(droplet_radius):
            if show_error:
                label_error_laser_radius.config(text='Некорректное значение')
            error = True

        # проверка пустых массивов
        for key, image in enumerate(scan_photos):
            if image == "":
                scan_photos.pop(key)

        if output_in_console:
            print("Parameters:")
            print("parameter_z = " + parameter_z)
            print("refractive_index = " + refractive_index)
            print("threshold_filter_value = " + threshold_filter_value)
            # print("amount_of_photos_scan = " + amount_of_photos_scan)
            # print("amount_of_photos_camera = " + amount_of_photos_camera)
            print("amount_of_pixels = " + amount_of_pixels)
            print("laser_radius = " + droplet_radius)
            print("error = " + str(error) + "\n")

        if error:
            return False
        else:
            return True

    # def vvod_foto_scan():
    #   amount_of_photos_scan = field_amount_scanned_photos.get()
    #
    #   if not (is_float(amount_of_photos_scan) or is_int(amount_of_photos_scan)):
    #     print("Некорректное значение кол-ва фотографий с видеоскана\n")
    #   else:
    #     print("Кол-ва фотографий с видеоскана = " + amount_of_photos_scan)

    # Окно для выбора файлов
    def load_images():
        global scan_photos

        if get_program_ready(show_error=True, output_in_console=False):
            scan_photos = filedialog.askopenfilenames(initialdir="/", title="Select file",
                                                      filetypes=(("bmp files", "*.bmp"), ("all files", "*.*")))
            print("Select images:")
            print(scan_photos)

    # def Vvod_Foto_Camera():
    #   amount_of_photos_camera = camera_photo_entry_field.get()
    #
    #   if not (is_float(amount_of_photos_camera) or is_int(amount_of_photos_camera)):
    #     print("Некорректное значение кол-ва фотографий с камеры")
    #   else:
    #     print("Кол-ва фотографий с камеры = " + amount_of_photos_camera)

    # Событие обработки отсканированых картинок
    def Video_Scan(photos=None):
        global scan_photos

        if photos is None:
            pics = scan_photos
        else:
            pics = photos

        if get_program_ready(show_error=True, output_in_console=False):
            amount_of_photos_scan = len(pics)
            picture_list = []
            b = []
            R = np.zeros(amount_of_photos_scan)
            b = np.zeros((amount_of_photos_scan, 4))

            if amount_of_photos_scan > 0:
                for key, photo in enumerate(pics):
                    picture_list.insert(key, Image.open(photo))

                for i in range(amount_of_photos_scan):
                    A = picture_list[i]
                    A = A.convert("L")
                    z = P0r0g(A, float(field_threshold_filter.get()))
                    print("Номер итерации " + str(i + 1))

                    for j in range(4):
                        b[i, j] = z[j]

                    R[i] = ((b[i, 2] - b[i, 0]) + (b[i, 3] - b[i, 1])) / 4
                    R[i] = (R[i] / float(field_amount_of_pixels.get())) + float(field_droplet_radius.get())
                    print("Радиус № " + str(i + 1) + " в мм")
                    print(R[i])
                    print("")

                z = float(field_parameter_z.get())
                n = float(field_indicator_n.get())
                tg = np.zeros(amount_of_photos_scan)

                for i in range(amount_of_photos_scan):
                    print("Тангенс краевого угла на фотографии № " + str(i + 1))
                    tg[i] = R[i] / (z * n)
                    print("в радианах " + str(tg[i]))
                    tg[i] = math.degrees(tg[i])
                    print("Значение угла в градусах = " + str(tg[i]))
                    print("")

                plt.plot(tg)
                plt.title("Тангенс краевого угла видеоскан")
                plt.show()

    # def Camera():
    #   print("Camera")
    #   amount_of_photos_camera = int(camera_photo_entry_field.get())
    #   PictList = []
    #   b = []
    #   R = np.zeros(amount_of_photos_camera)
    #   b = np.zeros((amount_of_photos_camera, 4))
    #   z = float(field_parameter_z.get())
    #   n = float(field_indicator_n.get())
    #   tg = np.zeros(amount_of_photos_camera)
    #
    #   for i in range(amount_of_photos_camera):
    #     PictList.insert(i, Image.open("J:\Photos for work\Five_mkl\Cam_rab\\" + str(i + 1) + ".jpg"))
    #
    #   for i in range(amount_of_photos_camera):
    #     A = PictList[i]
    #     A = A.convert("L")
    #     z = P0r0g(A, float(field_threshold_filter.get()))
    #     print("Номер итерации " + str(i + 1))
    #
    #     for j in range(4):
    #       b[i, j] = z[j]
    #
    #     R[i] = ((b[i, 2] - b[i, 0]) + (b[i, 3] - b[i, 1])) / 4
    #     R[i] = (R[i] / 22) + 3.53
    #
    #     print("Радиус № " + str(i + 1) + " в мм")
    #     print(R[i])
    #     print("")
    #
    #   for i in range(amount_of_photos_camera):
    #     print("Тангенс краевого угла на фотографии № " + str(i + 1))
    #     tg[i] = R[i] / (z * n)
    #     print(" " + str(tg[i]))
    #     tg[i] = math.degrees(tg[i])
    #     print("Значение угла в градусах " + str(tg[i]))
    #     print("")
    #
    #   plt.plot(tg)
    #   plt.title("Тангенс краевого угла фотоаппарат")
    #   plt.show()

    """
  Глобальные переменные
  """

    # Глобальные переменные
    scan_photos = []
    # scan_photos = ['/Users/konstantinegorov/develop/Nebula/Images/Scan/1.bmp',
    #               '/Users/konstantinegorov/develop/Nebula/Images/Scan/2.bmp']

    """
  Application
  """

    # tkinter
    program2 = Tk()

    # Menu
    # https://www.tutorialspoint.com/python/tk_menu.htm | https://younglinux.info/tkinter/menu.php
    menubar = Menu(program2)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New")
    # filemenu.add_command(label="Open", command=donothing)
    # filemenu.add_command(label="Save", command=donothing)
    # filemenu.add_command(label="Save as...", command=donothing)
    # filemenu.add_command(label="Close", command=program2.quit)
    # filemenu.add_command(label="Выход", command=program2.quit)
    filemenu.add_command(label="Выход", command=program2.quit)

    # filemenu.add_separator()

    # filemenu.add_command(label="Выход", command=program2.quit)
    menubar.add_cascade(label="Файл", menu=filemenu)

    # helpmenu = Menu(menubar, tearoff=0)
    # helpmenu.add_command(label="Help Index", command=donothing)
    # helpmenu.add_command(label="О программе", command=help_about)
    # menubar.add_cascade(label="Справка", menu=helpmenu)

    program2.config(menu=menubar)

    program2.title("Программа по обработке изображений")
    program2.geometry('1080x600')
    program2.config(bg='#FFE4B5')  # цвет поля
    program2.resizable(False, False)  # отмена ресайза окна

    print("Program \"Program2\" run!\n\n")

    """
  LABELS
  """

    # Этикетка для поля "значение параметра z"
    label_parameter_z = Label(program2, text='Укажите значение параметра z', fg='yellow', bg='#9932CC')
    label_parameter_z.config(font=('Verdana', 12))
    label_parameter_z.place(x=600, y=100)

    # Этикетка для вывода неверного значения у поля "значение параметра z"
    label_error_parameter_z = Label(program2, fg='#FFE4B5', bg='#FFE4B5')
    label_error_parameter_z.config(font=('Verdana', 10), fg='red')
    label_error_parameter_z.place(x=740, y=128)

    # Этикетка для поля "значение показателя n"
    label_parameter_n = Label(program2, text='Введите значение показателя n', fg='yellow', bg='#9932CC')
    label_parameter_n.config(font=('Verdana', 12))
    label_parameter_n.place(x=600, y=180)

    # Этикетка для вывода неверного значения у поля "значение показателя n"
    label_error_indicator_n = Label(program2, fg='#FFE4B5', bg='#FFE4B5')
    label_error_indicator_n.config(font=('Verdana', 10), fg='red')
    label_error_indicator_n.place(x=740, y=208)

    # Этикетка для поля "значение порогового фильтра"
    label_threshold_filter = Label(program2, text='Введите значение порогового фильтра', fg='yellow', bg='#9932CC')
    label_threshold_filter.config(font=('Verdana', 12))
    label_threshold_filter.place(x=600, y=250)

    # Этикетка для вывода неверного значения у поля "значение порогового фильтра"
    label_error_threshold_filter = Label(program2, fg='#FFE4B5', bg='#FFE4B5')
    label_error_threshold_filter.config(font=('Verdana', 10), fg='red')
    label_error_threshold_filter.place(x=740, y=278)

    # Этикетка для поля "кол-во фотографий с видеоскана"
    # label_number_scanned_photos = Label(program2, text='Введите кол-во фотографий с видеоскана', fg='yellow',
    #                                     bg='#9932CC')
    # label_number_scanned_photos.config(font=('Verdana', 15))
    # label_number_scanned_photos.place(x=5, y=50)

    # Этикетка для вывода неверного значения у поля "кол-ва фотографий с видеоскана"
    label_error_amount_scanned_photos = Label(program2, fg='#FFE4B5', bg='#FFE4B5')
    label_error_amount_scanned_photos.config(font=('Verdana', 10), fg='red')
    label_error_amount_scanned_photos.place(x=140, y=85)

    # # Этикетка для поля "кол-во фотографий с камеры"
    # label_camera_photo = Label(program2, text='Введите кол-во фотографий с камеры', fg='yellow', bg='#9932CC')
    # label_camera_photo.config(font=('Verdana', 15))
    # label_camera_photo.place(x=5, y=130)

    # Этикетка для вывода неверного значения у поля "кол-во фотографий с камеры"
    label_error_amount_camera_photo = Label(program2, fg='#FFE4B5', bg='#FFE4B5')
    label_error_amount_camera_photo.config(font=('Verdana', 10), fg='red')
    label_error_amount_camera_photo.place(x=140, y=165)

    # Этикетка для поля "кол-во пикселей в одном мм"
    label_amount_pixels_per_millimeter = Label(program2, text='Введите кол-во пикселей в одном мм', fg='yellow',
                                               bg='#9932CC')
    label_amount_pixels_per_millimeter.config(font=('Verdana', 12))
    label_amount_pixels_per_millimeter.place(x=600, y=30)

    # Этикетка для вывода неверного значения у поля "кол-ва пикселей в одном мм"
    label_error_amount_pixels_per_millimeter = Label(program2, fg='#FFE4B5', bg='#FFE4B5')
    label_error_amount_pixels_per_millimeter.config(font=('Verdana', 10), fg='red')
    label_error_amount_pixels_per_millimeter.place(x=740, y=57)

    # Этикетка для поля "радиуса лазерного пучка"
    label_laser_radius = Label(program2, text='Введите радиус капли', fg='yellow', bg='#9932CC')
    label_laser_radius.config(font=('Verdana', 12))
    label_laser_radius.place(x=600, y=310)

    # Этикетка для вывода неверного значения у поля "радиуса лазерного пучка"
    label_error_laser_radius = Label(program2, fg='#FFE4B5', bg='#FFE4B5')
    label_error_laser_radius.config(font=('Verdana', 10), fg='red')
    label_error_laser_radius.place(x=740, y=339)

    """
  FIELDS
  """

    # Поле для ввода данных z
    field_parameter_z = Entry(program2, width=20, bg='#DDA0DD')
    field_parameter_z.place(x=600, y=130)

    # Поле для ввода данных n
    field_indicator_n = Entry(program2, width=20, bg='#DDA0DD')
    field_indicator_n.place(x=600, y=210)

    # Поле для значения порогового фильтра
    field_threshold_filter = Entry(program2, width=20, bg='#DDA0DD')
    field_threshold_filter.place(x=600, y=280)

    # # Поле для ввода кол-ва фотографий с видеоскана
    # field_amount_scanned_photos = Entry(program2, width=20, bg='#DDA0DD')
    # field_amount_scanned_photos.place(x=5, y=87)

    # # Поле для ввода кол-ва фотографий с камеры
    # camera_photo_entry_field = Entry(program2, width=20, bg='#DDA0DD')
    # camera_photo_entry_field.place(x=5, y=167)

    # Поле для ввода кол-во пикселей в одном мм
    field_amount_of_pixels = Entry(program2, width=20, bg='#DDA0DD')
    field_amount_of_pixels.place(x=600, y=60)

    # Поле для ввода радиуса лазерного пучка
    field_droplet_radius = Entry(program2, width=20, bg='#DDA0DD')
    field_droplet_radius.place(x=600, y=342)

    """
  BUTTONS
  """

    # Ввод кол-ва фото видеоскана
    # b3 = Button(program2, text='Ввод кол-ва фото видеоскана', command=vvod_foto_scan)
    # b3.config(width=23, height=2, bg='#9ACD32', fg='black')
    # b3.place(x=200, y=250)

    # # Старт обработки с камеры
    # start_camera = Button(program2, text='Камера', command=Camera)
    # start_camera.config(width=23, height=2, bg='#9ACD32', fg='black')
    # start_camera.place(x=200, y=400)

    # # Видеоскан
    # start_Video_Scan = Button(program2, text='Видеоскан', command=Video_Scan)
    # start_Video_Scan.config(width=23, height=2, bg='#9ACD32', fg='black')
    # start_Video_Scan.place(x=200, y=300)

    # # Проверка фото камеры
    # camera_photo_check = Button(program2, text='Ввод кол-ва фото камеры', command=Vvod_Foto_Camera)
    # camera_photo_check.config(width=23, height=2, bg='#9ACD32', fg='black')
    # camera_photo_check.place(x=200, y=350)

    # Проверка значений n, z, коэф. интенсивности
    start_data_input = Button(program2, text='Ввод и проверка значений', command=validation_required_values)
    start_data_input.config(width=23, height=2, bg='#9ACD32', fg='black')
    start_data_input.place(x=600, y=400)

    # # Загрузка фото
    # button_photos_upload = Button(program2, text='Загрузить фото', command=load_images)
    # button_photos_upload.config(width=23, height=2, bg='#9ACD32', fg='black')
    # button_photos_upload.place(x=400, y=250)

    # # Загрузка фото
    button_photos_upload = Button(program2, text='Загрузить фото', command=load_images)
    button_photos_upload.config(width=23, height=2, bg='#9ACD32', fg='black')
    button_photos_upload.place(x=200, y=200)

    # Canny_filter
    start_Canny_filter = Button(program2, text='start_Фильтр Кэнни', command=Canny_filter)
    start_Canny_filter.config(width=23, height=2, bg='#9ACD32', fg='black')
    start_Canny_filter.place(x=200, y=300)

    program2.mainloop()
