if ~exist('mat_data', 'dir')
    % create folder
    mkdir('mat_data');  
end

pjDir = dir('ray_tracing_data');    % ray tracing data folder struct
pjDir([1,2]) = [];    % delete '.' and '..'
nPj = length(pjDir);  % number of projects
nTX = 10;   % ten TX location for each map
for iPj = 1: nPj    % print the projects
    fprintf('%s; ', pjDir(iPj).name);
end

nMaxPaths = 25;

for iPj = 1 : nPj
    matDir = join(['mat_data\',pjDir(iPj).name]);
    if ~exist(matDir, 'dir')
    % create folder
        mkdir(matDir);  
    end
    
    txPosFileName = strcat(pjDir(iPj).folder,'\',pjDir(iPj).name,'\',...
                    'tx_pos.csv');
    txPos = readmatrix(txPosFileName);
    txPos = txPos(:,2:3);
    pathData.fc = 2.8e10;
    
    for iTX = 1: nTX
%     for iTX = 10:10
        pathData = rmfield(pathData, fieldnames(pathData));
        disp(pathData);
        fileName = strcat(pjDir(iPj).folder,'\',pjDir(iPj).name,'\',...
                    pjDir(iPj).name,'_Tx_',int2str(iTX),'.csv');
        fprintf('%s; ',fileName);
        rtData = readtable(fileName,'Delimiter', ',');
        
        pathData.fc = 2.8e10;
        pathData.txPos = txPos(iTX,:)';
        pathData.rxPosInd = [rtData.rx_pos_ind_row, rtData.rx_pos_ind_column];
        pathData.rxPos = [rtData.rx_pos_x, rtData.rx_pos_y];
        pathData.lineIndex = [rtData.line_index];
        
        pathData.gain = [rtData.x1_srcvdpower];
        pathData.dly = [rtData.x1_arrival_time];
        pathData.aoaAz = [rtData.x1_aoa_az];
        pathData.aoaEl = [rtData.x1_aoa_el];
        pathData.aodAz = [rtData.x1_aod_az];
        pathData.aodEl = [rtData.x1_aod_el];
        pathData.pl = [rtData.x1_path_loss];
        
        pathData.los = logical(rtData.los);
        pathData.posStep = [0.15,0.15];
        pathData.npaths = rtData.npaths;
        pathData.linkStateLabel = {'Outage','LOS','NLOS'};
        pathData.linkState = rtData.link_state;
        pathData.NLOS1st = rtData.('x1st_NLOS');

        for i = 2:nMaxPaths
            pathData.gain = cat(2, pathData.gain, rtData.(strcat('x',int2str(i),'_srcvdpower')));
            pathData.pl = cat(2, pathData.pl, rtData.(strcat('x',int2str(i),'_path_loss')));
            pathData.dly = cat(2, pathData.dly, rtData.(strcat('x',int2str(i),'_arrival_time')));
            pathData.aoaAz = cat(2, pathData.aoaAz, rtData.(strcat('x',int2str(i),'_aoa_az')));
            pathData.aoaEl = cat(2, pathData.aoaEl, rtData.(strcat('x',int2str(i),'_aoa_el')));
            pathData.aodAz = cat(2, pathData.aodAz, rtData.(strcat('x',int2str(i),'_aod_az')));
            pathData.aodEl = cat(2, pathData.aodEl, rtData.(strcat('x',int2str(i),'_aod_el')));
        end
        pathData.aoaEl = 90 - pathData.aoaEl;
        pathData.aodEl = 90 - pathData.aodEl;
        resultFilename = strcat(matDir,'\',pjDir(iPj).name, '_Tx_',int2str(iTX),'_pathData.mat');
        save(resultFilename, 'pathData');
        
    end
end
