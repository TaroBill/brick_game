from controller.controller import IController
from pynput import keyboard

class KeyboardController(IController):
    def __init__(self):
        self.dir = None
        self.isSpaceClicked = False
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
            
    def on_press(self, key):
        if key == keyboard.Key.space:
            self.isSpaceClicked = True
            return 
        if not hasattr(key, 'char'):
            return
    
    def start_button(self) -> bool:
        if self.isSpaceClicked:
            self.isSpaceClicked = False
            return True
        return False