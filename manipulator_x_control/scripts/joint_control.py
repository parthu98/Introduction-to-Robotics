#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

joint_positions_1 = [0, 0, 0, 0]
joint_positions_2 = [1.57, 0, 0, 0]
joint_positions_3 = [1.57, 0.28, 0.05, 1.3]
joint_positions_4 = [1.57, 0, 0.05, 1.57]
joint_positions_5 = [0, 0, 0.05, 1.57]
joint_positions_6 = [0, 0.28, 0.05, 1.3]

gripper_state = [1, -1]

rospy.init_node('move_openmanipulator', anonymous=True)

joint_pub = [
    rospy.Publisher(f'/joint{i+1}_position/command', Float64, queue_size=10) 
    for i in range(4)
]

gripper_pub = rospy.Publisher('/gripper_position/command', Float64, queue_size=10)

# Send gripper command
gripper_pub.publish(gripper_state[0])
rospy.sleep(1)  # Wait for the gripper to open

# Send joint positions
for i in range(4):
    joint_pub[i].publish(joint_positions_1[i])

rospy.sleep(1)  # Allow time for the manipulator to move

for i in range(4):
    joint_pub[i].publish(joint_positions_2[i])

rospy.sleep(1)  # Allow time for the manipulator to move

for i in range(4):
    joint_pub[i].publish(joint_positions_3[i])

rospy.sleep(1)  # Allow time for the manipulator to move

# Send gripper command
gripper_pub.publish(gripper_state[1])
rospy.sleep(1)  # Wait for the gripper to close

for i in range(4):
    joint_pub[i].publish(joint_positions_4[i])

rospy.sleep(1)  # Allow time for the manipulator to move

for i in range(4):
    joint_pub[i].publish(joint_positions_5[i])

rospy.sleep(1)  # Allow time for the manipulator to move

for i in range(4):
    joint_pub[i].publish(joint_positions_6[i])

rospy.sleep(1)  # Allow time for the manipulator to move

# Send gripper command
gripper_pub.publish(gripper_state[0])
rospy.sleep(1)  # Wait for the gripper to open