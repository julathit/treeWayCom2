#!/usr/bin/env python3
import rospy
import pygame
import math as m
# from functools import lru_cache
from rescue_bot.msg import servo_angle, drive_motor
from std_msgs.msg import Bool

'''
Controller Guildlines:
- Use Q, A, W, S, E, D, R, F to control servos
    > Q, A: servo_1
    > W, S: servo_2
    > E, D: servo_3
    > R, F: servo_4
- Use J, N, K, M, Space to control motors
    > J, N: motor_1
    > K, M: motor_2
    > Space: stop all driving motors
'''

'''
JoyStick Guidlines:

  >> First Joystick - Servo control
        Left stick (UP-DOWN)  - servo 1
        Right stick (UP-DOWN) - servo 2
        LT-RT (Trigger)       - servo 3
        LB-RB (Button)        - servo 4

        D-pad (Hat)           - Control driving motor (Deactivate 2nd joystick when use)

        B-button (red)        - Middle position preset hotkey
        X-button (blue)       - set-zero preset hotkey
        Y-button (Yellow)     - /not assign
        A-button (Green)      - /not assign
    
  >> Second Joystick - Drive control
        Left stick (UP-DOWN)  - left motor
        Right stick (UP-DOWN) - sright motor
'''

'''
getbutton list
0 -> A 
1 -> B (HOME)
2 -> X (Normal)
3 -> Y
4 -> LB
5 -> RB
6 -> BACK
7 -> START
8 -> Logitech
9 -> left thumb
10 -> right thumb
'''

