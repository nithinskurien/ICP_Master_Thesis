;; Auto-generated. Do not edit!


(when (boundp 'robotclient::UpdateTwist)
  (if (not (find-package "ROBOTCLIENT"))
    (make-package "ROBOTCLIENT"))
  (shadow 'UpdateTwist (find-package "ROBOTCLIENT")))
(unless (find-package "ROBOTCLIENT::UPDATETWIST")
  (make-package "ROBOTCLIENT::UPDATETWIST"))
(unless (find-package "ROBOTCLIENT::UPDATETWISTREQUEST")
  (make-package "ROBOTCLIENT::UPDATETWISTREQUEST"))
(unless (find-package "ROBOTCLIENT::UPDATETWISTRESPONSE")
  (make-package "ROBOTCLIENT::UPDATETWISTRESPONSE"))

(in-package "ROS")





(defclass robotclient::UpdateTwistRequest
  :super ros::object
  :slots (_data ))

(defmethod robotclient::UpdateTwistRequest
  (:init
   (&key
    ((:data __data) (instance robotclient::Floats :init))
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
    ;; robotclient/Floats _data
    (send _data :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; robotclient/Floats _data
       (send _data :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; robotclient/Floats _data
     (send _data :deserialize buf ptr-) (incf ptr- (send _data :serialization-length))
   ;;
   self)
  )

(defclass robotclient::UpdateTwistResponse
  :super ros::object
  :slots (_ack ))

(defmethod robotclient::UpdateTwistResponse
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

(defclass robotclient::UpdateTwist
  :super ros::object
  :slots ())

(setf (get robotclient::UpdateTwist :md5sum-) "9b8578b5371575f7e032469638abea73")
(setf (get robotclient::UpdateTwist :datatype-) "robotclient/UpdateTwist")
(setf (get robotclient::UpdateTwist :request) robotclient::UpdateTwistRequest)
(setf (get robotclient::UpdateTwist :response) robotclient::UpdateTwistResponse)

(defmethod robotclient::UpdateTwistRequest
  (:response () (instance robotclient::UpdateTwistResponse :init)))

(setf (get robotclient::UpdateTwistRequest :md5sum-) "9b8578b5371575f7e032469638abea73")
(setf (get robotclient::UpdateTwistRequest :datatype-) "robotclient/UpdateTwistRequest")
(setf (get robotclient::UpdateTwistRequest :definition-)
      "Floats data

================================================================================
MSG: robotclient/Floats
float32[] data
---
int8 ack

")

(setf (get robotclient::UpdateTwistResponse :md5sum-) "9b8578b5371575f7e032469638abea73")
(setf (get robotclient::UpdateTwistResponse :datatype-) "robotclient/UpdateTwistResponse")
(setf (get robotclient::UpdateTwistResponse :definition-)
      "Floats data

================================================================================
MSG: robotclient/Floats
float32[] data
---
int8 ack

")



(provide :robotclient/UpdateTwist "9b8578b5371575f7e032469638abea73")


