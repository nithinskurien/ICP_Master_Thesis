// Generated by gencpp from file robotclient/RotateRobotRequest.msg
// DO NOT EDIT!


#ifndef ROBOTCLIENT_MESSAGE_ROTATEROBOTREQUEST_H
#define ROBOTCLIENT_MESSAGE_ROTATEROBOTREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace robotclient
{
template <class ContainerAllocator>
struct RotateRobotRequest_
{
  typedef RotateRobotRequest_<ContainerAllocator> Type;

  RotateRobotRequest_()
    : deg(0.0)  {
    }
  RotateRobotRequest_(const ContainerAllocator& _alloc)
    : deg(0.0)  {
  (void)_alloc;
    }



   typedef double _deg_type;
  _deg_type deg;




  typedef boost::shared_ptr< ::robotclient::RotateRobotRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::robotclient::RotateRobotRequest_<ContainerAllocator> const> ConstPtr;

}; // struct RotateRobotRequest_

typedef ::robotclient::RotateRobotRequest_<std::allocator<void> > RotateRobotRequest;

typedef boost::shared_ptr< ::robotclient::RotateRobotRequest > RotateRobotRequestPtr;
typedef boost::shared_ptr< ::robotclient::RotateRobotRequest const> RotateRobotRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::robotclient::RotateRobotRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::robotclient::RotateRobotRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace robotclient

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'robotclient': ['/home/tomek/TheTitans/robot_ws/src/robotclient/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::robotclient::RotateRobotRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::robotclient::RotateRobotRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robotclient::RotateRobotRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robotclient::RotateRobotRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robotclient::RotateRobotRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robotclient::RotateRobotRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::robotclient::RotateRobotRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ef1d1debd35ca46c1d4c1406904ea8d3";
  }

  static const char* value(const ::robotclient::RotateRobotRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xef1d1debd35ca46cULL;
  static const uint64_t static_value2 = 0x1d4c1406904ea8d3ULL;
};

template<class ContainerAllocator>
struct DataType< ::robotclient::RotateRobotRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "robotclient/RotateRobotRequest";
  }

  static const char* value(const ::robotclient::RotateRobotRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::robotclient::RotateRobotRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 deg\n\
";
  }

  static const char* value(const ::robotclient::RotateRobotRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::robotclient::RotateRobotRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.deg);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct RotateRobotRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::robotclient::RotateRobotRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::robotclient::RotateRobotRequest_<ContainerAllocator>& v)
  {
    s << indent << "deg: ";
    Printer<double>::stream(s, indent + "  ", v.deg);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROBOTCLIENT_MESSAGE_ROTATEROBOTREQUEST_H
