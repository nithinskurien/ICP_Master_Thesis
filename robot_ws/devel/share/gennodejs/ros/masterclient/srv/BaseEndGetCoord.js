// Auto-generated. Do not edit!

// (in-package masterclient.srv)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class BaseEndGetCoordRequest {
  constructor() {
    this.data = [];
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type BaseEndGetCoordRequest
    // Serialize the length for message field [data]
    bufferInfo = _serializer.uint32(obj.data.length, bufferInfo);
    // Serialize message field [data]
    obj.data.forEach((val) => {
      bufferInfo = _serializer.float32(val, bufferInfo);
    });
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type BaseEndGetCoordRequest
    let tmp;
    let len;
    let data = new BaseEndGetCoordRequest();
    // Deserialize array length for message field [data]
    tmp = _deserializer.uint32(buffer);
    len = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [data]
    data.data = new Array(len);
    for (let i = 0; i < len; ++i) {
      tmp = _deserializer.float32(buffer);
      data.data[i] = tmp.data;
      buffer = tmp.buffer;
    }
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'masterclient/BaseEndGetCoordRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '420cd38b6b071cd49f2970c3e2cee511';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32[] data
    
    `;
  }

};

class BaseEndGetCoordResponse {
  constructor() {
    this.in = 0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type BaseEndGetCoordResponse
    // Serialize message field [in]
    bufferInfo = _serializer.int8(obj.in, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type BaseEndGetCoordResponse
    let tmp;
    let len;
    let data = new BaseEndGetCoordResponse();
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
    return 'masterclient/BaseEndGetCoordResponse';
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

module.exports = {
  Request: BaseEndGetCoordRequest,
  Response: BaseEndGetCoordResponse
};
