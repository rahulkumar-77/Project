import tkinter as tk
import tkinter
from tkinter import *

class Developer:
    def __init__(self, name, title, email, phone, photo):
        self.name = name
        self.title = title
        self.email = email
        self.phone = phone
        self.photo = photo

developers = [
    Developer("Ankit Kumar Singh  ", "Software Engineer", "ankitsingh7319@gmail.com", "917250554279", "college_images/Aimg.png"),
    Developer("Rahul Kumar Sharma ", "Software Engineer", "rksharma18119856@gmail.com", "917970681347","college_images/Rimg.png"),
    Developer("Navjot Singh ", "Software Engineer", "navisingh4242@gmail.com", "916200037562", "college_images/Nimg.png"),
    Developer("Deepak Kumar", "Software Engineer", "anshpratapsingh45516@gmail.com", "918542948712", "college_images/Dimg.png"),
    Developer("Vikas Yadav", "Software Engineer", "vikasyadav0971@gmail.com", "917054437311", "college_images/Vimg.png"),
]

class DeveloperPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Developers")
        self.root.state('zoomed')  # maximize the window

        root.configure(bg="#FFFFFF")


        # Create a canvas to hold the developer frames
        canvas = tk.Canvas(self.root, height=500)
        canvas.pack(side="left", fill="both", expand=True)
        
        # Add a scrollbar to the canvas
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a frame to hold the developer frames inside the canvas
        frame = tk.Frame(canvas)

        # Add the frame to the canvas
        canvas.create_window((0, 0), window=frame, anchor="nw")

        # Create header label
        header_label = tk.Label(frame, text="Our Developers", font=("Arial", 20), bg="#0040ff", fg="#000000")
        header_label.pack(pady=10)

        # Create developer frames
        for i in range(0, len(developers), 2):
            sub_frame = tk.Frame(frame, bd=2, relief="groove", bg="#0040ff")
            sub_frame.pack(pady=10, fill="both", expand=True)

            # Load developer photo 1
            photo1 = tk.PhotoImage(file=developers[i].photo)
            photo_label1 = tk.Label(sub_frame, image=photo1, bg="#8c7373")
            photo_label1.image = photo1
            photo_label1.pack(side="left", padx=10)

            # Create developer information labels 1
            info_label1 = tk.Label(sub_frame, text=f"{developers[i].name}\n{developers[i].title}\n{developers[i].email}\n{developers[i].phone}", font=("Arial", 12), bg="#8c7373", fg="#000000")
            info_label1.pack(side="left")

            if i+1 < len(developers):
                # Load developer photo 2
                photo2 = tk.PhotoImage(file=developers[i+1].photo)
                photo_label2 = tk.Label(sub_frame, image=photo2, bg="#8c7373")
                photo_label2.image = photo2
                photo_label2.pack(side="right", padx=10)


                 # Create developer information labels 2
                info_label2 = tk.Label(sub_frame, text=f"{developers[i+1].name}\n{developers[i+1].title}\n{developers[i+1].email}\n{developers[i+1].phone}", font=("Arial", 12), bg="#8c7373", fg="#000000")
                info_label2.pack(side="right")

            # Set background color of header label
            header_label.configure(bg="#8c7373")

            # Set background color and text color of each sub_frame
            for sub_frame in frame.winfo_children():
                sub_frame.configure(bg="#8c7373")
                for label in sub_frame.winfo_children():
                    label.configure(bg="#8c7373", fg="#000000")

        # Show the scrollbar
        canvas.config(scrollregion=canvas.bbox("all"))

if __name__=="__main__":
    root = Tk()
    app = DeveloperPage(root)
    root.mainloop()
