# Generated with SMOP  0.41
from libsmop import *
# soblev99.m

    
    
@function
def soblev99(xx=None,b=None,c0=None,*args,**kwargs):
    varargin = soblev99.varargin
    nargin = soblev99.nargin

    ##########################################################################
    
    # SOBOL' & LEVITAN (1999) FUNCTION
    
    # Authors: Sonja Surjanovic, Simon Fraser University
#          Derek Bingham, Simon Fraser University
# Questions/Comments: Please email Derek Bingham at dbingham@stat.sfu.ca.
    
    # Copyright 2013. Derek Bingham, Simon Fraser University.
    
    # THERE IS NO WARRANTY, EXPRESS OR IMPLIED. WE DO NOT ASSUME ANY LIABILITY
# FOR THE USE OF THIS SOFTWARE.  If software is modified to produce
# derivative works, such modified software should be clearly marked.
# Additionally, this program is free software; you can redistribute it 
# and/or modify it under the terms of the GNU General Public License as 
# published by the Free Software Foundation; version 2.0 of the License. 
# Accordingly, this program is distributed in the hope that it will be 
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty 
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# General Public License for more details.
    
    # For function details and reference information, see:
# http://www.sfu.ca/~ssurjano/
    
    ##########################################################################
    
    # INPUTS:
    
    # xx = [x1, x2, ..., xd]
# b  = d-dimensional vector (optional), with default value
#      [2, 1.95, 1.9, 1.85, 1.8, 1.75, 1.7, 1.65, 0.4228, 0.3077, 0.2169,
#       0.1471, 0.0951, 0.0577, 0.0323, 0.0161, 0.0068, 0.0021, 0.0004, 0]
#      (when d<=20)
# c0 = constant term (optional), with default value 0
    
    ##########################################################################
    
    d=length(xx)
# soblev99.m:41
    if (nargin == 1):
        if (d <= 20):
            b=concat([2,1.95,1.9,1.85,1.8,1.75,1.7,1.65,0.4228,0.3077,0.2169,0.1471,0.0951,0.0577,0.0323,0.0161,0.0068,0.0021,0.0004,0])
# soblev99.m:45
        else:
            error('Value of the d-dimensional vector b is required.')
        c0=0
# soblev99.m:49
    else:
        if (nargin == 2):
            c0=0
# soblev99.m:51
    
    
    Id=1
# soblev99.m:54
    for ii in arange(1,d).reshape(-1):
        bi=b(ii)
# soblev99.m:56
        new=(exp(bi) - 1) / bi
# soblev99.m:57
        Id=dot(Id,new)
# soblev99.m:58
    
    sum=0
# soblev99.m:61
    for ii in arange(1,d).reshape(-1):
        bi=b(ii)
# soblev99.m:63
        xi=xx(ii)
# soblev99.m:64
        sum=sum + dot(bi,xi)
# soblev99.m:65
    
    y=exp(sum) - Id + c0
# soblev99.m:68
    return y
    
if __name__ == '__main__':
    pass
    