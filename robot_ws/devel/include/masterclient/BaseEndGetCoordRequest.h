// Generated by gencpp from file masterclient/BaseEndGetCoordRequest.msg
// DO NOT EDIT!


#ifndef MASTERCLIENT_MESSAGE_BASEENDGETCOORDREQUEST_H
#define MASTERCLIENT_MESSAGE_BASEENDGETCOORDREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace masterclient
{
template <class ContainerAllocator>
struct BaseEndGetCoordRequest_
{
  typedef BaseEndGetCoordRequest_<ContainerAllocator> Type;

  BaseEndGetCoordRequest_()
    : data()  {
    }
  BaseEndGetCoordRequest_(const ContainerAllocator& _alloc)
    : data(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _data_type;
  _data_type data;




  typedef boost::shared_ptr< ::masterclient::BaseEndGetCoordRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::masterclient::BaseEndGetCoordRequest_<ContainerAllocator> const> ConstPtr;

}; // struct BaseEndGetCoordRequest_

typedef ::masterclient::BaseEndGetCoordRequest_<std::allocator<void> > BaseEndGetCoordRequest;

typedef boost::shared_ptr< ::masterclient::BaseEndGetCoordRequest > BaseEndGetCoordRequestPtr;
typedef boost::shared_ptr< ::masterclient::BaseEndGetCoordRequest const> BaseEndGetCoordRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::masterclient::BaseEndGetCoordRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::masterclient::BaseEndGetCoordRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace masterclient

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'masterclient': ['/home/tomek/TheTitans/robot_ws/src/masterclient/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::masterclient::BaseEndGetCoordRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::masterclient::BaseEndGetCoordRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::masterclient::BaseEndGetCoordRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::masterclient::BaseEndGetCoordRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::masterclient::BaseEndGetCoordRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::masterclient::BaseEndGetCoordRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::masterclient::BaseEndGetCoordRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "420cd38b6b071cd49f2970c3e2cee511";
  }

  static const char* value(const ::masterclient::BaseEndGetCoordRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x420cd38b6b071cd4ULL;
  static const uint64_t static_value2 = 0x9f2970c3e2cee511ULL;
};

template<class ContainerAllocator>
struct DataType< ::masterclient::BaseEndGetCoordRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "masterclient/BaseEndGetCoordRequest";
  }

  static const char* value(const ::masterclient::BaseEndGetCoordRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::masterclient::BaseEndGetCoordRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32[] data\n\
";
  }

  static const char* value(const ::masterclient::BaseEndGetCoordRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::masterclient::BaseEndGetCoordRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.data);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct BaseEndGetCoordRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::masterclient::BaseEndGetCoordRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::masterclient::BaseEndGetCoordRequest_<ContainerAllocator>& v)
  {
    s << indent << "data[]" << std::endl;
    for (size_t i = 0; i < v.data.size(); ++i)
    {
      s << indent << "  data[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.data[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // MASTERCLIENT_MESSAGE_BASEENDGETCOORDREQUEST_H
