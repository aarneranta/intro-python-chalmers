# exam questions on OOP

class BookContents:
    def __init__(self):
        self.conts = {}

    def addChapter(self, title, page):
        self.conts[title] = page

    def printContents(self):
        for (t, p) in sorted(list(self.conts.items()), key = lambda c: c[1]):
            print(t, p)

    def pageToChapter(self, page):
        chapters = sorted(list(self.conts.items()), key = lambda c: c[1])
        title = None
        for (t, p) in chapters:
            if page >= p:
                title = t
            else:
                break
        return title

if __name__ == '__mainz__':
    contents = BookContents()
    contents.addChapter("Computers and Programs", 1)
    contents.addChapter("Objects and Graphics", 123)
    contents.addChapter("Writing Simple Programs", 25)
    contents.addChapter("Computing with Strings", 77)
    contents.addChapter("Computing with Numbers", 51)
    contents.printContents()
    
    print(contents.pageToChapter(0) == None)
    print(contents.pageToChapter(30) == "Writing Simple Programs")
    print(contents.pageToChapter(60) == "Computing with Numbers")
    print(contents.pageToChapter(150) == "Objects and Graphics")


class Account:
    def __init__(self, id, amount):
        self.id = id
        self.balance = amount

    def get_balance(self):
        return self.balance

    def set_balance(self, amount):
        self.balance = amount

def transfer(a, b, amount):
    if a.get_balance() >= amount:
        a.set_balance(a.get_balance() - amount)
        b.set_balance(b.get_balance() + amount)
        print('OK')
    else:
        print('not enough money')
    
        
        

if __name__ == '__mainz__':
    acc1 = Account('0010', 2000)
    acc2 = Account('0201', 2000)
    transfer(acc1,acc2,600)
    print(acc1.get_balance() == 1400)
    print(acc2.get_balance() == 2600)
    transfer(acc1,acc2,1600)
# not enough money
    print((acc1.get_balance(), acc2.get_balance()) == (1400, 2600))

    
from graphics import *
    
class Chessboard:
    def __init__(self, black, white, size):
        self.size = size
        self.squares = []
        for y in range(8):
            for x in range(8):
                r = Rectangle(Point(y*size, x*size),
                                  Point((y+1)*size, (x+1)*size))
                if (x+y) % 2 == 0:
                    r.setFill(white)
                else:
                    r.setFill(black)
                self.squares.append(r)
                
    def draw(self):
        win = GraphWin('Schackbrädet', 8*self.size, 8*self.size)
        for r in self.squares:
            r.draw(win)
        win.getKey()

if __name__ == '__main__':
#    Chessboard('brown','yellow',100).draw()
    Chessboard('green','red',10).draw()
    
