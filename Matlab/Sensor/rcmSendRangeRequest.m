function [status,msgIdCfrm] = rcmSendRangeRequest(socket,rcmIp,msgId,rangeRespId)
% rcmSendRangeRequest Sample function to send range request to RCM.
%
% Syntax
% rcmSendRangeRequest(socket,rcmIp,msgId,rangeRespId)
%
% Input
% socket - Java DatagramSocket object
% rcmIp - string containing IP address (e.g. 192.168.1.100)
% msgId - integer containing message ID
% rangeRespId - integer containing P400 ID for range response
%
% Output
% status - integer status of range request (0 = success, ~0 = fail)
% msgIdCfrm - integer containing confirm message ID
%
% Usage Notes
% Uses the provided socket to send a range request and receive the range
% request confirmation.
%
% References
% "A simple UDP communications application" by Kevin Bartlett
% MATLAB Central File Exchange
% http://www.mathworks.com/matlabcentral/fileexchange/24525-a-simple-udp-communications-application
%
% See also rcmSampleMain

% Copyright © 2011 Time Domain, Huntsville, AL


import java.net.InetAddress
import java.net.DatagramPacket

port = 21210;  % RCM port.

%% Send RCM_SEND_RANGE_REQUEST
MSG_TYPE = uint16(hex2dec('0003'));  % RCM_SEND_RANGE_REQUEST message type.
MSG_ID = uint16(msgId);
RESP_ID = uint32(rangeRespId);
ANT_MODE = uint8(0);
RESERVED = uint8(0);
DATA_SIZE = uint16(0);
DATA = uint8([]);

RCM_SEND_RANGE_REQUEST = ...
  [typecast(swapbytes(MSG_TYPE),'uint8'), ...
  typecast(swapbytes(MSG_ID),'uint8'), ...
  typecast(swapbytes(RESP_ID),'uint8'), ...
  ANT_MODE, RESERVED, ...
  typecast(swapbytes(DATA_SIZE),'uint8'), ...
  DATA];

try
  addr = InetAddress.getByName(rcmIp);
  
  packet = DatagramPacket(RCM_SEND_RANGE_REQUEST, length(RCM_SEND_RANGE_REQUEST), addr, port);
  
  socket.send(packet);

catch sendPacketError
  try
    socket.close;
  catch closeError
  end
  error('%s.m--Failed to send UDP packet.\n%s',mfilename,sendPacketError.message);
end

%% Receive RCM_SEND_RANGE_CONFIRM
timeout = 300;  % ms

packetLength = 8;  % RCM_SEND_RANGE_CONFIRM message length (bytes).

try
  socket.setSoTimeout(timeout);
  
  packet = DatagramPacket(zeros(1,packetLength,'uint8'),packetLength);
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

%% Extract message parameters.
% See the RCM API for message parameters.
msgType = typecast([msg(2) msg(1)],'uint16');

if msgType ~= uint16(hex2dec('0103'))
  fprintf('Message type %04x does not match RCM_SEND_RANGE_CONFIRM.\n',msgType);
  status = 1;
  msgIdCfrm = [];
  
else
  msgIdCfrm = typecast([msg(4) msg(3)],'uint16');
  status = typecast([msg(8) msg(7) msg(6) msg(5)],'uint32');

end
