; Auto-generated. Do not edit!


(cl:in-package rescue_bot-msg)


;//! \htmlinclude camera_config.msg.html

(cl:defclass <camera_config> (roslisp-msg-protocol:ros-message)
  ((scale
    :reader scale
    :initarg :scale
    :type cl:fixnum
    :initform 0)
   (fram_rate
    :reader fram_rate
    :initarg :fram_rate
    :type cl:fixnum
    :initform 0)
   (color_set
    :reader color_set
    :initarg :color_set
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass camera_config (<camera_config>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <camera_config>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'camera_config)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name rescue_bot-msg:<camera_config> is deprecated: use rescue_bot-msg:camera_config instead.")))

(cl:ensure-generic-function 'scale-val :lambda-list '(m))
(cl:defmethod scale-val ((m <camera_config>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rescue_bot-msg:scale-val is deprecated.  Use rescue_bot-msg:scale instead.")
  (scale m))

(cl:ensure-generic-function 'fram_rate-val :lambda-list '(m))
(cl:defmethod fram_rate-val ((m <camera_config>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rescue_bot-msg:fram_rate-val is deprecated.  Use rescue_bot-msg:fram_rate instead.")
  (fram_rate m))

(cl:ensure-generic-function 'color_set-val :lambda-list '(m))
(cl:defmethod color_set-val ((m <camera_config>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rescue_bot-msg:color_set-val is deprecated.  Use rescue_bot-msg:color_set instead.")
  (color_set m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <camera_config>) ostream)
  "Serializes a message object of type '<camera_config>"
  (cl:let* ((signed (cl:slot-value msg 'scale)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'fram_rate)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'color_set) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <camera_config>) istream)
  "Deserializes a message object of type '<camera_config>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'scale) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'fram_rate) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:setf (cl:slot-value msg 'color_set) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<camera_config>)))
  "Returns string type for a message object of type '<camera_config>"
  "rescue_bot/camera_config")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'camera_config)))
  "Returns string type for a message object of type 'camera_config"
  "rescue_bot/camera_config")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<camera_config>)))
  "Returns md5sum for a message object of type '<camera_config>"
  "d706ca6804416e58885c51a33d760341")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'camera_config)))
  "Returns md5sum for a message object of type 'camera_config"
  "d706ca6804416e58885c51a33d760341")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<camera_config>)))
  "Returns full string definition for message of type '<camera_config>"
  (cl:format cl:nil "int16 scale~%int16 fram_rate~%bool color_set~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'camera_config)))
  "Returns full string definition for message of type 'camera_config"
  (cl:format cl:nil "int16 scale~%int16 fram_rate~%bool color_set~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <camera_config>))
  (cl:+ 0
     2
     2
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <camera_config>))
  "Converts a ROS message object to a list"
  (cl:list 'camera_config
    (cl:cons ':scale (scale msg))
    (cl:cons ':fram_rate (fram_rate msg))
    (cl:cons ':color_set (color_set msg))
))
