function rangingDemo(reqId,respId,windowSize)
% rcmSampleMain Sample RCM interface function.
%
% Syntax
% rangingDemo('100','102')
% where '100' is a string with the ID of the requester (connected to the laptop
% via ethernet) and '102' is the ID of the (remote) responder
% Defaults set to '100' and '102'
%
% Input
% reqId - string containing the last octet of the IP address (e.g. 192.168.1.100)
% respId - string containing  ID for responder RCM
% windowSize - the length of the plot window (default is 50 points)
%
% Output
% NONE
%
% Usage Notes
% Connects to RCM through a UDP socket, gets the RCM configuration, and sends
% range requests to another specified RCM.
%
% See also rcmGetConfig, rcmSendRangeRequest, rcmReceiveData

% Copyright © 2012 Time Domain, Huntsville, AL
% If you make this better please send a copy to
% Brandon.Dewberry@timedomain.com

%%=============================================
% NOTE: this converts input reqID  to reqIP (IP address)
if exist('reqId')
  reqIp = ['192.168.1.' num2str(reqId)];
else
  reqIp = '192.168.1.102'; % Default requester IP
end

if ~exist('respId')
  respId = 103; % Default responder ID
end

if ~exist('windowSize')
  windowSize = 50;  % Default range window size
end
  
%build the GUI
mp = get(0,'monitorpositions');
scrn0Left = mp(1,1);  scrn0Bottom = mp(1,2); scrn0Width = mp(1,3); scrn0Height = mp(1,4);
fh = figure('Position',[scrn0Left+10 scrn0Bottom+20 scrn0Width-50 scrn0Height-20]);
set(fh,'menubar','none');

% Display the number of attempts
msgIdDispHdl = uicontrol('style','text', ...
   'string','1', ...
   'fontsize',16, ...
   'units','normalized',...
   'position',[.8 .3 .1 .03]);
%   'backgroundcolor','y');

% Pause button
pauseBtnHdl = uicontrol('style','pushbutton',...
   'string','Pause', ...
   'fontsize',16, ...
   'callback',@cbk_fcn, ...
   'units', 'Normalized', ...
   'position',[.8 .25 .1 .04],...
   'UserData',false);

% Quit button
quitBtnHdl = uicontrol('style','pushbutton',...
   'string','Quit', ...
   'fontsize',16, ...
   'callback',@cbk_fcn, ...
   'units', 'Normalized', ...
   'position',[.8 .2 .1 .04],...
   'UserData',false);
            
rangeTextHandle = uicontrol('Style','Text', ...
   'String', '000.00', ...
   'FontSize', 108, ...
   'units', 'Normalized', ...
   'Position', [0.75 .65 .25 .2]);%, ...
%   'BackgroundColor','y');
parentColor = get(get(rangeTextHandle, 'parent'), 'color');
set(rangeTextHandle,'foregroundcolor', [0 0 0], ...
      'backgroundcolor', parentColor);

import java.net.DatagramSocket

% Get the RCM configuration.
[socket,config] = rcmGetConfig(reqIp);

%% Uncomment this to change configuration parameters.
% Leave commented to accept the defaults from the radio
% config.pii = 7;  % This must match the responder
% config.codeChnl = 6; % This must match the responder
% config.txPwr = 10;
 config.flags = 1; % make sure scan data is set (not default)
 config.persistFlag = 0;  % Don't change this in flash
% 
status = rcmSetConfig(socket,reqIp,config);

%% Print the default config parameters
config


% Loop over number of ranges.  Stop with the stop button is pressed
msgId = 0;
T = []; prmVec = []; freVec = []; frvVec = [];
stop = false; freeze = false;
nAttempts = 0; nSuccesses = 0;
n = 0;
while ~stop
   
  % Freeze means 'pause'
  if (~freeze)
    n = n + 1;

    %% Create and send a range request message to the connected RCM
    msgId = mod(msgId + 1,double(intmax('uint16'))+1);
    % This function automatically waits for the response
    [status,msgIdCfrm] = rcmSendRangeRequest(socket,reqIp,msgId,respId);
    nAttempts = nAttempts + 1;

    %% Only plot if returned successfully from rcmSendRangeRequest
    if status == 0
       [rangeInfo,dataInfo,scanInfo] = rcmReceiveInfo(socket);

       % First time through set the start time
       if n == 1
          Tstart = rangeInfo.timeStamp;
       end

       % Process based on the return from the requesting radio
       switch rangeInfo.status
       case 0 %{0 4}
          nSuccesses = nSuccesses + 1;
          fprintf('msgId:%4i stopwatch:%3d status: %3d prm range: %7.3fm filtered :%7.3fm velocity: % 5.2fcm/s\n',...
          rangeInfo.msgID, rangeInfo.stopWatch, rangeInfo.status, rangeInfo.prm/1000, rangeInfo.fre/1000, rangeInfo.frv/10);
          if nAttempts <= windowSize
             T = [T double(rangeInfo.timeStamp - Tstart)/1000.0];
             prmVec = [prmVec rangeInfo.prm/1000];
             freVec = [freVec rangeInfo.fre/1000];
             frvVec = [frvVec rangeInfo.frv/10];
          else
             T = [T(2:end) double(rangeInfo.timeStamp - Tstart)/1000];
             prmVec = [prmVec(2:end) rangeInfo.prm/1000];
             freVec = [freVec(2:end) rangeInfo.fre/1000]; 
             frvVec = [frvVec(2:end) rangeInfo.frv/10];
          end      
          % Plot Range
           subplot(4,4,[1 2 3 5 6 7]);
           hold off
           plot(T, prmVec, 'ko');
