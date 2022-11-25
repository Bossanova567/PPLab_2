import unittest
from ball import Ball, Container


class TestBall(unittest.TestCase):
    def test_move(self):
        ball = Ball(50, 50, 5, 10, 30)
        box = Container(0, 0, 100, 100)
        for step in range(0, 100):
            ball.move()
            box.collides(ball)
            self.assertGreaterEqual(ball.x - ball.radius, box.x1)
            self.assertGreaterEqual(ball.y - ball.radius, box.y1)
            self.assertLessEqual(ball.x + ball.radius, box.x2)
            self.assertLessEqual(ball.y + ball.radius, box.y2)
