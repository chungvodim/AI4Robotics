# -----------------
# USER INSTRUCTIONS
#
# Write a function in the class robot called move()
#
# that takes self and a motion vector (this
# motion vector contains a steering* angle and a
# distance) as input and returns an instance of the class
# robot with the appropriate x, y, and orientation
# for the given motion.
#
# *steering is defined in the video
# which accompanies this problem.
#
# For now, please do NOT add noise to your move function.
#
# Please do not modify anything except where indicated
# below.
#
# There are test cases which you are free to use at the
# bottom. If you uncomment them for testing, make sure you
# re-comment them before you submit.

from math import *
import random

# --------
#
# the "world" has 4 landmarks.
# the robot's initial coordinates are somewhere in the square
# represented by the landmarks.
#
# NOTE: Landmark coordinates are given in (y, x) form and NOT
# in the traditional (x, y) format!

landmarks = [[0.0, 100.0], [0.0, 0.0], [100.0, 0.0], [100.0, 100.0]]  # position of 4 landmarks
world_size = 100.0  # world is NOT cyclic. Robot is allowed to travel "out of bounds"
max_steering_angle = pi / 4  # You don't need to use this value, but it is good to keep in mind the limitations of a real car.


# ------------------------------------------------
#
# this is the robot class
#

class robot:
    # --------

    # init:
    #	creates robot and initializes location/orientation
    #

    def __init__(self, length=10.0):
        self.x = random.random() * world_size  # initial x position
        self.y = random.random() * world_size  # initial y position
        self.orientation = random.random() * 2.0 * pi  # initial orientation
        self.length = length  # length of robot
        self.bearing_noise = 0.0  # initialize bearing noise to zero
        self.steering_noise = 0.0  # initialize steering noise to zero
        self.distance_noise = 0.0  # initialize distance noise to zero

    def __repr__(self):
        return '[x=%.6s y=%.6s orient=%.6s]' % (str(self.x), str(self.y), str(self.orientation))

    # --------
    # set:
    #	sets a robot coordinate
    #

    def set(self, new_x, new_y, new_orientation):
        if new_orientation < 0 or new_orientation >= 2 * pi:
            raise ValueError, 'Orientation must be in [0..2pi]'
        self.x = float(new_x)
        self.y = float(new_y)
        self.orientation = float(new_orientation)

    # --------
    # set_noise:
    #	sets the noise parameters
    #

    def set_noise(self, new_b_noise, new_s_noise, new_d_noise):
        # makes it possible to change the noise parameters
        # this is often useful in particle filters
        self.bearing_noise = float(new_b_noise)
        self.steering_noise = float(new_s_noise)
        self.distance_noise = float(new_d_noise)

    # --------
    # sense:
    #   obtains bearings from positions
    #   landmark(y,x)

    def sense(self, add_noise = 1):  # do not change the name of this function
        # HINT: You will probably need to use the function atan2()
        Z = []
        for i in range(len(landmarks)):
            # dist = sqrt((self.x - landmarks[i][0]) ** 2 + (self.y - landmarks[i][1]) ** 2)
            # dist += random.gauss(0.0, self.sense_noise)
            x = (landmarks[i][1] - self.x)
            y = (landmarks[i][0] - self.y)
            bearing = atan2(y,x) - self.orientation
            if add_noise:
                bearing += random.gauss(0.0, self.bearing_noise)
            bearing %= 2 * pi
            Z.append(bearing)
        return Z # Leave this line here. Return vector Z of 4 bearings.

    # --------
    # move:
    # Move along a section of a circular path according to motion
    # World is NOT cyclic. Robot is allowed to travel "out of bounds"
    def move(self, motion, tolerance = 0.001):
        dist = float(motion[1])
        steering = float(motion[0]) #anpha
        # validation
        if steering > max_steering_angle:
            raise ValueError, 'Exceeding max steering angle'
        if dist < 0.0:
            raise ValueError, 'Robot cant move backwards'
        # make a clone
        result = robot()
        result.length = self.length
        result.bearing_noise = self.bearing_noise
        result.distance_noise = self.distance_noise
        result.steering_noise = self.steering_noise
        # random.gauss(mu, sigma)
        steering2 = random.gauss(steering, self.steering_noise)
        dist2 = random.gauss(dist, self.distance_noise)

        # excute motion
        # orientation = theta
        # turn = beta
        turn = (dist2 / result.length) * tan(steering2)
        if abs(turn) < tolerance:
            # straight motion
            result.x = self.x + (dist2 * cos(self.orientation))
            result.y = self.y + (dist2 * sin(self.orientation))
            result.orientation = (self.orientation + turn) % (2.0 * pi)
        else:
            # cyclic motion
            orientation = self.orientation
            # r = d/beta = l / tan(steering)
            r = dist2 / turn
            cx = self.x - sin(orientation) * r
            cy = self.y + cos(orientation) * r

            x = cx + sin(orientation + turn) * r
            y = cy - cos(orientation + turn) * r

            orientation = (orientation + turn) % (2.0 * pi)
            result.set(x, y, orientation)
        return result



