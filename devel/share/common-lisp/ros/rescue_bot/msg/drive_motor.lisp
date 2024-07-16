; Auto-generated. Do not edit!


(cl:in-package rescue_bot-msg)


;//! \htmlinclude drive_motor.msg.html

(cl:defclass <drive_motor> (roslisp-msg-protocol:ros-message)
  ((m_1
    :reader m_1
    :initarg :m_1
    :type cl:fixnum
    :initform 0)
   (m_2
    :reader m_2
    :initarg :m_2
    :type cl:fixnum
    :initform 0))
)

(cl:defclass drive_motor (<drive_motor>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <drive_motor>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'drive_motor)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name rescue_bot-msg:<drive_motor> is deprecated: use rescue_bot-msg:drive_motor instead.")))

(cl:ensure-generic-function 'm_1-val :lambda-list '(m))
(cl:defmethod m_1-val ((m <drive_motor>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rescue_bot-msg:m_1-val is deprecated.  Use rescue_bot-msg:m_1 instead.")
  (m_1 m))

(cl:ensure-generic-function 'm_2-val :lambda-list '(m))
(cl:defmethod m_2-val ((m <drive_motor>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rescue_bot-msg:m_2-val is deprecated.  Use rescue_bot-msg:m_2 instead.")
  (m_2 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <drive_motor>) ostream)
  "Serializes a message object of type '<drive_motor>"
  (cl:let* ((signed (cl:slot-value msg 'm_1)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'm_2)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <drive_motor>) istream)
  "Deserializes a message object of type '<drive_motor>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'm_1) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'm_2) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<drive_motor>)))
  "Returns string type for a message object of type '<drive_motor>"
  "rescue_bot/drive_motor")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'drive_motor)))
  "Returns string type for a message object of type 'drive_motor"
  "rescue_bot/drive_motor")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<drive_motor>)))
  "Returns md5sum for a message object of type '<drive_motor>"
  "0a3cf26992116e8869f3387fe00a35d8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'drive_motor)))
  "Returns md5sum for a message object of type 'drive_motor"
  "0a3cf26992116e8869f3387fe00a35d8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<drive_motor>)))
  "Returns full string definition for message of type '<drive_motor>"
  (cl:format cl:nil "int16 m_1~%int16 m_2~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'drive_motor)))
  "Returns full string definition for message of type 'drive_motor"
  (cl:format cl:nil "int16 m_1~%int16 m_2~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <drive_motor>))
  (cl:+ 0
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <drive_motor>))
  "Converts a ROS message object to a list"
  (cl:list 'drive_motor
    (cl:cons ':m_1 (m_1 msg))
    (cl:cons ':m_2 (m_2 msg))
))
