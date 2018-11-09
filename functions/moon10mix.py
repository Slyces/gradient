# Generated with SMOP  0.41
from libsmop import *
# moon10mix.m

    
    
@function
def moon10mix(xx=None,*args,**kwargs):
    varargin = moon10mix.varargin
    nargin = moon10mix.nargin

    ##########################################################################
    
    # MOON (2010) MIXED FUNCTION
    
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
    
    # xx = [x1, x2, z]
    
    #########################################################################
    
    x1=xx(1)
# moon10mix.m:36
    x2=xx(2)
# moon10mix.m:37
    z=xx(3)
# moon10mix.m:38
    if (z == 1):
        term1=x1 + x2
# moon10mix.m:41
    else:
        if (z != 1):
            term1=0
# moon10mix.m:43
    
    if (z == 2):
        term2=dot(3,x1)
# moon10mix.m:47
    else:
        if (z != 2):
            term2=0
# moon10mix.m:49
    
    y=term1 + term2
# moon10mix.m:52
    return y
    
if __name__ == '__main__':
    pass
    