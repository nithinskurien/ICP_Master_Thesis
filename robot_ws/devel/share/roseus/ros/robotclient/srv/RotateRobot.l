;; Auto-generated. Do not edit!


(when (boundp 'robotclient::RotateRobot)
  (if (not (find-package "ROBOTCLIENT"))
    (make-package "ROBOTCLIENT"))
  (shadow 'RotateRobot (find-package "ROBOTCLIENT")))
(unless (find-package "ROBOTCLIENT::ROTATEROBOT")
  (make-package "ROBOTCLIENT::ROTATEROBOT"))
(unless (find-package "ROBOTCLIENT::ROTATEROBOTREQUEST")
  (make-package "ROBOTCLIENT::ROTATEROBOTREQUEST"))
(unless (find-package "ROBOTCLIENT::ROTATEROBOTRESPONSE")
  (make-package "ROBOTCLIENT::ROTATEROBOTRESPONSE"))

(in-package "ROS")





(defclass robotclient::RotateRobotRequest
  :super ros::object
  :slots (_deg ))

(defmethod robotclient::RotateRobotRequest
  (:init
   (&key
    ((:deg __deg) 0.0)
    )
   (send-super :init)
   (setq _deg (float __deg))
   self)
  (:deg
   (&optional __deg)
   (if __deg (setq _deg __deg)) _deg)
  (:serialization-length
   ()
   (+
    ;; float64 _deg
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _deg
       (sys::poke _deg (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _deg
     (setq _deg (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass robotclient::RotateRobotResponse
  :super ros::object
  :slots (_ack ))

(defmethod robotclient::RotateRobotResponse
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

(defclass robotclient::RotateRobot
  :super ros::object
  :slots ())

(setf (get robotclient::RotateRobot :md5sum-) "95b88eb44c4cda7e8bd208bebdd2aee8")
(setf (get robotclient::RotateRobot :datatype-) "robotclient/RotateRobot")
(setf (get robotclient::RotateRobot :request) robotclient::RotateRobotRequest)
(setf (get robotclient::RotateRobot :response) robotclient::RotateRobotResponse)

(defmethod robotclient::RotateRobotRequest
  (:response () (instance robotclient::RotateRobotResponse :init)))

(setf (get robotclient::RotateRobotRequest :md5sum-) "95b88eb44c4cda7e8bd208bebdd2aee8")
(setf (get robotclient::RotateRobotRequest :datatype-) "robotclient/RotateRobotRequest")
(setf (get robotclient::RotateRobotRequest :definition-)
      "float64 deg
---
int8 ack

")

(setf (get robotclient::RotateRobotResponse :md5sum-) "95b88eb44c4cda7e8bd208bebdd2aee8")
(setf (get robotclient::RotateRobotResponse :datatype-) "robotclient/RotateRobotResponse")
(setf (get robotclient::RotateRobotResponse :definition-)
      "float64 deg
---
int8 ack

")



(provide :robotclient/RotateRobot "95b88eb44c4cda7e8bd208bebdd2aee8")


