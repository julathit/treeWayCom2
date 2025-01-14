// Generated by gencpp from file rescue_bot/camera_config.msg
// DO NOT EDIT!


#ifndef RESCUE_BOT_MESSAGE_CAMERA_CONFIG_H
#define RESCUE_BOT_MESSAGE_CAMERA_CONFIG_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace rescue_bot
{
template <class ContainerAllocator>
struct camera_config_
{
  typedef camera_config_<ContainerAllocator> Type;

  camera_config_()
    : scale(0)
    , fram_rate(0)
    , color_set(false)  {
    }
  camera_config_(const ContainerAllocator& _alloc)
    : scale(0)
    , fram_rate(0)
    , color_set(false)  {
  (void)_alloc;
    }



   typedef int16_t _scale_type;
  _scale_type scale;

   typedef int16_t _fram_rate_type;
  _fram_rate_type fram_rate;

   typedef uint8_t _color_set_type;
  _color_set_type color_set;





  typedef boost::shared_ptr< ::rescue_bot::camera_config_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rescue_bot::camera_config_<ContainerAllocator> const> ConstPtr;

}; // struct camera_config_

typedef ::rescue_bot::camera_config_<std::allocator<void> > camera_config;

typedef boost::shared_ptr< ::rescue_bot::camera_config > camera_configPtr;
typedef boost::shared_ptr< ::rescue_bot::camera_config const> camera_configConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rescue_bot::camera_config_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rescue_bot::camera_config_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::rescue_bot::camera_config_<ContainerAllocator1> & lhs, const ::rescue_bot::camera_config_<ContainerAllocator2> & rhs)
{
  return lhs.scale == rhs.scale &&
    lhs.fram_rate == rhs.fram_rate &&
    lhs.color_set == rhs.color_set;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::rescue_bot::camera_config_<ContainerAllocator1> & lhs, const ::rescue_bot::camera_config_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace rescue_bot

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::rescue_bot::camera_config_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rescue_bot::camera_config_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rescue_bot::camera_config_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rescue_bot::camera_config_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rescue_bot::camera_config_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rescue_bot::camera_config_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rescue_bot::camera_config_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d706ca6804416e58885c51a33d760341";
  }

  static const char* value(const ::rescue_bot::camera_config_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd706ca6804416e58ULL;
  static const uint64_t static_value2 = 0x885c51a33d760341ULL;
};

template<class ContainerAllocator>
struct DataType< ::rescue_bot::camera_config_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rescue_bot/camera_config";
  }

  static const char* value(const ::rescue_bot::camera_config_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rescue_bot::camera_config_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int16 scale\n"
"int16 fram_rate\n"
"bool color_set\n"
;
  }

  static const char* value(const ::rescue_bot::camera_config_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rescue_bot::camera_config_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.scale);
      stream.next(m.fram_rate);
      stream.next(m.color_set);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct camera_config_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rescue_bot::camera_config_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rescue_bot::camera_config_<ContainerAllocator>& v)
  {
    s << indent << "scale: ";
    Printer<int16_t>::stream(s, indent + "  ", v.scale);
    s << indent << "fram_rate: ";
    Printer<int16_t>::stream(s, indent + "  ", v.fram_rate);
    s << indent << "color_set: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.color_set);
  }
};

} // namespace message_operations
} // namespace ros

#endif // RESCUE_BOT_MESSAGE_CAMERA_CONFIG_H
