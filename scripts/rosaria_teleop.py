#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import Joy

speed_limiter = 1

def callback(data):
    pub = rospy.Publisher('RosAria/cmd_vel', Twist)
    cmd_vel = Twist()
    cmd_vel.linear = Vector3(data.axes[1] / speed_limiter, 0, 0)
    cmd_vel.angular = Vector3(0, 0, data.axes[0] / speed_limiter)
    pub.publish(cmd_vel)

def joy_relay():
    rospy.init_node('joy_relay', anonymous=True)
    speed_limiter = rospy.get_param('~speed_limiter', '5')
    rospy.Subscriber('joy', Joy, callback)
    rospy.spin()

if __name__ == '__main__':
    joy_relay()
