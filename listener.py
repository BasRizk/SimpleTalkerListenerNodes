import rospy
from std_msgs.msg import String

def receiver(data):
    rospy.loginfo(data.data)

def listener():
    rospy.init_node('listener')
    rospy.Subscriber('talker', String, receiver)
    rospy.spin()
    

if __name__ == '__main__':
    listener()