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

class drive_motor {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.m_1 = null;
      this.m_2 = null;
    }
    else {
      if (initObj.hasOwnProperty('m_1')) {
        this.m_1 = initObj.m_1
      }
      else {
        this.m_1 = 0;
      }
      if (initObj.hasOwnProperty('m_2')) {
        this.m_2 = initObj.m_2
      }
      else {
        this.m_2 = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type drive_motor
    // Serialize message field [m_1]
    bufferOffset = _serializer.int16(obj.m_1, buffer, bufferOffset);
    // Serialize message field [m_2]
    bufferOffset = _serializer.int16(obj.m_2, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type drive_motor
    let len;
    let data = new drive_motor(null);
    // Deserialize message field [m_1]
    data.m_1 = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [m_2]
    data.m_2 = _deserializer.int16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'rescue_bot/drive_motor';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0a3cf26992116e8869f3387fe00a35d8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int16 m_1
    int16 m_2
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new drive_motor(null);
    if (msg.m_1 !== undefined) {
      resolved.m_1 = msg.m_1;
    }
    else {
      resolved.m_1 = 0
    }

    if (msg.m_2 !== undefined) {
      resolved.m_2 = msg.m_2;
    }
    else {
      resolved.m_2 = 0
    }

    return resolved;
    }
};

module.exports = drive_motor;
