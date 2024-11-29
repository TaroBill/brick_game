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
    GameOverLoss = 2
    GameOverWin = 3
    
class BrickGame():
    def __init__(self, controller: IController, display: IDisplay) -> None:
        self.mapWidth = display.width
        self.mapHeight = display.height
        self.refreshTime = 0.05 # 20fps
        self.controller = controller
        self.display = display
        self.displayText = ""
        self.map = [[(0,0,0)]*self.mapWidth for _ in range(8)]
        self.wait()
        self.game_loop()
    
    def wait(self):
        self.state = GameState.Waiting
        self.displayText = "Press 「Space」 to start"
        
    def waiting_scene(self):
        if self.controller.start_button():
            self.start()

    def start(self):
        self.state = GameState.Start
        self.displayText = ""
        self.spawn_brick()
        self.paddle = Paddle(0, 6.2)
        self.ball = Ball(3, 5, (0, -1))
        self.ball.rotate(45)

    def start_scene(self):
        control = self.controller.get_dir()
        if control is not None:
            moveTarget = self.paddle.locX + control
            if moveTarget >= 0 and (moveTarget + self.paddle.length) <= self.mapWidth:
                self.paddle.move(moveTarget)
        self.draw_ball()
        self.draw_paddle()
        self.draw_brick()
        self.displayText = f"Ball location: ({self.ball.locX:.2f}, {self.ball.locY:.2f})\nBall vector: {self.ball.vector}"
        self.ball.move()
        
        for brick in self.bricks:
            if brick.is_hit_brick(self.ball.locX, self.ball.locY):
                brick.hit()
                self.ball.bounce((0, 1))
                if brick.health == 0:
                    self.bricks.remove(brick)
                    if len(self.bricks) == 0:
                        self.game_over("Win")
                        return
        if self.paddle.is_in_paddle(self.ball.locX, self.ball.locY):
            self.ball.bounce((0, -1))
        elif self.is_in_left_wall(self.ball.locX):
            self.ball.bounce((1, 0))
        elif self.is_in_right_wall(self.ball.locX):
            self.ball.bounce((-1, 0))
        elif self.is_in_top_wall(self.ball.locY):
            self.ball.bounce((0, 1))
        if self.is_in_bottom_wall(self.ball.locY):
            self.game_over("Lose")
            return
        
    def game_over(self, state="Lose"):
        self.state = GameState.GameOverLoss if state == "Lose" else GameState.GameOverWin
        self.displayText = f"Game Over! You {state}!"
        self.game_over_timer = 50  
    
    def lose_scene(self):
        self.game_over_timer -= 1
        for y in range(self.mapHeight):
            for x in range(self.mapWidth):
                self.map[y][x] = (255, 0, 0)
        if self.game_over_timer <= 0:
            self.wait()
            
    def win_scene(self):
        self.game_over_timer -= 1
        for y in range(self.mapHeight):
            for x in range(self.mapWidth):
                self.map[y][x] = (0, 255, 0)
        if self.game_over_timer <= 0:
            self.wait()

    
    def game_loop(self):
        while True:
            self.clear_map()
            if self.state == GameState.Waiting:
                self.waiting_scene()
            elif self.state == GameState.Start:
                self.start_scene()
            elif self.state == GameState.GameOverLoss:
                self.lose_scene()
            elif self.state == GameState.GameOverWin:
                self.win_scene()
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
            self.map[int(self.paddle.locY)+1][x] = self.paddle.color
    
    def draw_ball(self):
        self.map[int(self.ball.locY)][int(self.ball.locX)] = self.ball.color
        
    def is_in_left_wall(self, x):
        return x <= 0
    
    def is_in_right_wall(self, x):
        return x+1 >= self.mapWidth
    
    def is_in_top_wall(self, y):
        return y <= 0
    
    def is_in_bottom_wall(self, y):
        return y+1 >= self.mapHeight
    
from controller.keyboard_controller import KeyboardController
from display.cli_display import CliDisplay
controller = KeyboardController()
display = CliDisplay(8, 8)
BrickGame(controller, display)