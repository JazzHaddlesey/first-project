
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, leg_num, fur_colour):
       self.leg_num = leg_num
       self.fur_colour = fur_colour
       
    def __repr__(self) -> str:
        return f"{self.leg_num} {self.fur_colour}"
    
    @abstractmethod
    def speak(self):
        pass
    
class Cat(Animal):
    def __init__(self, leg_num, fur_colour, love_of_fish):
        super().__init__(leg_num, fur_colour)
        self.love_of_fish = love_of_fish
        
class Dog(Animal):
    def __init__(self, leg_num, fur_colour,):
        super().__init__(leg_num, fur_colour)
    
                         

       