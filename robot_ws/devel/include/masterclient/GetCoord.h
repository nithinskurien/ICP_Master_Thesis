// Generated by gencpp from file masterclient/GetCoord.msg
// DO NOT EDIT!


#ifndef MASTERCLIENT_MESSAGE_GETCOORD_H
#define MASTERCLIENT_MESSAGE_GETCOORD_H

#include <ros/service_traits.h>


#include <masterclient/GetCoordRequest.h>
#include <masterclient/GetCoordResponse.h>


namespace masterclient
{

struct GetCoord
{

typedef GetCoordRequest Request;
typedef GetCoordResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct GetCoord
} // namespace masterclient


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::masterclient::GetCoord > {
  static const char* value()
  {
    return "ec7fb4cadb363741bad99758dda47526";
  }

  static const char* value(const ::masterclient::GetCoord&) { return value(); }
};

template<>
struct DataType< ::masterclient::GetCoord > {
  static const char* value()
  {
    return "masterclient/GetCoord";
  }

  static const char* value(const ::masterclient::GetCoord&) { return value(); }
};


// service_traits::MD5Sum< ::masterclient::GetCoordRequest> should match 
// service_traits::MD5Sum< ::masterclient::GetCoord > 
template<>
struct MD5Sum< ::masterclient::GetCoordRequest>
{
  static const char* value()
  {
    return MD5Sum< ::masterclient::GetCoord >::value();
  }
  static const char* value(const ::masterclient::GetCoordRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::masterclient::GetCoordRequest> should match 
// service_traits::DataType< ::masterclient::GetCoord > 
template<>
struct DataType< ::masterclient::GetCoordRequest>
{
  static const char* value()
  {
    return DataType< ::masterclient::GetCoord >::value();
  }
  static const char* value(const ::masterclient::GetCoordRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::masterclient::GetCoordResponse> should match 
// service_traits::MD5Sum< ::masterclient::GetCoord > 
template<>
struct MD5Sum< ::masterclient::GetCoordResponse>
{
  static const char* value()
  {
    return MD5Sum< ::masterclient::GetCoord >::value();
  }
  static const char* value(const ::masterclient::GetCoordResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::masterclient::GetCoordResponse> should match 
// service_traits::DataType< ::masterclient::GetCoord > 
template<>
struct DataType< ::masterclient::GetCoordResponse>
{
  static const char* value()
  {
    return DataType< ::masterclient::GetCoord >::value();
  }
  static const char* value(const ::masterclient::GetCoordResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // MASTERCLIENT_MESSAGE_GETCOORD_H
