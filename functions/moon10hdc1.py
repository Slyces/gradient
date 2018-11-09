# Generated with SMOP  0.41
from libsmop import *
# moon10hdc1.m

    
    
@function
def moon10hdc1(xx=None,*args,**kwargs):
    varargin = moon10hdc1.varargin
    nargin = moon10hdc1.nargin

    ##########################################################################
    
    # MOON (2010) HIGH-DIMENSIONALITY FUNCTION, C-1
# This function is a modification of the function moon10hd.m.
    
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
    
    # xx = [x1, x2, ..., x20]
    
    #########################################################################
    
    x1=xx(1)
# moon10hdc1.m:37
    x7=xx(7)
# moon10hdc1.m:38
    x12=xx(12)
# moon10hdc1.m:39
    x18=xx(18)
# moon10hdc1.m:40
    x19=xx(19)
# moon10hdc1.m:41
    term1=dot(dot(- 19.71,x1),x18) + dot(dot(23.72,x1),x19)
# moon10hdc1.m:43
    term2=dot(- 13.34,x19 ** 2) + dot(dot(28.99,x7),x12)
# moon10hdc1.m:44
    y=term1 + term2
# moon10hdc1.m:46
    return y
    
if __name__ == '__main__':
    pass
    