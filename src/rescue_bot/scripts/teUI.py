#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import pygame
import numpy as np
import sys
import os

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 760, 600
border_thickness = 5
screen = pygame.display.set_mode((width * 2, height + 100))
pygame.display.set_caption('Camera Feeds')

class ImageSubscriber:
    def __init__(self):
        self.bridge = CvBridge()
        self.image1_received = False
        self.image2_received = False
        self.cv_image1 = None
        self.cv_image2 = None
        # Publisher
        self.publisher = rospy.Publisher('chatter2', String, queue_size=10)

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
    
    def publish_message(self, message):
        rospy.loginfo("Publishing: %s", message)
        self.publisher.publish(message)

    def save_image(self, image, filename):
        if image is not None:
            if os.path.exists(filename):
                # Split filename and extension
                name, ext = os.path.splitext(filename)
                count = 1
                
                while os.path.exists(f"{name}_{count}{ext}"):
                    count += 1
                filename = f"{name}_{count}{ext}"

            cv2.imwrite(filename, image) # It'll write the picture as new file as you want (image = ***.jpg or .png etc.)
            rospy.loginfo("Saved image as {}".format(filename))
        else:
            rospy.logerr("No image received to save.")

class N_button:
    def __init__(self,surface,text,color, textColor = (0,0,0)):
        self.surface = surface
        self.text = text
        self.color = color
        self.textColor = textColor
        self.x, self.y = None,None
        self.w, self.h = None,None
    
    def draw_button(self,x,y,w,h):
        self.x, self.y = x,y
        self.w, self.h = w,h
        pygame.draw.rect(self.surface, self.color, (x, y, w, h))
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, self.textColor)
        self.surface.blit(text_surface, (x + (w - text_surface.get_width()) // 2, y + (h - text_surface.get_height()) // 2))

    def click_button(self,click_function):
        mouse = pygame.mouse.get_pos()
        if self.x <= mouse[0] <= self.x + self.w and self.y <= mouse[1] <= self.y + self.h :
            click_function()

#click function
def terminateFunction(Sub,terminate_button : N_button):
    msg = String()
    msg.data = "p"
    Sub.publish_message(msg)
    if terminate_button.color == (255,0,0):
        terminate_button.color = (125,0,0)
    pygame.display.flip()


def ledFunction(Sub,Led_button : N_button):
    msg = String()
    if Led_button.color == (0,255,0):
        Led_button.color = (255,255,255)
        msg.data = "ledOff"
    else:
        Led_button.color = (0,255,0)
        msg.data = "ledOn"
    Sub.publish_message(msg)

def NavSnapFunction(Sub,NavSnap_button : N_button):
    msg = String()
    msg.data = "Nav Snap"
    Sub.publish_message(msg)
    # It will get image from Sub then we just use save_image method from ImageSubscriber to save the pic as new file
    # IMPLEMENT THE GOD !!! 
    cv_image1 = Sub.get_image1()
    if cv_image1 is not None: 
        Sub.save_image(cv_image1, "/home/rtx/GIT/catkin_ws/src/rescue_bot/scripts/web.jpg")
    else:
        rospy.logwarn("No image available to save.")

def ArmSnapFunction(Sub,ArmSnap_button : N_button):
    msg = String()
    msg.data = "Arm Snap" 
    Sub.publish_message(msg)
    cv_image2 = Sub.get_image2()
    if cv_image2 is not None:
        Sub.save_image(cv_image2, "/home/rtx/GIT/catkin_ws/src/rescue_bot/scripts/web.jpg")
    else:
        rospy.logwarn("No image available to save.")

def BatteryFunction(Sub,Battery_button : N_button):
    msg = String()
    msg.data = "Battery"
    Sub.publish_message(msg)

def main():
    image_subscriber = ImageSubscriber()
    image_subscriber.subscribe()
    terminateButton = N_button(screen,"",(255, 0, 0))
    ledButton = N_button(screen,"led",(255,255,255))
    NavSnapButton = N_button(screen,"Nav",(255,253,208))
    ArmSnapButton = N_button(screen,"Arm",(255,253,208))
    BatteryButton = N_button(screen,"",(169,169,169))

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
                    message = String()
                    message.data = key_name
                    image_subscriber.publish_message(message)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                terminateButton.click_button(
                    lambda: terminateFunction(image_subscriber,terminateButton)
                )
                ledButton.click_button(
                    lambda: ledFunction(image_subscriber,ledButton)
                )
                NavSnapButton.click_button(
                    lambda: NavSnapFunction(image_subscriber,NavSnapButton)
                )
                ArmSnapButton.click_button(
                    lambda: ArmSnapFunction(image_subscriber,ArmSnapButton)
                )
                BatteryButton.click_button(
                    lambda: BatteryFunction(image_subscriber,BatteryButton)
                )

        # if image_subscriber.image1_received:
        #     cv_image1 = image_subscriber.get_image1()
        #     cv_image1 = cv2.resize(cv_image1, (width, height))
        #     pygame_frame1 = pygame.image.frombuffer(cv_image1.tobytes(), cv_image1.shape[1::-1], "BGR")
        #     screen.blit(pygame_frame1, (0, 0))
        #     image_subscriber.image1_received = False
        
        # if image_subscriber.image2_received:
        #     cv_image2 = image_subscriber.get_image2()
        #     cv_image2 = cv2.resize(cv_image2, (width, height))
        #     pygame_frame2 = pygame.image.frombuffer(cv_image2.tobytes(), cv_image2.shape[1::-1], "BGR")
        #     screen.blit(pygame_frame2, (width, 0))
        #     image_subscriber.image2_received = False

        if image_subscriber.image1_received:
            cv_image1 = image_subscriber.get_image1()
            cv_image1 = cv2.resize(cv_image1, (width, height))
            pygame_frame1 = pygame.image.frombuffer(cv_image1.tobytes(), cv_image1.shape[1::-1], "BGR")
            screen.blit(pygame_frame1, (0 ,0))
            # pygame.draw.rect(screen, (0, 0, 0), (50, 50, width + border_thickness * 2, height + border_thickness * 2), border_thickness)
            image_subscriber.image1_received = False
        
        if image_subscriber.image2_received:
            cv_image2 = image_subscriber.get_image2()
            cv_image2 = cv2.resize(cv_image2, (width, height))
            pygame_frame2 = pygame.image.frombuffer(cv_image2.tobytes(), cv_image2.shape[1::-1], "BGR")
            screen.blit(pygame_frame2, (765 ,0))
            # pygame.draw.rect(screen, (0, 0, 0), (750, 50, width + border_thickness * 2, height + border_thickness * 2), border_thickness)
            image_subscriber.image2_received = False

        bar_height = 200             

        # Draw black bars under the camera feeds
        pygame.draw.rect(screen, (100, 100, 100), (0, height-40, 2*width, bar_height))
        # pygame.draw.rect(screen,(255,0,0),(750,height, 20, 10))
        pygame.draw.rect(screen,(100,100,100),(757,0,6,height+100))

        terminateButton.draw_button(820, height - 20, 40, 40) #done
        ledButton.draw_button(710, height - 20, 40, 40) #done
        BatteryButton.draw_button(770, height - 20, 40, 40) #done

        NavSnapButton.draw_button(380-30, height - 30, 50, 40) #done
        ArmSnapButton.draw_button(1140-30, height - 30, 50, 40) #done

        # Add picture *JUST ADD*
        button_image_ter = pygame.image.load('/home/rtx/GIT/catkin_ws/src/rescue_bot/scripts/terminate.webp')
        button_image_ter = pygame.transform.scale(button_image_ter, (40, 40))
        screen.blit(button_image_ter, (820, height-20))

        button_image_bat = pygame.image.load('/home/rtx/GIT/catkin_ws/src/rescue_bot/scripts/battery.webp')
        button_image_bat = pygame.transform.scale(button_image_bat, (40, 40))
        screen.blit(button_image_bat, (770, height-20))

        button_image_LED = pygame.image.load('/home/rtx/GIT/catkin_ws/src/rescue_bot/scripts/LED.webp')
        button_image_LED = pygame.transform.scale(button_image_LED, (40, 40))
        screen.blit(button_image_LED, (710, height-20))

        # button_image = pygame.image.load('arm.png')
        # button_image = pygame.transform.scale(button_image, (50, 50))
        # screen.blit(button_image, (200, height))        

        # # Draw the Quit button
        # draw_button(screen, "P Terminate", 50, height + 10, 140, 30, (255, 0, 0))

        pygame.display.flip()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
    finally:
        pygame.quit()