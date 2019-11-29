import tkinter
from tkinter import *
import PIL
from PIL import Image,ImageTk

root=Tk()
root.state("z")
root.title("Welcome")
icn1=Image.open("icon.png")
icon=ImageTk.PhotoImage(icn1)
root.tk.call('wm', 'iconphoto', root._w, icon)

back_img1=Image.open(r"signupwelcome.png")
back_img1 = back_img1.resize((1366, 710), Image.ANTIALIAS)
back_img2=ImageTk.PhotoImage(back_img1)
background_label=Label(root,image=back_img2)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

welcome_image1=Image.open(r"l.png")
welcome_image2 = ImageTk.PhotoImage(welcome_image1)
welcome_label=Label(root,image=welcome_image2)
welcome_label.place(x=570, y=55)

msg_label1=Label(root,text="Welcome Name",fg="#1A237E",font=("Segoe Print",36),bg="#FFF9C4")
msg_label1.place(x=500,y=280)
msg_label2=Label(root,text="Let's get started a journy of mail",font=("Segoe Print",26),fg="#1A237E",bg="#FFF9C4")
msg_label2.place(x=400,y=348)

btn1= Button(root,
           text="Let's Go",bg="#5C6BC0",fg="white",
           font=("Times",40,"bold"),
           activebackground="#9FA8DA",
           activeforeground="white")
btn1.place(x=559,y=519)
root.mainloop()