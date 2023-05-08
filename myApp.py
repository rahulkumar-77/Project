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
import numpy as np



class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        title_lbl=Label(self.root, text="FACE RECOGNITION", font=("times new roman",30, "bold"), bg='white', fg='green')
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
    # 1st Image    
        img_top=Image.open("college_images/face_detector1.jpg")
        img_top=img_top.resize((650,700),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)
        
    #  2nd Image   
        img_bottom=Image.open("college_images/facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom=img_bottom.resize((950,700),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)
        
    # button
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2", command=self.face_recog,font=("times new roman",15,"bold"),bg="darkgreen",fg="red")
        b1_1.place(x=365,y=620,width=200,height=40)
        
        
        # ===============Attendance=============
        
    def mark_attendance(self,r_n,s_n,v_d,b_y):
        with open("atten.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((s_n not in name_list) and (v_d not in name_list)and (b_y not in name_list) and (r_n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{r_n},{s_n},{v_d},{b_y},{dtString},{d1},Present")
        
        # ===============Face Face_Recognition============
        
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",user="root",password="deepakbabu",database="face_detector")
                my_cursor=conn.cursor()
                my_cursor.execute("select Student_Name from student where Reg_No= "+str(id))
                s_n=my_cursor.fetchone()
                s_n="+".join(s_n)
                
                my_cursor.execute("select var_dep from student where Reg_No= "+str(id))
                v_d=my_cursor.fetchone()
                v_d="+".join(v_d)
                
                my_cursor.execute("select b_year from student where Reg_No= "+str(id))
                b_y=my_cursor.fetchone()
                b_y="+".join(b_y)
                
                
                my_cursor.execute("select Reg_No from student where Reg_No= "+str(id))
                r_n=my_cursor.fetchone()
                r_n="+".join(r_n)
            
                
                if confidence>77:
                    cv2.putText(img,f"Roll_NO:{r_n}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Student_Name:{s_n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"var_dep:{v_d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"b_year:{b_y}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(r_n,s_n,v_d,b_y)
                   
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    cv2.putText(img,f"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,y]
            
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classfier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
                
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
