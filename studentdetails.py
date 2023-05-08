import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
class StudentDetail:
    def __init__(self, window):
        self.window = window
        self.window.title("Student Details")
        self.window.geometry("%dx%d" % (window.winfo_screenwidth(),
                                        window.winfo_screenheight()))
        
        #==============variables=================
        self.var_dep=StringVar()
        self.b_year=StringVar()
        self.admi_session=StringVar()
        self.section=StringVar()
        self.Reg_No=StringVar()
        self.DOB=StringVar()
        self.Student_Name=StringVar()
        self.Contact_No=StringVar()
        self.Father_Name=StringVar()
        self.Fatherphone=StringVar()
        self.Mother_name=StringVar()
        self.email=StringVar()
        self.Gender=StringVar()
        self.address=StringVar()

        #Title Frame
        F1 = LabelFrame(self.window, relief = GROOVE)
        F1.place(x = 0, y = 30, relwidth = 1)
        title = Label(F1, text = "STUDENT MANAGEMENT SYSTEM",
                      font = ("times new roman", 30, "bold"),
                      fg = "#074463", relief = GROOVE).pack(fill = X)
        button_back = Button(F1, text = "Back", fg = "#074463").pack()

        #Course Information
        F2 = LabelFrame(self.window, text = "Course Information",
                        font = ("times new roman", 15, "bold"), fg = "#074463", relief = GROOVE)
        F2.place(x = 0, y = 115, relwidth = 1)

        dpt_name_lb = Label(F2, text = "Department Name",
                      font = ("times new roman", 12, "bold"),
                      fg = "#074463").grid(row = 0, column = 0, padx = 20, pady = 10)

        dept_name_txt = ttk.Combobox(F2, textvariable=self.var_dep, values = ('-Select-','Agriculture','Bioengineering and Biosciences',
                                                   'Business','Civil Engineering','Computer Applications',
                                                   'Computer Science and Engineering','Electronics & Electrical Engineering'
                                                   'Design','Hotel Management and Tourism','Journalism, Films and Creative Arts',
                                                   'Law','Arts and Languages','Architecture and Design','Education',
                                                   'Mechanical Engineering','Pharmaceutical Sciences',
                                                   'Chemical Engineering and Physical Sciences','Polytechnic','Physical Education'), width = 30,
                                  font = "arial 12", state = "readonly")
        dept_name_txt.grid(row = 0, column = 1)
        dept_name_txt.current(0)

        batch_yr_lb = Label(F2, text = "Batch Year",
                      font = ("times new roman", 12, "bold"),
                      fg = "#074463").grid(row = 0, column = 2, padx = 20, pady = 10)
        batch_yr_txt = ttk.Combobox(F2,textvariable=self.b_year, values = ('-Select-','2018','2019','2020','2021','2022','2023','2024'), width = 16,
                                  font = "arial 12", state = "readonly")
        batch_yr_txt.grid(row = 0, column = 3)
        batch_yr_txt.current(0)

        adm_ssn_lb = Label(F2, text = "Admission Session",
                      font = ("times new roman", 12, "bold"),
                      fg = "#074463").grid(row = 0, column = 4, padx = 20, pady = 10)
        adm_ssn_txt = ttk.Combobox(F2,textvariable=self.admi_session, values = ('-Select-','Semester-1','Semester-2'), width = 16,
                                  font = "arial 12", state = "readonly")
        adm_ssn_txt.grid(row = 0, column = 5)
        adm_ssn_txt.current(0)

        '''
        batch_yr_txt = Entry(F2, width = 15, font = "arial 12", bd = 2,
                             relief = SUNKEN).grid(row = 0, column = 5)
        '''

        section_lb = Label(F2, text = "Section",
                      font = ("times new roman", 12, "bold"),
                      fg = "#074463").grid(row = 0, column = 6, padx = 20, pady = 10)
        section_txt = Entry(F2,textvariable=self.section, width = 16, font = "arial 12", bd = 2,
                             relief = SUNKEN).grid(row = 0, column = 7)

        #Student Information
        F3 = LabelFrame(self.window, text = "Student Information",
                        font = ("times new roman", 15, "bold"), fg = "#074463", relief = GROOVE)
        F3.place(x = 0, y = 195, width = 700)

        reg_no_lb = Label(F3, text = "Registration No.",
                      font = ("times new roman", 12, "bold"),
                      fg = "#074463").grid(row = 0, column = 0, padx = 20, pady = 20, sticky = "w")
        reg_no_txt = Entry(F3,textvariable=self.Reg_No, width = 20, font = "arial 12", bd = 2,
                             relief = SUNKEN).grid(row = 0, column = 1)

        std_name_lb = Label(F3, text = "Student Name",
                      font = ("times new roman", 12, "bold"),
                      fg = "#074463").grid(row = 1, column = 0, padx = 20, pady = 20, sticky = "w")
        std_name_txt = Entry(F3,textvariable=self.Student_Name, width = 20, font = "arial 12", bd = 2,
                             relief = SUNKEN).grid(row = 1, column = 1)

        fthr_name_lb = Label(F3, text = "Father Name",
                      font = ("times new roman", 12, "bold"),
                      fg = "#074463").grid(row = 2, column = 0, padx = 20, pady = 20, sticky = "w")
        fthr_name_txt = Entry(F3,textvariable=self.Father_Name, width = 20, font = "arial 12", bd = 2,
                             relief = SUNKEN).grid(row = 2, column = 1)

        mthr_name_lb = Label(F3, text = "Mother Name",
                      font = ("times new roman", 12, "bold"),
                      fg = "#074463").grid(row = 3, column = 0, padx = 20, pady = 20, sticky = "w")
        mthr_name_txt = Entry(F3,textvariable=self.Mother_name, width = 20, font = "arial 12", bd = 2,
                             relief = SUNKEN).grid(row = 3, column = 1)

        gender_lb = Label(F3, text = "Gender",
                      font = ("times new roman", 12, "bold"),
                      fg = "#074463").grid(row = 4, column = 0, padx = 20, pady = 20, sticky = "w")
        gender_txt = ttk.Combobox(F3,textvariable=self.Gender, values = ('-Select-','Male','Female'), width = 18,
                                  font = "arial 12", state = "readonly")
        gender_txt.grid(row = 4, column = 1)
        gender_txt.current(0)
        
        dob_lb = Label(F3, text = "Date of Birth",
                      font = ("times new roman", 12, "bold"),
                      fg = "#074463").grid(row = 0, column = 3, padx = 20, pady = 20, sticky = "w")
        dob_txt = Entry(F3,textvariable=self.DOB, width = 20, font = "arial 12", bd = 2,
                             relief = SUNKEN).grid(row = 0, column = 4)

        contact_lb = Label(F3, text = "Contact No.",
                      font = ("times new roman", 12, "bold"),
                      fg = "#074463").grid(row = 1, column = 3, padx = 20, pady = 20, sticky = "w")
        contact_txt = Entry(F3,textvariable=self.Contact_No, width = 20, font = "arial 12", bd = 2,
                             relief = SUNKEN).grid(row = 1, column = 4)

        fcontact_lb = Label(F3, text = "Father's No.",
                      font = ("times new roman", 12, "bold"),
                      fg = "#074463").grid(row = 2, column = 3, padx = 20, pady = 20, sticky = "w")
        fcontact_txt = Entry(F3,textvariable=self.Fatherphone, width = 20, font = "arial 12", bd = 2,
                             relief = SUNKEN).grid(row = 2, column = 4)

        email_lb = Label(F3, text = "Email",
                      font = ("times new roman", 12, "bold"),
                      fg = "#074463").grid(row = 3, column = 3, padx = 20, pady = 20, sticky = "w")
        email_txt = Entry(F3,textvariable=self.email, width = 20, font = "arial 12", bd = 2,
                             relief = SUNKEN).grid(row = 3, column = 4)

        address_lb = Label(F3, text = "Address",
                      font = ("times new roman", 12, "bold"),
                      fg = "#074463").grid(row = 4, column = 3, padx = 20, pady = 20, sticky = "w")
        address_txt = Entry(F3,textvariable=self.address, width = 20, font = "arial 12", bd = 2,
                             relief = SUNKEN).grid(row = 4, column = 4)

        self.varb1=StringVar()
        b1 = ttk.Radiobutton(F3, text = "Take Photo Sample", variable=self.varb1, value = "Yes").grid(row = 5, column = 0, padx = 5, pady = 2)
        b2 = ttk.Radiobutton(F3, text = "No Photo Sample", variable=self.varb1 , value = "No").grid(row = 5, column = 1, padx = 5, pady = 2)
        
        F4 = LabelFrame(self.window, relief = GROOVE)
        F4.place(x = 0, y = 580, width = 700)

        save_btn = Button(F4, text = "SAVE",command=self.add_data, font = ("times new roman", 12, "bold"), bg = "#074463", fg = "white",
                          width = 18, height = 2).grid(row = 0, column = 0, sticky = "w")
        
        update_btn = Button(F4, text = "UPDATE",command=self.update_data, font = ("times new roman", 12, "bold"), bg = "#074463", fg = "white",
                          width = 18, height = 2).grid(row = 0, column = 1, sticky = "w")
        
        delete_btn = Button(F4, text = "DELETE",command=self.delete_data, font = ("times new roman", 12, "bold"), bg = "#074463", fg = "white",
                          width = 18, height = 2).grid(row = 0, column = 2, sticky = "w")
        
        reset_btn = Button(F4, text = "RESET",command=self.reset_data, font = ("times new roman", 12, "bold"), bg = "#074463", fg = "white",
                          width = 19, height = 2).grid(row = 0, column = 3, sticky = "w")

        F5 = LabelFrame(self.window, relief = GROOVE)
        F5.place(x = 0, y = 635, width = 700)

        add_photo_btn = Button(F5,command=self.generate_dataset, text = "ADD PHOTO SAMPLE", font = ("times new roman", 12, "bold"), bg = "#074463", fg = "white",
                          width = 37, height = 2).grid(row = 0, column = 0, sticky = "w")
        
        upload_photo_btn = Button(F5, text = "UPLOAD PHOTO SAMPLE", font = ("times new roman", 12, "bold"), bg = "#074463", fg = "white",
                          width = 38, height = 2).grid(row = 0, column = 1, sticky = "w")

        F6 = LabelFrame(self.window, text = "Student Details", font = ("times new roman", 15, "bold"), fg = "#074463", relief = GROOVE)
        F6.place(x = 700, y = 195, height = 495, width = 666)

        search_lb = Label(F6, text = "Search By", font = ("times new roman", 12, "bold"),
                      bg = "#074463", fg = "white").grid(row = 0, column = 0, padx = 20, pady = 20)

        search_op = ttk.Combobox(F6, values = ('-Select-','Registration No.','Contact No.','Email'), width = 18,
                                  font = "arial 12", state = "readonly")
        search_op.grid(row = 0, column = 1)
        search_op.current(0)

        search_txt = Entry(F6, width = 20, font = "arial 12", bd = 2,
                             relief = SUNKEN).grid(row = 0, column = 3, padx = 18)

        search_btn = Button(F6, text = "SEARCH", font = ("times new roman", 12, "bold"), bg = "#074463", fg = "white",
                          width = 12).grid(row = 0, column = 4)

        F7 = Frame(self.window, bg = "#074463", relief = RIDGE, bd = 4)
        F7.place(x = 710, y = 290, height = 380, width = 640)

        scroll_x = ttk.Scrollbar(F7, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(F7, orient = VERTICAL)

        self.student_table = ttk.Treeview(F7, column = ("dep", "year", "admssn", "section", "regno", "name", "fname", "mname", "gender",
                                             "dob", "cont", "fcont", "email", "addr","photo"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)
        scroll_x.config(command = self.student_table.xview)
        scroll_y.config(command = self.student_table.yview)

        self.student_table.heading("dep", text = "Department Name")
        self.student_table.heading("year", text = "Batch Year")
        self.student_table.heading("admssn", text = "Admission Session")
        self.student_table.heading("section", text = "Section")
        self.student_table.heading("regno", text = "Registration No.")
        self.student_table.heading("name", text = "Student Name")
        self.student_table.heading("fname", text = "Father Name")
        self.student_table.heading("mname", text = "Mother Name")
        self.student_table.heading("gender", text = "Gender")
        self.student_table.heading("dob", text = "Date of Birth")
        self.student_table.heading("cont", text = "Contact No.")
        self.student_table.heading("fcont", text = "Father's No.")
        self.student_table.heading("email", text = "Email")
        self.student_table.heading("addr", text = "Address")
        self.student_table.heading("photo",text="PhotoSampeStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width = 150)
        self.student_table.column("year", width = 150)
        self.student_table.column("admssn", width = 150)
        self.student_table.column("section", width = 150)
        self.student_table.column("regno", width = 150)
        self.student_table.column("name", width = 150)
        self.student_table.column("fname", width = 150)
        self.student_table.column("mname", width = 150)
        self.student_table.column("gender", width = 150)
        self.student_table.column("dob", width = 150)
        self.student_table.column("cont", width = 150)
        self.student_table.column("fcont", width = 150)
        self.student_table.column("email", width = 150)
        self.student_table.column("addr", width = 150)
        self.student_table.column("photo", width = 150)

        self.student_table.pack(fill = BOTH, expand = 1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #========================================= store student data =================================== 
    def add_data(self):
        if self.var_dep.get()=="-Select-" or self.b_year.get()=="-Select-" or self.admi_session.get()=="-Select-":
            messagebox.showerror("Error","All Fields are required",parent=self.window)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Yadav@7311",database="face_detector")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.b_year.get(),
                    self.admi_session.get(),
                    self.section.get(),
                    self.Reg_No.get(),
                    self.DOB.get(),
                    self.Student_Name.get(),
                    self.Contact_No.get(),
                    self.Father_Name.get(),
                    self.Fatherphone.get(),
                    self.Mother_name.get(),
                    self.email.get(),
                    self.Gender.get(),
                    self.address.get(),
                    self.varb1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student details has been added Successfully",parent=self.window)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.window)
                
    #==================fetch data=======================            
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Yadav@7311",database="face_detector")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    #==============================getdata====================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.b_year.set(data[1]),
        self.admi_session.set(data[2]),
        self.section.set(data[3]),
        self.Reg_No.set(data[4]),
        self.DOB.set(data[5]),
        self.Student_Name.set(data[6]),
        self.Contact_No.set(data[7]),
        self.Father_Name.set(data[8]),
        self.Fatherphone.set(data[9]),
        self.Mother_name.set(data[10]),
        self.email.set(data[11]),
        self.Gender.set(data[12]),
        self.address.set(data[13]),
        self.varb1.set(data[14])
        
        #=============updateFunction=======================
    def update_data(self):
        if self.var_dep.get()=="-Select-" or self.b_year.get()=="-Select-" or self.admi_session.get()=="-Select-" or self.Reg_No.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.window)
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you want to update this student details",parent=self.window)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Yadav@7311",database="face_detector")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set var_dep=%s,b_year=%s,admi_session=%s,section=%s,DOB=%s,Student_Name=%s,Contact_No=%s,Father_Name=%s,Fatherphone=%s,Mother_name=%s,email=%s,Gender=%s,address=%s,verb1=%s where Reg_No=%s",(

                            self.var_dep.get(),
                            self.b_year.get(),
                            self.admi_session.get(),
                            self.section.get(),
                            self.DOB.get(),
                            self.Student_Name.get(),
                            self.Contact_No.get(),
                            self.Father_Name.get(),
                            self.Fatherphone.get(),
                            self.Mother_name.get(),
                            self.email.get(),
                            self.Gender.get(),
                            self.address.get(),
                            self.varb1.get(),
                            self.Reg_No.get()
                    ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success", "Student Details Successfully updated",parent=self.window)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.window)
                
    #==================DELETE FUNCTION=========================
    def delete_data(self):
        if self.Reg_No.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.window)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.window)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Yadav@7311",database="face_detector")
                    my_cursor=conn.cursor()
                    sql="delete from student where Regno=%s"
                    val=(self.Reg_No.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfuly Deleted student detials",parent=self.window)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.window)
                
    def reset_data(self):
        self.var_dep.set("-Select-"),
        self.b_year.set("-Select-"),
        self.admi_session.set("-Select-"),
        self.section.set(""),
        self.Reg_No.set(""),
        self.DOB.set(""),
        self.Student_Name.set(""),
        self.Contact_No.set(""),
        self.Father_Name.set(""),
        self.Fatherphone.set(""),
        self.Mother_name.set(""),
        self.email.set(""),
        self.Gender.set("-Select-"),
        self.address.set(""),
        self.varb1.set("")

# ============================Generate data set or Take photo samples=================================

    def generate_dataset(self):
        if self.var_dep.get()=='select Department' or self.Student_Name.get()=="" or self.Reg_No.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.window)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Yadav@7311", database="face_detector")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set var_dep=%s,b_year=%s,admi_session=%s,section=%s,DOB=%s,Student_Name=%s,Contact_No=%s,Father_Name=%s,Fatherphone=%s,Mother_name=%s,email=%s,Gender=%s,address=%s,verb1=%s where Reg_No=%s",(
                                    self.var_dep.get(),
                                    self.b_year.get(),
                                    self.admi_session.get(),
                                    self.section.get(),
                                    self.DOB.get(),
                                    self.Student_Name.get(),
                                    self.Contact_No.get(),
                                    self.Father_Name.get(),
                                    self.Fatherphone.get(),
                                    self.Mother_name.get(),
                                    self.email.get(),
                                    self.Gender.get(),
                                    self.address.get(),
                                    self.varb1.get(),
                                    self.Reg_No.get()==id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                # ========Load predifiend data on face frontals from opencv====
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor=1.3
                    # Minimum Neighbor=5
                    
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break   
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data set completed!!!")
            
            except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.window)
            
            
                
            
            
            
            
            







if __name__ == "__main__":
    root=Tk()
    obj=StudentDetail(root)
    root.mainloop()