function [socket,config] = rcmGetConfig(rcmIp)
% rcmGetConfig Sample function to get RCM configuration.
%
% Syntax
% rcmGetConfig(rcmIp)
%
% Input
% rcmIp - string containing IP address (e.g. 192.168.1.100)
%
% Output
% socket - Java DatagramSocket object
% config - structure containing RCM configuration
%
% Usage Notes
% Creates a UDP socket. The socket is returned for use by other functions.
%
% Sends a request to get RCM configuration and receives the response from
% RCM. The config structure is returned.
%
% The message ID is set to 0 in this example, but a specific application can be
% set it to any value within UINT16 range.
%
% References
% "A simple UDP communications application" by Kevin Bartlett
% MATLAB Central File Exchange
% http://www.mathworks.com/matlabcentral/fileexchange/24525-a-simple-udp-communications-application
%
% See also rcmSampleMain

% Copyright © 2012 Time Domain, Huntsville, AL


import java.io.*
import java.net.DatagramSocket
import java.net.DatagramPacket
import java.net.InetAddress

port = 21210;  % RCM port.

%% Send RCM_GET_CONFIG_REQUEST
% NOTE: The interface requires bytes (int8). Intel machines are little-endian so
% swapbytes is necessary.

% RCM_GET_CONFIG_REQUEST message type.
MSG_TYPE = uint16(hex2dec('0002'));  
MSG_ID = uint16(hex2dec('0000'));

RCM_GET_CONFIG_REQUEST = typecast(swapbytes([MSG_TYPE MSG_ID]),'uint8');

% TRY/CATCH is used to close the socket in case of an error. Otherwise
% MATLAB must be restarted to use the socket again.
try
  socket = DatagramSocket;
  socket.setReuseAddress(1);
  
  addr = InetAddress.getByName(rcmIp);

  packet = DatagramPacket(RCM_GET_CONFIG_REQUEST,length(RCM_GET_CONFIG_REQUEST),addr,port);

  socket.send(packet);

catch sendPacketError
  try
    socket.close
  catch closeError
  end
  error('%s.m--Failed to send UDP packet.\n%s',mfilename,sendPacketError.message);

end

%% Receive RCM_GET_CONFIG_CONFIRM
timeout = 200;  % Max time to wait for confirm in milliseconds

PACKET_LENGTH = 32;  % RCM_GET_CONFIG_CONFIRM message length (bytes).

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

if msgType ~= uint16(hex2dec('0102'))
  fprintf('Message type %04x does not match RCM_GET_CONFIG_CONFIRM.\n',msgType);
  config = [];
  
else
  config.msgID = typecast([msg(4) msg(3)],'uint16');
  config.nodeID = typecast([msg(8) msg(7) msg(6) msg(5)],'uint32');
  config.PII = typecast([msg(10) msg(9)],'uint16');
  config.antMode = uint8(msg(11));
  config.codeChnl = uint8(msg(12));
  config.antDlyA = typecast([msg(16) msg(15) msg(14) msg(13)],'uint32');
  config.antDlyB = typecast([msg(20) msg(19) msg(18) msg(17)],'uint32');
  config.flags = typecast([msg(22) msg(21)],'uint16');
  config.txPwr = uint8(msg(23));
  unused = uint8(msg(24));
  config.timeStamp = typecast([msg(28) msg(27) msg(26) msg(25)],'uint32');
  config.stat = typecast([msg(32) msg(31) msg(30) msg(29)],'uint32');
end
