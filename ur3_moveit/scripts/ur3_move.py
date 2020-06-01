#!/usr/bin/env python

# Author: Hyeonjun Park, Ph.D. candidate
# Affiliation: Human-Robot Interaction LAB, Kyung Hee University, South Korea
# koreaphj91@gmail.com
# init: 9 Apr 2019
# revision: 17 Feb 2020


import sys
import rospy
import tf
import moveit_commander  # https://answers.ros.org/question/285216/importerror-no-module-named-moveit_commander/
import random
import math
from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import *
#from pilz_robot_programming import *

pose_goal = Pose()
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('ur3_move',anonymous=True)
group = [moveit_commander.MoveGroupCommander("manipulator")]  # ur3 moveit group name: manipulator

xx = 1
x = [0,0,0]

while not rospy.is_shutdown():  
  quater = quaternion_from_euler(x[0], x[1], x[2])
  x[1] = x[1]+0.3
  
  if(xx%2 == 1):        
    pose_goal.orientation.w = 0.0
    pose_goal.position.x = 0.4 # red line      0.2   0.2
    pose_goal.position.y = 0.15  # green line  0.15   0.15
    pose_goal.position.z = 0.2  # blue line   # 0.35   0.6
    pose_goal.orientation.x = quater[0]
    pose_goal.orientation.y = quater[1]
    pose_goal.orientation.z = quater[2]
    pose_goal.orientation.w = quater[3]
    group[0].set_pose_target(pose_goal)
    group[0].go(True)
    
    #print(xx)
    rospy.sleep(2)
      
  else:
    pose_goal.orientation.w = 0.0
    pose_goal.position.x = 0.2 # red line      0.2   0.2
    pose_goal.position.y = 0.15  # green line  0.15   0.15
    pose_goal.position.z = 0.3  # blue line   # 0.35   0.6
    pose_goal.orientation.x = quater[0]
    pose_goal.orientation.y = quater[1]
    pose_goal.orientation.z = quater[2]
    pose_goal.orientation.w = quater[3]
    group[0].set_pose_target(pose_goal)
    group[0].go(True)
      
    #print(xx)
    rospy.sleep(2) 

  xx = xx + 1 

  
'''
pose_goal.orientation.w = 0.0
pose_goal.position.x = 0.4 # red line      0.2   0.2
pose_goal.position.y = 0.15  # green line  0.15   0.15
pose_goal.position.z = 0.5  # blue line   # 0.35   0.6
group[0].set_pose_target(pose_goal)
group[0].go(True)
'''
moveit_commander.roscpp_shutdown()
