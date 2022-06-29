#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import cv2
import numpy as np


class TimerGui:
    def __init__(self):
        rospy.init_node("timer_gui")
        rospy.Subscriber("/timer", String, callback=self.gui)

    def gui(self, msg):
        blank_image = np.zeros(shape=[50, 800, 3], dtype=np.uint8)
        string = msg.data
        cv2.putText(blank_image, string, (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 4)
        cv2.imshow("Timer", blank_image)
        cv2.waitKey(1)

TimerGui()
rospy.spin()