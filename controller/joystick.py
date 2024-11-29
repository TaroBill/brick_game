from sense_emu import SenseHat
import time
from controller.controller import IController

class JoystickController(IController):
    def __init__(self, sense: SenseHat) -> None:
        self.sense = sense
        self.dir = None

    def start_button(self) -> bool:
        for event in self.sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "middle":
                    return True
        return False

    def get_dir(self) -> int:
        for event in self.sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "left":
                    return -1
                if event.direction == "right":
                    return 1