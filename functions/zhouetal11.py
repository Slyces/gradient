# Generated with SMOP  0.41
from libsmop import *
# zhouetal11.m

    
    
@function
def zhouetal11(xx=None,*args,**kwargs):
    varargin = zhouetal11.varargin
    nargin = zhouetal11.nargin

    ##########################################################################
    
    # ZHOU ET AL. (2011) FUNCTION
    
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
#
    
    ##########################################################################
    
    # INPUT:
    
    # xx = [x, z]
    
    #########################################################################
    
    x=xx(1)
# zhouetal11.m:36
    z=xx(2)
# zhouetal11.m:37
    sign=1
# zhouetal11.m:39
    if (z == 1):
        c=6.8
# zhouetal11.m:42
    else:
        if (z == 2):
            c=7
# zhouetal11.m:44
            sign=- 1
# zhouetal11.m:45
        else:
            if (z == 3):
                c=7.2
# zhouetal11.m:47
    
    y=dot(sign,cos(dot(dot(c,pi),x) / 2))
# zhouetal11.m:50
    return y
    
if __name__ == '__main__':
    pass
    