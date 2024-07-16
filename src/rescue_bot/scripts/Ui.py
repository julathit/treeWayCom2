#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import pygame
import sys
from threading import Timer
from Nframe import N_button as N
from RescueBOT_controller_v1 import RobotController
from rescue_bot.msg import camera_config

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 640, 480 
screen = pygame.display.set_mode((width * 2, height + 50+200))
pygame.display.set_caption('Camera Feeds')

class ImageSubscriber:
    def __init__(self):
        self.bridge = CvBridge()
        self.image1_received = False
        self.image2_received = False
        self.cv_image1 = None
        self.cv_image2 = None

        # Initialize the publisher
        self.pub = rospy.Publisher('image_set', camera_config, queue_size=2)

    def callback1(self, data):
        try:
            self.cv_image1 = self.bridge.imgmsg_to_cv2(data, "bgr8")
            self.image1_received = True
        except CvBridgeError as e:
            rospy.logerr(e)

    def callback2(self, data):
        try:
            self.cv_image2 = self.bridge.imgmsg_to_cv2(data, "bgr8")
            self.image2_received = True
        except CvBridgeError as e:
            rospy.logerr(e)

    def subscribe(self):
        rospy.init_node('image_subscriber', anonymous=True)
        rospy.Subscriber('camera/image', Image, self.callback1)
        rospy.Subscriber('camera/image2', Image, self.callback2)

    def get_image1(self):
        return self.cv_image1

    def get_image2(self):
        return self.cv_image2

    def publish_message(self, msg):
        self.pub.publish(msg)

# Click function
def terminateFunction(terminate_button: N.button):

    if terminate_button.color == (255, 0, 0):
        terminate_button.color = (125, 0, 0)

    def resetColor():
        terminate_button.color = (255, 0, 0)
    
    Timer(0.25, resetColor).start()

def ledFunction(Led_button: N.button):
    if Led_button.color == (255, 255, 255):
        Led_button.color = (0, 255, 0)
    else:
        Led_button.color = (255, 255, 255)

def Up_scale_function(Sub,Up_button : N.button,msg = camera_config()):
    if msg.scale < 3:
        msg.scale = msg.scale + 1
    else:
        msg.scale = 1
    
    if Up_button.color == (255, 255, 255):
        Up_button.color = (225, 225, 225)

    def resetColor():
        Up_button.color = (255, 255, 255)
    
    Timer(0.25, resetColor).start()

    Sub.publish_message(msg)  
# end of the function


#button modify class
class button_Ind(N.button):
    def __init__(self, surface, text,msg ,color ,textColor=(0,0,0)):
        super().__init__(surface, text, color, textColor)
        self.msg = msg

    def draw_button(self, x, y, w, h):
        super().draw_button(x, y, w - 15, h)  # Ensure this method call is correct

        font = pygame.font.Font(None, 36)  # Use None for default font
        text_surface = font.render(str(self.msg.scale), True, self.textColor)  # Ensure self.text and self.textColor are correct
        text_rect = text_surface.get_rect(center=(x + w - 4, y + h // 2))  # Center text within button
        pygame.draw.rect(self.surface, [2*i//3 for i in self.color], (x + w -15, y, 20, h))

        self.surface.blit(text_surface, text_rect)
        

def main():
    image_subscriber = ImageSubscriber()
    image_subscriber.subscribe()
    terminateButton = N.button(screen, "P Terminate", (255, 0, 0))
    ledButton = N.button(screen, "led", (255, 255, 255))
    R_controler = RobotController()
    CaomandList = camera_config()
    CaomandList.scale, CaomandList.fram_rate, CaomandList.color_set = 1,15,False

    #image set up
    Up_Button = button_Ind(screen,"UpScale",CaomandList,(255,255,255))

    while not rospy.is_shutdown():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rospy.signal_shutdown("Pygame Quit")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    rospy.signal_shutdown("ESC pressed")
                    pygame.quit()
                    sys.exit()
                else:
                    key_name = pygame.key.name(event.key)
                    print(f"Key pressed: {key_name}")

                if event.key == pygame.K_SLASH:
                    ledFunction(image_subscriber, ledButton)
                elif event.key == pygame.K_p:
                    terminateFunction(terminateButton)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                terminateButton.click_button(
                    lambda: terminateFunction(terminateButton)
                )
                ledButton.click_button(
                    lambda: ledFunction(ledButton)
                )
                Up_Button.click_button(
                    lambda: Up_scale_function(image_subscriber,Up_Button,CaomandList)
                )

        if image_subscriber.image1_received:
            cv_image1 = image_subscriber.get_image1()
            cv_image1 = cv2.resize(cv_image1, (width, height))
            pygame_frame1 = pygame.image.frombuffer(cv_image1.tobytes(), cv_image1.shape[1::-1], "BGR")
            screen.blit(pygame_frame1, (0, 0))
            image_subscriber.image1_received = False
        
        if image_subscriber.image2_received:
            cv_image2 = image_subscriber.get_image2()
            cv_image2 = cv2.resize(cv_image2, (width, height))
            pygame_frame2 = pygame.image.frombuffer(cv_image2.tobytes(), cv_image2.shape[1::-1], "BGR")
            screen.blit(pygame_frame2, (width, 0))
            image_subscriber.image2_received = False

        bar_height = 250

        # Draw black bars under the camera feeds
        pygame.draw.rect(screen, (128, 128, 128), (0, height, 2 * width, bar_height))

        terminateButton.draw_button(50, height + 10, 140, 30)
        ledButton.draw_button(200, height + 10, 140, 30)
        Up_Button.draw_button(350,height + 10,140,30)

        R_controler.run(screen, (127, 255, 0))

        pygame.display.flip()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
    finally:
        pygame.quit()
