#! /usr/bin/env python3

import rospy #import library python untuk ros
from std_msgs.msg import Int32 #import message Int32 dari package std_msgs

def callback(msg): #mendefinisikan fungsi dengan nama callback dan menerima parameter msg
    print(msg.data) #cetak nilai dari data yang berada di dalam parameter msg

rospy.init_node('topic_subscriber') #inisialisasi node dengan nama topic_subscriber
sub = rospy.Subscriber('/counter', Int32, callback) # membuat objek subscriber yang akan mensubscribe topic /counter dan akan memanggil fungsi callback setiap membaca sesuatu dari topic
rospy.spin() # looping selama program dieksekusi



