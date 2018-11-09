# Generated with SMOP  0.41
from libsmop import *
# gfunc.m

    
    
@function
def gfunc(xx=None,a=None,*args,**kwargs):
    varargin = gfunc.varargin
    nargin = gfunc.nargin

    ##########################################################################
    
    # G-FUNCTION
    
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
# a = [a1, a2, ..., ad] (optional), with default values given by Crestaux
#     et al. (2007)
    
    #########################################################################
    
    d=length(xx)
# gfunc.m:38
    if (nargin == 1):
        a=zeros(1,d)
# gfunc.m:41
        for ii in arange(1,d).reshape(-1):
            a[ii]=(ii - 1) / 2
# gfunc.m:43
    
    prod=1
# gfunc.m:47
    for ii in arange(1,d).reshape(-1):
        xi=xx(ii)
# gfunc.m:49
        ai=a(ii)
# gfunc.m:50
        new1=abs(dot(4,xi) - 2) + ai
# gfunc.m:51
        new2=1 + ai
# gfunc.m:52
        prod=dot(prod,new1) / new2
# gfunc.m:53
    
    y=copy(prod)
# gfunc.m:56
    return y
    
if __name__ == '__main__':
    pass
    