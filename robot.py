from motor import Motor
from sensor import Sensor


class Robot:
    def __init__(self, name):
        self.name = name
        self.motor = Motor()
        self.sensor = Sensor()

    def move(self):

        distance = self.sensor.read_distance()

        if distance < 20:
            self.motor.stop()
            print("Obstacle detected")
        else:
            self.motor.move(50)

if __name__ == "__main__":

    robot = Robot("TestRobot")
    robot.move()
    print(robot.name)
    
