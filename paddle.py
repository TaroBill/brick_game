class Paddle:
    def __init__(self, x: int, y: int) -> None:
        self.locX = x
        self.locY = y
        self.length = 4
        self.color = (0, 255, 0)

    def move(self, x):
        self.locX = x
        
    def is_in_paddle(self, x, y):
        if y >= self.locY:
            return False
        if x >= self.locX and x < self.locX + self.length:
            return True
        return False