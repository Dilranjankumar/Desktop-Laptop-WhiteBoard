from tkinter import*
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
 
# creating Window 
window =Tk()
window.title("White Board")
window.geometry("1050x570+150+50")
window.configure(bg="#f2f3f5")
window.resizable(False,False)


#creating function
current_x = 0
current_y = 0
color ='black'

def locate_xy(work):
    global current_x , current_y
    current_x = work.x
    current_y = work.y

def addline(work):
    global current_x , current_y
    canvas.create_line((current_x,current_y, work.x, work.y),width=5,fill=color, capstyle=ROUND,smooth=TRUE)
    current_x, current_y = work.x , work.y
    

def show_color(new_color):
    global color
    color =new_color


def new_canvas():
    canvas.delete('all')
    display_pallete()
    



# icon
image_icon = PhotoImage(file="logo.png")
window.iconphoto(False,image_icon)


#color box
color_box= PhotoImage(file="color section.png")
Label(window,image=color_box,bg="#f2f3f5").place(x=10,y=20)


#Eraser 
eraser =PhotoImage(file="eraser.png")
Button(window,image=eraser,bg="#f2f3f5",command=new_canvas).place(x=30,y=400)


#colors
colors = Canvas(window,bg="#ffffff",width=37,height=300,bd=0)
colors.place(x=30,y=60)

def display_pallete():
    id=colors.create_rectangle((10,10,30,30),fill='black')
    colors.tag_bind(id, '<Button-1>', lambda X: show_color('black'))

    id=colors.create_rectangle((10,40,30,60),fill='gray')
    colors.tag_bind(id, '<Button-1>', lambda X: show_color('gray'))

    id=colors.create_rectangle((10,70,30,90),fill='brown')
    colors.tag_bind(id, '<Button-1>', lambda X: show_color('brown'))

    id=colors.create_rectangle((10,100,30,120),fill='red')
    colors.tag_bind(id, '<Button-1>', lambda X: show_color('red'))

    id=colors.create_rectangle((10,130,30,150),fill='orange')
    colors.tag_bind(id, '<Button-1>', lambda X: show_color('orange'))

    id=colors.create_rectangle((10,160,30,180),fill='yellow')
    colors.tag_bind(id, '<Button-1>', lambda X: show_color('yellow'))

    id=colors.create_rectangle((10,190,30,210),fill='green')
    colors.tag_bind(id, '<Button-1>', lambda X: show_color('green'))

    id=colors.create_rectangle((10,220,30,240),fill='blue')
    colors.tag_bind(id, '<Button-1>', lambda X: show_color('blue'))

    id=colors.create_rectangle((10,250,30,270),fill='purple')
    colors.tag_bind(id, '<Button-1>', lambda X: show_color('purple'))

    id=colors.create_rectangle((10,280,30,300),fill='pink')
    colors.tag_bind(id, '<Button-1>', lambda X: show_color('pink'))
display_pallete()

# canvas
canvas = Canvas(window,width=930,height=500,background="white",cursor="hand2")
canvas.place(x=100,y=10)

#Canvas Bind
canvas.bind('<Button-1>',locate_xy)
canvas.bind('<B1-Motion>',addline)



window.mainloop()
