;; Auto-generated. Do not edit!


(when (boundp 'rescue_bot::servo_angle)
  (if (not (find-package "RESCUE_BOT"))
    (make-package "RESCUE_BOT"))
  (shadow 'servo_angle (find-package "RESCUE_BOT")))
(unless (find-package "RESCUE_BOT::SERVO_ANGLE")
  (make-package "RESCUE_BOT::SERVO_ANGLE"))

(in-package "ROS")
;;//! \htmlinclude servo_angle.msg.html


(defclass rescue_bot::servo_angle
  :super ros::object
  :slots (_servo_1 _servo_2 _servo_3 _servo_4 ))

(defmethod rescue_bot::servo_angle
  (:init
   (&key
    ((:servo_1 __servo_1) 0)
    ((:servo_2 __servo_2) 0)
    ((:servo_3 __servo_3) 0)
    ((:servo_4 __servo_4) 0)
    )
   (send-super :init)
   (setq _servo_1 (round __servo_1))
   (setq _servo_2 (round __servo_2))
   (setq _servo_3 (round __servo_3))
   (setq _servo_4 (round __servo_4))
   self)
  (:servo_1
   (&optional __servo_1)
   (if __servo_1 (setq _servo_1 __servo_1)) _servo_1)
  (:servo_2
   (&optional __servo_2)
   (if __servo_2 (setq _servo_2 __servo_2)) _servo_2)
  (:servo_3
   (&optional __servo_3)
   (if __servo_3 (setq _servo_3 __servo_3)) _servo_3)
  (:servo_4
   (&optional __servo_4)
   (if __servo_4 (setq _servo_4 __servo_4)) _servo_4)
  (:serialization-length
   ()
   (+
    ;; int16 _servo_1
    2
    ;; int16 _servo_2
    2
    ;; int16 _servo_3
    2
    ;; int16 _servo_4
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _servo_1
       (write-word _servo_1 s)
     ;; int16 _servo_2
       (write-word _servo_2 s)
     ;; int16 _servo_3
       (write-word _servo_3 s)
     ;; int16 _servo_4
       (write-word _servo_4 s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _servo_1
     (setq _servo_1 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _servo_2
     (setq _servo_2 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _servo_3
     (setq _servo_3 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _servo_4
     (setq _servo_4 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get rescue_bot::servo_angle :md5sum-) "15c6708a289bad19b3aa103b1ef56bbc")
(setf (get rescue_bot::servo_angle :datatype-) "rescue_bot/servo_angle")
(setf (get rescue_bot::servo_angle :definition-)
      "int16 servo_1
int16 servo_2
int16 servo_3
int16 servo_4
")



(provide :rescue_bot/servo_angle "15c6708a289bad19b3aa103b1ef56bbc")


