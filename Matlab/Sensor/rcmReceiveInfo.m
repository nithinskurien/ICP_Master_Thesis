function [rangeInfo,dataInfo,scanInfo] = rcmReceiveInfo(socket)
% rcmReceiveInfo Sample function to receive information from RCM.
%
% Syntax
% rcmReceiveInfo(socket)
%
% Input
% socket - Java DatagramSocket object
%
% Output
% rangeInfo - structure containing range information
% dataInfo - structure containing data information
% scanInfo - structure containing scan information
%
% Usage Notes
% Receives range information resulting from a range request. Also receives data
% information and scan information if available.
%
% References
% "A simple UDP communications application" by Kevin Bartlett
% MATLAB Central File Exchange
% http://www.mathworks.com/matlabcentral/fileexchange/24525-a-simple-udp-communications-application
%
% See also rangingDemo.m

% Copyright © 2012 Time Domain, Huntsville, AL

import java.net.InetAddress
import java.net.DatagramPacket

rangeInfo = [];
scanInfo = [];
dataInfo = [];

timeout = 500;  % ms

packetLength = 1500;  % Largest expected UDP packet (bytes).

rngInfoRcvd = false;

while ~rngInfoRcvd
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
%      fprintf('Java error message follows:\n%s\n',receiveError.message);    
    else
      errorStr = sprintf('%s.m--Failed to receive UDP packet.\nJava error message follows:\n%s',mfilename,receiveError.message);
    end
    try
      %socket.close;
    catch closeError
    end
      fprintf('ERROR: %s\n',errorStr);  % Don't stop on a UDP blunder
      rangeInfo.rngStat = 9;  % This is not normal but makes the logic work.
      return
    %error(errorStr);
  end

  msgType = typecast([msg(2) msg(1)],'uint16');

  switch msgType
    case uint16(hex2dec('0201'))  % RCM_RANGE_INFO message type.
      rangeInfo = parseRangeInfo(msg);
      rngInfoRcvd = true;  % RCM_RANGE_INFO is always last.

    case uint16(hex2dec('0202'))  % RCM_DATA_INFO message type.
      dataInfo = parseDataInfo(msg);

    case uint16(hex2dec('0203'))  % RCM_SCAN_INFO message type.
      scanInfo = parseScanInfo(msg);
  end

end


function rangeInfo = parseRangeInfo(msg)

% See the RCM API for message parameters.
rangeInfo.msgID = typecast([msg(4) msg(3)],'uint16');
rangeInfo.rspID = typecast([msg(8) msg(7) msg(6) msg(5)],'uint32');
rangeInfo.status = uint8(msg(9));
rangeInfo.antMode = uint8(msg(10));
rangeInfo.stopWatch = typecast([msg(12) msg(11)],'uint16');  % ms
rangeInfo.prm = double(typecast([msg(16) msg(15) msg(14) msg(13)],'uint32'));  % mm
rangeInfo.cre = double(typecast([msg(20) msg(19) msg(18) msg(17)],'uint32'));  % mm
rangeInfo.fre = double(typecast([msg(24) msg(23) msg(22) msg(21)],'uint32'));  % mm
rangeInfo.prme = double(typecast([msg(26) msg(25)],'uint16'));  % mm
rangeInfo.cree = double(typecast([msg(28) msg(27)],'uint16'));  % mm
rangeInfo.free = double(typecast([msg(30) msg(29)],'uint16'));  % mm
rangeInfo.frv = double(typecast([msg(32) msg(31)],'int16'));  % mm/s
rangeInfo.frve = double(typecast([msg(34) msg(33)],'uint16'));  % mm/s
rangeInfo.measType = uint8(msg(35));
rangeInfo.reserved = uint8(msg(36));
rangeInfo.reqFlags = double(typecast([msg(38) msg(37)],'uint16'));
rangeInfo.rspFlags = double(typecast([msg(40) msg(39)],'uint16'));
rangeInfo.channelRise = typecast([msg(42) msg(41)],'uint16');
rangeInfo.vpeak = typecast([msg(44) msg(43)],'uint16');
rangeInfo.coarseTOF = double(typecast([msg(48) msg(47) msg(46) msg(45)],'uint32'));
rangeInfo.timeStamp = typecast([msg(52) msg(51) msg(50) msg(49)],'uint32');  % ms

return


function dataInfo = parseDataInfo(msg)

% See the RCM API for message parameters.
dataInfo.msgId = typecast([msg(4) msg(3)],'uint16');
dataInfo.sourceId = typecast([msg(8) msg(7) msg(6) msg(5)],'uint32');
dataInfo.scanQlty = typecast([msg(12) msg(11) msg(10) msg(9)],'uint32');
dataInfo.RSSI = typecast([msg(16) msg(15) msg(14) msg(13)],'uint32');
dataInfo.timeStamp = typecast([msg(20) msg(19) msg(18) msg(17)],'uint32');  % ms
dataInfo.antMode = uint8(msg(21));
dataInfo.reserved = uint8(msg(22));
dataInfo.dataSz = typecast([msg(24) msg(23)],'uint16');
% Data bytes. Interpretation depends on application.
dataInfo.data = int8(msg(25:end));

return


function scanInfo = parseScanInfo(msg)

% See the RCM API for message parameters.
scanInfo.msgID = typecast([msg(4) msg(3)],'uint16');
scanInfo.sourceID = typecast([msg(8) msg(7) msg(6) msg(5)],'uint32');
scanInfo.antMode = uint8(msg(9));
scanInfo.reserved = uint8(msg(10));
scanInfo.ledFlags = typecast([msg(12) msg(11)],'uint16');
scanInfo.channelRise = typecast([msg(14) msg(13)],'uint16');
scanInfo.vpeak = typecast([msg(16) msg(15)],'uint16');
scanInfo.timeStamp = typecast([msg(20) msg(19) msg(18) msg(17)],'uint32');  % ms
scanInfo.ldgEdgeOff = typecast([msg(24) msg(23) msg(22) msg(21)],'uint32');
scanInfo.lckSptOff = typecast([msg(28) msg(27) msg(26) msg(25)],'uint32');
scanInfo.numSamp = typecast([msg(32) msg(31) msg(30) msg(29)],'uint32');

for k = 1:scanInfo.numSamp
  K = 4*(k-1);  % 4 bytes per sample.
  scanInfo.samp(k) = typecast([msg(36+K) msg(35+K) msg(34+K) msg(33+K)],'int32');
end

return
