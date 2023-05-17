import tkinter as tk
import mysql.connector
#pip install bcrypt
import bcrypt
from main import Face_Recognization_System
from PasswordResetGUI import PasswordResetGUI
import random
from twilio.rest import Client
#pip install twilio


class LoginPage:
    def __init__(self, root):

        # Create a MySQL database connection
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Yadav@7311",
            database="adminlogin"
        )

        self.root = root
        self.root.title("Login Page")

        # Calculate the x and y coordinates for the window to be centered on the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (500 / 2)
        y = (screen_height / 2) - (600 / 2)
        self.root.geometry("%dx%d+%d+%d" % (500, 600, x, y))

        # Create the background gradient
        self.canvas = tk.Canvas(self.root, width=500, height=600)
        self.canvas.pack()
        gradient_start = "#ffb6b9"  # Light red
        gradient_end = "#7ed6df"  # Light blue
        self.canvas.create_rectangle(0, 0, 500, 600, fill=gradient_start, width=0)
        for i in range(0, 600):
            r = int(255 - (255 * i / 600))
            g = int(182 - (182 * i / 600))
            b = int(185 - (185 * i / 600))
            color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            self.canvas.create_line(0, i, 500, i, fill=color, width=1)

        # Create the login form
        self.username_label = tk.Label(root, text="Enter credentials", bg='LightPink3',
                                       font=("Lucida Handwriting", 16, "bold"))
        self.username_label.place(relx=0.46, rely=0.25, anchor=tk.CENTER)  # username_label.place(x=90, y=180)

        def on_entry_click1(event):
            if self.username_entry.get() == 'Username':
                self.username_entry.delete(0, 'end')  # Delete all the text in the entry
                self.username_entry.insert(0, '')  # Insert blank for user input
                self.username_entry.config(fg='black')  # Change the text color to black

        def on_entry_leave1(event):
            if self.username_entry.get() == '':
                self.username_entry.insert(0, 'Username')
                self.username_entry.config(fg='grey')

        self.username_entry = tk.Entry(self.root, width=20, font=("Arial", 16), fg='grey', bd=4)
        self.username_entry.insert(0, 'Username')
        self.username_entry.bind('<FocusIn>', on_entry_click1)
        self.username_entry.bind('<FocusOut>', on_entry_leave1)
        self.username_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)  # username_entry.place(x=210, y=180)

        def on_entry_click2(event):
            if self.password_entry.get() == 'Password':
                self.password_entry.delete(0, 'end')  # Delete all the text in the entry
                self.password_entry.insert(0, '')  # Insert blank for user input
                self.password_entry.config(fg='black', show="*")  # Change the text color to black

        def on_entry_leave2(event):
            if self.password_entry.get() == '':
                self.password_entry.insert(0, 'Password')
                self.password_entry.config(fg='grey', show="")

        self.password_entry = tk.Entry(self.root, width=20, font=("Arial", 16), fg='grey', bd=4)
        self.password_entry.insert(0, 'Password')
        self.password_entry.bind('<FocusIn>', on_entry_click2)
        self.password_entry.bind('<FocusOut>', on_entry_leave2)
        self.password_entry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)  # password_entry.place(x=210, y=230)

       
        def login():
            # Get the entered username and password
            username = self.username_entry.get()
            password = self.password_entry.get()



            # Check if the username and password exist in the database
            cursor = self.mydb.cursor()

            cursor.execute("SELECT * FROM loginDetails WHERE username = %s", [username])

            result=cursor.fetchmany(3)

            if not result:

                failure_label = tk.Label(self.root, text="Invalid username or Password", font=("Arial", 12), fg="red")
                failure_label.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
            else:
                # compare the hashed password with the user-entered password
              
                hashed_password = result[0][1].encode('utf-8')
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password):

                    obj = Face_Recognization_System(root)
                else:
                    failure_label1 = tk.Label(self.root, text="Invalid username or Password", font=("Arial", 12),
                                             fg="red")
                    failure_label1.place(relx=0.5, rely=0.85, anchor=tk.CENTER)




        # Create the login button
        login_button = tk.Button(self.root, text="Login", command=login, font=("Arial", 14), bg="#4b4e6d", fg="#ffffff",
                                 bd=2)
        login_button.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

        # Create the forgot password function
        def forgot_password():
            obj = PasswordResetGUI(root)

        forgot_password_button = tk.Button(self.root, text="Forgot Password", command=forgot_password,
                                           font=("Arial", 14), bg="#FF6B6B", fg="white", bd=2, padx=20)
        forgot_password_button.place(relx=0.5, rely=0.65,
                                     anchor=tk.CENTER)


if __name__ == "__main__":
    root = tk.Tk()
    obj=LoginPage(root)
    root.mainloop()
