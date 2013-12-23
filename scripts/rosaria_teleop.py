#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import Joy

def callback(data):
	pub = rospy.Publisher('RosAria/cmd_vel', Twist)
	cmd_vel = Twist()
	cmd_vel.linear = Vector3(data.axes[1] / 5, 0, 0)
	cmd_vel.angular = Vector3(0, 0, data.axes[0] / 5)
	pub.publish(cmd_vel)

def joy_relay():
	rospy.init_node('joy_relay', anonymous=True)
	rospy.Subscriber('joy', Joy, callback)
	rospy.spin()

if __name__ == '__main__':
	joy_relay()