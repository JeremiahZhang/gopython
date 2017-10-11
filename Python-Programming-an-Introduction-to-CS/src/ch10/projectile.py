# cball2.py

"""cball2.py
Provides a simple class for modeling the
flight of projectiles.
"""

from math import radians
from math import sin
from math import cos

class Projectile:

    """Simulates the flight of simple projectiles near the earth's
    surface, ignoring wind resistance. Tracking is done in two
    dimensions, height (y) and distance (x).

    Attributes:
        angle: A number representing lanuch angle.
        velocity: A number representing initial velocity.
        height: A number representing initial height.
    """

    def __init__(self, angle, velocity, height):
        """Create a projectile with given lanuch angle, initial
        velocity and height.
        """
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def get_x(self):
        """Returns the x position (distance) of this projectile.
        """
        return self.xpos

    def get_y(self):
        """Returns the y position (height) of this projectile.
        """
        return self.ypos

    def update(self, time):
        """Update the state of this projectile to move it time seconds
        farther into its flight.
        """
        self.xpos = self.xpos + time * self.xvel
        yvel_after = self.yvel - 9.8 * time
        self.ypos = self.ypos + self.yvel * time - 0.5 * 9.8 * time ** 2
        self.vyel = yvel_after

def get_input():
    a = eval(input("Enter the launch angle (in degrees): "))
    v = eval(input("Enter the initial velocity (in m/s): "))
    h = eval(input("Enter the initial height (in meters): "))
    t = eval(input("Enter the time interval between position calculations: "))

    return a, v, h, t

def main():
    angle, vel, h0, time = get_input()
    cball = Projectile(angle, vel, h0)

    while cball.get_y() > 0:
        cball.update(time)

    print()
    print("Distance traveled: {0:0.2f} meters.".format(cball.xpos))
    print("The y position: {} meters.".format(cball.ypos))

if __name__ == '__main__':
    main()
