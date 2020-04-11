import os  # accessing the os functions
import Capture_Image
import Train_Image
import Recognize
import tkinter as tk
from tkinter import Message ,Text
import tkinter.ttk as ttk
import tkinter.font as font


window = tk.Tk()
window.geometry("1000x800")
window.title("Face_Recogniser")
dialog_title = 'QUIT'

C = tk.Canvas(window, bg="blue", height=250, width=300)
filename = tk.PhotoImage(file = "E:/AI-SSP-master/AI_Attendance_Sys/background_img.png")
background_label = tk.Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

dialog_text = 'Are you sure?'
window.configure(background='black')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
message = tk.Label(window, text="Attendance System" ,bg="black"  ,fg="white"  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
message.place(x=150, y=20)
lbl = tk.Label(window, text="Enter ID",width=20  ,height=2  ,fg="white"  ,bg="black" ,font=('times', 15, ' bold ') ) 
lbl.place(x=400, y=200)
txt = tk.Entry(window,width=20  ,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt.place(x=700, y=215)
lbl2 = tk.Label(window, text="Enter Name",width=20  ,fg="white"  ,bg="black"    ,height=2 ,font=('times', 15, ' bold ')) 
lbl2.place(x=400, y=300)
txt2 = tk.Entry(window,width=20  ,bg="white"  ,fg="black",font=('times', 15, ' bold ')  )
txt2.place(x=700, y=315)
lbl3 = tk.Label(window, text="Notification : ",width=20  ,fg="white"  ,bg="black"  ,height=2 ,font=('times', 15, ' bold underline ')) 
lbl3.place(x=400, y=400)
message = tk.Label(window, text="" ,bg="white"  ,fg="black"  ,width=30  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
message.place(x=700, y=400)
lbl3 = tk.Label(window, text="Attendance : ",width=20  ,fg="white"  ,bg="black"  ,height=2 ,font=('times', 15, ' bold  underline')) 
lbl3.place(x=400, y=650)
message2 = tk.Label(window, text="" ,fg="black"   ,bg="white",activeforeground = "green",width=30  ,height=2  ,font=('times', 15, ' bold ')) 
message2.place(x=700, y=650)
def clear():
    txt.delete(0, 'end')    
    res = ""
    message.configure(text= res)
def clear2():
    txt2.delete(0, 'end')    
    res = ""
    message.configure(text= res)    
#verifying valid id and name
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False
# -----------------------------------------------------------------
# calling the take images from Capture_Image.py file
def CaptureFaces():
    Id=(txt.get())
    name=(txt2.get())
    if(is_number(Id) and name.isalpha()):
         Capture_Image.takeImages(Id,name)
    else:
        if(is_number(Id)):
            res = "Enter Alphabetical Name"
            message.configure(text= res)
        if(name.isalpha()):
            res = "Enter Numeric Id"
            message.configure(text= res)
# -----------------------------------------------------------------
# calling the train images from train_images.py file
def Trainimages():
    res = Train_Image.TrainImages()
    message.configure(text= res)
# --------------------------------------------------------------------
# calling the recognize_attendance from recognize.py file
def RecognizeFaces():
    res = Recognize.recognize_attendence()
    message2.configure(text= res)
# --------------------------------------------------------------------
# calling the automail from automail.py file
def Automail():
    os.system("py automail.py")
    res = "Mail Sent"
    message2.configure(text= res)

clearButton = tk.Button(window, text="Clear", command=clear  ,fg="white"  ,bg="black"  ,width=17  ,height=2 ,activebackground = "white" ,font=('times', 15, ' bold '))
clearButton.place(x=950, y=200)
clearButton2 = tk.Button(window, text="Clear", command=clear2  ,fg="white"  ,bg="black"  ,width=17  ,height=2, activebackground = "white" ,font=('times', 15, ' bold '))
clearButton2.place(x=950, y=300)    
takeImg = tk.Button(window, text="Capture Faces", command=CaptureFaces  ,fg="white"  ,bg="black"  ,width=17  ,height=2, activebackground = "white" ,font=('times', 15, ' bold '))
takeImg.place(x=150, y=500)
trainImg = tk.Button(window, text="Train Images", command=Trainimages  ,fg="white"  ,bg="black"  ,width=17  ,height=2, activebackground = "white" ,font=('times', 15, ' bold '))
trainImg.place(x=400, y=500)
trackImg = tk.Button(window, text="Recognize Faces", command=RecognizeFaces  ,fg="white"  ,bg="black"  ,width=17  ,height=2, activebackground = "white" ,font=('times', 15, ' bold '))
trackImg.place(x=650, y=500)
automail_but = tk.Button(window, text="Mail Attendance", command=Automail  ,fg="white" ,bg="black"   ,width=17  ,height=2, activebackground = "white" ,font=('times', 15, ' bold '))
automail_but.place(x=900, y=500)
quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="white"  ,bg="black"  ,width=17  ,height=2, activebackground = "white" ,font=('times', 15, ' bold '))
quitWindow.place(x=1150, y=500)
window.mainloop()