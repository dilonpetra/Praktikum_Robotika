#! /usr/bin/env python3

import rospkg
rospack = rospkg.RosPack()
# This rospack.get_path() works in the same way as $(find name_of_package) in the launch files.<br>
traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"
print(traj)