class Game:
    name = "Simple RPG"
    tick_rate = 120

    class Window:
        size = (500, 500)
        center = (size[0] / 2, size[1] / 2)
        minX = -size[0] / 2
        maxX = size[0] / 2
        minY = -size[1] / 2
        maxY = size[1] / 2
