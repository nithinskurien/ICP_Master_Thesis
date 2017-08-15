// Generated by gencpp from file robotclient/MoveRobotRequest.msg
// DO NOT EDIT!


#ifndef ROBOTCLIENT_MESSAGE_MOVEROBOTREQUEST_H
#define ROBOTCLIENT_MESSAGE_MOVEROBOTREQUEST_H


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
struct MoveRobotRequest_
{
  typedef MoveRobotRequest_<ContainerAllocator> Type;

  MoveRobotRequest_()
    : length(0.0)  {
    }
  MoveRobotRequest_(const ContainerAllocator& _alloc)
    : length(0.0)  {
  (void)_alloc;
    }



   typedef double _length_type;
  _length_type length;




  typedef boost::shared_ptr< ::robotclient::MoveRobotRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::robotclient::MoveRobotRequest_<ContainerAllocator> const> ConstPtr;

}; // struct MoveRobotRequest_

typedef ::robotclient::MoveRobotRequest_<std::allocator<void> > MoveRobotRequest;

typedef boost::shared_ptr< ::robotclient::MoveRobotRequest > MoveRobotRequestPtr;
typedef boost::shared_ptr< ::robotclient::MoveRobotRequest const> MoveRobotRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::robotclient::MoveRobotRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::robotclient::MoveRobotRequest_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::robotclient::MoveRobotRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::robotclient::MoveRobotRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robotclient::MoveRobotRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robotclient::MoveRobotRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robotclient::MoveRobotRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robotclient::MoveRobotRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::robotclient::MoveRobotRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "a67ae5be9f180b7bd9038cd515fe45c1";
  }

  static const char* value(const ::robotclient::MoveRobotRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xa67ae5be9f180b7bULL;
  static const uint64_t static_value2 = 0xd9038cd515fe45c1ULL;
};

template<class ContainerAllocator>
struct DataType< ::robotclient::MoveRobotRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "robotclient/MoveRobotRequest";
  }

  static const char* value(const ::robotclient::MoveRobotRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::robotclient::MoveRobotRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 length\n\
";
  }

  static const char* value(const ::robotclient::MoveRobotRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::robotclient::MoveRobotRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.length);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct MoveRobotRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::robotclient::MoveRobotRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::robotclient::MoveRobotRequest_<ContainerAllocator>& v)
  {
    s << indent << "length: ";
    Printer<double>::stream(s, indent + "  ", v.length);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROBOTCLIENT_MESSAGE_MOVEROBOTREQUEST_H
