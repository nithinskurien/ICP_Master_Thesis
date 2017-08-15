// Auto-generated. Do not edit!

// (in-package masterclient.srv)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------


//-----------------------------------------------------------

class IteratorRequest {
  constructor() {
    this.data = new std_msgs.msg.String();
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type IteratorRequest
    // Serialize message field [data]
    bufferInfo = std_msgs.msg.String.serialize(obj.data, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type IteratorRequest
    let tmp;
    let len;
    let data = new IteratorRequest();
    // Deserialize message field [data]
    tmp = std_msgs.msg.String.deserialize(buffer);
    data.data = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'masterclient/IteratorRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '131c7b16e90d7646b67a1c83cd590279';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    std_msgs/String data
    
    ================================================================================
    MSG: std_msgs/String
    string data
    
    `;
  }

};

class IteratorResponse {
  constructor() {
    this.ack = 0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type IteratorResponse
    // Serialize message field [ack]
    bufferInfo = _serializer.int8(obj.ack, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type IteratorResponse
    let tmp;
    let len;
    let data = new IteratorResponse();
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
    return 'masterclient/IteratorResponse';
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
  Request: IteratorRequest,
  Response: IteratorResponse
};
