# Generated with SMOP  0.41
from libsmop import *
# hanetal09.m

    
    
@function
def hanetal09(xx=None,b=None,*args,**kwargs):
    varargin = hanetal09.varargin
    nargin = hanetal09.nargin

    ##########################################################################
    
    # HAN ET AL. (2009) FUNCTION
    
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
    
    # xx = [x, z]
# b = [b01, b02, b03, b11, b12, b13, b21, b22, b23] (optional)
    
    #########################################################################
    
    x=xx(1)
# hanetal09.m:37
    z=xx(2)
# hanetal09.m:38
    if (nargin == 1):
        b=concat([1,0,- 1,6,4,5,- 6,- 6,- 6])
# hanetal09.m:41
    
    b01=b(1)
# hanetal09.m:44
    b11=b(4)
# hanetal09.m:45
    b21=b(7)
# hanetal09.m:46
    b02=b(2)
# hanetal09.m:47
    b12=b(5)
# hanetal09.m:48
    b22=b(8)
# hanetal09.m:49
    b03=b(3)
# hanetal09.m:50
    b13=b(6)
# hanetal09.m:51
    b23=b(9)
# hanetal09.m:52
    if (z == 1):
        y=b01 + dot(b11,x) + dot(b21,x ** 2)
# hanetal09.m:55
    else:
        if (z == 2):
            y=b02 + dot(b12,x) + dot(b22,x ** 2)
# hanetal09.m:57
        else:
            if (z == 3):
                y=b03 + dot(b13,x) + dot(b23,x ** 2)
# hanetal09.m:59
    
    return y
    
if __name__ == '__main__':
    pass
    