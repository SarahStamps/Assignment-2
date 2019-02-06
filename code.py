import numpy as np
import math as m
import matplotlib.pyplot as plt
"""
Make sure you make this module as modular as you can.
That is add as many functions as you can.
1) Have a main function
2) A function to capture user input, this could be inside your "main" function
3) A function to calculate the projectile motion
4) A function to display the graph

Make sure you use docstring to document your module and all
your functions.

Make sure your python module works in dual-mode: by itself or import to other module
"""
# NOTE: You may need to run: $ pip install matplotlib
GRAVITY = -9.8
# Function to calculate projectile motion
def main():
       x0 = float(input("initial x position: "))
       vx0 = float(input("initial x velocity: "))        # TODO: capture input

       y0 = float(input("initial y position: "))
       vy0 = float(input("initial y velocity: "))          # TODO: capture input

       ax = 0.0
       ay = GRAVITY           # define a constant

       delt = 0.1
       t = 0.0
       intervals = 170
       x = []
       y = []
       for i in range(intervals):
              x.append(projectile_motion(x0,vx0,t,ax))
              y.append(projectile_motion(y0,vy0,t,ay))
              t = t + delt

              if y[i] < 0.0:            # exits when y value is less than 0
                     break
       print("number of points", i)
       plot_data(x, y)
      


def projectile_motion(position,velocity,initial_time,acceleration):
       """
       calculate x and y using projectile motion
       param position: position
       param velocity: velocity
       param initial_time: initial time
       param acceleration: acceleration
       """
       return position + velocity*initial_time + 0.5*acceleration*initial_time**2    # formula for position

# Function to plot data
def plot_data(x, y):
       """
       function plots x and y pairs
       param x: x coordinate
       param y: y coordinate
       """
       plt.plot(x, y)
       plt.xlabel('time')
       plt.ylabel('distance')
       plt.show()


 # set module for dual mode
if __name__ == "__main__":
        main()