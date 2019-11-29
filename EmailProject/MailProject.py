import smtplib
import email.mime.multipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pickle
import tkinter.messagebox
import tkinter.filedialog
from tkinter import *
from PIL import Image,ImageTk
class EmailClient:

    # All Shared or Static Function Start from Here
    @staticmethod
    def saveEmailClientInFile():
        f = open("EmailClient.qmt", 'wb')
        pickle.dump(EmailClient.emailClientList, f)

    @staticmethod
    def loadEmailClientFromFile():
        try:
            f = open("EmailClient.qmt", 'rb')
            EmailClient.emailClientList = pickle.load(f)
        except Exception as ex:
            pass

    # All Shared or Static Function Start End Here

    # All Shared or Static Variable Start from Here
    emailClientList = []
    currentUser=None

    # All Shared or Static Variable Start End Here

    def __init__(self):
        self.firstName=""
        self.lastName=""
        self.gmailID=""
        self.gmailPassword=""
        self.mobileNo=""
        self.dayBirth=""
        self.monthBirth=""
        self.yearBirth=""
    def SignUp(self):
        EmailClient.loadEmailClientFromFile()
        self.checkEmailIDExists(self.gmailID)
        EmailClient.emailClientList.append(self)
        EmailClient.saveEmailClientInFile()
        EmailClient.currentUser = self

    def checkEmailIDExists(self,userEmailId):
        for element in EmailClient.emailClientList:
            if (element.gmailID == userEmailId):
                raise Exception("Email Id already Exists")

    def getUserbyEmailID(self, userEmailId):
        EmailClient.loadEmailClientFromFile()
        for element in EmailClient.emailClientList:
            if(element.gmailID==userEmailId):
                self.firstName = element.firstName
                self.lastName = element.lastName
                self.gmailID = element.gmailID
                self.gmailPassword = element.gmailPassword
                self.mobileNo = element.mobileNo
                self.dayBirth = element.dayBirth
                self.monthBirth = element.monthBirth
                self.yearBirth = element.yearBirth
                return True
        raise Exception("Id not found")
    def login(self, userEmailId,userPassword):
        EmailClient.loadEmailClientFromFile()
        for element in EmailClient.emailClientList:
            if(element.gmailID==userEmailId and element.gmailPassword==userPassword):
                self.firstName = element.firstName
                self.lastName = element.lastName
                self.gmailID = element.gmailID
                self.gmailPassword = element.gmailPassword
                self.mobileNo = element.mobileNo
                self.dayBirth = element.dayBirth
                self.monthBirth = element.monthBirth
                self.yearBirth = element.yearBirth
                EmailClient.currentUser=self
                return True
        raise Exception("Login Id or Password Incorrect")

    def sendEmail(self,strTo, strFrom_GmailID, strPassword_GmailPassword, strSubject, strBody,strBodyType='plain', lstAttachment=None):
        # Create Email Details
        msgMultiPart = email.mime.multipart.MIMEMultipart()
        msgMultiPart["subject"] = strSubject
        msgMultiPart["From"] = strFrom_GmailID
        msgMultiPart["To"] = strTo
        # Create Body may be plain or html

        msgMultiPart.attach(MIMEText(strBody, strBodyType))
        # create Attachment
        if (lstAttachment != None):
            count = 1
            for filePath in lstAttachment:
                file1 = open(filePath, 'rb')
                attachpart = MIMEBase('application', 'octet-stream')
                attachpart.set_payload(file1.read())
                encoders.encode_base64(attachpart)
                attachpart.add_header('Content-Disposition', "attachment; filename=File1Attach" + str(count))
                count += 1
                msgMultiPart.attach(attachpart)

        # Send Mail in attachment
        smtpobj = smtplib.SMTP(host="smtp.gmail.com", port="587")
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.login(strFrom_GmailID, strPassword_GmailPassword)
        smtpobj.sendmail(strFrom_GmailID, strTo, msgMultiPart.as_string())
