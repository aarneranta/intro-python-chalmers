class Point:
    
# constructor

    def __init__(self, x, y):
        self.x = x  # instance variables
        self.y = y

# method

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

# getters
        
    def getX(self):
        return self.x

    
    def getY(self):
        return self.y


# setters

    def setX(self, x):
        self.x = x

        
    def setY(self, y):
        self.y = y

    
