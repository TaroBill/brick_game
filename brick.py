
class Brick:
    def __init__(self, x: int, y: int) -> None:
        self.locX = x
        self.locY = y
        self.health = 2
        self.healthColor = [(0, 0, 0), (255, 0, 255), (255, 255, 0)]
        
    def hit(self):
        self.health -= 1
        
    def get_color(self):
        return self.healthColor[self.health]
    
    def is_hit_brick(self, x, y):
        if y < self.locY or y > self.locY + 1:
            return False
        if x < self.locX or x > self.locX + 1:
            return False
        return True