import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import os
import numpy as np
import cv2
import os
import csv
from tkinter import filedialog
import numpy as np


mydata=[]
class Attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # ======Variable=======
        self.var_atten_id=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_batch=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        
        
    # 1st Image
        img_top=Image.open("college_images/smart-attendance.jpg")
        img_top=img_top.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=800,height=200)
        
    #  2nd Image   
        img_bottom=Image.open("college_images/iStock-182059956_18390_t12.jpg")
        img_bottom=img_bottom.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lb2=Label(self.root,image=self.photoimg_bottom)
        f_lb2.place(x=800,y=0,width=800,height=200)
        
    # bg Image
    
        img3=Image.open("college_images/wp2551980.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg_top3=ImageTk.PhotoImage(img3)
        
        f_lb3=Label(self.root,image=self.photoimg_top3)
        f_lb3.place(x=0,y=200,width=1530,height=710)
        
    # Title
        b1_1=Button(f_lb3,text="ATTENDENCE MANAGEMENT SYSTEM",cursor="hand2",font=("times new roman",30,"bold"),bg="white",fg="green")
        b1_1.place(x=0,y=0,width=1530,height=45)
        
    # Frame
    
        main_frame = Frame(f_lb3,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)
        
    # left_frame
    
        left_frame = LabelFrame(main_frame, text = "Student Attendance Information",
                        font = ("times new roman", 15, "bold"), fg = "#074463", relief = GROOVE)
        left_frame.place(x = 10, y = 10, width = 730, height=580)
        
        left_frame_image=Image.open("college_images/AdobeStock_303989091.jpeg")
        left_frame_image=left_frame_image.resize((720,130),Image.ANTIALIAS)
        self.photoimg_top4=ImageTk.PhotoImage(left_frame_image)
        
        f_lb4=Label(left_frame,image=self.photoimg_top4)
        f_lb4.place(x=5,y=0,width=720,height=130)
        
        left_frame_inside = Frame(left_frame,bd=2,bg="white")
        left_frame_inside.place(x=0,y=135,width=720,height=370)
        
        # label
        
        
        # attendanceId
        attendanceId_lable=Label(left_frame_inside,text="RegistrationNo:",font=("times new roman",12, "bold"),bg="white")
        attendanceId_lable.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendenceId_entry=Entry(left_frame_inside, width=20,textvariable=self.var_atten_id,font=("times new roman",12, "bold"),bg="white")
        attendenceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        # name
        nameLabel=Label(left_frame_inside,text="Name:",font=("times new roman",12, "bold"),bg="white")
        nameLabel.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        nameEntry=Entry(left_frame_inside, width=20,textvariable=self.var_atten_name,font=("times new roman",12, "bold"),bg="white")
        nameEntry.grid(row=0,column=3,padx=4,pady=8)
        
        # department
        departmentLabel=Label(left_frame_inside,text="Department:",font=("times new roman",12, "bold"),bg="white")
        departmentLabel.grid(row=1,column=0)
        
        department_name=Entry(left_frame_inside, width=20,textvariable=self.var_atten_dep,font=("times new roman",12, "bold"),bg="white")
        department_name.grid(row=1,column=1,pady=8)
        
        # batch
        batch_lable=Label(left_frame_inside,text="Batch:",font=("times new roman",12, "bold"),bg="white")
        batch_lable.grid(row=1,column=2)
        
        batch_entry=Entry(left_frame_inside, width=20,textvariable=self.var_atten_batch,font=("times new roman",12, "bold"),bg="white")
        batch_entry.grid(row=1,column=3,pady=8)
        
        # time
        time_lable=Label(left_frame_inside,text="Time:",font=("times new roman",12, "bold"),bg="white")
        time_lable.grid(row=2,column=0)
        
        time_entry=Entry(left_frame_inside, width=20,textvariable=self.var_atten_time,font=("times new roman",12, "bold"),bg="white")
        time_entry.grid(row=2,column=1,padx=8)
        
        
        # date
        date_lable=Label(left_frame_inside,text="Date:",font=("times new roman",12, "bold"),bg="white")
        date_lable.grid(row=2,column=2)
        
        date_entry=Entry(left_frame_inside, width=20,textvariable=self.var_atten_date,font=("times new roman",12, "bold"),bg="white")
        date_entry.grid(row=2,column=3,pady=8)
        
        
        
        
        # attendance
        attendance_status_lable=Label(left_frame_inside,text="Attendance Status:",font=("times new roman",12, "bold"),bg="white")
        attendance_status_lable.grid(row=3,column=0)
        
        self.attendence_status=ttk.Combobox(left_frame_inside, width=20,textvariable=self.var_atten_attendance,font=("times new roman",12, "bold"),state="readonly")
        self.attendence_status["values"]=("Status","Present","Absent")
        self.attendence_status.grid(row=3,column=1,pady=8)
        self.attendence_status.current(0)
        
        
        
        F4 = Frame(left_frame_inside, relief = GROOVE)
        F4.place(x = 0, y = 300, width = 715, height=35)

        import_csv = Button(F4, text = "Import csv",command=self.importCsv, font = ("times new roman", 12, "bold"), bg = "#074463", fg = "white",
                          width = 17).grid(row = 0, column = 0, sticky = "w")
        
        Export_csv = Button(F4, text = "Export csv",command=self.exportCsv, font = ("times new roman", 12, "bold"), bg = "#074463", fg = "white",
                          width = 17).grid(row = 0, column = 1, sticky = "w")
        
        Update_btn = Button(F4, text = "Update", font = ("times new roman", 12, "bold"), bg = "#074463", fg = "white",
                          width = 17).grid(row = 0, column = 2, sticky = "w")
        
        reset_btn = Button(F4, text = "RESET",command=self.reset_data, font = ("times new roman", 12, "bold"), bg = "#074463", fg = "white",
                          width = 17).grid(row = 0, column = 3, sticky = "w")
        
        
        
        
        
    # Right_frame
        right_frame = LabelFrame(main_frame, text = "Attendance Details",
                        font = ("times new roman", 15, "bold"), fg = "#074463", relief = GROOVE)
        right_frame.place(x = 750, y = 10, width = 720,height=580)
        
        
        F5 = Frame(right_frame, relief = GROOVE)
        F5.place(x = 5, y = 5, width = 700, height=455)
        
        # ===========scroll bar table=============
        
        scroll_x=ttk.Scrollbar(F5,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(F5,orient=VERTICAL)
        
        self.AttendaceReportTable=ttk.Treeview(F5,column=("id","name","department","batch","time","date","attendace"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)
        
        self.AttendaceReportTable.heading("id",text="RegNo")
        self.AttendaceReportTable.heading("name",text="Name")
        self.AttendaceReportTable.heading("department",text="Department")
        self.AttendaceReportTable.heading("batch",text="Batch")
        self.AttendaceReportTable.heading("time",text="Time")
        self.AttendaceReportTable.heading("date",text="Date")
        self.AttendaceReportTable.heading("attendace",text="Attandace Status")
        
        self.AttendaceReportTable["show"]="headings"
        
        self.AttendaceReportTable.column("id",width="100")
        self.AttendaceReportTable.column("name",width="100")
        self.AttendaceReportTable.column("department",width="100")
        self.AttendaceReportTable.column("batch",width="100")
        self.AttendaceReportTable.column("time",width="100")
        self.AttendaceReportTable.column("date",width="100")
        self.AttendaceReportTable.column("attendace",width="100")
        
        
        
        self.AttendaceReportTable.pack(fill=BOTH,expand=1)
        self.AttendaceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
    # ===============fetch data============
    
    def fetchData(self,rows):
        self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())
        for i in rows:
            self.AttendaceReportTable.insert("",END,values=i)
     
    #  import csv       
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
            
    # export csv
    
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data", "No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
            
    def get_cursor(self,event=""):
        cursor_row=self.AttendaceReportTable.focus()
        content=self.AttendaceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_dep.set(rows[2])
        self.var_atten_batch.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])  
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_batch.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("") 
        
    
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()