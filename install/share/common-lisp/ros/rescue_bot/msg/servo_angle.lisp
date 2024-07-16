; Auto-generated. Do not edit!


(cl:in-package rescue_bot-msg)


;//! \htmlinclude servo_angle.msg.html

(cl:defclass <servo_angle> (roslisp-msg-protocol:ros-message)
  ((servo_1
    :reader servo_1
    :initarg :servo_1
    :type cl:fixnum
    :initform 0)
   (servo_2
    :reader servo_2
    :initarg :servo_2
    :type cl:fixnum
    :initform 0)
   (servo_3
    :reader servo_3
    :initarg :servo_3
    :type cl:fixnum
    :initform 0)
   (servo_4
    :reader servo_4
    :initarg :servo_4
    :type cl:fixnum
    :initform 0))
)

(cl:defclass servo_angle (<servo_angle>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <servo_angle>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'servo_angle)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name rescue_bot-msg:<servo_angle> is deprecated: use rescue_bot-msg:servo_angle instead.")))

(cl:ensure-generic-function 'servo_1-val :lambda-list '(m))
(cl:defmethod servo_1-val ((m <servo_angle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rescue_bot-msg:servo_1-val is deprecated.  Use rescue_bot-msg:servo_1 instead.")
  (servo_1 m))

(cl:ensure-generic-function 'servo_2-val :lambda-list '(m))
(cl:defmethod servo_2-val ((m <servo_angle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rescue_bot-msg:servo_2-val is deprecated.  Use rescue_bot-msg:servo_2 instead.")
  (servo_2 m))

(cl:ensure-generic-function 'servo_3-val :lambda-list '(m))
(cl:defmethod servo_3-val ((m <servo_angle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rescue_bot-msg:servo_3-val is deprecated.  Use rescue_bot-msg:servo_3 instead.")
  (servo_3 m))

(cl:ensure-generic-function 'servo_4-val :lambda-list '(m))
(cl:defmethod servo_4-val ((m <servo_angle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rescue_bot-msg:servo_4-val is deprecated.  Use rescue_bot-msg:servo_4 instead.")
  (servo_4 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <servo_angle>) ostream)
  "Serializes a message object of type '<servo_angle>"
  (cl:let* ((signed (cl:slot-value msg 'servo_1)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'servo_2)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'servo_3)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'servo_4)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <servo_angle>) istream)
  "Deserializes a message object of type '<servo_angle>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'servo_1) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'servo_2) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'servo_3) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'servo_4) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<servo_angle>)))
  "Returns string type for a message object of type '<servo_angle>"
  "rescue_bot/servo_angle")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'servo_angle)))
  "Returns string type for a message object of type 'servo_angle"
  "rescue_bot/servo_angle")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<servo_angle>)))
  "Returns md5sum for a message object of type '<servo_angle>"
  "15c6708a289bad19b3aa103b1ef56bbc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'servo_angle)))
  "Returns md5sum for a message object of type 'servo_angle"
  "15c6708a289bad19b3aa103b1ef56bbc")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<servo_angle>)))
  "Returns full string definition for message of type '<servo_angle>"
  (cl:format cl:nil "int16 servo_1~%int16 servo_2~%int16 servo_3~%int16 servo_4~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'servo_angle)))
  "Returns full string definition for message of type 'servo_angle"
  (cl:format cl:nil "int16 servo_1~%int16 servo_2~%int16 servo_3~%int16 servo_4~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <servo_angle>))
  (cl:+ 0
     2
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <servo_angle>))
  "Converts a ROS message object to a list"
  (cl:list 'servo_angle
    (cl:cons ':servo_1 (servo_1 msg))
    (cl:cons ':servo_2 (servo_2 msg))
    (cl:cons ':servo_3 (servo_3 msg))
    (cl:cons ':servo_4 (servo_4 msg))
))
