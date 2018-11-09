# Generated with SMOP  0.41
from libsmop import *
# roosarn63.m

    
    
@function
def roosarn63(xx=None,*args,**kwargs):
    varargin = roosarn63.varargin
    nargin = roosarn63.nargin

    ##########################################################################
    
    # ROOS & ARNOLD (1963) FUNCTION
    
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
    
    #########################################################################
    
    d=length(xx)
# roosarn63.m:36
    prod=1
# roosarn63.m:37
    for ii in arange(1,d).reshape(-1):
        xi=xx(ii)
# roosarn63.m:40
        new=abs(dot(4,xi) - 2)
# roosarn63.m:41
        prod=dot(prod,new)
# roosarn63.m:42
    
    y=copy(prod)
# roosarn63.m:45
    return y
    
if __name__ == '__main__':
    pass
    