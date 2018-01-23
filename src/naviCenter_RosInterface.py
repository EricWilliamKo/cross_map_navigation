#!/usr/bin/env python

import rospy
import rospkg
import sys
import time
import math
import tf
from geometry_msgs.msg import Twist, Pose2D, PoseStamped
from std_msgs.msg import *
from move_base_msgs.msg import *
from actionlib_msgs.msg import *

from NavigationCenter.NaviCenter import NaviCenter
from NavigationCenter.hotelGoals import GoalMsg

rospack = rospkg.RosPack()
print rospack.get_path('elevator')

naviCenter = NaviCenter(rospack.get_path('elevator'))
hotelGoals = GoalMsg()


goalPub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size = 1)
goalCancel = rospy.Publisher('/move_base/cancel',GoalID,queue_size = 1)
callEVpub = rospy.Publisher('/callEV',Int16,queue_size=1)
checkEVpub = rospy.Publisher('/checkEV',Bool,queue_size=1)
enterEVpub = rospy.Publisher('/enterEV',Bool,queue_size=1)
alightEVpub = rospy.Publisher('/alightEV',Bool,queue_size=1)
changeMapPub = rospy.Publisher('/map_server/reload',String, queue_size=1)


def goalPublish(goal):
    global hotelGoals,goalPub
    rosGoal = hotelGoals.toGoal(goal)
    goalPub.publish(rosGoal)
    return

def goalCancelPub():
    global goalCancel
    goalCancel.publish()
    return

def naviResultCB(msg):
    global naviCenter
    naviCenter.GoalReachCB()
    return

def hotelGoal(msg):
    global naviCenter
    naviCenter.getNaviGoal(msg.data)
    return

def callEV(floor):
    global callEVpub
    callEVpub.publish(floor)
    return

def elevatorCB(msg):
    global naviCenter
    naviCenter.elevatorCB()
    return

def checkEV():
    global checkEVpub
    checkEVpub.publish(True)
    return

def checkEVcb(msg):
    global naviCenter
    naviCenter.enterEVcheckCB(msg.data)
    return

def enterEV():
    global enterEVpub
    enterEVpub.publish(True)
    return

def enterEVcb(msg):
    global naviCenter
    naviCenter.enterEVcallback(msg.data)
    return

def alightEV():
    global alightEVpub
    alightEVpub.publish(True)
    return

def alightEVcb(msg):
    global naviCenter
    naviCenter.alightEVcallback(msg.data)
    return

def changeMap(floor):
    global changeMapPub
    pubMsg = {1:'change to 1F',2:'change to 2F',3:'change to 3F',4:'change to 4F'}
    changeMapPub.publish(pubMsg[floor])
    return

    



if __name__ == '__main__':

    rospy.init_node('NaviCenter',anonymous = True)
    
    naviCenter.register(goalPublish,callEV,checkEV,enterEV,alightEV,changeMap)

    rospy.Subscriber('move_base/result', MoveBaseActionResult, naviResultCB)
    rospy.Subscriber('/hotelGoal', String, hotelGoal)
    rospy.Subscriber('/elevatorCB',Bool,elevatorCB)
    rospy.Subscriber('/checkEVcb',Bool,checkEVcb)
    rospy.Subscriber('/enterEVcb',Bool,enterEVcb)
    rospy.Subscriber('/alightEVcb',Bool,alightEVcb)

    rospy.spin()