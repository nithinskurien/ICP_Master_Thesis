
(cl:in-package :asdf)

(defsystem "masterclient-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :masterclient-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "BaseEndGetCoord" :depends-on ("_package_BaseEndGetCoord"))
    (:file "_package_BaseEndGetCoord" :depends-on ("_package"))
    (:file "GetCoord" :depends-on ("_package_GetCoord"))
    (:file "_package_GetCoord" :depends-on ("_package"))
    (:file "Iterator" :depends-on ("_package_Iterator"))
    (:file "_package_Iterator" :depends-on ("_package"))
  ))