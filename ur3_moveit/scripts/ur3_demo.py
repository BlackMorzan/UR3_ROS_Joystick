#!/usr/bin/env python

import sys
import rospy
import tf
import moveit_commander
import random
import re
import os
import moveit_msgs.msg
from geometry_msgs.msg import Pose, Point, Quaternion
from math import pi


def WASD():
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
        print(" X - save point and exit")

        command = raw_input("Control : ")
        if command == 'w':		
	    pose_goal.orientation.w = 0.0
	    pose_goal.position.x = pose_goal.position.x + 0.05
	    pose_goal.position.y = pose_goal.position.y
	    pose_goal.position.z = pose_goal.position.z
	    group[0].set_pose_target(pose_goal)
	    group[0].go(True)
        elif command == 's':
	    pose_goal.orientation.w = 0.0
	    pose_goal.position.x = pose_goal.position.x - 0.05
	    pose_goal.position.y = pose_goal.position.y
       	    pose_goal.position.z = pose_goal.position.z
	    group[0].set_pose_target(pose_goal)
	    group[0].go(True)
        elif command == 'a':
	    pose_goal.orientation.w = 0.0
	    pose_goal.position.x = pose_goal.position.x
	    pose_goal.position.y = pose_goal.position.y - 0.05
	    pose_goal.position.z = pose_goal.position.z
	    group[0].set_pose_target(pose_goal)
	    group[0].go(True)
        elif command == 'd':
	    pose_goal.orientation.w = 0.0
	    pose_goal.position.x = pose_goal.position.x
	    pose_goal.position.y = pose_goal.position.y + 0.05
	    pose_goal.position.z = pose_goal.position.z
	    group[0].set_pose_target(pose_goal)
	    group[0].go(True)
        elif command == 'r':
	    pose_goal.orientation.w = 0.0
	    pose_goal.position.x = pose_goal.position.x
	    pose_goal.position.y = pose_goal.position.y
	    pose_goal.position.z = pose_goal.position.z + 0.05
	    group[0].set_pose_target(pose_goal)
	    group[0].go(True)
        elif command == 'f':
	    pose_goal.orientation.w = 0.0
	    pose_goal.position.x = pose_goal.position.x
	    pose_goal.position.y = pose_goal.position.y
	    pose_goal.position.z = pose_goal.position.z - 0.05
	    group[0].set_pose_target(pose_goal)
	    group[0].go(True)
            
                ## SAVE AND EXIT ##
	elif command == 'x':
	    break

        print("Position : ",pose_goal.position.x, pose_goal.position.y , pose_goal.position.z)
	rospy.sleep(0.5)
        
    point = [pose_goal.position.x, pose_goal.position.y, pose_goal.position.z]
    return point
## END OF WASD
        
def text_input():
    print("zaraz tu dokoncze ")

def freedrive():
    print("zaraz tu dokoncze")
    
def on_click():
    raw_input("Select desired TCP position and press enter to continue...")
    file  = open("trajectory.txt")
    
    lines = file.readlines()
    x_pos = lines[desired_line]
    y_pos = lines[desired_line + 1]
    z_pos = lines[desired_line + 2]

    file.close()
    
    x_pos_string = re.findall(r"[-+]?\d*\.\d+|\d+", x_pos)
    y_pos_string = re.findall(r"[-+]?\d*\.\d+|\d+", y_pos)
    z_pos_string = re.findall(r"[-+]?\d*\.\d+|\d+", z_pos)
    x_pos = float(x_pos_string.pop(0))
    y_pos = float(y_pos_string.pop(0))
    z_pos = float(z_pos_string.pop(0))
    
    print(x_pos,y_pos,z_pos)

    pose_goal.orientation.w = 1.0
    pose_goal.position.x = x_pos  
    pose_goal.position.y = y_pos  
    pose_goal.position.z = z_pos 

    group[0].set_pose_target(pose_goal)
    group[0].go(True)
    rospy.sleep(2)

    desired_line = desired_line + 11

    
def add_point():
    print("Please select an input option")
    print("Avaliable options : ")
    print("1 - WASD control")
    print("2 - terminal input")
    print("3 - freedrive -> drag and drop in Rviz")
    print("4 - clicking desired TCP position in Rviz")
    print("5 - cancel and save the program")
    
    control_menu_choice = raw_input()
    if control_menu_choice == '1':
        point = WASD()
    elif control_menu_choice == '2':
        point = text_input()
    elif control_menu_choice == '3':
        point = freedrive()
    elif control_menu_choice  == '4':
        point = on_click()
    elif control_menu_choice == '5':
        point = 0

    return point

        
def display_programs():
    current_directory = os.getcwd()
    dir_for_programs = os.path.join(current_directory, "programs")
    if not os.path.exists(dir_for_programs):
        print("No programs avaliable. Let's  create a new one :) ")
        return
    all_programs = os.listdir(dir_for_programs)
    ## "listdir" returns a list containing the names
    number_of_programs = len(all_programs)
    
    print("\n")
    for i in range(number_of_programs-1):
        print(str(i+1)+".")
        print("PROGRAM NAME :")
        print(all_programs[i]) # prints the program's name
        filepath = os.path.join(dir_for_programs, all_programs[i])
        file = open(filepath, "r")
        print("PROGRAM DESCRIPTION :")
        print(file.readline())
    print("\n")
        
def new_program():
    pose_goal.orientation.w = 0.0
    pose_goal.position.x = 0.2
    pose_goal.position.y = 0.0
    pose_goal.position.z = 0.2

    group[0].set_pose_target(pose_goal)
    group[0].go(True)

    current_directory = os.getcwd()
    dir_for_programs = os.path.join(current_directory, "programs")
    if not os.path.exists(dir_for_programs):
        os.mkdir(dir_for_programs)

    new_program_name = raw_input("Please insert the name for your program : ")
    filepath = os.path.join(dir_for_programs, new_program_name)
    file = open(filepath, "a")    
    # 'a' = "opens file in append mode. If file does not exist, it creates a new one
    
    while True:
        point = add_point()
        if(point == 0):
            break
        file.write(point)
    file.close()

    
def execute_program():
    print("execute")
    
## main ##
pose_goal = Pose()
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node ( 'ur3_move', anonymous = True )
group = [moveit_commander.MoveGroupCommander("manipulator")]
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory,queue_size=20)

while not rospy.is_shutdown():
    print("**** MAIN MENU ****")
    print("Please select an option and press << enter >> : ")
    print("1 - display avaliable programs")
    print("2 - add new program")
    print("3 - execute program")

    main_menu_choice = raw_input()
    if main_menu_choice == '1':
        display_programs()
    elif main_menu_choice == '2':
        new_program()
    elif main_menu_choice == '3':
        execute_program()
moveit_commander.roscpp_shutdown()
