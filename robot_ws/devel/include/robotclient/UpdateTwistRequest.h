// Generated by gencpp from file robotclient/UpdateTwistRequest.msg
// DO NOT EDIT!


#ifndef ROBOTCLIENT_MESSAGE_UPDATETWISTREQUEST_H
#define ROBOTCLIENT_MESSAGE_UPDATETWISTREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <robotclient/Floats.h>

namespace robotclient
{
template <class ContainerAllocator>
struct UpdateTwistRequest_
{
  typedef UpdateTwistRequest_<ContainerAllocator> Type;

  UpdateTwistRequest_()
    : data()  {
    }
  UpdateTwistRequest_(const ContainerAllocator& _alloc)
    : data(_alloc)  {
  (void)_alloc;
    }



   typedef  ::robotclient::Floats_<ContainerAllocator>  _data_type;
  _data_type data;




  typedef boost::shared_ptr< ::robotclient::UpdateTwistRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::robotclient::UpdateTwistRequest_<ContainerAllocator> const> ConstPtr;

}; // struct UpdateTwistRequest_

typedef ::robotclient::UpdateTwistRequest_<std::allocator<void> > UpdateTwistRequest;

typedef boost::shared_ptr< ::robotclient::UpdateTwistRequest > UpdateTwistRequestPtr;
typedef boost::shared_ptr< ::robotclient::UpdateTwistRequest const> UpdateTwistRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::robotclient::UpdateTwistRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::robotclient::UpdateTwistRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace robotclient

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'robotclient': ['/home/tomek/TheTitans/robot_ws/src/robotclient/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::robotclient::UpdateTwistRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::robotclient::UpdateTwistRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robotclient::UpdateTwistRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robotclient::UpdateTwistRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robotclient::UpdateTwistRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robotclient::UpdateTwistRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::robotclient::UpdateTwistRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2f6cb9944d2c5ab5cff8aff4ba87d255";
  }

  static const char* value(const ::robotclient::UpdateTwistRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2f6cb9944d2c5ab5ULL;
  static const uint64_t static_value2 = 0xcff8aff4ba87d255ULL;
};

template<class ContainerAllocator>
struct DataType< ::robotclient::UpdateTwistRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "robotclient/UpdateTwistRequest";
  }

  static const char* value(const ::robotclient::UpdateTwistRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::robotclient::UpdateTwistRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Floats data\n\
\n\
================================================================================\n\
MSG: robotclient/Floats\n\
float32[] data\n\
";
  }

  static const char* value(const ::robotclient::UpdateTwistRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::robotclient::UpdateTwistRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.data);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct UpdateTwistRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::robotclient::UpdateTwistRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::robotclient::UpdateTwistRequest_<ContainerAllocator>& v)
  {
    s << indent << "data: ";
    s << std::endl;
    Printer< ::robotclient::Floats_<ContainerAllocator> >::stream(s, indent + "  ", v.data);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROBOTCLIENT_MESSAGE_UPDATETWISTREQUEST_H
