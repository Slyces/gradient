# Generated with SMOP  0.41
from libsmop import *
# rothyp.m

    
    
@function
def rothyp(xx=None,*args,**kwargs):
    varargin = rothyp.varargin
    nargin = rothyp.nargin

    ##########################################################################
    
    # ROTATED HYPER-ELLIPSOID FUNCTION
    
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
    
    # INPUT:
    
    # xx = [x1, x2, ..., xd]
    
    ##########################################################################
    
    d=length(xx)
# rothyp.m:36
    outer=0
# rothyp.m:37
    for ii in arange(1,d).reshape(-1):
        inner=0
# rothyp.m:40
        for jj in arange(1,ii).reshape(-1):
            xj=xx(jj)
# rothyp.m:42
            inner=inner + xj ** 2
# rothyp.m:43
        outer=outer + inner
# rothyp.m:45
    
    y=copy(outer)
# rothyp.m:48
    return y
    
if __name__ == '__main__':
    pass
    