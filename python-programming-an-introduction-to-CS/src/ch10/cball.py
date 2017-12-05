from math import radians
from math import cos
from math import sin

def main():
    # Input
    angle = eval(input("Enter the launch angle (in degrees): "))
    vel = eval(input("Enter the initial velocity (in meters): "))
    h0 = eval(input("Enter the initial height (in meters): "))
    time = eval(input("Enter the time interval between position calculations: "))

    # Processing
    pos_x = 0.0
    pos_y = h0

    theta = radians(angle)
    vel_x = vel * cos(theta)
    vel_y = vel * sin(theta)


    while  pos_y > 0:
        pos_x = pos_x + vel_x * time
        vel_y_change = vel_y - 9.8 * time

        pos_y = pos_y + vel_y * time - 0.5 * 9.8 * time ** 2
        vel_y = vel_y_change

    # Output
    print("Distance traveled: {0:0.2f} meters".format(pos_x))

if __name__ == '__main__':
    main()
