from geometry_msgs.msg import Twist, Pose2D, PoseStamped
from move_base_msgs.msg import *

class GoalMsg:

    def __init__(self):
        print 'goals inited'
        

    def toGoal(self,goal):
        goalDic = {'Lobby':self.toLobby,
                    'EVW1':self.toEVW1,'EVW2':self.toEVW2,'EVW3':self.toEVW3,'EVW4':self.toEVW4,
                    '201':self.to201,'202':self.to202,'203':self.to203,
                    '301':self.to301,'302':self.to302,'303':self.to303,
                    '401':self.to401,'402':self.to402,'403':self.to403}
        rosGoal = goalDic[goal]()
        return rosGoal

    def getELlist(self):
        ELlist = ['EVW1','EVW2','EVW3','EVW4']
        return ELlist

    def toLobby(self):
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.pose.position.x = 101
        goal.pose.position.y = 1
        goal.pose.orientation.w = 1
        return goal

    def toEVW1(self):
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.pose.position.x = 100
        goal.pose.position.y = 1
        goal.pose.orientation.w = 1
        return goal

    def toEVW2(self):
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.pose.position.x = 200
        goal.pose.position.y = 1
        goal.pose.orientation.w = 1
        return goal

    def toEVW3(self):
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.pose.position.x = 300
        goal.pose.position.y = 1
        goal.pose.orientation.w = 1
        return goal

    def toEVW4(self):
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.pose.position.x = 400
        goal.pose.position.y = 1
        goal.pose.orientation.w = 1
        return goal

    def to201(self):
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.pose.position.x = 201
        goal.pose.position.y = 1
        goal.pose.orientation.w = 1
        return goal

    def to202(self):
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.pose.position.x = 202
        goal.pose.position.y = 1
        goal.pose.orientation.w = 1
        return goal

    def to203(self):
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.pose.position.x = 203
        goal.pose.position.y = 1
        goal.pose.orientation.w = 1
        return goal

    def to301(self):
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.pose.position.x = 301
        goal.pose.position.y = 1
        goal.pose.orientation.w = 1
        return goal

    def to302(self):
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.pose.position.x = 302
        goal.pose.position.y = 1
        goal.pose.orientation.w = 1
        return goal

    def to303(self):
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.pose.position.x = 303
        goal.pose.position.y = 1
        goal.pose.orientation.w = 1
        return goal

    def to401(self):
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.pose.position.x = 401
        goal.pose.position.y = 1
        goal.pose.orientation.w = 1
        return goal

    def to402(self):
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.pose.position.x = 402
        goal.pose.position.y = 1
        goal.pose.orientation.w = 1
        return goal

    def to403(self):
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.pose.position.x = 403
        goal.pose.position.y = 1
        goal.pose.orientation.w = 1
        return goal