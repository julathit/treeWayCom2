#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

def image_publisher():
    rospy.init_node('image_publisher', anonymous=True)
    pub = rospy.Publisher('camera/image', Image, queue_size=10)
    frame_rate = 15  # 15 frames per second

    cap = cv2.VideoCapture(0)
    bridge = CvBridge()

    if not cap.isOpened():
        rospy.logerr("Could not open video device")
        return

    # Adjust capture resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

    # Desired frame rate limit
    frame_rate_limit = rospy.Duration(1.0 / frame_rate)

    while not rospy.is_shutdown():
        start_time = rospy.Time.now()

        ret, frame = cap.read()
        if ret:
            # Resize frame
            frame_resized = cv2.resize(frame, (320, 240))
            # Convert to ROS Image message
            image_message = bridge.cv2_to_imgmsg(frame_resized, encoding="bgr8")
            # Publish the image message
            pub.publish(image_message)

        # Ensure minimum time between frames to cap frame rate
        elapsed_time = rospy.Time.now() - start_time
        if elapsed_time < frame_rate_limit:
            rospy.sleep(frame_rate_limit - elapsed_time)

    cap.release()

if __name__ == '__main__':
    try:
        image_publisher()
    except rospy.ROSInterruptException:
        pass
