// Auto-generated. Do not edit!

// (in-package rescue_bot.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class camera_config {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.scale = null;
      this.fram_rate = null;
      this.color_set = null;
    }
    else {
      if (initObj.hasOwnProperty('scale')) {
        this.scale = initObj.scale
      }
      else {
        this.scale = 0;
      }
      if (initObj.hasOwnProperty('fram_rate')) {
        this.fram_rate = initObj.fram_rate
      }
      else {
        this.fram_rate = 0;
      }
      if (initObj.hasOwnProperty('color_set')) {
        this.color_set = initObj.color_set
      }
      else {
        this.color_set = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type camera_config
    // Serialize message field [scale]
    bufferOffset = _serializer.int16(obj.scale, buffer, bufferOffset);
    // Serialize message field [fram_rate]
    bufferOffset = _serializer.int16(obj.fram_rate, buffer, bufferOffset);
    // Serialize message field [color_set]
    bufferOffset = _serializer.bool(obj.color_set, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type camera_config
    let len;
    let data = new camera_config(null);
    // Deserialize message field [scale]
    data.scale = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [fram_rate]
    data.fram_rate = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [color_set]
    data.color_set = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 5;
  }

  static datatype() {
    // Returns string type for a message object
    return 'rescue_bot/camera_config';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd706ca6804416e58885c51a33d760341';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int16 scale
    int16 fram_rate
    bool color_set
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new camera_config(null);
    if (msg.scale !== undefined) {
      resolved.scale = msg.scale;
    }
    else {
      resolved.scale = 0
    }

    if (msg.fram_rate !== undefined) {
      resolved.fram_rate = msg.fram_rate;
    }
    else {
      resolved.fram_rate = 0
    }

    if (msg.color_set !== undefined) {
      resolved.color_set = msg.color_set;
    }
    else {
      resolved.color_set = false
    }

    return resolved;
    }
};

module.exports = camera_config;
