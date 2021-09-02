#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String

drive_pub = rospy.Publisher('/position/drive', String, queue_size = 10)
arm_pub= rospy.Publisher('/position/robotic_arm', String, queue_size = 10)

def drive_callback(msg):
    print( "I heard is " + msg.data)
    if msg.data[0] == 'A' and msg.data[-1] == 'B':
        data = msg.data[1:-1]
        group = [data[i:i+4] for i in range(0, len(data), 4)]
        drive_msg = String()
        for i in group :
            value = int(i[1:])
            if i[0] == '0'and value > 255: #positive
                value = 255
            elif i[0] == '1':
                value = -value
                if value < -255 :
                    value = -255
            drive_msg.data += str(value) + ' '
        drive_msg.data = drive_msg.data[:-1]
        drive_pub.publish(drive_msg)

def arm_callback(msg):
    print( "I heard is " + msg.data)
    if msg.data[0] == 'A' and msg.data[-1] == 'B':
        data = msg.data[1:-1]
        group = [data[i:i+4] for i in range(0, len(data), 4)]
        arm_msg = String()
        for i in group :
            value = int(i[1:])
            if i[0] == '0'and value > 255: #positive
                value = 255
            elif i[0] == '1':
                value = -value
                if value < -255 :
                    value = -255
            arm_msg.data += str(value) + ' '
        arm_msg.data = arm_msg.data[:-1]
        arm_pub.publish(arm_msg)

def subs():

    rospy.init_node('subscriber', anonymous=True)

    rospy.Subscriber("/serial/drive",String,drive_callback)
    rospy.Subscriber("/serial/robotic_arm", String, arm_callback)


    while not rospy.is_shutdown():
        pass


if __name__ == '__main__':
    subs()
