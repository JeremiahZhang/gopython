# cball4.py

from projectile import Projectile

def get_inputs():
    a = eval(input("Enter the launch angle (in degrees): "))
    v = eval(input("Enter the initial velocity (in m/s): "))
    h = eval(input("Enter the initial height (in meters): "))
    t = eval(input("Enter the time interval between position calculations: "))

    return a, v, h, t

def main():
    angle, vel, h0, time = get_inputs()
    cball = Projectile(angle, vel, h0)

    while cball.get_y() >= 0:
        cball.update(time)

    print("\n Distance: {0:0.2f} meters.".format(cball.get_x()))

if __name__ == '__main__':
    main()
