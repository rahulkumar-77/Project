from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import tkinter
from studentdetails import StudentDetail
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendence
from app import ChatApplication

class Face_Recognization_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")
        #First image
        img=Image.open("college_images/Stanford.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #Second image
        img1=Image.open("college_images/facialrecognition.png")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #Third Image
        img2=Image.open("college_images/u.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #Baground image

        img3=Image.open("college_images/wp2551980.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #Student button

        img4=Image.open("college_images/gettyimages-1022573162.jpg")
        img4=img4.resize((210,210),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=210,height=210)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=210,height=40)

        #Detect face button

        img5=Image.open("college_images/face_detector1.jpg")
        img5=img5.resize((210,210),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=210,height=210)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=210,height=40)


        #Attendace face button

        img6=Image.open("college_images/report.jpg")
        img6=img6.resize((210,210),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=210,height=210)

        b1_1=Button(bg_img,text="Attendace",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=210,height=40)

        #Chatbot button

        img7=Image.open("college_images/chat.jpg")
        img7=img7.resize((210,210),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.chatbot)
        b1.place(x=1100,y=100,width=210,height=210)

        b1_1=Button(bg_img,text="ChatBot",cursor="hand2",command=self.chatbot,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=210,height=40)

         #Train Face button

        img8=Image.open("college_images/Train.jpg")
        img8=img8.resize((210,210),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=210,height=210)

        b1_1=Button(bg_img,text="Train",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=210,height=40)

        #Photo button

        img9=Image.open("college_images/opencv_face_reco_more_data.jpg")
        img9=img9.resize((210,210),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=210,height=210)

        b1_1=Button(bg_img,text="Photo",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=210,height=40)

        #Developer button

        img10=Image.open("college_images/Team-Management-Software-Development.jpg")
        img10=img10.resize((210,210),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=210,height=210)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=210,height=40)

        #Exit button

        img11=Image.open("college_images/exit.jpg")
        img11=img11.resize((210,210),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.Exit_app)
        b1.place(x=1100,y=380,width=210,height=210)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.Exit_app, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=210,height=40)
        
    def open_img(self):
        os.startfile("data")
        
    #=======================functionbuttom for student_details window==========================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=StudentDetail(self.new_window)
        
    #=======================functionbuttom for train window==========================
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    #=======================functionbuttom for face_data window==========================  

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    #=======================functionbuttom for attendance_data window==========================
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)

    #=======================functionbuttom for chatbot window==========================

    def chatbot(self):
        self.app=ChatApplication()

    #=======================Exit button==========================

    def Exit_app(self):
        self.Exit_app=tkinter.messagebox.askyesno("Face Recognization System","Are you sure exit this project",parent=self.root)
        if self.Exit_app>0:
            self.root.destroy()
        else:
            return
        





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognization_System(root)
    root.mainloop()
    
    