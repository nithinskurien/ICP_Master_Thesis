// Generated by gencpp from file robotclient/MoveRobot.msg
// DO NOT EDIT!


#ifndef ROBOTCLIENT_MESSAGE_MOVEROBOT_H
#define ROBOTCLIENT_MESSAGE_MOVEROBOT_H

#include <ros/service_traits.h>


#include <robotclient/MoveRobotRequest.h>
#include <robotclient/MoveRobotResponse.h>


namespace robotclient
{

struct MoveRobot
{

typedef MoveRobotRequest Request;
typedef MoveRobotResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct MoveRobot
} // namespace robotclient


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::robotclient::MoveRobot > {
  static const char* value()
  {
    return "73d983cb94f147797fb40bd0af7e75a5";
  }

  static const char* value(const ::robotclient::MoveRobot&) { return value(); }
};

template<>
struct DataType< ::robotclient::MoveRobot > {
  static const char* value()
  {
    return "robotclient/MoveRobot";
  }

  static const char* value(const ::robotclient::MoveRobot&) { return value(); }
};


// service_traits::MD5Sum< ::robotclient::MoveRobotRequest> should match 
// service_traits::MD5Sum< ::robotclient::MoveRobot > 
template<>
struct MD5Sum< ::robotclient::MoveRobotRequest>
{
  static const char* value()
  {
    return MD5Sum< ::robotclient::MoveRobot >::value();
  }
  static const char* value(const ::robotclient::MoveRobotRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::robotclient::MoveRobotRequest> should match 
// service_traits::DataType< ::robotclient::MoveRobot > 
template<>
struct DataType< ::robotclient::MoveRobotRequest>
{
  static const char* value()
  {
    return DataType< ::robotclient::MoveRobot >::value();
  }
  static const char* value(const ::robotclient::MoveRobotRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::robotclient::MoveRobotResponse> should match 
// service_traits::MD5Sum< ::robotclient::MoveRobot > 
template<>
struct MD5Sum< ::robotclient::MoveRobotResponse>
{
  static const char* value()
  {
    return MD5Sum< ::robotclient::MoveRobot >::value();
  }
  static const char* value(const ::robotclient::MoveRobotResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::robotclient::MoveRobotResponse> should match 
// service_traits::DataType< ::robotclient::MoveRobot > 
template<>
struct DataType< ::robotclient::MoveRobotResponse>
{
  static const char* value()
  {
    return DataType< ::robotclient::MoveRobot >::value();
  }
  static const char* value(const ::robotclient::MoveRobotResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // ROBOTCLIENT_MESSAGE_MOVEROBOT_H
