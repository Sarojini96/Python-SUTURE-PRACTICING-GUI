import tkinter as tk
#import RPi.GPIO as GPIO
#import tkinter.messagebox
import datetime
import pygame
pygame.init()
alarm=pygame.mixer.Sound("alarm.wav")
# Create the main window...
root =tk.Tk()
root.title("SUTURE PRACTICING SITE")
root.geometry("333x170")
root.configure(background='black')
#global root1
#global root
#create another window for threshold bar...
def secscr():
   
   root1 =tk.Tk()
   root1.config(bg='cyan')
   root1.title("threshold")

   #create label for root1 window...
   tk.Label(root1, 
                    text="THRESHOLD SETTING",
                    fg = "black",
                    bg = "cyan",
                    font = "Helvetica 16 bold italic").pack()


   #create entry feilds for threshold setting...
   fields = 'MIN','MAX'
   def fetchdata(entries):
      for entry in entries:
         field = entry[0]
         text  = entry[1].get()
         print('%s: "%s"' % (field, text))

             
   def makeform(root1, fields):
      entries = []
      for field in fields:
         row = tk.Frame(root1)
         lab = tk.Label(row, width=15, text=field, anchor='w')
         ent = tk.Entry(row)
         row.pack(side=tk.TOP,fill='both', padx=5, pady=5)
         lab.pack(side=tk.LEFT)
         ent.pack(side=tk.RIGHT,expand='YES',fill='both')
         entries.append((field, ent))
      return entries
      

   ents = makeform(root1, fields)
   root1.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b1 = tk.Button(root1, text='Show',command=(lambda e=ents: fetchdata(e)))
   b1.pack(side=tk.LEFT, padx=60, pady=5)
   b2 = tk.Button(root1, text='close', command=root1.destroy)
   b2.pack(side=tk.LEFT, padx=5, pady=5)
   return("form opened")
#create doc to record the datas
#def record():
file = open("records.txt", "a")
file.writelines(str(datetime.datetime.now()) + "sensor data")

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
submenu.add_cascade(label="THRESHOLD",command=secscr)
fmenu4.add_cascade(label="SKIN",menu=submenu)
fmenu4.add_separator()
#fmenu4.add_command(label="SOFT TISSUE")
submenu1=tk.Menu(fmenu)#create a  submenu...
submenu1.add_cascade(label="THRESHOLD",command=secscr)
fmenu4.add_cascade(label="SOFT TISSUE",menu=submenu1)
fmenu4.add_separator()
#fmenu4.add_command(label="SOFT TISSUE")

#create a container...
topframe=tk.Frame(root)
topframe.pack()
bottomFrame =tk.Frame(root, bg="black")
bottomFrame.pack(side=tk.BOTTOM)

#create buttons...
#theButton1 = tk.Button(bottomFrame, text="ALARM ON  ", fg="red",font="verdana 10 bold", bg="black")
#theButton1.pack(side=tk.LEFT)
#theButton2 = tk.Button(bottomFrame, text="ALARM OFF", font="verdana 10 bold",fg="red", bg="black")
#theButton2.pack(side=tk.LEFT)
quitbutton=tk.Button(bottomFrame,text='Quit',font="verdana 10 bold",fg="dark green",command=root.destroy)
quitbutton.pack(side=tk.RIGHT)

# create a canvas
frame1 =tk.Frame(root,bg="black")
frame1.pack(pady=5)
#frame.config(bg="black")
canva1=tk.Canvas(frame1,bg='black')
canva1=tk.Canvas(frame1,bg='black')

canva1.create_line(2,55,500,50,fill='green',width=2)#sensor1
canva1.create_line(2, 115, 500, 111,fill='green',width=2)#sensor2
canva1.create_line(2,65,400,65,fill='white',width=1)#seperator
canva1.pack()
label1=tk.Label(root,text="Force :",font="verdana 10 bold")
label1.place(x=50, y=-20)
label1.pack(side=tk.TOP)

