; Auto-generated. Do not edit!


(cl:in-package masterclient-srv)


;//! \htmlinclude BaseEndGetCoord-request.msg.html

(cl:defclass <BaseEndGetCoord-request> (roslisp-msg-protocol:ros-message)
  ((data
    :reader data
    :initarg :data
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass BaseEndGetCoord-request (<BaseEndGetCoord-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BaseEndGetCoord-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BaseEndGetCoord-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name masterclient-srv:<BaseEndGetCoord-request> is deprecated: use masterclient-srv:BaseEndGetCoord-request instead.")))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <BaseEndGetCoord-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader masterclient-srv:data-val is deprecated.  Use masterclient-srv:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BaseEndGetCoord-request>) ostream)
  "Serializes a message object of type '<BaseEndGetCoord-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BaseEndGetCoord-request>) istream)
  "Deserializes a message object of type '<BaseEndGetCoord-request>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'data) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'data)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BaseEndGetCoord-request>)))
  "Returns string type for a service object of type '<BaseEndGetCoord-request>"
  "masterclient/BaseEndGetCoordRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BaseEndGetCoord-request)))
  "Returns string type for a service object of type 'BaseEndGetCoord-request"
  "masterclient/BaseEndGetCoordRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BaseEndGetCoord-request>)))
  "Returns md5sum for a message object of type '<BaseEndGetCoord-request>"
  "b6fb5bf1382e6a4ebdbf5eee1e4c5505")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BaseEndGetCoord-request)))
  "Returns md5sum for a message object of type 'BaseEndGetCoord-request"
  "b6fb5bf1382e6a4ebdbf5eee1e4c5505")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BaseEndGetCoord-request>)))
  "Returns full string definition for message of type '<BaseEndGetCoord-request>"
  (cl:format cl:nil "float32[] data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BaseEndGetCoord-request)))
  "Returns full string definition for message of type 'BaseEndGetCoord-request"
  (cl:format cl:nil "float32[] data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BaseEndGetCoord-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'data) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BaseEndGetCoord-request>))
  "Converts a ROS message object to a list"
  (cl:list 'BaseEndGetCoord-request
    (cl:cons ':data (data msg))
))
;//! \htmlinclude BaseEndGetCoord-response.msg.html

(cl:defclass <BaseEndGetCoord-response> (roslisp-msg-protocol:ros-message)
  ((in
    :reader in
    :initarg :in
    :type cl:fixnum
    :initform 0))
)

(cl:defclass BaseEndGetCoord-response (<BaseEndGetCoord-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BaseEndGetCoord-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BaseEndGetCoord-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name masterclient-srv:<BaseEndGetCoord-response> is deprecated: use masterclient-srv:BaseEndGetCoord-response instead.")))

(cl:ensure-generic-function 'in-val :lambda-list '(m))
(cl:defmethod in-val ((m <BaseEndGetCoord-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader masterclient-srv:in-val is deprecated.  Use masterclient-srv:in instead.")
  (in m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BaseEndGetCoord-response>) ostream)
  "Serializes a message object of type '<BaseEndGetCoord-response>"
  (cl:let* ((signed (cl:slot-value msg 'in)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BaseEndGetCoord-response>) istream)
  "Deserializes a message object of type '<BaseEndGetCoord-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'in) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BaseEndGetCoord-response>)))
  "Returns string type for a service object of type '<BaseEndGetCoord-response>"
  "masterclient/BaseEndGetCoordResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BaseEndGetCoord-response)))
  "Returns string type for a service object of type 'BaseEndGetCoord-response"
  "masterclient/BaseEndGetCoordResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BaseEndGetCoord-response>)))
  "Returns md5sum for a message object of type '<BaseEndGetCoord-response>"
  "b6fb5bf1382e6a4ebdbf5eee1e4c5505")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BaseEndGetCoord-response)))
  "Returns md5sum for a message object of type 'BaseEndGetCoord-response"
  "b6fb5bf1382e6a4ebdbf5eee1e4c5505")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BaseEndGetCoord-response>)))
  "Returns full string definition for message of type '<BaseEndGetCoord-response>"
  (cl:format cl:nil "int8 in~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BaseEndGetCoord-response)))
  "Returns full string definition for message of type 'BaseEndGetCoord-response"
  (cl:format cl:nil "int8 in~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BaseEndGetCoord-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BaseEndGetCoord-response>))
  "Converts a ROS message object to a list"
  (cl:list 'BaseEndGetCoord-response
    (cl:cons ':in (in msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'BaseEndGetCoord)))
  'BaseEndGetCoord-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'BaseEndGetCoord)))
  'BaseEndGetCoord-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BaseEndGetCoord)))
  "Returns string type for a service object of type '<BaseEndGetCoord>"
  "masterclient/BaseEndGetCoord")