#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist, Pose2D, PoseStamped
from std_msgs.msg import *
from move_base_msgs.msg import *
from actionlib_msgs.msg import *

def goalSub(msg):
    print 'new goal ',msg.pose.position.x
    return

def callEVsub(msg):
    print 'elevator is going to ',msg.data
    return

def checkSub(msg):
    print 'check elevator'
    return

def enterEVsub(msg):
    print 'enter elevator'
    return

def alightEVsub(msg):
    print 'alight elevator'
    return

def changeMap(msg):
    print msg.data
    return

if __name__=="__main__":
    rospy.init_node('fake_data_sub')

    rospy.Subscriber('/move_base_simple/goal', PoseStamped,goalSub)
    rospy.Subscriber('/callEV',Int16,callEVsub)
    rospy.Subscriber('/checkEV',Bool,checkSub)
    rospy.Subscriber('/enterEV',Bool,enterEVsub)
    rospy.Subscriber('/alightEV',Bool,alightEVsub)
    rospy.Subscriber('/map_server/reload',String,changeMap)

    rospy.spin()