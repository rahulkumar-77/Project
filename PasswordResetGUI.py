
import random
import bcrypt
import mysql.connector
import tkinter as tk
from twilio.rest import Client

class PasswordResetGUI:
    def __init__(self, root):
        self.loginroot=root
        self.root = tk.Tk()
        self.root.geometry("400x200")
        self.root.title("Password Reset")

        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Rakeshsharma77@",
            database="adminlogin"
        )

        self.username_label = tk.Label(self.root, text="Username:", font=("Arial", 14))
        self.username_label.place(relx=0.3, rely=0.3, anchor=tk.CENTER)
        self.username_entry = tk.Entry(self.root, font=("Arial", 14), bd=2)
        self.username_entry.place(relx=0.7, rely=0.3, anchor=tk.CENTER)

        # Create the forgot password button
        self.forgot_password_button = tk.Button(self.root, text="Forgot Password", command=self.forgot_password,
                                           font=("Arial", 14), bg="#FF6B6B", fg="white", bd=2, padx=20)
        self.forgot_password_button.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

    def forgot_password(self):
        # Get the entered username
        username = self.username_entry.get()

        # Check if the username exists in the database
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM loginDetails WHERE username = %s", (username,))
        result = cursor.fetchmany(3)

        if result:

            userFound = tk.Label(self.root, text="         User Exist         ", font=("Arial", 12), fg="green")
            userFound.place(relx=0.5, rely=0.85, anchor=tk.CENTER)



            cursor.execute("SELECT * FROM loginDetails WHERE username = %s", [username])


            # Send a password reset email to the user's Mobile number


            otp= random.randint(1000,9999)
            try:
                account_sid="Enter yours"
                auth_token= "Enter Yours"
                client= Client(account_sid,auth_token)
                msg=client.messages.create(
                    body=f"Your Face-Up Detector verification code is {otp}. Please do not share with anyone",
                    from_= "Enter Yours from twilio",
                    to = result[0][2]
                )

            except:
                cannot = tk.Label(self.root, text="cannot send otp", font=("Arial", 12), fg="green")
                cannot.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
                self.root.after(5000,self.root.destroy)


            # Create a new window for entering OTP and new password
            self.otp_window = tk.Toplevel(self.root)
            self.otp_window.title("Enter OTP and new password")
            self.otp_window.geometry("400x400")

            otp_label = tk.Label(self.otp_window, text="Enter OTP", font=("Arial", 14))
            otp_label.pack(pady=5)

            otp_entry = tk.Entry(self.otp_window, font=("Arial", 14), width=20)
            otp_entry.pack(pady=5)



            submit_button = tk.Button(self.otp_window, text="Validate", command=lambda: self.submit_otp(
                otp_entry.get(),
                otp,
                username
            ), font=("Arial", 14), bg="#4b4e6d", fg="#ffffff", bd=2, padx=20)
            submit_button.pack(pady=10)


        else:

            nouser = tk.Label(self.root, text="User does not exist", font=("Arial", 12), fg="red")
            nouser.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    def submit_otp(self, entered_otp, actual_otp, username):

        if entered_otp == str(actual_otp):

            new_password_label = tk.Label(self.otp_window, text="Enter new password", font=("Arial", 14))
            new_password_label.pack(pady=5)

            new_password_entry = tk.Entry(self.otp_window, font=("Arial", 14), width=20, show="*")
            new_password_entry.pack(pady=5)

            confirm_password_label = tk.Label(self.otp_window, text="Confirm new password", font=("Arial", 14))
            confirm_password_label.pack(pady=5)

            confirm_password_entry = tk.Entry(self.otp_window, font=("Arial", 14), width=20, show="*")
            confirm_password_entry.pack(pady=5)


            submitbutton = tk.Button(self.otp_window, text="Submit",
                                     command=lambda: self.submit_new_password(new_password_entry.get(),
                                                                              confirm_password_entry.get(), username),
                                     font=("Arial", 14), bg="#FF6B6B", fg="white", bd=2, padx=20)

            submitbutton.pack(pady=10)




        else:
            # Show failure message in GUI
            failure_label = tk.Label(self.root, text="OTP verification failed", font=("Arial", 12), fg="red")
            failure_label.place(relx=0.5, rely=0.85, anchor=tk.CENTER)


    def submit_new_password(self,new_password,confirm_password,username):

        if new_password == confirm_password:
            self.save_new_password(new_password, username)
        else:
            failure_label = tk.Label(self.otp_window, text="Passwords do not match", font=("Arial", 12), fg="red")
            failure_label.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
    def save_new_password(self,new_password,username):


        # Update the password in the database
        Newhashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        cursor = self.mydb.cursor()

        cursor.execute("UPDATE loginDetails SET passwd = %s WHERE username = %s",[Newhashed_password.decode('utf-8'), username])
        self.mydb.commit()

        # Show success message in GUI
        success_label = tk.Label(self.otp_window, text="Password stored successfully!", font=("Arial", 12), fg="green")
        success_label.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

        self.otp_window.after(2000, self.otp_window.destroy)
        success_label = tk.Label(self.loginroot, text="Password stored successfully!", font=("Arial", 12), fg="green")
        success_label.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    obj = PasswordResetGUI(root)
    root.mainloop()
