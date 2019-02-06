import tkinter as tk
import tkinter.messagebox

# Create the main window
root =tk.Tk()
root.title("SUTURE PRACTICING SITE")
root.geometry("500x300")

#create a container...
frame=tk.Frame(root)
frame.pack()
root.configure(background='black')


def clicked():
    label2 = tk.Label(text="skin")
    label2.pack()
    

#create buttons accordingly...
button1 = tk.Button(frame,text="START",fg="dark green",bg="cyan",font="verdana 10 bold")
button1.pack(side=tk.LEFT)

button2 =tk.Button(frame,text="STOP",fg="dark green",bg="cyan",font="verdana 10 bold",command=root.quit)
button2.pack(side=tk.LEFT,padx=5)


button3 =tk.Button(frame,text="RECORD",fg="dark green",bg="cyan",font="verdana 10 bold")
button3.pack(side=tk.LEFT,padx=5)

button4 =tk.Button(frame,text="PAUSE",fg="dark green",bg="cyan",font="verdana 10 bold")
button4.pack(side=tk.LEFT,padx=5)


button5 =tk.Button(frame,text="ALARM",fg="dark green",bg="cyan",font="verdana 10 bold")
button5.pack(side=tk.RIGHT,padx=5)

button6 =tk.Button(frame,text="S AREA",fg="dark green",bg="cyan",font="verdana 10 bold",command=clicked)
button6.pack(side=tk.RIGHT,padx=5)

button7=tk.Button(root, text='Quit',font="verdana 10 bold",fg="dark green",command=root.destroy)
button7.pack(side=tk.RIGHT)

# Create label
label1 = tk.Label(root, text="Hello, World!",bg="black",fg="white",font=("Arial Bold", 20))

# Lay out label
label1.pack()



'''canvas_width =90
canvas_height=50
scr=Canvas(root,width=canvas_width,height=canvas_height)
scr.pack()'''


canvas = tk.Canvas(root, bg='white', width=50, height=50)
# Draw something in the canvas
canvas.create_oval(5, 15, 35, 45, outline='blue')
canvas.create_line(10, 10, 40, 30, fill='red')

def SensorValue():
    print ("SensorValue is = ")
val=89

root.mainloop()



