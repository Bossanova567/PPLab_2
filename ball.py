from math import cos, sin


class Ball:
    def __init__(self, x: int, y: int, radius: int, velocity: int, direction: int):
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = velocity
        self.direction = direction
        self.delta_x = velocity * cos(direction)
        self.delta_y = -velocity * sin(direction)

    def move(self) -> None:
        self.x += self.delta_x
        self.y += self.delta_y

    def reflect_horizontal(self) -> None:
        self.delta_x = -self.delta_x

    def reflect_vertical(self) -> None:
        self.delta_y = -self.delta_y

    def __str__(self) -> str:
        return f"Ball at ({self.x}, {self.y}) of velocity ({self.delta_x}, {self.delta_y})"


class Container:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.width = width
        self.height = height
        self.x2 = self.x1 + self.width - 1
        self.y2 = self.y1 + self.height - 1

    def collides(self, ball: Ball) -> bool:
        if ball.x + ball.radius + ball.delta_x > self.x2 or ball.x - ball.radius + ball.delta_x < self.x1:
            ball.reflect_horizontal()
            return True
        elif ball.y + ball.radius + ball.delta_y < self.y2 or ball.y - ball.radius + ball.delta_y > self.y1:
            ball.reflect_vertical()
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"Container[({self.x1},{self.y1}),({self.x2}, {self.y2})]"


ball = Ball(50, 50, 5, 10, 30)
box = Container(0, 0, 100, 100)
print(box)
for step in range(0, 100):
    ball.move()
    box.collides(ball)
    print(ball)  # check the position of the ball
