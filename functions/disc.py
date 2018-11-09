# Generated with SMOP  0.41
from libsmop import *
# disc.m

    
    
@function
def disc(xx=None,u=None,a=None,*args,**kwargs):
    varargin = disc.varargin
    nargin = disc.nargin

    ##########################################################################
    
    # DISCONTINUOUS INTEGRAND FAMILY
    
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
# u = [u1, u2, ..., ud] (optional), with default value
#     [0.5, 0.5, ..., 0.5]
# a = [a1, a2, ..., ad] (optional), with default value [5, 5, ..., 5]
    
    ##########################################################################
    
    d=length(xx)
# disc.m:39
    if (nargin == 1):
        u=repmat(0.5,1,d)
# disc.m:42
        a=repmat(5,1,d)
# disc.m:43
    else:
        if (nargin == 2):
            a=repmat(5,1,d)
# disc.m:45
    
    x1=xx(1)
# disc.m:48
    x2=xx(2)
# disc.m:49
    u1=u(1)
# disc.m:50
    u2=u(2)
# disc.m:51
    if (x1 > u1 or x2 > u2):
        y=0
# disc.m:54
    else:
        sum=0
# disc.m:56
        for ii in arange(1,d).reshape(-1):
            xi=xx(ii)
# disc.m:58
            ai=a(ii)
# disc.m:59
            sum=sum + dot(ai,xi)
# disc.m:60
        y=exp(sum)
# disc.m:62
    
    return y
    
if __name__ == '__main__':
    pass
    