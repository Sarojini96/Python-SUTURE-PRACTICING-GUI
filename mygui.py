import tkinter as tk
#import RPi.GPIO as GPIO
import tkinter.messagebox

# Create the main window
root =tk.Tk()
root.title("SUTURE PRACTICING SITE")
root.geometry("500x300")

#create a container...
frame=tk.Frame(root)
frame.pack()
root.configure(background='black')

#radio_option = tk.IntVar()
'''def clicked():
    label2 = tk.Label(text="skin")
    label2.pack()'''


    

#create buttons accordingly...
button1 = tk.Button(frame,text="START",fg="dark green",bg="cyan",font="verdana 10 bold")
button1.pack(side=tk.LEFT,fill="both")

button2 =tk.Button(frame,text="STOP",fg="dark green",bg="cyan",font="verdana 10 bold",command=root.quit)
button2.pack(side=tk.LEFT,fill="both")
#cmd1=tk.OptionMenu(frame,text="ok")


button3 =tk.Button(frame,text="RECORD",fg="dark green",bg="cyan",font="verdana 10 bold")
button3.pack(side=tk.LEFT,fill="both")
cmd=tk.Button(text="skin")
button4 =tk.Button(frame,text="PAUSE",fg="dark green",bg="cyan",font="verdana 10 bold")
button4.pack(side=tk.LEFT,fill="both")



#button5 =tk.Button(frame,text="ALARM",fg="dark green",bg="cyan",font="verdana 10 bold")
#button5.pack(side=tk.RIGHT,fill="both")

button6 =tk.Button(frame,text="S AREA",fg="dark green",bg="cyan",font="verdana 10 bold")
button6.pack(side=tk.RIGHT,fill="both")

#button7=tk.Button(root, text='Quit',font="verdana 10 bold",fg="dark green",command=root.destroy)
#button7.pack(side="right")

# Create label
#label1 = tk.Label(root, text="Hello, World!",bg="black",fg="white",font=("Arial Bold", 20))

# Lay out label
#label1.pack()
'''radiobutton_1 = tk.Radiobutton( root, 
                                text="Option 1", 
                                variable=radio_option,
                                fg="white",
                                value=1)
radiobutton_2 = tk.Radiobutton( root, 
                                text="Option 2",
                                fg="white",
                                variable=radio_option, 
                                value=2)'''
bottomFrame =tk.Frame(root, bg="black")
bottomFrame.pack(side=tk.BOTTOM)
#bottomFrame_Label =tk.Label(bottomFrame, text="ALARM",fg="red",font=("verdana 10 bold",16))
#bottomFrame_Label.pack(side=tk.LEFT)
theButton1 = tk.Button(bottomFrame, text="ALARM ON  ", fg="red",font="verdana 10 bold", bg="black")
theButton1.pack(side=tk.LEFT)
theButton2 = tk.Button(bottomFrame, text="ALARM OFF", font="verdana 10 bold",fg="red", bg="black")
theButton2.pack(side=tk.LEFT)
quitbutton=tk.Button(bottomFrame,text='Quit',font="verdana 10 bold",fg="dark green",command=root.destroy)
quitbutton.pack(side=tk.RIGHT)


'''canvas_width =90
canvas_height=50
scr=Canvas(root,width=canvas_width,height=canvas_height)
scr.pack()'''


'''canvas = tk.Canvas(root, bg='white', width=50, height=50)
# Draw something in the canvas
canvas.create_oval(5, 15, 35, 45, outline='blue')
canvas.create_line(10, 10, 40, 30, fill='red')'''

def SensorValue():
    print ("SensorValue is = ")
val=89
'''class App:
    def __init__(self, root):
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.entry_var)
        self.entry.bind('<Return>', self.show_output)
        self.entry.pack()
         
    def show_output(self, event):
        print(self.entry_var.get())
         
App(root)
tk.mainloop()'''
root.mainloop()



