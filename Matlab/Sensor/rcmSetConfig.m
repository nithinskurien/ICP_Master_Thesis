function status = rcmSetConfig(socket,rcmIp,config)
% rcmSetConfig Sample function to set RCM configuration.
%
% Syntax
% status = rcmSetConfig(socket,config)
%
% Input
% socket - Java DatagramSocket object
% rcmIp - string containing IP address (e.g. 192.168.1.100)
% config - structure containing RCM configuration
%
% Output
% status - 0 if successful
%
% Usage Notes
% Utilizes a previously created UDP socket.  See rcmGetConfig for socket
% creation
%
% Sends a request to set RCM configuration and receives the response from
% RCM.
%
% The message ID is set to 3 in this example, but a specific application can be
% set it to any value within UINT16 range.
%
% See also rcmSampleMain, rcmGetConfig

% Copyright © 2012 Time Domain, Huntsville, AL


import java.io.*
import java.net.DatagramSocket
import java.net.DatagramPacket
import java.net.InetAddress

port = 21210;  % RCM port.

%% Send RCM_GET_CONFIG_REQUEST
% NOTE: The interface requires bytes (int8). Intel machines are little-endian so
% swapbytes is necessary.

MSG_TYPE = swapbytes(uint16(hex2dec('0001')));  % RCM_SET_CONFIG_REQUEST message type.
MSG_ID = swapbytes(uint16(hex2dec('0003')));
NODE_ID = swapbytes(uint32(config.nodeID));
PII = swapbytes(uint16(config.PII));
ANTMODE = uint8(config.antMode);
CODE = uint8(config.codeChnl);
ANTDELAYA = swapbytes(uint32(config.antDlyA));
ANTDELAYB = swapbytes(uint32(config.antDlyB));
FLAGS = swapbytes(uint16(config.flags));
TXGAIN = uint8(config.txPwr);
if exist('config.persistFlag')
PERSIST = uint8(config.persistFlag);
else
  PERSIST = uint8(0);
end

RCM_SET_CONFIG_REQUEST = [...
   typecast([MSG_TYPE MSG_ID],'uint8') ...
   typecast(NODE_ID, 'uint8') typecast(PII,'uint8') ANTMODE CODE ...
   typecast([ANTDELAYA ANTDELAYB], 'uint8') ...
   typecast(FLAGS, 'uint8') TXGAIN typecast(PERSIST, 'uint8')];

% TRY/CATCH is used to close the socket in case of an error. Otherwise
% MATLAB must be restarted to use the socket again.
try
%  socket = DatagramSocket;
  socket.setReuseAddress(1);
  
  addr = InetAddress.getByName(rcmIp);

  packet = DatagramPacket(RCM_SET_CONFIG_REQUEST,length(RCM_SET_CONFIG_REQUEST),addr,port);

  socket.send(packet);

catch sendPacketError
  try
    socket.close
  catch closeError
  end
  error('%s.m--Failed to send UDP packet.\n%s',mfilename,sendPacketError.message);
  return
end


%% Receive RCM_GET_CONFIG_CONFIRM
timeout = 400;  % ms

PACKET_LENGTH = 8;  % RCM_SET_CONFIG_CONFIRM message length (bytes).

try
  socket.setSoTimeout(timeout);
  
  packet = DatagramPacket(zeros(1,PACKET_LENGTH,'uint8'),PACKET_LENGTH);
  socket.receive(packet);
  
  msg = packet.getData;
  msg = msg(1:packet.getLength);
  
catch receiveError
  if ~isempty(strfind(receiveError.message,'java.net.SocketTimeoutException'))
    % Error occurred because of time out.
    errorStr = sprintf('%s.m--Failed to receive UDP packet. Connection timed out.\n',mfilename);
  else
    errorStr = sprintf('%s.m--Failed to receive UDP packet.\nJava error message follows:\n%s',mfilename,receiveError.message);
  end
  try
    socket.close;
  catch closeError
  end
  error(errorStr);
end

%% Put message parameters in structure.
% See the RCM API for message parameters.
msgType = typecast([msg(2) msg(1)],'uint16');

if msgType ~= uint16(hex2dec('0101'))
  fprintf('Message type %04x does not match RCM_SET_CONFIG_CONFIRM.\n',msgType);
  config = [];
  
else
   msgId = typecast([msg(4) msg(3)],'uint16');  % msgId in confirm should be equal to msgId in request
   status = typecast([msg(8) msg(7) msg(6) msg(5)],'uint32');
end
