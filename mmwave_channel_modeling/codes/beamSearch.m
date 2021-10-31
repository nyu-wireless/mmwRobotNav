fc = 28e9;  % Carrier frequency
% Patch element design
elem = design(patchMicrostrip, fc);
elem.Tilt = 90;
elem.TiltAxis = [0,1,0];
% Number of antennas 
nantgNB = [4,4];
nantUE = 8;
% Construct the arrays
lambda = physconst('Lightspeed') / fc;
dsep = 0.5*lambda;
arrgNB = phased.URA(nantgNB,dsep,'ArrayNormal','x');
arrUE  = phased.ULA(nantUE,dsep);
% Create the gNB multi-array platform
narrgNB = 3;
multiArrgNB = MultiArrayPlatform('narr', narrgNB, 'elem', elem, ...
    'array', arrgNB);
multiArrgNB.alignAzimuth(0);
% Create the UE multi-array platform
narrUE = 3;
multiArrUE = MultiArrayPlatform('narr', narrUE, 'elem', elem, ...
    'array', arrUE);
multiArrUE.alignAzimuth(0);
% Create the codebook
multiArrgNB.createCodebook('layout', 'azimuth');
multiArrUE.createCodebook('layout', 'azimuth');
dirSim = DirSearchSim('tx', multiArrgNB, 'rx', multiArrUE);
%%
if ~exist('beam_search_result', 'dir')
    % create folder
    mkdir('beam_search_result');  
end

pjDir = dir('mat_data');    % ray tracing data folder struct
pjDir([1,2]) = [];    % delete '.' and '..'
nPj = length(pjDir);  % number of projects
nTx = 10;   % ten TX location for each map
nPathRecord = 5;  % use top5 eigenvalues
for iPj = 1: nPj    % print the projects name
    fprintf('%s; ', pjDir(iPj).name);
end

for iPj = 1 : nPj
    resultDir = join(['beam_search_result\',pjDir(iPj).name]);
    if ~exist(resultDir, 'dir')
    % create folder for results
        mkdir(resultDir);  
    end
    for iTx = 1: nTx
        fprintf('%d',iTx);
        fileName = strcat(pjDir(iPj).folder,'\',pjDir(iPj).name,'\',...
                    pjDir(iPj).name,'_Tx_',int2str(iTx),'_pathData.mat');
        load(fileName);
        nRx = length(pathData.rxPos);
        aoaAzResult = zeros([nRx, nPathRecord]);
        aodAzResult = zeros([nRx, nPathRecord]);
        snrResult = zeros([nRx, nPathRecord]);
        peakFracResult = zeros([nRx, nPathRecord]);
        for indRx = 1:nRx
            if pathData.linkState(indRx) ~= 0 % Not outage
                % Set the path parameters from the ray tracing data
                dirSim.setPathParams(pathData,indRx);
                % Get the RX channel response along each antenna and array
                h = dirSim.chanResp();
                hrx = dirSim.chanRespRxCw(h);
                pathEst = dirSim.estimatePaths(h, hrx);
                aoaAzResult(indRx, :) = pathEst.aoaAz;
                aodAzResult(indRx, :) = pathEst.aodAz;
                snrResult(indRx, :) = pathEst.snr;
                peakFracResult(indRx, :) = pathEst.peakFrac;
            else % outage
            end
        
            
        end
        % store in csv
        lineIndex = pathData.lineIndex;
        rxPos = pathData.rxPos;
        rxPosInd = pathData.rxPosInd;
        los = pathData.los;
        linkState = pathData.linkState;
        Nlos1st = pathData.NLOS1st;
        T = table(lineIndex, rxPos, rxPosInd,los,linkState,Nlos1st, aoaAzResult,...
            aodAzResult,snrResult, peakFracResult);
        resultFilename = strcat(resultDir, ...
            '\', pjDir(iPj).name, '_Tx_',int2str(iTx),'_beam_search.csv');
        writetable(T, resultFilename);
       
    end

    
    
end