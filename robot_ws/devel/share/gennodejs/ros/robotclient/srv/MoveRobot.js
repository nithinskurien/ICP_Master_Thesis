// Auto-generated. Do not edit!

// (in-package robotclient.srv)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class MoveRobotRequest {
  constructor() {
    this.length = 0.0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type MoveRobotRequest
    // Serialize message field [length]
    bufferInfo = _serializer.float64(obj.length, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type MoveRobotRequest
    let tmp;
    let len;
    let data = new MoveRobotRequest();
    // Deserialize message field [length]
    tmp = _deserializer.float64(buffer);
    data.length = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'robotclient/MoveRobotRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a67ae5be9f180b7bd9038cd515fe45c1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 length
    
    `;
  }

};

class MoveRobotResponse {
  constructor() {
    this.ack = 0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type MoveRobotResponse
    // Serialize message field [ack]
    bufferInfo = _serializer.int8(obj.ack, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type MoveRobotResponse
    let tmp;
    let len;
    let data = new MoveRobotResponse();
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
    return 'robotclient/MoveRobotResponse';
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
  Request: MoveRobotRequest,
  Response: MoveRobotResponse
};
