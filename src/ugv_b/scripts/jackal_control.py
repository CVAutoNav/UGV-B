#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

if __name__ =="__main1__":
  rospy.init_node('topic_pu7blisher')
  pub = rospy.Publisher('/jackal_velocity_controller/cmd_vel', Twist, queue_size=1)
  rate = rospy.Rate(2)
  move = Twist() # defining the way we can allocate the values
  move.linear.x = 0.5 # allocating the values in x direction - linear
  move.angular.z = 0.5  # allocating the values in z direction - angular

  while not rospy.is_shutdown():
    pub.publish(move)
    rate.sleep()

if __name__ =="__main__":
  rospy.init_node('topic_pu7blisher')
  pub = rospy.Publisher('/jackal_velocity_controller/cmd_vel', Twist, queue_size=1)
  rate = rospy.Rate(2)
  move = Twist()  # defining the way we can allocate the values
  while not rospy.is_shutdown():
    movement_input = raw_input("Enter the movement coordinates in the following format: x y z roll pitch yaw : \n").split()
    movement_input = [float(i) for i in movement_input]
    print(movement_input)
    move.linear.x = movement_input[0]
    move.linear.y = movement_input[1]
    move.linear.z = movement_input[2]
    move.angular.x = movement_input[3]
    move.angular.y = movement_input[4]
    move.angular.z = movement_input[5]
    pub.publish(move)
    rate.sleep()
