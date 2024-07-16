;; Auto-generated. Do not edit!


(when (boundp 'rescue_bot::drive_motor)
  (if (not (find-package "RESCUE_BOT"))
    (make-package "RESCUE_BOT"))
  (shadow 'drive_motor (find-package "RESCUE_BOT")))
(unless (find-package "RESCUE_BOT::DRIVE_MOTOR")
  (make-package "RESCUE_BOT::DRIVE_MOTOR"))

(in-package "ROS")
;;//! \htmlinclude drive_motor.msg.html


(defclass rescue_bot::drive_motor
  :super ros::object
  :slots (_m_1 _m_2 ))

(defmethod rescue_bot::drive_motor
  (:init
   (&key
    ((:m_1 __m_1) 0)
    ((:m_2 __m_2) 0)
    )
   (send-super :init)
   (setq _m_1 (round __m_1))
   (setq _m_2 (round __m_2))
   self)
  (:m_1
   (&optional __m_1)
   (if __m_1 (setq _m_1 __m_1)) _m_1)
  (:m_2
   (&optional __m_2)
   (if __m_2 (setq _m_2 __m_2)) _m_2)
  (:serialization-length
   ()
   (+
    ;; int16 _m_1
    2
    ;; int16 _m_2
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _m_1
       (write-word _m_1 s)
     ;; int16 _m_2
       (write-word _m_2 s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _m_1
     (setq _m_1 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _m_2
     (setq _m_2 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get rescue_bot::drive_motor :md5sum-) "0a3cf26992116e8869f3387fe00a35d8")
(setf (get rescue_bot::drive_motor :datatype-) "rescue_bot/drive_motor")
(setf (get rescue_bot::drive_motor :definition-)
      "int16 m_1
int16 m_2
")



(provide :rescue_bot/drive_motor "0a3cf26992116e8869f3387fe00a35d8")


