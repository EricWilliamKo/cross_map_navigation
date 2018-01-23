#!/usr/bin/env python

import cherrypy

import rospy
import sys
from std_msgs.msg import *

class PC_server(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"
    
    @cherrypy.expose
    def reached(self):
        print 'QQ'
        return "GOOOOOOOOOOOOD!"

if __name__ == '__main__':
    rospy.init_node('NaviCenter',anonymous = False)

    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.server.thread_pool = 10
    cherrypy.quickstart(PC_server())
