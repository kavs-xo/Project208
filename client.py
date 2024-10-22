#-----------Bolierplate Code Start -----
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

def musicWindow():

    #Client GUI starts here
    window=Tk()
    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg='LightskyBlue')

    select_Label = Label(window, text= "Select Song", bg="LightSkyBlue", font = ("Calibri",8))
    select_Label.place(x=2, y=1)

    listbox = Listbox(window,height = 10,width = 39,activestyle = 'dotbox', bg="LightSkyBlue", borderwidth=2, font = ("Calibri",10))
    listbox.place(x=10, y=10)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    Playbutton=Button(window,text="Play",width=10,bd=1,bg="SkyBlue",font=("Calibri",10))
    Playbutton.place(x=30,y=200)
    
    Stop=Button(window,text="Stop",width=10,bd=1,bg="SkyBlue",font=("Calibri",10))
    Stop.place(x=200,y=200)

    Upload=Button(window,text="Upload",width=10,bd=1,bg="SkyBlue",font=("Calibri",10))
    Upload.place(x=30,y=250)

    Download=Button(window,text="Download",width=10,bd=1,bg="SkyBlue",font=("Calibri",10))
    Download.place(x=200,y=250)

    infoLabel=Label(window,text="",fg="blue",font=("Calibri",0))
    infoLabel.place(x=4,y=200)
  
    window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()

setup()