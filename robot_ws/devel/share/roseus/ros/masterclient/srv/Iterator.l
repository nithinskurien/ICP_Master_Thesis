;; Auto-generated. Do not edit!


(when (boundp 'masterclient::Iterator)
  (if (not (find-package "MASTERCLIENT"))
    (make-package "MASTERCLIENT"))
  (shadow 'Iterator (find-package "MASTERCLIENT")))
(unless (find-package "MASTERCLIENT::ITERATOR")
  (make-package "MASTERCLIENT::ITERATOR"))
(unless (find-package "MASTERCLIENT::ITERATORREQUEST")
  (make-package "MASTERCLIENT::ITERATORREQUEST"))
(unless (find-package "MASTERCLIENT::ITERATORRESPONSE")
  (make-package "MASTERCLIENT::ITERATORRESPONSE"))

(in-package "ROS")

(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))




(defclass masterclient::IteratorRequest
  :super ros::object
  :slots (_data ))

(defmethod masterclient::IteratorRequest
  (:init
   (&key
    ((:data __data) (instance std_msgs::String :init))
    )
   (send-super :init)
   (setq _data __data)
   self)
  (:data
   (&rest __data)
   (if (keywordp (car __data))
       (send* _data __data)
     (progn
       (if __data (setq _data (car __data)))
       _data)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/String _data
    (send _data :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/String _data
       (send _data :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/String _data
     (send _data :deserialize buf ptr-) (incf ptr- (send _data :serialization-length))
   ;;
   self)
  )

(defclass masterclient::IteratorResponse
  :super ros::object
  :slots (_ack ))

(defmethod masterclient::IteratorResponse
  (:init
   (&key
    ((:ack __ack) 0)
    )
   (send-super :init)
   (setq _ack (round __ack))
   self)
  (:ack
   (&optional __ack)
   (if __ack (setq _ack __ack)) _ack)
  (:serialization-length
   ()
   (+
    ;; int8 _ack
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _ack
       (write-byte _ack s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _ack
     (setq _ack (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _ack 127) (setq _ack (- _ack 256)))
   ;;
   self)
  )

(defclass masterclient::Iterator
  :super ros::object
  :slots ())

(setf (get masterclient::Iterator :md5sum-) "8869b2ff5bcea599c212b1e75b68818b")
(setf (get masterclient::Iterator :datatype-) "masterclient/Iterator")
(setf (get masterclient::Iterator :request) masterclient::IteratorRequest)
(setf (get masterclient::Iterator :response) masterclient::IteratorResponse)

(defmethod masterclient::IteratorRequest
  (:response () (instance masterclient::IteratorResponse :init)))

(setf (get masterclient::IteratorRequest :md5sum-) "8869b2ff5bcea599c212b1e75b68818b")
(setf (get masterclient::IteratorRequest :datatype-) "masterclient/IteratorRequest")
(setf (get masterclient::IteratorRequest :definition-)
      "std_msgs/String data

================================================================================
MSG: std_msgs/String
string data
---
int8 ack

")

(setf (get masterclient::IteratorResponse :md5sum-) "8869b2ff5bcea599c212b1e75b68818b")
(setf (get masterclient::IteratorResponse :datatype-) "masterclient/IteratorResponse")
(setf (get masterclient::IteratorResponse :definition-)
      "std_msgs/String data

================================================================================
MSG: std_msgs/String
string data
---
int8 ack

")



(provide :masterclient/Iterator "8869b2ff5bcea599c212b1e75b68818b")


