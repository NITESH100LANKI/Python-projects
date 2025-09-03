from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def handle_login():
    email = email_input.get()
    password = password_input.get()
    if email == "nitish@gmail.com" and password == "1234":
        messagebox.showinfo("Login", "Login successful")
    else:
        messagebox.showerror("Login", "Invalid email or password")

root = Tk()
root.title("Login Form")
root.iconbitmap("IMG_E6499.JPG")
root.geometry("350x500")
root.configure(bg="#0096dc")


img = Image.open(r"C:\CODING\HTML\flipcartlogo.png")


image_resize = img.resize((150, 150))
Img = ImageTk.PhotoImage(image_resize)

# ✅ Show image in tkinter
label_image = Label(root, image=Img, bg="#0096dc")
label_image.pack(pady=(10,10))

# Heading
text_label = Label(root, text="Flipkart", bg="#0096dc", fg="white", font=("verdana", 20))
text_label.pack(pady=(10,10))

# Email field
email_label = Label(root, text="Enter Email", bg="#0096dc", fg="white", font=("verdana", 12))
email_label.pack(pady=(20,5))
email_input = Entry(root, width=40)
email_input.pack(pady=(1,15))

# Password field
password_label = Label(root, text="Enter Password", bg="#0096dc", fg="white", font=("verdana", 12))
password_label.pack(pady=(20,5))
password_input = Entry(root, width=40, show="*")
password_input.pack(ipady=6, pady=(1,15))

# Login button
login_button = Button(root, text="Login", command=handle_login, bg="white", fg="#0096dc", width=20, height=2, font=("verdana", 10))
login_button.pack(pady=(10,20))

root.mainloop()
