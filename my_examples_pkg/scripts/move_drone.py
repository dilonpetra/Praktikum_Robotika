#! /usr/bin/env python3

from actionlib import action_server
import rospy
import time
import actionlib
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

PENDING = 0
ACTIVE = 1
DONE = 2
WARN = 3
ERROR = 4

nImage = 1

def feedback_callback(feedback):
    global nImage
    print('[Feedback] image n.%d received'%nImage)
    nImage += 1

rospy.init_node('drone_action_client') # initializes the action client node
action_server_name = '/ardrone_action_server'
client = actionlib.SimpleActionClient(action_server_name, ArdroneAction) # create the connection to the action server
move = rospy.Publisher('/cmd_vel', Twist, queue_size=1) # membuat publisher topic 
move_msg = Twist()
takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
takeoff_msg = Empty()
land = rospy.Publisher('/drone/land', Empty, queue_size=1)
land_msg = Empty()

rospy.loginfo('Waiting for action Server '+action_server_name) 
client.wait_for_server() # waits until the action server is up and running
rospy.loginfo('Action server found.....'+action_server_name)




goal = ArdroneGoal() # creates a goal to send to the action server
goal.nseconds = 10 # indicates, take pictures along 10 seconds

client.send_goal(goal, feedback_cb=feedback_callback)
state_result = client.get_state()

rate = rospy.Rate(1)

rospy.loginfo("state_result: "+str(state_result))


i=0
#takeoff
while not i ==3:
    takeoff.publish(takeoff_msg)
    rospy.loginfo('taking off........')
    time.sleep(1)
    i +=1

#move when state drone not Done yet
while state_result < DONE:
    move_msg.linear.x = 1
    move_msg.angular.z = 1
    move.publish(move_msg)
    rate.sleep()
    state_result = client.get_state()
    rospy.loginfo('Moving around...')
    rospy.loginfo("state_result: "+str(state_result))

rospy.loginfo("[Result] State: "+str(state_result))
if state_result == ERROR:
    rospy.logerr("Something went wrong in the Server Side")
if state_result == WARN:
    rospy.logwarn("There is a warning in the Server Side")

# land the drone when action is finished

i = 0
while not i ==3:
    move_msg.linear.x=0
    move_msg.angular.z = 0
    move.publish(move_msg)
    land.publish(land_msg)
    rospy.loginfo('Landing ......')
    time.sleep(1)
    i += 1
