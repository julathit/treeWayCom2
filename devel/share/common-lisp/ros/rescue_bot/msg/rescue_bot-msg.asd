
(cl:in-package :asdf)

(defsystem "rescue_bot-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "camera_config" :depends-on ("_package_camera_config"))
    (:file "_package_camera_config" :depends-on ("_package"))
    (:file "drive_motor" :depends-on ("_package_drive_motor"))
    (:file "_package_drive_motor" :depends-on ("_package"))
    (:file "servo_angle" :depends-on ("_package_servo_angle"))
    (:file "_package_servo_angle" :depends-on ("_package"))
  ))