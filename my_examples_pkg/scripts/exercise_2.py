#! /usr/bin/env python3

import rospy #import  library python untuk ros
from nav_msgs.msg import Odometry ##import message Odometry dari nav_msgs

def callback(msg): #mendefinisikan fungsi dengan nama callback dan menerima parameter msg
    print(msg)  #cetak nilai dari msg

rospy.init_node('exercise_2') #inisialisasi node dengan nama exercise_2
sub = rospy.Subscriber('/odom', Odometry, callback)  #membuat objek subscriber yang akan mensubscribe topic /odom dan akan memanggil fungsi callback setiap membaca sesuatu dari topic
rospy.spin() # looping selama program dieksekusi

