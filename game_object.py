class GameObject:
    def __init__(self, type_: str, pos: tuple[int, int]):
        self.type = type_
        self.x, self.y = float(pos[0]), float(pos[1])

    @property
    def pos(self) -> tuple[float, float]:
        return (self.x, self.y)