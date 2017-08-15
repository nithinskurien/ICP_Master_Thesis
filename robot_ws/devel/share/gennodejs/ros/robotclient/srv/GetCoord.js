// Auto-generated. Do not edit!

// (in-package robotclient.srv)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------

let Floats = require('../msg/Floats.js');

//-----------------------------------------------------------

class GetCoordRequest {
  constructor() {
    this.in = 0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type GetCoordRequest
    // Serialize message field [in]
    bufferInfo = _serializer.int8(obj.in, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type GetCoordRequest
    let tmp;
    let len;
    let data = new GetCoordRequest();
    // Deserialize message field [in]
    tmp = _deserializer.int8(buffer);
    data.in = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'robotclient/GetCoordRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd8a5cea836bd62441c9efcd5dff5bc52';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int8 in
    
    `;
  }

};

class GetCoordResponse {
  constructor() {
    this.data = new Floats();
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type GetCoordResponse
    // Serialize message field [data]
    bufferInfo = Floats.serialize(obj.data, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type GetCoordResponse
    let tmp;
    let len;
    let data = new GetCoordResponse();
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
    return 'robotclient/GetCoordResponse';
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

module.exports = {
  Request: GetCoordRequest,
  Response: GetCoordResponse
};
