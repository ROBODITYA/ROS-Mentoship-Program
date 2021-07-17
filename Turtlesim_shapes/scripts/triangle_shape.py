#!/usr/bin/env python

'''In this python script we are moving the turtle in triangular shape using geometry_msgs...!!!'''
''' GitHub: https://github.com/ROBODITYA '''

import rospy
from geometry_msgs.msg  import Twist

# main function
def triangle():
    
    # initializing the node
    rospy.init_node('triangle', anonymous=True)
    
    # seting the topic on which all msgs have to publish
    pub = rospy.Publisher("/turtlesim3/turtle1/cmd_vel", Twist, queue_size=20)
    
    rate = rospy.Rate(1) # 1hz
    
    # storing twist msgs in veriable
    vel_msg = Twist()
    rate.sleep()
    
    for i in range(3):
        #Forward
        vel_msg.linear.x = 3 # m/s
        vel_msg.angular.z = 0 # r/s
        pub.publish(vel_msg)
        rate.sleep()

        #Stop
        vel_msg.linear.x = 0 # m/s
        vel_msg.angular.z = 0 # r/s
        pub.publish(vel_msg)
        rate.sleep()

        #Turn
        vel_msg.linear.x = 0 # m/s
        vel_msg.angular.z = 2.0943951024 #r/s
        pub.publish(vel_msg)
        rate.sleep()

        #Stop
        vel_msg.linear.x = 0 # m/s
        vel_msg.angular.z = 0 # r/s
        pub.publish(vel_msg)
        rate.sleep()

        #Forward
        vel_msg.linear.x = 3 # m/s
        vel_msg.angular.z = 0 # r/s
        pub.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    triangle()
