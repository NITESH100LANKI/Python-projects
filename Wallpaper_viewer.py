from tkinter import *
from PIL import ImageTk, Image
counter=1
def rotate_image():
    global counter
    image_label.configure(image=image_array[counter % len(image_array)])
    counter +=1
import os
root = Tk()
root.title("Wallpaper Viewer")
root.geometry("250x400")
root.configure(bg="black")
image_folder = r"C:\CODING\HTML\cssproject\wallpaper"
valid_exts = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
files = [f for f in os.listdir(image_folder) if f.lower().endswith(valid_exts)]
image_array=[]
for file in files:
    img=Image.open(os.path.join(image_folder, file))
    resized_image=img.resize((200,300))
    image_array.append(ImageTk.PhotoImage(resized_image))
image_label=Label(root, image=image_array[0])
image_label.pack(pady=(15,10))
next_btn=Button(root, text="Next",bg='white',fg='black',width=28,height=2,command=rotate_image)
next_btn.pack()
root.mainloop()