class MainForm(Frame):
    refMainForm=None
    refMaster=None
    def __init__(self,master=None):
        super().__init__(master)
        MainForm.refMaster=master
        MainForm.refMainForm=self
        self.pack()
        self.createWidget()
    def createWidget(self):
        MainForm.refMaster.state("z")
        MainForm.refMaster.title("Mail Client Application")
        self.icn1 = Image.open(r"icon.png")
        self.icon = ImageTk.PhotoImage(self.icn1)
        MainForm.refMaster.tk.call('wm', 'iconphoto', MainForm.refMaster._w, self.icon)

        self.image_back1 = Image.open(r"homepage.png")
        self.image_back11 = self.image_back1.resize((1366, 710), Image.ANTIALIAS)
        self.image_back2 = ImageTk.PhotoImage(self.image_back11)

        self.background_label = Label(self, image=self.image_back2)
        self.background_label.pack(fill=BOTH,expand=True)

        self.welcome_image1 = Image.open(r"l.png")
        self.welcome_image2 = ImageTk.PhotoImage(self.welcome_image1)
        self.welcome_label = Label(self, image=self.welcome_image2)
        self.welcome_label.place(x=570, y=55)

        self.msg_label1 = Label(self, text="Let's gether all your email here and", fg="#388E3C", font=("Segoe Print", 16))
        self.msg_label1.place(x=477, y=280)
        self.msg_label2 = Label(self, text="simplify life a bit.", font=("Segoe Print", 16), fg="#388E3C")
        self.msg_label2.place(x=572, y=313)
        self.signup_btn = Button(self,
                            text="SignUp", bg="white", fg="#5C6BC0",
                            font=("Times", 40, "bold"),
                            activebackground="#9FA8DA",
                            activeforeground="white", command=self.signup_btn_Click)

        self.login_btn = Button(self,
                           text="LogIn", bg="white", fg="#5C6BC0",
                           font=("Times", 40, "bold"),
                           activebackground="#9FA8DA",
                           activeforeground="white", command=self.login_btn_Click)
        self.signup_btn.place(x=350, y=500)
        self.login_btn.place(x=780, y=500)
    def signup_btn_Click(self):
        SignUpWelcome(MainForm.refMaster)
        self.destroy()
        # print("ok")
        pass
    def login_btn_Click(self):
        Login(MainForm.refMaster)
        self.destroy()
        # print("ok")
class Login(Frame):
    refMainForm = None
    refMaster = None

    def __init__(self, master=None):
        super().__init__(master)
        Login.refMaster = master
        Login.refMainForm = self
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.back_img1 = Image.open(r"signUp.png")
        self.back_img11 = self.back_img1.resize((1366, 710), Image.ANTIALIAS)
        self.back_img2 = ImageTk.PhotoImage(self.back_img11)
        self.background_label = Label(self, image=self.back_img2)


        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # self.background_label.pack(fill=BOTH,expand=True)

        self.root_frame = Frame(self,height=710, width=1366)
        self.root_frame.pack(padx=430, pady=75)

        login_label = Label(self.root_frame, text="Login into your Account", font=("Segoe Print", 29), fg="#1A237E")
        login_label.place(x=7, y=3)

        self.welcome_image1 = Image.open(r"logo.png")
        self.welcome_image22 = ImageTk.PhotoImage(self.welcome_image1)
        self.welcome_img_label = Label(self.root_frame, image=self.welcome_image22)
        self.welcome_img_label.place(x=190, y=83)

        self.varGmailID=StringVar()
        self.frame_entry1 = Entry(self.root_frame, text=self.varGmailID, font=("Times", 34, "italic"),
                             bg="#26A69A", fg="#F5F5F5")
        self.frame_entry1.place(x=17, y=279)
        # frame_entry1.insert(0,"Username")
        self.entry_label1 = Label(self.root_frame, text="Gmail Id", font=("Segoe Print", 19), fg="#004D40")
        self.entry_label1.place(x=12, y=230)

        self.varGmailPassword=StringVar()
        self.frame_entry2 = Entry(self.root_frame,text=self.varGmailPassword,show="*", font=("Times", 34, "italic"),
                             bg="#26A69A", fg="#F5F5F5")
        self.frame_entry2.place(x=17, y=399)
        # frame_entry2.insert(0,"Password")
        self.entry_label2 = Label(self.root_frame, text="Gmail Password:", font=("Segoe Print", 19), fg="#004D40")
        self.entry_label2.place(x=12, y=350)

        self.login_btn = Button(self.root_frame,
                           text="Login", bg="#00695C", fg="#F5F5F5",
                           font=("Times", 20, "bold"),
                           activebackground="#F5F5F5",
                           activeforeground="#00695C",command=self.login_btn_Click)
        self.login_btn.place(x=19, y=483, width=461)
    def login_btn_Click(self):
        try:
            client=EmailClient()

            gmailID=self.varGmailID.get()
            gmailPassword=self.varGmailPassword.get()
            client.login(gmailID,gmailPassword)
            tkinter.messagebox.showinfo("Sucess", "Login Sucessfully", parent=MainForm.refMaster)
            SendMail(MainForm.refMaster)
            self.destroy()
        except Exception as ex:
            tkinter.messagebox.showerror("Error",ex,parent=MainForm.refMaster)

