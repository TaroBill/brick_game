from abc import ABC, abstractmethod

class IController(ABC):
    @abstractmethod
    def start_button(self) -> bool:
        pass
    
    @abstractmethod
    def get_dir(self) -> int:
        pass