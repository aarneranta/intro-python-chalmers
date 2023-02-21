from graphics import *

class Racer:
    def __init__(self,title,width,height,size,color,animationSpeed):
        self.win = GraphWin(title,width,height)
        self.win.setCoords(-width/2,-height/2,width/2,height/2)
        self.racer = Circle(Point(0,0), size)
        self.racer.setFill(color)
        self.racer.draw(self.win)
        self.animationSpeed = animationSpeed

    def play(self):
        xvelocity = 0
        yvelocity = 0
        while True:
            try:
                key = self.win.checkKey()
            except GraphicsError:
                break

            if key == "Up":
                yvelocity = yvelocity + 1
            elif key == "Down":
                yvelocity = yvelocity - 1
            elif key == "Left":
                xvelocity = xvelocity - 1
            elif key == "Right":
                xvelocity = xvelocity + 1
            elif key == "BackSpace":
                xvelocity = 0
                yvelocity = 0
                self.racer.move(-self.racer.getCenter().getX(),-self.racer.getCenter().getY())
            elif key == "space":
                xvelocity = 0.9 * xvelocity
                yvelocity = 0.9 * yvelocity
                
            self.racer.move(xvelocity,yvelocity)
            update(self.animationSpeed)

racer = Racer("racer", 1000, 680, 40, 'orange', 100)
racer.play()
