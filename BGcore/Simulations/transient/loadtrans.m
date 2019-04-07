function [dataX, dataY] = loadtrans(path)
%path = '/Users/kimhedelin/Documents/THESIS_LOCAL/data/first100/';
%d = dir(path);
%for n = 3:length(d)
%    disp(d(n).name)
    
% Loads D1
dataX.D1 = [];
dataX.D2 = [];
dataX.GPTI = [];
dataX.GPTA = [];
dataX.STN = [];
dataX.GPI = [];

dataY.D1 = [];
dataY.D2 = [];
dataY.GPTI = [];
dataY.GPTA = [];
dataY.STN = [];
dataY.GPI = [];



d = dir(path);
for n = 3:length(d)
    file = split(d(n).name,'-');
    
    switch char(file(1))
        case 'D1'
            dat = load(fullfile(path,d(n).name));
            dataX.D1 = [dataX.D1 ; dat(:,2)];
            dataY.D1 = [dataY.D1 ; dat(:,1)];
        case 'D2'
            dat = load(fullfile(path,d(n).name));
            dataX.D2 = [dataX.D2 ; dat(:,2)];
            dataY.D2 = [dataY.D2 ; dat(:,1)];
        case 'GPTI'
            dat = load(fullfile(path,d(n).name));
            dataX.GPTI = [dataX.GPTI ; dat(:,2)];
            dataY.GPTI = [dataY.GPTI ; dat(:,1)];
        case 'GPTA'
            dat = load(fullfile(path,d(n).name));
            dataX.GPTA = [dataX.GPTA ; dat(:,2)];
            dataY.GPTA = [dataY.GPTA ; dat(:,1)];
        case 'STN'
            dat = load(fullfile(path,d(n).name));
            dataX.STN = [dataX.STN ; dat(:,2)];
            dataY.STN = [dataY.STN ; dat(:,1)];
        
        case 'GPI'
            dat = load(fullfile(path,d(n).name));
            dataX.GPI = [dataX.GPI ; dat(:,2)];
            dataY.GPI = [dataY.GPI ; dat(:,1)];
            
            
    end
        
    
    
 
    
    
    
    
 



end