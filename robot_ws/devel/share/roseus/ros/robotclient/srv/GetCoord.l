;; Auto-generated. Do not edit!


(when (boundp 'robotclient::GetCoord)
  (if (not (find-package "ROBOTCLIENT"))
    (make-package "ROBOTCLIENT"))
  (shadow 'GetCoord (find-package "ROBOTCLIENT")))
(unless (find-package "ROBOTCLIENT::GETCOORD")
  (make-package "ROBOTCLIENT::GETCOORD"))
(unless (find-package "ROBOTCLIENT::GETCOORDREQUEST")
  (make-package "ROBOTCLIENT::GETCOORDREQUEST"))
(unless (find-package "ROBOTCLIENT::GETCOORDRESPONSE")
  (make-package "ROBOTCLIENT::GETCOORDRESPONSE"))

(in-package "ROS")





(defclass robotclient::GetCoordRequest
  :super ros::object
  :slots (_in ))

(defmethod robotclient::GetCoordRequest
  (:init
   (&key
    ((:in __in) 0)
    )
   (send-super :init)
   (setq _in (round __in))
   self)
  (:in
   (&optional __in)
   (if __in (setq _in __in)) _in)
  (:serialization-length
   ()
   (+
    ;; int8 _in
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _in
       (write-byte _in s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _in
     (setq _in (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _in 127) (setq _in (- _in 256)))
   ;;
   self)
  )

(defclass robotclient::GetCoordResponse
  :super ros::object
  :slots (_data ))

(defmethod robotclient::GetCoordResponse
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

(defclass robotclient::GetCoord
  :super ros::object
  :slots ())

(setf (get robotclient::GetCoord :md5sum-) "ec7fb4cadb363741bad99758dda47526")
(setf (get robotclient::GetCoord :datatype-) "robotclient/GetCoord")
(setf (get robotclient::GetCoord :request) robotclient::GetCoordRequest)
(setf (get robotclient::GetCoord :response) robotclient::GetCoordResponse)

(defmethod robotclient::GetCoordRequest
  (:response () (instance robotclient::GetCoordResponse :init)))

(setf (get robotclient::GetCoordRequest :md5sum-) "ec7fb4cadb363741bad99758dda47526")
(setf (get robotclient::GetCoordRequest :datatype-) "robotclient/GetCoordRequest")
(setf (get robotclient::GetCoordRequest :definition-)
      "int8 in
---
Floats data


================================================================================
MSG: robotclient/Floats
float32[] data
")

(setf (get robotclient::GetCoordResponse :md5sum-) "ec7fb4cadb363741bad99758dda47526")
(setf (get robotclient::GetCoordResponse :datatype-) "robotclient/GetCoordResponse")
(setf (get robotclient::GetCoordResponse :definition-)
      "int8 in
---
Floats data


================================================================================
MSG: robotclient/Floats
float32[] data
")



(provide :robotclient/GetCoord "ec7fb4cadb363741bad99758dda47526")


