import rospy
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('talker', String, queue_size=8)
    
    rospy.init_node('talker')
    rate = rospy.Rate(1)
    
    msgs = ["BAS RIZK", "STEVEN NASSEF"]
    msg_i = 0
    
    while not rospy.is_shutdown():
        msg_str = msgs[msg_i] 
        rospy.loginfo("Sending %s" % msg_str + " @ %s" % rospy.get_time())
        pub.publish(msg_str)
        
        msg_i += 1
        if msg_i == len(msgs):
            msg_i = 0            
            
        rate.sleep()

        
        
if __name__ == '__main__':
    talker()
        
