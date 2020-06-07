from tkinter import *
from math import sin
import graphfunc

w = 1400
h = 700
canv_w = w * 0.714    #"(w * 0.714)" - is width of graph field

#WINDOW CREATE
root = Tk()
root.title('graph buider')
root.geometry('{}x{}'.format(w, h))
root.resizable(width=True, height=False)

Label(root, font = 'Courier 20', text = 'THE GRAPH BUILDER').place(x = 37, y = 40)

#canvas
canv = Canvas(root, width = canv_w, height = h, bg = '#fff')               

#lines
for x in range(int(w)):
    if x % 25 == 0:
        canv.create_line(x, h, x, 0, fill = '#ccc')
for y in range(int(h)):
    if y % 25 == 0:
        canv.create_line(0, y, w, y, fill = '#ccc')

#Vertical & horisontal bold lines
canv.create_line(0, h / 2, w, h / 2, width = 2)
canv.create_line((w * 0.714) / 2, 0, canv_w / 2 , h, width = 2)

#marks
canv.create_text(canv_w / 1.95, 10, text = 'Y')
canv.create_text(10, h / 2.07, text = 'X')
canv.create_text(canv_w / 1.95, h / 2.07, text = '0')

def udolit():
    try:
        entry_w.destroy()
        entry_phi.destroy()
        entry_a.destroy()
        entry_dy.destroy()

        entry_k.destroy()
        
        entry_yl.destroy()
        entry_xl.destroy()
        entry_yl2.destroy()
        entry_xl2.destroy()
    except:
        pass

def call_hiperbola():
    global entry_k 
    udolit()

    entry_k = Entry(root, width = 30)#for hiperbol
    entry_k.insert(1, 'K')
    entry_k.place(x = 40, y = 200)

    btn_calc = Button(root, text = 'Build', width = 10, heigh = 2) #build btn
    btn_calc.bind('<Button-1>', lambda e: graphfunc.hiperbola(float(entry_k.get()), canv))
    btn_calc.place(x = 160, y = 600)
    
def call_sine():
    global entry_w, entry_phi, entry_a, entry_dy
    udolit()

    entry_w = Entry(root, width = 30)#for sine graph
    entry_phi = Entry(root, width = 30)
    entry_a = Entry(root, width = 30)
    entry_dy = Entry(root, width = 30)

    entry_w.insert(0, 'W')
    entry_phi.insert(0, 'Phi')
    entry_a.insert(0, 'A')
    entry_dy.insert(0, 'dy')

    entry_w.place(x = 40, y = 200)
    entry_phi.place(x = 40, y = 250)
    entry_a.place(x = 40, y = 300)
    entry_dy.place(x = 40, y = 350)

    btn_calc = Button(root, text = 'Build', width = 10, heigh = 2) #build btn
    btn_calc.bind('<Button-1>', lambda e: graphfunc.sine(float(entry_w.get()), float(entry_phi.get()), float(entry_a.get()), float(entry_dy.get()), canv))
    btn_calc.place(x = 160, y = 600)

def call_line():
    global entry_xl, entry_yl, entry_xl2, entry_yl2
    udolit()

    entry_xl = Entry(root, width = 30)
    entry_yl = Entry(root, width = 30)
    entry_xl2 = Entry(root, width = 30)
    entry_yl2 = Entry(root, width = 30)

    entry_xl.insert(0, 'x')
    entry_yl.insert(0, 'y')
    entry_xl2.insert(0, 'x2')
    entry_yl2.insert(0, 'y2')

    entry_xl.place(x = 40, y = 200)
    entry_yl.place(x = 40, y = 250)
    entry_xl2.place(x = 40, y = 300)
    entry_yl2.place(x = 40, y = 350)
    
    btn_calc = Button(root, text = 'Build', width = 10, heigh = 2) #build btn
    btn_calc.bind('<Button-1>', lambda e: graphfunc.line(int(entry_xl.get()), int(entry_yl.get()), int(entry_xl2.get()), int(entry_yl2.get()), canv))
    btn_calc.place(x = 160, y = 600)

#Buttons
btn_hpbla = Button(root, text = 'hiperbola', width = 8)
btn_hpbla.bind('<Button-1>', lambda e: call_hiperbola())
btn_hpbla.place(x = 40, y = 130)

btn_sine = Button(root, text = 'sine', width = 8)
btn_sine.bind('<Button-1>', lambda e: call_sine())
btn_sine.place(x = 120, y = 130)

btn_line = Button(root, text = 'line', width = 8)
btn_line.bind('<Button-1>', lambda e: call_line())
btn_line.place(x = 200, y = 130)

canv.pack(side = 'right')
canv.mainloop()