class SignUpWelcome(Frame):
    refMainForm = None
    refMaster = None

    def __init__(self, master=None):
        super().__init__(master)
        SignUpWelcome.refMaster = master
        SignUpWelcome.refMainForm = self
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.back_img1 = Image.open(r"signupwelcome.png")
        self.back_img11 = self.back_img1.resize((1366, 710), Image.ANTIALIAS)
        self.back_img2 = ImageTk.PhotoImage(self.back_img11)
        self.background_label = Label(self, image=self.back_img2)
        self.background_label.pack()


        # self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.welcome_image1 = Image.open(r"l.png")
        self.welcome_image2 = ImageTk.PhotoImage(self.welcome_image1)
        self.welcome_label = Label(self, image=self.welcome_image2)
        self.welcome_label.place(x=570, y=55)

        self.msg_label1 = Label(self, text="Welcome Name", fg="#1A237E", font=("Segoe Print", 36), bg="#FFF9C4")
        self.msg_label1.place(x=500, y=280)
        self.msg_label2 = Label(self, text="Let's get started a journy of mail", font=("Segoe Print", 26), fg="#1A237E",
                           bg="#FFF9C4")
        self.msg_label2.place(x=400, y=348)

        btn1 = Button(self,
                      text="Let's Go", bg="#5C6BC0", fg="white",
                      font=("Times", 40, "bold"),
                      activebackground="#9FA8DA",
                      activeforeground="white",command=self.btn1_Click)
        btn1.place(x=559, y=519)


    def btn1_Click(self):
        SignUp(MainForm.refMaster)
        self.destroy()
