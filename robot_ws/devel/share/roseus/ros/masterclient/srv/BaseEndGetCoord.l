;; Auto-generated. Do not edit!


(when (boundp 'masterclient::BaseEndGetCoord)
  (if (not (find-package "MASTERCLIENT"))
    (make-package "MASTERCLIENT"))
  (shadow 'BaseEndGetCoord (find-package "MASTERCLIENT")))
(unless (find-package "MASTERCLIENT::BASEENDGETCOORD")
  (make-package "MASTERCLIENT::BASEENDGETCOORD"))
(unless (find-package "MASTERCLIENT::BASEENDGETCOORDREQUEST")
  (make-package "MASTERCLIENT::BASEENDGETCOORDREQUEST"))
(unless (find-package "MASTERCLIENT::BASEENDGETCOORDRESPONSE")
  (make-package "MASTERCLIENT::BASEENDGETCOORDRESPONSE"))

(in-package "ROS")





(defclass masterclient::BaseEndGetCoordRequest
  :super ros::object
  :slots (_data ))

(defmethod masterclient::BaseEndGetCoordRequest
  (:init
   (&key
    ((:data __data) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _data __data)
   self)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; float32[] _data
    (* 4    (length _data)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32[] _data
     (write-long (length _data) s)
     (dotimes (i (length _data))
       (sys::poke (elt _data i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32[] _data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _data i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(defclass masterclient::BaseEndGetCoordResponse
  :super ros::object
  :slots (_in ))

(defmethod masterclient::BaseEndGetCoordResponse
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

(defclass masterclient::BaseEndGetCoord
  :super ros::object
  :slots ())

(setf (get masterclient::BaseEndGetCoord :md5sum-) "b6fb5bf1382e6a4ebdbf5eee1e4c5505")
(setf (get masterclient::BaseEndGetCoord :datatype-) "masterclient/BaseEndGetCoord")
(setf (get masterclient::BaseEndGetCoord :request) masterclient::BaseEndGetCoordRequest)
(setf (get masterclient::BaseEndGetCoord :response) masterclient::BaseEndGetCoordResponse)

(defmethod masterclient::BaseEndGetCoordRequest
  (:response () (instance masterclient::BaseEndGetCoordResponse :init)))

(setf (get masterclient::BaseEndGetCoordRequest :md5sum-) "b6fb5bf1382e6a4ebdbf5eee1e4c5505")
(setf (get masterclient::BaseEndGetCoordRequest :datatype-) "masterclient/BaseEndGetCoordRequest")
(setf (get masterclient::BaseEndGetCoordRequest :definition-)
      "float32[] data
---
int8 in

")

(setf (get masterclient::BaseEndGetCoordResponse :md5sum-) "b6fb5bf1382e6a4ebdbf5eee1e4c5505")
(setf (get masterclient::BaseEndGetCoordResponse :datatype-) "masterclient/BaseEndGetCoordResponse")
(setf (get masterclient::BaseEndGetCoordResponse :definition-)
      "float32[] data
---
int8 in

")



(provide :masterclient/BaseEndGetCoord "b6fb5bf1382e6a4ebdbf5eee1e4c5505")


