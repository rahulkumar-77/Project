import tkinter as tk
from login import LoginPage
from face_recognition import Face_Recognition

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.title("My App")

        # Create Student button
        student_button = tk.Button(self.root, text="STUDENT", command=self.student_clicked, font=("Arial", 14),
                                   bg="#4b4e6d", fg="#ffffff", bd=2, padx=20)
        student_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        # Create Admin button
        admin_button = tk.Button(self.root, text="ADMIN", command=self.admin_clicked, font=("Arial", 14), bg="#4b4e6d",
                                 fg="#ffffff", bd=2, padx=20)
        admin_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def student_clicked(self):
        obj=Face_Recognition(self.root)

    def admin_clicked(self):
        obj=LoginPage(self.root)



if __name__=="__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

