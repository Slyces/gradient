# Generated with SMOP  0.41
from libsmop import *
# powersum.m

    
    
@function
def powersum(xx=None,b=None,*args,**kwargs):
    varargin = powersum.varargin
    nargin = powersum.nargin

    ##########################################################################
    
    # POWER SUM FUNCTION
    
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
#      [8, 18, 44, 114] (when d=4)
    
    ##########################################################################
    
    d=length(xx)
# powersum.m:38
    if (nargin == 1):
        if (d == 4):
            b=concat([8,18,44,114])
# powersum.m:42
        else:
            error('Value of the d-dimensional vector b is required.')
    
    outer=0
# powersum.m:48
    for ii in arange(1,d).reshape(-1):
        inner=0
# powersum.m:51
        for jj in arange(1,d).reshape(-1):
            xj=xx(jj)
# powersum.m:53
            inner=inner + xj ** ii
# powersum.m:54
        outer=outer + (inner - b(ii)) ** 2
# powersum.m:56
    
    y=copy(outer)
# powersum.m:59
    return y
    
if __name__ == '__main__':
    pass
    