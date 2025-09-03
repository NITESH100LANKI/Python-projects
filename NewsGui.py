import urllib
import webbrowser
import io
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image

class NewsGui:
    def __init__(self):
        #fetch Api
        self.data=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=26e9b3be1a624246873e53625463777a").json()

        #inital Gui load
        self.load_gui()

        #load the first news
        self.load_news_iteams(0)
    def load_gui(self):
        self.root=Tk()
        self.root.geometry("380x700")
        self.root.resizable(0,0)
        self.root.configure(bg="black")
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    def load_news_iteams(self,index):
        #clear the screen for next news item
        self.clear()
        #image
        try:
            img_url=self.data['articles'][index]['urlToImage']
            raw_data=urlopen(img_url).read()
            im=Image.open(io.BytesIO(raw_data)).resize((350,250))
            photos=ImageTk.PhotoImage(im)
        except:
            img_url = 'https://www.imagefilesize.com/img/icon.png'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photos = ImageTk.PhotoImage(im)
        label=Label(self.root,image=photos)
        label.image=photos
        label.pack(pady=(10,0))
        heading=Label(self.root,text=self.data['articles'][index]['title'],bg="black",fg="white",wraplength=380,justify=CENTER)
        heading.pack(padx=10,pady=10)
        heading.config(font=("verdana",20))
        details= Label(self.root, text=self.data['articles'][index]['description'], bg="black", fg="white", wraplength=380,justify=CENTER)
        details.pack(padx=10, pady=10)
        details.config(font=("verdana", 14))
        frame=Frame(self.root,bg="black")
        #frame.pack(expand=True, fill=BOTH)
        frame.pack(pady=10, side=BOTTOM)
        if index !=0:
            prev=Button(frame,text='Prev',width=16,height=3,command=lambda:self.load_news_iteams(index-1))
            prev.pack(side=LEFT)
        read=Button(frame,text='Read',width=16,height=3,command=lambda:self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)
        if index !=len(self.data['articles'])-1:
            next=Button(frame,text='Next',width=16,height=3,command=lambda:self.load_news_iteams(index+1))
            next.pack(side=LEFT)
        self.root.mainloop()
    def open_link(self,url):
        webbrowser.open(url)
object=NewsGui()
