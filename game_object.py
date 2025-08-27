class GameObject():
    def __init__(self, type: str, pos=(0, 0), angle=0.0):
        self.type = type
        self.x, self.y = pos
        self.angle = angle

    @property
    def pos(self):
        return (self.x, self.y)