class SignUp(Frame):
    refMainForm = None
    refMaster = None

    def __init__(self, master=None):
        super().__init__(master)
        SignUp.refMaster = master
        SignUp.refMainForm = self
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.back_img1 = Image.open(r"signUp.png")
        self.back_img11 = self.back_img1.resize((1366, 710), Image.ANTIALIAS)
        self.back_img2 = ImageTk.PhotoImage(self.back_img11)
        self.background_label = Label(self, image=self.back_img2)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)


        # self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.root_frame = Frame(self, height=710, width=1366)
        self.root_frame.pack(padx=430, pady=10)

        self.login_label = Label(self.root_frame, text="Create your Account", font=("Segoe Print", 29), fg="#1A237E")
        self.login_label.place(x=37, y=3)

        self.welcome_image1 = Image.open(r"signuplogo.png")
        self.welcome_image2 = ImageTk.PhotoImage(self.welcome_image1)
        self.welcome_img_label = Label(self.root_frame, image=self.welcome_image2)
        self.welcome_img_label.place(x=185, y=83)

        self.varFirstName=StringVar()
        self.frame_entry1 = Entry(self.root_frame, text=self.varFirstName, font=("Times", 20, "italic"), bg="#26A69A", fg="#F5F5F5")
        self.frame_entry1.place(x=17, y=271, width=227)
        self.frame_entry1.insert(0, "First name")

        self.varLastName = StringVar()
        self.frame_entry2 = Entry(self.root_frame,text=self.varLastName, font=("Times", 20, "italic"), bg="#26A69A", fg="#F5F5F5")
        self.frame_entry2.place(x=253, y=271, width=230)
        self.frame_entry2.insert(0, "Last name")

        self.entry_label1 = Label(self.root_frame, text="Name:", font=("Segoe Print", 15), fg="#004D40")
        self.entry_label1.place(x=14, y=230)

        self.varGmailID=StringVar()
        self.frame_entry3 = Entry(self.root_frame, text=self.varGmailID, font=("Times", 20, "italic"), bg="#26A69A", fg="#F5F5F5")
        self.frame_entry3.place(x=17, y=346, width=467)
        self.entry_label3 = Label(self.root_frame, text="Your Gmail Id:", font=("Segoe Print", 15), fg="#004D40")
        self.entry_label3.place(x=14, y=305)

        self.varGmailPassword=StringVar()
        self.frame_entry4 = Entry(self.root_frame,text=self.varGmailPassword, show="*", font=("Times", 20, "italic"), bg="#26A69A", fg="#F5F5F5")
        self.frame_entry4.place(x=17, y=421, width=467)
        self.entry_label4 = Label(self.root_frame, text="Your Gmail Password:", font=("Segoe Print", 15), fg="#004D40")
        self.entry_label4.place(x=14, y=380)


        self.frame_entry5 = Spinbox(self.root_frame, from_=1, to=31, font=("Times", 20, "italic"), bg="#26A69A", fg="#F5F5F5")
        self.frame_entry5.place(x=17, y=496, width=150)
        self.frame_entry5.insert(0, "Day")

        self.varMonth=StringVar()
        self.frame_entry6 = Entry(self.root_frame,text=self.varMonth, font=("Times", 20, "italic"), bg="#26A69A", fg="#F5F5F5")
        self.frame_entry6.place(x=175, y=496, width=150)
        self.frame_entry6.insert(0, "Month")

        self.varYear=StringVar()
        self.frame_entry7 = Entry(self.root_frame,text=self.varYear, font=("Times", 20, "italic"), bg="#26A69A", fg="#F5F5F5")
        self.frame_entry7.place(x=333, y=496, width=150)
        self.frame_entry7.insert(0, "Year")

        self.entry_label5 = Label(self.root_frame, text="Birthday:", font=("Segoe Print", 15), fg="#004D40")
        self.entry_label5.place(x=14, y=455)

        self.varMobileNo=StringVar()
        self.frame_entry8 = Entry(self.root_frame,text=self.varMobileNo, font=("Times", 20, "italic"), bg="#26A69A", fg="#F5F5F5")
        self.frame_entry8.place(x=17, y=571, width=467)
        self.entry_label8 = Label(self.root_frame, text="Mobile:", font=("Segoe Print", 15), fg="#004D40")
        self.entry_label8.place(x=14, y=530)

        self.login_btn = Button(self.root_frame,
                           text="SignUp", bg="#00695C", fg="#F5F5F5",
                           font=("Times", 17, "bold"),
                           activebackground="#F5F5F5",
                           activeforeground="#00695C",command=self.login_btn_Click)
        self.login_btn.place(x=17, y=620, width=466)
    def login_btn_Click(self):
        try:
            client=EmailClient()
            client.firstName=self.varFirstName.get()
            client.lastName=self.varLastName.get()
            client.gmailID=self.varGmailID.get()
            client.gmailPassword=self.varGmailPassword.get()
            client.mobileNo=self.varMobileNo.get()
            client.dayBirth=self.frame_entry5.get()
            client.monthBirth=self.varMonth.get()
            client.yearBirth=self.varYear.get()
            client.SignUp()
            tkinter.messagebox.showinfo("Success", "User Created Sucessfully", parent=MainForm.refMaster)
            SendMail(MainForm.refMaster)
            self.destroy()
        except Exception as ex:
            tkinter.messagebox.showerror("Error",ex,parent=MainForm.refMaster)

