# Generated with SMOP  0.41
from libsmop import *
# morretal06.m

    
    
@function
def morretal06(xx=None,k1=None,*args,**kwargs):
    varargin = morretal06.varargin
    nargin = morretal06.nargin

    ##########################################################################
    
    # MORRIS ET AL. (2006) FUNCTION
    
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
    
    # xx = [x1, x2, ..., x30]
# k1 = number of arguments with an effect (optional), with default value
#      2
    
    #########################################################################
    
    if (nargin == 1):
        k1=2
# morretal06.m:39
    
    alpha=sqrt(12) - dot(dot(6,sqrt(0.1)),sqrt(k1 - 1))
# morretal06.m:42
    beta=dot(dot(12,sqrt(0.1)),sqrt(k1 - 1))
# morretal06.m:43
    outer=0
# morretal06.m:45
    for ii in arange(1,k1).reshape(-1):
        xi=xx(ii)
# morretal06.m:47
        inner=0
# morretal06.m:48
        for jj in arange((ii + 1),k1).reshape(-1):
            xj=xx(jj)
# morretal06.m:50
            inner=inner + dot(xi,xj)
# morretal06.m:51
        outer=outer + xi + dot(beta,inner)
# morretal06.m:53
    
    y=dot(alpha,outer)
# morretal06.m:56
    return y
    
if __name__ == '__main__':
    pass
    