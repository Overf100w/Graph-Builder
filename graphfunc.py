from math import sin

cash = 0

#GRAPH FUNCTIONS
def sine(w, phi, a, dy, canvas):
    global cash
    canvas.delete(cash)
    xy = []

    for x in range(1000):
        y = sin(x * w)
        xy.append(x + phi)
        xy.append(y * a + dy)
    cash = canvas.create_line(xy, fill = 'blue')

def hiperbola(k, canvas):
    global cash
    canvas.delete(cash)
    xy = []

    for x in range(1, 600):
        y = k / x
        xy.append(x + 500)
        xy.append(y + 350)
    cash = canvas.create_line(xy, fill = 'blue')

def line(x, y, x2, y2, canvas):
    global cash 
    canvas.delete(cash)
    cash = canvas.create_line(x + 500, y + 350, x2 + 500, y2 + 350, fill = 'blue')