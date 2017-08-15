;; Auto-generated. Do not edit!


(when (boundp 'masterclient::GetCoord)
  (if (not (find-package "MASTERCLIENT"))
    (make-package "MASTERCLIENT"))
  (shadow 'GetCoord (find-package "MASTERCLIENT")))
(unless (find-package "MASTERCLIENT::GETCOORD")
  (make-package "MASTERCLIENT::GETCOORD"))
(unless (find-package "MASTERCLIENT::GETCOORDREQUEST")
  (make-package "MASTERCLIENT::GETCOORDREQUEST"))
(unless (find-package "MASTERCLIENT::GETCOORDRESPONSE")
  (make-package "MASTERCLIENT::GETCOORDRESPONSE"))

(in-package "ROS")





(defclass masterclient::GetCoordRequest
  :super ros::object
  :slots (_in ))

(defmethod masterclient::GetCoordRequest
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

(defclass masterclient::GetCoordResponse
  :super ros::object
  :slots (_data ))

(defmethod masterclient::GetCoordResponse
  (:init
   (&key
    ((:data __data) (instance masterclient::Floats :init))
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
    ;; masterclient/Floats _data
    (send _data :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; masterclient/Floats _data
       (send _data :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; masterclient/Floats _data
     (send _data :deserialize buf ptr-) (incf ptr- (send _data :serialization-length))
   ;;
   self)
  )

(defclass masterclient::GetCoord
  :super ros::object
  :slots ())

(setf (get masterclient::GetCoord :md5sum-) "ec7fb4cadb363741bad99758dda47526")
(setf (get masterclient::GetCoord :datatype-) "masterclient/GetCoord")
(setf (get masterclient::GetCoord :request) masterclient::GetCoordRequest)
(setf (get masterclient::GetCoord :response) masterclient::GetCoordResponse)

(defmethod masterclient::GetCoordRequest
  (:response () (instance masterclient::GetCoordResponse :init)))

(setf (get masterclient::GetCoordRequest :md5sum-) "ec7fb4cadb363741bad99758dda47526")
(setf (get masterclient::GetCoordRequest :datatype-) "masterclient/GetCoordRequest")
(setf (get masterclient::GetCoordRequest :definition-)
      "int8 in
---
Floats data


================================================================================
MSG: masterclient/Floats
float32[] data
")

(setf (get masterclient::GetCoordResponse :md5sum-) "ec7fb4cadb363741bad99758dda47526")
(setf (get masterclient::GetCoordResponse :datatype-) "masterclient/GetCoordResponse")
(setf (get masterclient::GetCoordResponse :definition-)
      "int8 in
---
Floats data


================================================================================
MSG: masterclient/Floats
float32[] data
")



(provide :masterclient/GetCoord "ec7fb4cadb363741bad99758dda47526")


