#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
import time
import cv2
import numpy as np

class TimeTrial:
    def __init__(self):
        
        rospy.init_node("timer")
        rospy.Subscriber("/ir", Int32, callback= self.timer)
        self.pub = rospy.Publisher("/timer", String, queue_size=1)
        self.start_time = 0
        self.end_time = 0
        self.lap_time = 0.1
        
    def timer(self, msg):
        
        if msg.data == 0:
            self.start_time = time.time()

        if msg.data == 1:
            self.end_time = time.time() - self.start_time
            
            if self.lap_time > 100000:
                self.lap_time = 0.1
            
            if self.end_time > self.lap_time:
                self.lap_time = self.end_time
        
        text = f"Current time: {self.end_time:.04f} | Best time: {self.lap_time:0.4f}"
        self.pub.publish(text)


TimeTrial()
rospy.spin()