import pyqrcode
import tkinter
code = pyqrcode.create('http://www.rtu.ac.in/RTU/')
code_xbm = code.xbm(scale=5)
top = tkinter.Tk()
code_bmp = tkinter.BitmapImage(data=code_xbm)
code_bmp.config(foreground="black")
code_bmp.config(background="white")
label = tkinter.Label(image=code_bmp)
label.pack()
