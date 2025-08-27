import math
from game_object import GameObject

class Camera(GameObject):
    def __init__(self, type: str, pos=(0, 0), angle=0.0):
        super().__init__(type, pos, angle)
    
    def distance_to_object(self, object_pos=(int, int)):
        return math.sqrt((self.x-object_pos[0])**2+(self.y-object_pos[1])**2)