%           plot(T(end),prmVec(end),'d','MarkerEdgeColor','k','MarkerFaceColor','r','MarkerSize',10);
           hold on
           plot(T, freVec, 'b.--');
           
           axis tight
  %             set(gca,'color','none');
  %             set(gca,'FontWeight', 'bold');
            rmean = mean(prmVec);
            rstd = std(prmVec);
          title(sprintf('Req: %s, Resp: %d, mean: %5.3fm, std: %4.3fcm',...
             reqIp(end-2:end),respId, rmean, rstd*100), ...
             'FontWeight', 'bold', 'FontSize', 16);
          xlabel('Time (sec)','FontWeight', 'bold', 'FontSize', 14);
          ylabel('Range (m)','FontWeight', 'bold', 'FontSize', 14);
          set(msgIdDispHdl,'string',num2str(rangeInfo.msgID));
          legend('Raw','Filtered','Location','NorthWest')
          
          % Update Range Text
          rangeStr = sprintf('% 6.2f',rangeInfo.prm/1000);
          set(rangeTextHandle,'String',rangeStr)            
  %            set(rangeTextHandle,'String',num2str(100+rangeInfo.rngVal/1000, '% 7.2f'))

          % Plot Radial Velocity
          subplot(4,4,[9 10 11]);
          plot(T, frvVec, 'r.-');
          grid on
          ylabel({'Range Velocity', 'Estimate (cm/s)'},'FontWeight', 'bold', 'FontSize', 14);
  %            set(gca,'color','none');
         axis tight
       case 1
          fprintf('range timeout\n');
       case 2
          fprintf('LED failure\n');
       case 9
          fprintf('UDP failure on InfoReceive\n');
       otherwise
          fprintf('Unrecognized range status: %d\n',rangeInfo.rngStat);
          fprintf('msgId:%4i stopwatch:%3d status: %3d range: %7.3fm \n',rangeInfo.msgID,rangeInfo.stopWatch, rangeInfo.status, rangeInfo.prm/1000);
       end
    end

    % Process and plot scans
    if ~isempty(scanInfo)
      %fprintf('LED: %d\n',scanInfo.ldgEdgeOff);
      subplot(4,4,[13 14 15]);
      plot([0:length(scanInfo.samp)-1]*61/1000,scanInfo.samp,'b-');
      xlabel('Time (ns)','FontWeight', 'bold', 'FontSize', 14);
      ylabel('Amplitude','FontWeight', 'bold', 'FontSize', 14);
  %        set(gca,'color','none');
      line(([scanInfo.ldgEdgeOff scanInfo.ldgEdgeOff]-1)*61/1000,[min(scanInfo.samp) max(scanInfo.samp)],'Color','r','LineWidth',1); 
      axis tight
    end

  end

  drawnow;

  stop = get(quitBtnHdl,'UserData');
  freeze = get(pauseBtnHdl,'UserData');
   
end

% Close the file handles (added this early.  Maybe not necessary now?
if stop
  % Comment this out to leave the GUI displayed after hitting the quit button
  close(fh);
end

successRate = nSuccesses/nAttempts * 100;
fprintf('Success Rate = %3.2f%%\n',successRate);

%% This callback function is used by all the buttons
function cbk_fcn(obj,evt)
  switch get(obj,'String')
    case 'Quit'
      set(obj,'UserData',true)
    case 'Pause'
      set(obj,'UserData',true,'String','Resume')
    case 'Resume'
      set(obj,'UserData',false,'String','Pause')
  end
end

end


