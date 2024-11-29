class Paddle:
    def __init__(self, x: float, y: float) -> None:
        self.locX = x
        self.locY = y
        self.length = 8
        self.color = (0, 255, 0)

    def move(self, x):
        self.locX = x
        
    def is_in_paddle(self, x, y):
        if y <= self.locY:
            return False
        if x < self.locX or x >= self.locX + self.length:
            return False
        return True