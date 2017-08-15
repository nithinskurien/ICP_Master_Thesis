; Auto-generated. Do not edit!


(cl:in-package robotclient-srv)


;//! \htmlinclude UpdateTwist-request.msg.html

(cl:defclass <UpdateTwist-request> (roslisp-msg-protocol:ros-message)
  ((data
    :reader data
    :initarg :data
    :type robotclient-msg:Floats
    :initform (cl:make-instance 'robotclient-msg:Floats)))
)

(cl:defclass UpdateTwist-request (<UpdateTwist-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <UpdateTwist-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'UpdateTwist-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robotclient-srv:<UpdateTwist-request> is deprecated: use robotclient-srv:UpdateTwist-request instead.")))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <UpdateTwist-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotclient-srv:data-val is deprecated.  Use robotclient-srv:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <UpdateTwist-request>) ostream)
  "Serializes a message object of type '<UpdateTwist-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'data) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <UpdateTwist-request>) istream)
  "Deserializes a message object of type '<UpdateTwist-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'data) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<UpdateTwist-request>)))
  "Returns string type for a service object of type '<UpdateTwist-request>"
  "robotclient/UpdateTwistRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'UpdateTwist-request)))
  "Returns string type for a service object of type 'UpdateTwist-request"
  "robotclient/UpdateTwistRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<UpdateTwist-request>)))
  "Returns md5sum for a message object of type '<UpdateTwist-request>"
  "9b8578b5371575f7e032469638abea73")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'UpdateTwist-request)))
  "Returns md5sum for a message object of type 'UpdateTwist-request"
  "9b8578b5371575f7e032469638abea73")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<UpdateTwist-request>)))
  "Returns full string definition for message of type '<UpdateTwist-request>"
  (cl:format cl:nil "Floats data~%~%================================================================================~%MSG: robotclient/Floats~%float32[] data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'UpdateTwist-request)))
  "Returns full string definition for message of type 'UpdateTwist-request"
  (cl:format cl:nil "Floats data~%~%================================================================================~%MSG: robotclient/Floats~%float32[] data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <UpdateTwist-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'data))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <UpdateTwist-request>))
  "Converts a ROS message object to a list"
  (cl:list 'UpdateTwist-request
    (cl:cons ':data (data msg))
))
;//! \htmlinclude UpdateTwist-response.msg.html

(cl:defclass <UpdateTwist-response> (roslisp-msg-protocol:ros-message)
  ((ack
    :reader ack
    :initarg :ack
    :type cl:fixnum
    :initform 0))
)

(cl:defclass UpdateTwist-response (<UpdateTwist-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <UpdateTwist-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'UpdateTwist-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robotclient-srv:<UpdateTwist-response> is deprecated: use robotclient-srv:UpdateTwist-response instead.")))

(cl:ensure-generic-function 'ack-val :lambda-list '(m))
(cl:defmethod ack-val ((m <UpdateTwist-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robotclient-srv:ack-val is deprecated.  Use robotclient-srv:ack instead.")
  (ack m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <UpdateTwist-response>) ostream)
  "Serializes a message object of type '<UpdateTwist-response>"
  (cl:let* ((signed (cl:slot-value msg 'ack)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <UpdateTwist-response>) istream)
  "Deserializes a message object of type '<UpdateTwist-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ack) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<UpdateTwist-response>)))
  "Returns string type for a service object of type '<UpdateTwist-response>"
  "robotclient/UpdateTwistResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'UpdateTwist-response)))
  "Returns string type for a service object of type 'UpdateTwist-response"
  "robotclient/UpdateTwistResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<UpdateTwist-response>)))
  "Returns md5sum for a message object of type '<UpdateTwist-response>"
  "9b8578b5371575f7e032469638abea73")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'UpdateTwist-response)))
  "Returns md5sum for a message object of type 'UpdateTwist-response"
  "9b8578b5371575f7e032469638abea73")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<UpdateTwist-response>)))
  "Returns full string definition for message of type '<UpdateTwist-response>"
  (cl:format cl:nil "int8 ack~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'UpdateTwist-response)))
  "Returns full string definition for message of type 'UpdateTwist-response"
  (cl:format cl:nil "int8 ack~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <UpdateTwist-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <UpdateTwist-response>))
  "Converts a ROS message object to a list"
  (cl:list 'UpdateTwist-response
    (cl:cons ':ack (ack msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'UpdateTwist)))
  'UpdateTwist-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'UpdateTwist)))
  'UpdateTwist-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'UpdateTwist)))
  "Returns string type for a service object of type '<UpdateTwist>"
  "robotclient/UpdateTwist")