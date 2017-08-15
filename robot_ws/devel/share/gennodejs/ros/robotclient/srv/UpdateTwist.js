// Auto-generated. Do not edit!

// (in-package robotclient.srv)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');
let Floats = require('../msg/Floats.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class UpdateTwistRequest {
  constructor() {
    this.data = new Floats();
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type UpdateTwistRequest
    // Serialize message field [data]
    bufferInfo = Floats.serialize(obj.data, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type UpdateTwistRequest
    let tmp;
    let len;
    let data = new UpdateTwistRequest();
    // Deserialize message field [data]
    tmp = Floats.deserialize(buffer);
    data.data = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'robotclient/UpdateTwistRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2f6cb9944d2c5ab5cff8aff4ba87d255';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Floats data
    
    ================================================================================
    MSG: robotclient/Floats
    float32[] data
    
    `;
  }

};

class UpdateTwistResponse {
  constructor() {
    this.ack = 0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type UpdateTwistResponse
    // Serialize message field [ack]
    bufferInfo = _serializer.int8(obj.ack, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type UpdateTwistResponse
    let tmp;
    let len;
    let data = new UpdateTwistResponse();
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
    return 'robotclient/UpdateTwistResponse';
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
  Request: UpdateTwistRequest,
  Response: UpdateTwistResponse
};
