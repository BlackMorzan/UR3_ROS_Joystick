#!/usr/bin/env python

# Author: Hyeonjun Park, Ph.D. candidate
# Affiliation: Human-Robot Interaction LAB, Kyung Hee University, South Korea
# koreaphj91@gmail.com
# init: 9 Apr 2019
# revision: 19 Mar 2020

import sys
import rospy
import copy, math
from math import pi

from moveit_commander import RobotCommander, MoveGroupCommander
from moveit_commander import PlanningSceneInterface, roscpp_initialize, roscpp_shutdown
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion
from moveit_msgs.msg import Grasp, GripperTranslation, PlaceLocation, MoveItErrorCodes
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import random

GROUP_NAME_ARM = "manipulator"
FIXED_FRAME = 'world'
#GROUP_NAME_GRIPPER = "NAME OF GRIPPER"
pose_goal = Pose()
Orientation = [0,0,0]

class TestMove():

    def __init__(self):
        roscpp_initialize(sys.argv)        
        rospy.init_node('ur3_move',anonymous=True)

        self.scene = PlanningSceneInterface()
        self.robot_cmd = RobotCommander()

        self.robot_arm = MoveGroupCommander(GROUP_NAME_ARM)
        #robot_gripper = MoveGroupCommander(GROUP_NAME_GRIPPER)
        self.robot_arm.set_goal_orientation_tolerance(0.005)
        
        
        self.robot_arm.set_planning_time(5)
        #self.robot_arm.set_num_planning_attempts(5)

        self.robot_arm.remember_joint_values("zeros", None)

        rospy.sleep(2)
        # Allow replanning to increase the odds of a solution
        self.robot_arm.allow_replanning(True)  
        
        

	#add Tabl
	
        p = PoseStamped()
        p.header.frame_id = FIXED_FRAME
        p.pose.position.x = 0.3
        p.pose.position.y = 0.2
        p.pose.position.z = 0.1
        self.scene.add_box("table", p, (0.02, 0.02, 0.02)) 
        
        
        pose_goal.position.x = 0.3
        pose_goal.position.y = 0.2
        pose_goal.position.z = 0.15
        
        #Orientation = [1.57,0,0]
        Orientation[0] = 0
        Orientation[1] = 0
        Orientation[2] = 1.57

    def WASD(self):
        
        quater = quaternion_from_euler(Orientation[0], Orientation[1], Orientation[2])
        rospy.sleep(2)
        pose_goal.orientation.x = quater[0]
        pose_goal.orientation.y = quater[1]
        pose_goal.orientation.z = quater[2]
        pose_goal.orientation.w = quater[3]
        
        rospy.sleep(2)
        self.robot_arm.set_pose_target(pose_goal)
        self.robot_arm.go(True) 
        print("trying done")
        
        print("\n")
        print("WASD keyboard control")
        while(True):
            print("Available commands : ")
            print(" W - move X forward")
            print(" S - move X backward")
            print(" A - move Y left")
            print(" D - move Y right")
            print(" R - move Z left")
            print(" F - move Z right")
            print("*****************")
            print(" X - pick object")
            print(" Y - pick object")
            print("current orient",  Orientation)

            command = raw_input("Control : ")
            if command == 'w':		
                pose_goal.orientation.w = 0.0
                pose_goal.position.x = pose_goal.position.x + 0.05
                pose_goal.position.y = pose_goal.position.y
                pose_goal.position.z = pose_goal.position.z
                pose_goal.orientation.x = quater[0]
                pose_goal.orientation.y = quater[1]
                pose_goal.orientation.z = quater[2]
                pose_goal.orientation.w = quater[3]
                self.robot_arm.set_pose_target(pose_goal)
                self.robot_arm.go(True)  
            elif command == 's':
                pose_goal.orientation.w = 0.0
                pose_goal.position.x = pose_goal.position.x - 0.05
                pose_goal.position.y = pose_goal.position.y
                pose_goal.position.z = pose_goal.position.z
                pose_goal.orientation.x = quater[0]
                pose_goal.orientation.y = quater[1]
                pose_goal.orientation.z = quater[2]
                pose_goal.orientation.w = quater[3]
                self.robot_arm.set_pose_target(pose_goal)
                self.robot_arm.go(True)  
            elif command == 'a':
                pose_goal.orientation.w = 0.0
                pose_goal.position.x = pose_goal.position.x
                pose_goal.position.y = pose_goal.position.y - 0.05
                pose_goal.position.z = pose_goal.position.z
                pose_goal.orientation.x = quater[0]
                pose_goal.orientation.y = quater[1]
                pose_goal.orientation.z = quater[2]
                pose_goal.orientation.w = quater[3]
                self.robot_arm.set_pose_target(pose_goal)
                self.robot_arm.go(True)  
            elif command == 'd':
                pose_goal.orientation.w = 0.0
                pose_goal.position.x = pose_goal.position.x
                pose_goal.position.y = pose_goal.position.y + 0.05
                pose_goal.position.z = pose_goal.position.z
                pose_goal.orientation.x = quater[0]
                pose_goal.orientation.y = quater[1]
                pose_goal.orientation.z = quater[2]
                pose_goal.orientation.w = quater[3]
                self.robot_arm.set_pose_target(pose_goal)
                self.robot_arm.go(True)  
            elif command == 'r':
                pose_goal.orientation.w = 0.0
                pose_goal.position.x = pose_goal.position.x
                pose_goal.position.y = pose_goal.position.y
                pose_goal.position.z = pose_goal.position.z + 0.05
                pose_goal.orientation.x = quater[0]
                pose_goal.orientation.y = quater[1]
                pose_goal.orientation.z = quater[2]
                pose_goal.orientation.w = quater[3]
                self.robot_arm.set_pose_target(pose_goal)
                self.robot_arm.go(True)  
            elif command == 'f':
                pose_goal.orientation.w = 0.0
                pose_goal.position.x = pose_goal.position.x
                pose_goal.position.y = pose_goal.position.y
                pose_goal.position.z = pose_goal.position.z - 0.05
                pose_goal.orientation.x = quater[0]
                pose_goal.orientation.y = quater[1]
                pose_goal.orientation.z = quater[2]
                pose_goal.orientation.w = quater[3]
                self.robot_arm.set_pose_target(pose_goal)
                self.robot_arm.go(True)  
            elif command == 'x':
                self.robot_arm.attach_object("table")
            elif command == 'y':
                self.robot_arm.detach_object("table")
            elif command == 'v':
                self.set_pose_target(pose_goal)
            elif command == 'i':
                Orientation[0] = Orientation[0] + 0.2
                Orientation[1] = Orientation[1]
                Orientation[2] = Orientation[2]
                quater = quaternion_from_euler(Orientation[0], Orientation[1], Orientation[2])
                pose_goal.orientation.x = quater[0]
                pose_goal.orientation.y = quater[1]
                pose_goal.orientation.z = quater[2]
                pose_goal.orientation.w = quater[3]
                self.robot_arm.set_pose_target(pose_goal)
                self.robot_arm.go(True)  
            elif command == 'k':
                Orientation[0] = Orientation[0] - 0.2
                Orientation[1] = Orientation[1]
                Orientation[2] = Orientation[2]
                quater = quaternion_from_euler(Orientation[0], Orientation[1], Orientation[2])
                pose_goal.orientation.x = quater[0]
                pose_goal.orientation.y = quater[1]
                pose_goal.orientation.z = quater[2]
                pose_goal.orientation.w = quater[3]
                self.robot_arm.set_pose_target(pose_goal)
                self.robot_arm.go(True)  
            # yaw
            elif command == 'u':
                Orientation[0] = Orientation[0]
                Orientation[1] = Orientation[1] + 0.2
                Orientation[2] = Orientation[2]
                quater = quaternion_from_euler(Orientation[0], Orientation[1], Orientation[2])
                pose_goal.orientation.x = quater[0]
                pose_goal.orientation.y = quater[1]
                pose_goal.orientation.z = quater[2]
                pose_goal.orientation.w = quater[3]
                self.robot_arm.set_pose_target(pose_goal)
                self.robot_arm.go(True)  
            elif command == 'o':
                Orientation[0] = Orientation[0]
                Orientation[1] = Orientation[1] - 0.2
                Orientation[2] = Orientation[2]
                quater = quaternion_from_euler(Orientation[0], Orientation[1], Orientation[2])
                pose_goal.orientation.x = quater[0]
                pose_goal.orientation.y = quater[1]
                pose_goal.orientation.z = quater[2]
                pose_goal.orientation.w = quater[3]
                self.robot_arm.set_pose_target(pose_goal)
                self.robot_arm.go(True)  
            # roll
            elif command == 'j':
                Orientation[0] = Orientation[0]
                Orientation[1] = Orientation[1]
                Orientation[2] = Orientation[2] + 0.2
                quater = quaternion_from_euler(Orientation[0], Orientation[1], Orientation[2])
                pose_goal.orientation.x = quater[0]
                pose_goal.orientation.y = quater[1]
                pose_goal.orientation.z = quater[2]
                pose_goal.orientation.w = quater[3]
                self.robot_arm.set_pose_target(pose_goal)	
                self.robot_arm.go(True)  
            elif command == 'l':
                Orientation[0] = Orientation[0]
                Orientation[1] = Orientation[1]
                Orientation[2] = Orientation[2] - 0.2
                quater = quaternion_from_euler(Orientation[0], Orientation[1], Orientation[2])
                pose_goal.orientation.x = quater[0]
                pose_goal.orientation.y = quater[1]
                pose_goal.orientation.z = quater[2]
                pose_goal.orientation.w = quater[3]
                self.robot_arm.set_pose_target(pose_goal)
                self.robot_arm.go(True)  
                
                
            #self.robot_arm.set_pose_target(pose_goal)
            #self.robot_arm.go(True)  
                

if __name__=='__main__':
    tm = TestMove()
    #tm.__init__()
    tm.WASD()

    rospy.spin()
    roscpp_shutdown()
