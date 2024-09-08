#!/usr/bin/env python3

import rospy
from open_manipulator_msgs.srv import SetJointPosition, SetJointPositionRequest
# from open_manipulator_msgs.srv import SetActuatorState, SetActuatorStateRequest
import math  # Import math for conversion functions

# Initialize ROS node
rospy.init_node('move_openmanipulator_with_service')

# Wait for the joint control service to be available
rospy.wait_for_service('/goal_joint_space_path')
rospy.wait_for_service('/goal_tool_control')

# Create service proxies
joint_service = rospy.ServiceProxy('/goal_joint_space_path', SetJointPosition)
gripper_service = rospy.ServiceProxy('/goal_tool_control', SetJointPosition)

# Function to convert degrees to radians
def degrees_to_radians(degrees):
    return [math.radians(degree) for degree in degrees]

# Function to set joint positions
def set_joint_positions(joint_angles_in_degrees):
    joint_angles_in_radians = degrees_to_radians(joint_angles_in_degrees)  # Convert to radians
    joint_request = SetJointPositionRequest()
    joint_request.joint_position.joint_name = ['joint1', 'joint2', 'joint3', 'joint4']
    joint_request.joint_position.position = joint_angles_in_radians
    joint_request.path_time = 1.0  # Time for the path to be completed (in seconds)
    
    try:
        joint_service(joint_request)
        rospy.sleep(1)  # Allow time for the manipulator to move
    except rospy.ServiceException as e:
        rospy.logerr(f"Failed to call service: {e}")

# Function to control the gripper
def control_gripper(position):
    gripper_request = SetJointPositionRequest()
    gripper_request.joint_position.joint_name = ['gripper']
    gripper_request.joint_position.position = [position]  # Open or close
    gripper_request.path_time = 1.0
    
    try:
        gripper_service(gripper_request)
        rospy.sleep(1)  # Wait for the gripper to act
    except rospy.ServiceException as e:
        rospy.logerr(f"Failed to call service: {e}")

# Joint positions in degrees
joint_positions_1 = [0, 0, 0, 0]
joint_positions_2 = [90, 0, 0, 0]  # 90 degrees = pi/2 radians
joint_positions_3 = [90, 15, 3, 75]  # Degrees for each joint
joint_positions_4 = [90, -15, 3, 90]
joint_positions_5 = [0, -15, 3, 90]
joint_positions_6 = [0, 15, 3, 75]
joint_positions_7 = [0, 0, 0, 0]

gripper_open = 0.01  # Define gripper open position
gripper_close = -0.01  # Define gripper closed position

# Send gripper open command
control_gripper(gripper_open)

# Send joint position commands (in degrees, converted to radians)
set_joint_positions(joint_positions_1)
set_joint_positions(joint_positions_2)
set_joint_positions(joint_positions_3)

# Send gripper close command
control_gripper(gripper_close)

# Continue sending joint position commands
set_joint_positions(joint_positions_4)
set_joint_positions(joint_positions_5)
set_joint_positions(joint_positions_6)

# Send gripper open command
control_gripper(gripper_open)

set_joint_positions(joint_positions_7)