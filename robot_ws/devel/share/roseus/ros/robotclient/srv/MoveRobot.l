;; Auto-generated. Do not edit!


(when (boundp 'robotclient::MoveRobot)
  (if (not (find-package "ROBOTCLIENT"))
    (make-package "ROBOTCLIENT"))
  (shadow 'MoveRobot (find-package "ROBOTCLIENT")))
(unless (find-package "ROBOTCLIENT::MOVEROBOT")
  (make-package "ROBOTCLIENT::MOVEROBOT"))
(unless (find-package "ROBOTCLIENT::MOVEROBOTREQUEST")
  (make-package "ROBOTCLIENT::MOVEROBOTREQUEST"))
(unless (find-package "ROBOTCLIENT::MOVEROBOTRESPONSE")
  (make-package "ROBOTCLIENT::MOVEROBOTRESPONSE"))

(in-package "ROS")





(defclass robotclient::MoveRobotRequest
  :super ros::object
  :slots (_length ))

(defmethod robotclient::MoveRobotRequest
  (:init
   (&key
    ((:length __length) 0.0)
    )
   (send-super :init)
   (setq _length (float __length))
   self)
  (:length
   (&optional __length)
   (if __length (setq _length __length)) _length)
  (:serialization-length
   ()
   (+
    ;; float64 _length
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _length
       (sys::poke _length (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _length
     (setq _length (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass robotclient::MoveRobotResponse
  :super ros::object
  :slots (_ack ))

(defmethod robotclient::MoveRobotResponse
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

(defclass robotclient::MoveRobot
  :super ros::object
  :slots ())

(setf (get robotclient::MoveRobot :md5sum-) "73d983cb94f147797fb40bd0af7e75a5")
(setf (get robotclient::MoveRobot :datatype-) "robotclient/MoveRobot")
(setf (get robotclient::MoveRobot :request) robotclient::MoveRobotRequest)
(setf (get robotclient::MoveRobot :response) robotclient::MoveRobotResponse)

(defmethod robotclient::MoveRobotRequest
  (:response () (instance robotclient::MoveRobotResponse :init)))

(setf (get robotclient::MoveRobotRequest :md5sum-) "73d983cb94f147797fb40bd0af7e75a5")
(setf (get robotclient::MoveRobotRequest :datatype-) "robotclient/MoveRobotRequest")
(setf (get robotclient::MoveRobotRequest :definition-)
      "float64 length
---
int8 ack

")

(setf (get robotclient::MoveRobotResponse :md5sum-) "73d983cb94f147797fb40bd0af7e75a5")
(setf (get robotclient::MoveRobotResponse :datatype-) "robotclient/MoveRobotResponse")
(setf (get robotclient::MoveRobotResponse :definition-)
      "float64 length
---
int8 ack

")



(provide :robotclient/MoveRobot "73d983cb94f147797fb40bd0af7e75a5")


