import tkinter as tk
#import RPi.GPIO as GPIO
import tkinter.messagebox

# Create the main window...

root =tk.Tk()
root.title("SUTURE PRACTICING SITE")
root.geometry("500x300")
root.configure(background='black')

#Create menu...
menu=tk.Menu(root)
root.config(menu=menu)
menu.config(bg='cyan')
fmenu=tk.Menu(menu)
menu.add_cascade(label="START",font=("verdana 10 bold",12),menu=fmenu)

fmenu1=tk.Menu(menu)
menu.add_cascade(label="STOP",font=("verdana 10 bold",12),menu=fmenu1)

fmenu2=tk.Menu(menu)
menu.add_cascade(label="RECORD",font=("verdana 10 bold",12),menu=fmenu2)

fmenu3=tk.Menu(menu)
menu.add_cascade(label="PAUSE",font=("verdana 10 bold",12),menu=fmenu3)

fmenu4=tk.Menu(menu)
menu.add_cascade(label="SAREA",font=("verdana 10 bold",12),menu=fmenu4)

submenu=tk.Menu(fmenu)#create a  submenu...
submenu.add_command(label="THRESHOLD")
fmenu4.add_cascade(label="SKIN",menu=submenu)
fmenu4.add_separator()
fmenu4.add_command(label="SOFT TISSUE")

#create a container...
topframe=tk.Frame(root)
topframe.pack()
bottomFrame =tk.Frame(root, bg="black")
bottomFrame.pack(side=tk.BOTTOM)

#create buttons...
theButton1 = tk.Button(bottomFrame, text="ALARM ON  ", fg="red",font="verdana 10 bold", bg="black")
theButton1.pack(side=tk.LEFT)
theButton2 = tk.Button(bottomFrame, text="ALARM OFF", font="verdana 10 bold",fg="red", bg="black")
theButton2.pack(side=tk.LEFT)
quitbutton=tk.Button(bottomFrame,text='Quit',font="verdana 10 bold",fg="dark green",command=root.destroy)
quitbutton.pack(side=tk.RIGHT)
