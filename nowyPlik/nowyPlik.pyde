class Czlowiek(object):
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        global t, m, r, y1, y2, r, g, b, rt, gt, bt, rm, gm, bm
    
    def display(self):
        fill(self.c)
        r = 30
        circle(self.xpos, self.ypos, r);
        
    def bieg(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
    
#ZMIENNE TATY
xspeed = 2
ypos = 300
r = 0
g = 255
b = 255
tata = Czlowiek(color(r, g, b), 0, ypos, xspeed)
#ZAPISANE DANE
rt = r
gt = g
bt = b
y1 = ypos
t = xspeed

#ZMIENNE MAMY
ypos = 100
xspeed = 4
r = 255
g = 0
b = 255
mama = Czlowiek(color(r, g, b), 0, ypos, xspeed)
#ZAPISANE DANE
rm = r
gm = g
bm = b
y2 = ypos
m = xspeed

#DZIECKO
ypos = (y1+y2)/2
xspeed = (t+m)/2
r = (rt+rm)/2
g = (gt+gm)/2
b = (bt+bm)/2
dziecko = Czlowiek(color(r, g, b), 0, ypos, xspeed)

def setup():
    size(800,400)

def draw(): 
    background(150)
    tata.bieg()
    tata.display()
    mama.bieg()
    mama.display()
    dziecko.bieg()
    dziecko.display()
    
# ciekawe ćwiczenie, ale nie ma tu dziedziczenia, 0,75 pkt
