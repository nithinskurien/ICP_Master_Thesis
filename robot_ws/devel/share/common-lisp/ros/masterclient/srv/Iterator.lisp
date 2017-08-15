; Auto-generated. Do not edit!


(cl:in-package masterclient-srv)


;//! \htmlinclude Iterator-request.msg.html

(cl:defclass <Iterator-request> (roslisp-msg-protocol:ros-message)
  ((data
    :reader data
    :initarg :data
    :type std_msgs-msg:String
    :initform (cl:make-instance 'std_msgs-msg:String)))
)

(cl:defclass Iterator-request (<Iterator-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Iterator-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Iterator-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name masterclient-srv:<Iterator-request> is deprecated: use masterclient-srv:Iterator-request instead.")))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <Iterator-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader masterclient-srv:data-val is deprecated.  Use masterclient-srv:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Iterator-request>) ostream)
  "Serializes a message object of type '<Iterator-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'data) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Iterator-request>) istream)
  "Deserializes a message object of type '<Iterator-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'data) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Iterator-request>)))
  "Returns string type for a service object of type '<Iterator-request>"
  "masterclient/IteratorRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Iterator-request)))
  "Returns string type for a service object of type 'Iterator-request"
  "masterclient/IteratorRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Iterator-request>)))
  "Returns md5sum for a message object of type '<Iterator-request>"
  "8869b2ff5bcea599c212b1e75b68818b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Iterator-request)))
  "Returns md5sum for a message object of type 'Iterator-request"
  "8869b2ff5bcea599c212b1e75b68818b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Iterator-request>)))
  "Returns full string definition for message of type '<Iterator-request>"
  (cl:format cl:nil "std_msgs/String data~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Iterator-request)))
  "Returns full string definition for message of type 'Iterator-request"
  (cl:format cl:nil "std_msgs/String data~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Iterator-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'data))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Iterator-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Iterator-request
    (cl:cons ':data (data msg))
))
;//! \htmlinclude Iterator-response.msg.html

(cl:defclass <Iterator-response> (roslisp-msg-protocol:ros-message)
  ((ack
    :reader ack
    :initarg :ack
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Iterator-response (<Iterator-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Iterator-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Iterator-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name masterclient-srv:<Iterator-response> is deprecated: use masterclient-srv:Iterator-response instead.")))

(cl:ensure-generic-function 'ack-val :lambda-list '(m))
(cl:defmethod ack-val ((m <Iterator-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader masterclient-srv:ack-val is deprecated.  Use masterclient-srv:ack instead.")
  (ack m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Iterator-response>) ostream)
  "Serializes a message object of type '<Iterator-response>"
  (cl:let* ((signed (cl:slot-value msg 'ack)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Iterator-response>) istream)
  "Deserializes a message object of type '<Iterator-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ack) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Iterator-response>)))
  "Returns string type for a service object of type '<Iterator-response>"
  "masterclient/IteratorResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Iterator-response)))
  "Returns string type for a service object of type 'Iterator-response"
  "masterclient/IteratorResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Iterator-response>)))
  "Returns md5sum for a message object of type '<Iterator-response>"
  "8869b2ff5bcea599c212b1e75b68818b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Iterator-response)))
  "Returns md5sum for a message object of type 'Iterator-response"
  "8869b2ff5bcea599c212b1e75b68818b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Iterator-response>)))
  "Returns full string definition for message of type '<Iterator-response>"
  (cl:format cl:nil "int8 ack~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Iterator-response)))
  "Returns full string definition for message of type 'Iterator-response"
  (cl:format cl:nil "int8 ack~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Iterator-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Iterator-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Iterator-response
    (cl:cons ':ack (ack msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Iterator)))
  'Iterator-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Iterator)))
  'Iterator-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Iterator)))
  "Returns string type for a service object of type '<Iterator>"
  "masterclient/Iterator")