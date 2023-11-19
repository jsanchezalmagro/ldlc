% tx_ASM.m - ASM
%
% Adds the ASM header
%
% Creation:     16/01/2020
% Author:       P.M. Rodriguez / V. Sanchez
% Copyright:    SENER Aerespacial
%
% Output parameters:

% 
% Input parameters:

function [myStruct] = json2struc(fileName)

%------------------------------------------------------------------------------
% Input arguments checking
%------------------------------------------------------------------------------
switch(nargin)
  case 1
    if exist(fileName) == 0
      error('File not find')
    end
  case 3
    otherwise        
    error('Aditional argument');
end

fid = fopen(fileName); 
raw = fread(fid,inf); 
str = char(raw'); 
fclose(fid); 
myStruct=struct();
myStruct=jsondecode(str);