class RobotController:
    def __init__(self):
        if __name__ == "__main__":
            rospy.init_node("robot_controller", anonymous=True)
        self.servo_pub = rospy.Publisher('servo_angle', servo_angle, queue_size=75)
        self.motor_pub = rospy.Publisher('drive_motor', drive_motor, queue_size=75)
        self.light_pub = rospy.Publisher('light_control', Bool, queue_size=75)
        self.rate = rospy.Rate(10)  # 30hz for smoother control

        # Initialize pygame
        pygame.init()
        pygame.joystick.init()
    

        # Initialize joysticks
        self.joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        for joystick in self.joysticks:
            joystick.init()

        if len(self.joysticks) < 2:
            rospy.logwarn(f"Only {len(self.joysticks)} joystick(s) found. Some functions may be limited.")

        # Initialize servo angles
        self.angles = servo_angle()
        self.angles.servo_1 = 45   # Start at middle position (0-180 range)
        self.angles.servo_2 = 60  # Start at middle position (0-270 range)
        self.angles.servo_3 = 90   # Start at middle position (0-180 range)
        self.angles.servo_4 = 0   # Start at middle position (0-180 range)

        # Initialize drive motor values
        self.motor = drive_motor()
        self.motor.m_1 = 0  # Start at stop
        self.motor.m_2 = 0  # Start at stop

        # Define servo limits
        self.servo_limits = [
            (0, 180),   # servo_1
            (0, 270),   # servo_2
            (0, 180),   # servo_3
            (0, 90)    # servo_4
        ]

        # Define motor limits
        self.motor_limits = (-255, 255)  # Assuming -255 is full reverse and 255 is full forward

        self.INVERSE_KINEMATIC = False
        self.LIGHT = False

    def update_angle(self, servo_index, change):
        current_angle = getattr(self.angles, f'servo_{servo_index + 1}')
        new_angle = current_angle + change
        new_angle = max(self.servo_limits[servo_index][0], min(new_angle, self.servo_limits[servo_index][1]))
        setattr(self.angles, f'servo_{servo_index + 1}', new_angle)
    
    def update_motor(self, motor_index, value):
        if abs(value) > 0.1:
            new_value = int(round(value,4) * 255)
        else:
            new_value = 0
            # rospy.logwarn(f"Motor {motor_index}: 0")
        new_value = max(self.motor_limits[0], min(new_value, self.motor_limits[1]))
        # rospy.logfatal(f"Joystick value: {value}")
        # rospy.logfatal(f"Motor value: {new_value}")
        setattr(self.motor, f'm_{motor_index + 1}', new_value)

    def update_motor_keyboard(self, motor_index, value):
        current_value = getattr(self.motor, f'm_{motor_index + 1}')
        new_value = current_value + value
        new_value = max(self.motor_limits[0], min(new_value, self.motor_limits[1]))
        # rospy.logfatal(f"Motor value: {new_value}")
        setattr(self.motor, f'm_{motor_index + 1}', new_value)

    def run(self,screen,textColor = (0,0,0), Font = 35):

            keys = pygame.key.get_pressed()
            
            # Keyboard control for servos
            if keys[pygame.K_q]: self.update_angle(0, 1)
            if keys[pygame.K_a]: self.update_angle(0, -1)
            if keys[pygame.K_w]: self.update_angle(1, 1)
            if keys[pygame.K_s]: self.update_angle(1, -1)
            if keys[pygame.K_e]: self.update_angle(2, 1)
            if keys[pygame.K_d]: self.update_angle(2, -1)
            if keys[pygame.K_r]: self.update_angle(3, 10)
            if keys[pygame.K_f]: self.update_angle(3, -10)
            # Keyboard hotkeys for Servo preset
            if keys[pygame.K_1]:  # Reset all servos to safe position
                self.angles.servo_1 = 45
                self.angles.servo_2 = 90
                self.angles.servo_3 = 90
                self.angles.servo_4 = 0
            if keys[pygame.K_2]:  # Set the arm to middle position
                self.angles.servo_1 = 45
                self.angles.servo_2 = 60
                self.angles.servo_3 = 50
                self.angles.servo_4 = 0
            if keys[pygame.K_3]:  # set the arm pointing down
                self.angles.servo_1 = 40
                self.angles.servo_2 = 20
                self.angles.servo_3 = 100
                self.angles.servo_4 = 0
            if keys[pygame.K_4]:  # Set the arm pointing up
                self.angles.servo_1 = 90
                self.angles.servo_2 = 90
                self.angles.servo_3 = 90
                self.angles.servo_4 = 0
            if keys[pygame.K_5]:  # Set the arm pointing to the sky
                self.angles.servo_1 = 90
                self.angles.servo_2 = 125
                self.angles.servo_3 = 90
                self.angles.servo_4 = 0
            if keys[pygame.K_6]:  # Set the arm pointing backward
                self.angles.servo_1 = 110
                self.angles.servo_2 = 170
                self.angles.servo_3 = 130
                self.angles.servo_4 = 0
            if keys[pygame.K_7]:  # Set all servos to Home position
                self.angles.servo_1 = 0
                self.angles.servo_2 = 0
                self.angles.servo_3 = 90
                self.angles.servo_4 = 0

            # Keyboard control for drive motors
            if keys[pygame.K_j]: self.update_motor_keyboard(0, 5)   # Increase speed of motor 1
            if keys[pygame.K_n]: self.update_motor_keyboard(0, -5)  # Decrease speed of motor 1
            if keys[pygame.K_k]: self.update_motor_keyboard(1, 5)   # Increase speed of motor 2
            if keys[pygame.K_m]: self.update_motor_keyboard(1, -5)  # Decrease speed of motor 2
            if keys[pygame.K_SPACE]:  # Stop all motors
                self.motor.m_1 = 0
                self.motor.m_2 = 0
            if keys[pygame.K_SLASH]:  # Toggle light
                self.LIGHT = not self.LIGHT
                rospy.sleep(0.25)

            ### Joystick control ###
            if len(self.joysticks) > 0:
                ACTIVATE_SECOND_JOYSTICK = True
                hat_control = self.joysticks[0].get_hat(0)

                ## Press Logitech button to switch between manual servo and inverse kinematic ##
                if self.joysticks[0].get_button(8):
                    self.INVERSE_KINEMATIC = not self.INVERSE_KINEMATIC
                    rospy.sleep(0.25)

                if self.INVERSE_KINEMATIC:
                    # Calculate current_x current_y from forward kinematic of self.angle.servo_1, self.angle.servo_2
                    ## Confirmed correct
                    pos_x1 = -8 * m.cos(m.radians(self.angles.servo_1))
                    pos_y1 = 8 * m.sin(m.radians(self.angles.servo_1))
                    pos_x2 = pos_x1 + 13 * m.cos(m.radians(self.angles.servo_2 - self.angles.servo_1))
                    pos_y2 = pos_y1 + 13 * m.sin(m.radians(self.angles.servo_2 - self.angles.servo_1))
                    # rospy.loginfo(f"servo_1: {self.angles.servo_1}")
                    # rospy.loginfo(f"servo_2: {self.angles.servo_2}")
                    # rospy.loginfo(f"pos_x1: {pos_x1}")
                    # rospy.loginfo(f"pos_y1: {pos_y1}")
                    rospy.loginfo(f"pos_x2: {pos_x2}")
                    rospy.loginfo(f"pos_y2: {pos_y2}")
                    
                    # set the current position from forward kinematic
                    current_x = pos_x2
                    current_y = pos_y2

                    # servo_x, servo_y will nudge the value of the current position
                    servo_x = self.joysticks[0].get_axis(1)
                    servo_y = self.joysticks[0].get_axis(4)
                    
                    # nudge the pos_x and pos_y with inverse kinematic (Position: float)
                    new_x = current_x + int(servo_x * -2)
                    new_y = current_y + int(servo_y * -2)
                    # rospy.logwarn(f"current_x: {current_x}")
                    # rospy.logwarn(f"current_y: {current_y}")
                    rospy.logwarn(f"sum: {m.sqrt(new_x**2 + new_y**2)}")
                    # rospy.logfatal(f"new_x: {new_x}")
                    # rospy.logfatal(f"new_y: {new_y}")
                    # check if sqrt(pos_x**2 + pos_y**2) > 8+13 if yes return current angle
                    if m.sqrt(new_x**2 + new_y**2) <= 21:
                        try:
                            A0 = int(m.degrees(m.atan2(new_y, new_x) + m.acos((64 + (new_x**2 + new_y**2) - 169) / (16 * m.sqrt(new_x**2 + new_y**2)))))
                            B0 = int(m.degrees(m.acos((64 + 169 - (new_x**2 + new_y**2)) / 208)))
                            
                            new_angle_1 = 180 - A0
                            new_angle_2 = B0
                            if (0 <= new_angle_1 <= 180 and 0 <= new_angle_2 <= 270):
                                rospy.loginfo(f"A0: {A0}")
                                rospy.loginfo(f"B0: {B0}")
                                setattr(self.angles, 'servo_1', new_angle_1)
                                setattr(self.angles, 'servo_2', new_angle_2)
                            else:
                                rospy.logwarn(f"over limit range: \nnew_angle_1 {new_angle_1}\nnew_angle_2 {new_angle_2}")
                                setattr(self.angles, f'servo_1', self.angles.servo_1)
                                setattr(self.angles, f'servo_2', self.angles.servo_2)
                        except (ValueError):
                            rospy.logwarn(ValueError)
                            setattr(self.angles, f'servo_1', self.angles.servo_1)
                            setattr(self.angles, f'servo_2', self.angles.servo_2)
                    else:
                        rospy.logwarn(f"over area limit: {m.sqrt(new_x**2 + new_y**2)}")
                        setattr(self.angles, f'servo_1', self.angles.servo_1)
                        setattr(self.angles, f'servo_2', self.angles.servo_2)
                        # Not sure if current angle/current_x-y remain the same? But likely yes
                else:
                    # First joystick controls servos
                    servo_1 = self.joysticks[0].get_axis(1)
                    servo_2 = self.joysticks[0].get_axis(4)
                    if abs(servo_1) > 0.1:
                        self.update_angle(0, int(servo_1 * -5))
                    if abs(servo_2) > 0.1:
                        self.update_angle(1, int(servo_2 * -5))
                
                ## Common Joystick control ##
                servo_3_down = self.joysticks[0].get_axis(2)
                servo_3_up = self.joysticks[0].get_axis(5)
                servo_4_down = self.joysticks[0].get_button(4)
                servo_4_up = self.joysticks[0].get_button(5)
                if servo_3_down > 0.1:
                    self.update_angle(2, int(-servo_3_down * 5))
                if servo_3_up > 0.1:
                    self.update_angle(2, int(servo_3_up * 5))
                if servo_4_down:
                    self.update_angle(3, -5)
                if servo_4_up:
                    self.update_angle(3, 5)

                # Joystick control for Servo preset
                if self.joysticks[0].get_button(2): # X: HOME
                    self.angles.servo_1 = 0
                    self.angles.servo_2 = 0
                    self.angles.servo_3 = 90
                    # keep the same gripper (servo_4) position
                if self.joysticks[0].get_button(1): # B: Middle
                    self.angles.servo_1 = 45
                    self.angles.servo_2 = 60
                    self.angles.servo_3 = 50
                    # keep the same gripper (servo_4) position
                if self.joysticks[0].get_button(7) or self.joysticks[1].get_button(7):  # Toggle light
                    self.LIGHT = not self.LIGHT
                    rospy.sleep(0.25)
                
                # D-pad (Hat) control for driving control in servo's joystick
                if (hat_control == (1,0)):  # right hat
                    rospy.logfatal("RIGHT")
                    ACTIVATE_SECOND_JOYSTICK = False
                    self.update_motor(0, 0.355)
                    self.update_motor(1, -0.355)
                    self.motor_pub.publish(self.motor)
                elif (hat_control == (-1,0)):  # left hat
                    rospy.logfatal("LEFT")
                    ACTIVATE_SECOND_JOYSTICK = False
                    self.update_motor(0, -0.355)
                    self.update_motor(1, 0.355)
                    self.motor_pub.publish(self.motor)
                elif (hat_control == (0,1)):  # up hat
                    rospy.logfatal("UP")
                    ACTIVATE_SECOND_JOYSTICK = False
                    self.update_motor(0, 0.355)
                    self.update_motor(1, 0.355)
                    self.motor_pub.publish(self.motor)
                elif (hat_control == (0,-1)):  # down hat
                    rospy.logfatal("DOWN")
                    ACTIVATE_SECOND_JOYSTICK = False
                    self.update_motor(0, -0.355)
                    self.update_motor(1, -0.355)
                    self.motor_pub.publish(self.motor)
                elif (hat_control == (0,0)):
                    ACTIVATE_SECOND_JOYSTICK = True
                # rospy.logfatal(f"ACTIVATE_SECOND_JOYSTICK: {ACTIVATE_SECOND_JOYSTICK}")
                
                # Joystick control for drive with second joystick
                if (len(self.joysticks) > 1 and ACTIVATE_SECOND_JOYSTICK == True):
                    # Second joystick controls drive motors
                    left_motor = self.joysticks[1].get_axis(1)  # Left stick Y-axis
                    right_motor = self.joysticks[1].get_axis(4)  # Right stick Y-axis
                    # rospy.logwarn(f"left_motor: {round(left_motor,4)}")
                    # rospy.logwarn(f"right_motor: {round(right_motor,4)}")
                    self.update_motor(0, left_motor * -1)
                    self.update_motor(1, right_motor * -1)
                elif (len(self.joysticks) == 1 and ACTIVATE_SECOND_JOYSTICK == True):
                    self.update_motor(0, 0)
                    self.update_motor(1, 0)
                if len(self.joysticks) > 1:
                    # Small increment movement with second joystick
                    if self.joysticks[1].get_button(3): # Y: UP
                        self.update_motor(0, 0.355)
                        self.update_motor(1, 0.355)
                        self.motor_pub.publish(self.motor)
                    if self.joysticks[1].get_button(0): # A: DOWN
                        self.update_motor(0, -0.355)
                        self.update_motor(1, -0.355)
                        self.motor_pub.publish(self.motor)
                    if self.joysticks[1].get_button(2): # X: LEFT
                        self.update_motor(0, -0.355)
                        self.update_motor(1, 0.355)
                        self.motor_pub.publish(self.motor)
                    if self.joysticks[1].get_button(1): # B: RIGHT
                        self.update_motor(0, 0.355)
                        self.update_motor(1, -0.355)
                        self.motor_pub.publish(self.motor)
            
            if self.LIGHT:
                self.light_pub.publish(True)
            else:
                self.light_pub.publish(False)

            # Publish servo angles and motor values
            rospy.loginfo(f"Servos: {self.angles}")
            rospy.loginfo(f"Motors: {self.motor}")
            self.servo_pub.publish(self.angles)
            self.motor_pub.publish(self.motor)
            self.rate.sleep()
            font = pygame.font.Font(None, Font)
            text = font.render(f"Inverse Kinematic: {self.INVERSE_KINEMATIC}", True, textColor)
            screen.blit(text, (10, 10))
            for i in range(4):
                text = font.render(f"Servo {i+1}: {getattr(self.angles, f'servo_{i+1}')}", True, textColor)
                screen.blit(text, (10, 45 + i * 30))
            for i in range(2):
                text = font.render(f"Motor {i+1}: {getattr(self.motor, f'm_{i+1}')}", True, textColor)
                screen.blit(text, (10, 175 + i * 30))
                text = font.render(f"LIGHT: {self.LIGHT}", True, textColor)
                screen.blit(text, (10, 245))

            
    def main(self):
        # Set up a window for keyboard events
        self.screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Robot Controller")
        while not rospy.is_shutdown():
            self.screen.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            self.run(self.screen)
            # Update display
            pygame.display.flip()

if __name__ == '__main__':
    try:
        rospy.loginfo("[START] robot_controller has been started")
        controller = RobotController()
        controller.main()
    except rospy.ROSInterruptException:
        pass
    finally:
        pygame.quit 