class SendMail(Frame):
    refMainForm = None
    refMaster = None

    def __init__(self, master=None):
        super().__init__(master)
        SignUp.refMaster = master
        SignUp.refMainForm = self
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.back_img1 = Image.open(r"bk1.png")
        self.back_img11 = self.back_img1.resize((1366, 710), Image.ANTIALIAS)
        self.back_img2 = ImageTk.PhotoImage(self.back_img11)
        self.background_label = Label(self, image=self.back_img2)
        self.background_label.pack(fill=BOTH,expand=True)#(x=0, y=0, relwidth=1, relheight=1)
        self.attachementList=[]

        self.varTo=StringVar()
        self.frame_entry1 = Entry(self,text=self.varTo, font=("Times", 20, "italic"), bg="white", fg="#26A69A")
        self.frame_entry1.place(x=621, y=40, width=667)
        self.entry_label1 = Label(self, text="To:", font=("Segoe Print", 17), fg="#1A237E", bg="#B2EBF2")
        self.entry_label1.place(x=530, y=35)

        self.varFrom=StringVar()
        self.frame_entry2 = Entry(self,text=self.varFrom,state=DISABLED, font=("Times", 20, "italic"), bg="white", fg="#26A69A")
        self.frame_entry2.place(x=621, y=100, width=667)
        self.varFrom.set(EmailClient.currentUser.gmailID)
        self.entry_label2 = Label(self, text="From:", font=("Segoe Print", 17), fg="#1A237E", bg="#B2EBF2")
        self.entry_label2.place(x=517, y=95)

        self.varSubject=StringVar()
        self.frame_entry3 = Entry(self,text=self.varSubject, font=("Times", 20, "italic"), bg="white", fg="#26A69A")
        self.frame_entry3.place(x=621, y=165, width=667)
        self.entry_label3 = Label(self, text="Subject:", font=("Segoe Print", 17), fg="#1A237E", bg="#B2EBF2")
        self.entry_label3.place(x=505, y=160)

        self.varRadio = StringVar()
        self.radio1 = Radiobutton(self, text="Plain", fg="#1A237E", bg="#B2EBF2",
                             font=("Times", 20, ""), variable=self.varRadio,
                             value="plain")

        self.radio2 = Radiobutton(self, text="Html",
                             font=("Times", 20, ""), variable=self.varRadio,
                             value="html", fg="#1A237E", bg="#B2EBF2")
        self.radio1.place(x=1047, y=249, width=100)
        self.radio2.place(x=1182, y=249, width=100)
        self.varRadio.set("plain")

        self.textarea_label1 = Label(self, text="write your mail :", font=("Segoe Print", 15), fg="#1A237E", bg="#B2EBF2")
        self.textarea_label1.place(x=25, y=295)

        self.textarea = Text(self, width=120, height=20)
        self.textarea.place(x=25, y=351)

        self.send_btn = Button(self,
                          text="Send", bg="#5C6BC0", fg="white",
                          font=("Times", 30, "bold"),
                          activebackground="#9FA8DA",
                          activeforeground="white",command=self.send_btn_Click)
        self.send_btn.place(x=1089, y=397, width=147)

        self.attach_btn = Button(self,
                            text="Attach", bg="#5C6BC0", fg="white",
                            font=("Times", 30, "bold"),
                            activebackground="#9FA8DA",
                            activeforeground="white",command=self.attach_btn_Click)
        self.attach_btn.place(x=1089, y=550, width=150)

        self.welcome_image1 = Image.open(r"l.png")
        self.welcome_image2 = ImageTk.PhotoImage(self.welcome_image1)
        self.welcome_label = Label(self, image=self.welcome_image2)
        self.welcome_label.place(x=65, y=37)
    def send_btn_Click(self):
        try:
            client=EmailClient()
            strTo=self.varTo.get()
            strFrom=EmailClient.currentUser.gmailID
            strPassword=EmailClient.currentUser.gmailPassword
            strSubject=self.varSubject.get()
            strMsgType=self.varRadio.get()
            strBody=self.textarea.get(0.0,END)
            lstAttach=self.attachementList
            client.sendEmail(strTo,strFrom,strPassword,strSubject,strBody,strMsgType,lstAttach)

            tkinter.messagebox.showinfo("Success", "Mail Send Sucessfully", parent=MainForm.refMaster)
            SendMail(MainForm.refMaster)
            self.destroy()
        except Exception as ex:
            tkinter.messagebox.showerror("Error",ex,parent=MainForm.refMaster)
    def attach_btn_Click(self):
        result=tkinter.filedialog.askopenfilename()
        if(result!=''):
            self.attachementList.append(result)



        # if(result):
        #


root=Tk()
frmMain=MainForm(root)
# frmMain=SendMail(root)
root.mainloop()