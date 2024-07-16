#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import Bool
import cv2
import numpy as np

class AdaptiveVideoPublisher:
    def __init__(self, camera_id, topic_name):
        self.pub = rospy.Publisher(topic_name, CompressedImage, queue_size=10)
        self.heartbeat_sub = rospy.Subscriber('network_quality', Bool, self.network_quality_callback)
        self.cap = cv2.VideoCapture(camera_id)
        self.network_quality = True
        self.frame_rate = 15
        self.resolution = (320, 240)
        self.jpeg_quality = 50

    def network_quality_callback(self, msg):
        self.network_quality = msg.data
        self.adapt_quality()

    def adapt_quality(self):
        if self.network_quality:
            self.frame_rate = 15
            self.resolution = (320, 240)
            self.jpeg_quality = 50
        else:
            self.frame_rate = 5
            self.resolution = (160, 120)
            self.jpeg_quality = 30

    def publish_video(self):
        rate = rospy.Rate(self.frame_rate)
        while not rospy.is_shutdown():
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.resize(frame, self.resolution)
                _, jpeg = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), self.jpeg_quality])
                msg = CompressedImage()
                msg.header.stamp = rospy.Time.now()
                msg.format = "jpeg"
                msg.data = np.array(jpeg).tostring()
                self.pub.publish(msg)
            rate.sleep()

    def run(self):
        self.publish_video()

def main():
    rospy.init_node('adaptive_video_publisher', anonymous=True)
    pub1 = AdaptiveVideoPublisher(0, 'camera/image1')
    pub2 = AdaptiveVideoPublisher(2, 'camera/image2')

    try:
        pub1.run()
        pub2.run()
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()