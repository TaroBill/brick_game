from enum import Enum
from display.display import IDisplay
from controller.controller import IController
from time import sleep
from brick import Brick
from paddle import Paddle
from ball import Ball

class GameState(Enum):
    Waiting = 0
    Start = 1
    GameOver = 2
    
class BrickGame():
    def __init__(self, controller: IController, display: IDisplay) -> None:
        self.mapWidth = display.width
        self.mapHeight = display.height
        self.refreshTime = 0.05 # 20fps
        self.controller = controller
        self.display = display
        self.map = [[(0,0,0)]*self.mapWidth for _ in range(8)]
        self.displayText = ""
        # self.spawn_brick()
        # self.paddle = Paddle(3, 7)
        self.ball = Ball(3, 6, (2.1, -6.7))
        self.game_loop()

    def start_scene(self):
        self.draw_ball()
        self.displayText = f"Ball location: ({self.ball.locX:.2f}, {self.ball.locY:.2f})\nBall speed: {self.ball.speedVector}"
        self.ball.move()
        # if self.paddle.is_in_paddle(self.ball.locX, self.ball.locY):
        #     self.ball.bounce((0, -1))
        if self.is_in_left_wall(self.ball.locX):
            self.ball.bounce((1, 0))
        if self.is_in_right_wall(self.ball.locX):
            self.ball.bounce((-1, 0))
        if self.is_in_top_wall(self.ball.locY):
            self.ball.bounce((0, 1))
        if self.is_in_bottom_wall(self.ball.locY):
            self.ball.bounce((0, -1))
    
    
    def game_loop(self):
        while True:
            self.clear_map()
            self.start_scene()
            self.display.draw(self.map, self.displayText) 
            sleep(self.refreshTime)
            
    def clear_map(self):
        for y in range(self.mapHeight):
            for x in range(self.mapWidth):
                self.map[y][x] = (0,0,0)
                
    def spawn_brick(self):
        self.bricks = list()
        for x in range(self.mapWidth):
            self.bricks.append(Brick(x, 0))
            
    def draw_brick(self):
        for brick in self.bricks:
            self.map[brick.locY][brick.locX] = brick.get_color()
    
    def draw_paddle(self):
        for x in range(self.paddle.locX, self.paddle.locX + self.paddle.length):
            self.map[self.paddle.locY][x] = self.paddle.color
    
    def draw_ball(self):
        self.map[int(self.ball.locY)][int(self.ball.locX)] = self.ball.color
        
    def is_in_left_wall(self, x):
        return x <= 0
    
    def is_in_right_wall(self, x):
        return x >= self.mapWidth - 1
    
    def is_in_top_wall(self, y):
        return y <= 0
    
    def is_in_bottom_wall(self, y):
        return y >= self.mapHeight - 1
    
from controller.keyboard_controller import KeyboardController
from display.cli_display import CliDisplay
controller = KeyboardController()
display = CliDisplay(8, 8)
BrickGame(controller, display)