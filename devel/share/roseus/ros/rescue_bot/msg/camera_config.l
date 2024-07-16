;; Auto-generated. Do not edit!


(when (boundp 'rescue_bot::camera_config)
  (if (not (find-package "RESCUE_BOT"))
    (make-package "RESCUE_BOT"))
  (shadow 'camera_config (find-package "RESCUE_BOT")))
(unless (find-package "RESCUE_BOT::CAMERA_CONFIG")
  (make-package "RESCUE_BOT::CAMERA_CONFIG"))

(in-package "ROS")
;;//! \htmlinclude camera_config.msg.html


(defclass rescue_bot::camera_config
  :super ros::object
  :slots (_scale _fram_rate _color_set ))

(defmethod rescue_bot::camera_config
  (:init
   (&key
    ((:scale __scale) 0)
    ((:fram_rate __fram_rate) 0)
    ((:color_set __color_set) nil)
    )
   (send-super :init)
   (setq _scale (round __scale))
   (setq _fram_rate (round __fram_rate))
   (setq _color_set __color_set)
   self)
  (:scale
   (&optional __scale)
   (if __scale (setq _scale __scale)) _scale)
  (:fram_rate
   (&optional __fram_rate)
   (if __fram_rate (setq _fram_rate __fram_rate)) _fram_rate)
  (:color_set
   (&optional (__color_set :null))
   (if (not (eq __color_set :null)) (setq _color_set __color_set)) _color_set)
  (:serialization-length
   ()
   (+
    ;; int16 _scale
    2
    ;; int16 _fram_rate
    2
    ;; bool _color_set
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _scale
       (write-word _scale s)
     ;; int16 _fram_rate
       (write-word _fram_rate s)
     ;; bool _color_set
       (if _color_set (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _scale
     (setq _scale (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _fram_rate
     (setq _fram_rate (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; bool _color_set
     (setq _color_set (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get rescue_bot::camera_config :md5sum-) "d706ca6804416e58885c51a33d760341")
(setf (get rescue_bot::camera_config :datatype-) "rescue_bot/camera_config")
(setf (get rescue_bot::camera_config :definition-)
      "int16 scale
int16 fram_rate
bool color_set
")



(provide :rescue_bot/camera_config "d706ca6804416e58885c51a33d760341")


