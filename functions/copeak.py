# Generated with SMOP  0.41
from libsmop import *
# copeak.m

    
    
@function
def copeak(xx=None,u=None,a=None,*args,**kwargs):
    varargin = copeak.varargin
    nargin = copeak.nargin

    ##########################################################################
    
    # CORNER PEAK INTEGRAND FAMILY
    
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
# copeak.m:39
    if (nargin == 1):
        u=repmat(0.5,1,d)
# copeak.m:42
        a=repmat(5,1,d)
# copeak.m:43
    else:
        if (nargin == 2):
            a=repmat(5,1,d)
# copeak.m:45
    
    sum=0
# copeak.m:48
    for ii in arange(1,d).reshape(-1):
        xi=xx(ii)
# copeak.m:50
        ai=a(ii)
# copeak.m:51
        sum=sum + dot(ai,xi)
# copeak.m:52
    
    y=(1 + sum) ** (- d - 1)
# copeak.m:55
    return y
    
if __name__ == '__main__':
    pass
    