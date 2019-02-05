import tkinter as tk
import tkinter.messagebox

# Create the main window
root =tk.Tk()
root.title("SUTURE PRACTICING SITE")
root.geometry("500x500")

#create a container...
frame=tk.Frame(root)
frame.pack()
root.configure(background='black')

#create buttons accordingly...
button1 = tk.Button(frame,text="START",fg="dark green",bg="cyan",font="verdana 10 bold")
button1.pack(side=tk.LEFT)

button2 =tk.Button(frame,text="STOP",fg="dark green",bg="cyan",font="verdana 10 bold",command=root.quit)
button2.pack(side=tk.LEFT,padx=5)


button3 =tk.Button(frame,text="RECORD",fg="dark green",bg="cyan",font="verdana 10 bold")
button3.pack(side=tk.LEFT,padx=5)

button4 =tk.Button(frame,text="ALARM",fg="dark green",bg="cyan",font="verdana 10 bold")
button4.pack(side=tk.RIGHT,padx=5)

button5 =tk.Button(frame,text="S AREA",fg="dark green",bg="cyan",font="verdana 10 bold")
button5.pack(side=tk.RIGHT,padx=5)

'''canvas_width =90
canvas_height=50
scr=Canvas(root,width=canvas_width,height=canvas_height)
scr.pack()'''

button6=tk.Button(root, text='Quit',font="verdana 10 bold",fg="dark green",command=root.destroy)
button6.pack(side=tk.RIGHT)

canvas = tk.Canvas(root, bg='white', width=50, height=50)
# Draw something in the canvas
canvas.create_oval(5, 15, 35, 45, outline='blue')
canvas.create_line(10, 10, 40, 30, fill='red')

def SensorValue():
    print ("SensorValue is = ")
val=89
text = Text(root)
root.mainloop()



