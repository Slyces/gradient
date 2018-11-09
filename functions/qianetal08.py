# Generated with SMOP  0.41
from libsmop import *
# qianetal08.m

    
    
@function
def qianetal08(xx=None,*args,**kwargs):
    varargin = qianetal08.varargin
    nargin = qianetal08.nargin

    ##########################################################################
    
    # QIAN ET AL. (2008) FUNCTION
    
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
    
    # xx = [x, z]
    
    #########################################################################
    
    x=xx(1)
# qianetal08.m:36
    z=xx(2)
# qianetal08.m:37
    if (z == 1):
        c=1.4
# qianetal08.m:40
    else:
        if (z == 2):
            c=3
# qianetal08.m:42
    
    y=dot(exp(dot(c,x)),cos(dot(dot(7,pi),x) / 2))
# qianetal08.m:45
    return y
    
if __name__ == '__main__':
    pass
    