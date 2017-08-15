// Auto-generated. Do not edit!

// (in-package robotclient.srv)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class RotateRobotRequest {
  constructor() {
    this.deg = 0.0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type RotateRobotRequest
    // Serialize message field [deg]
    bufferInfo = _serializer.float64(obj.deg, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type RotateRobotRequest
    let tmp;
    let len;
    let data = new RotateRobotRequest();
    // Deserialize message field [deg]
    tmp = _deserializer.float64(buffer);
    data.deg = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'robotclient/RotateRobotRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ef1d1debd35ca46c1d4c1406904ea8d3';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 deg
    
    `;
  }

};

class RotateRobotResponse {
  constructor() {
    this.ack = 0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type RotateRobotResponse
    // Serialize message field [ack]
    bufferInfo = _serializer.int8(obj.ack, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type RotateRobotResponse
    let tmp;
    let len;
    let data = new RotateRobotResponse();
    // Deserialize message field [ack]
    tmp = _deserializer.int8(buffer);
    data.ack = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'robotclient/RotateRobotResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'fb706f4edb700568d7fd69c87cdd4a79';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int8 ack
    
    
    `;
  }

};

module.exports = {
  Request: RotateRobotRequest,
  Response: RotateRobotResponse
};
