# Generated with SMOP  0.41
from libsmop import *
# moon10low.m

    
    
@function
def moon10low(xx=None,*args,**kwargs):
    varargin = moon10low.varargin
    nargin = moon10low.nargin

    ##########################################################################
    
    # MOON (2010) LOW-DIMENSIONALITY FUNCTION
    
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
    
    # xx = [x1, x2, x3]
    
    #########################################################################
    
    x1=xx(1)
# moon10low.m:36
    x2=xx(2)
# moon10low.m:37
    x3=xx(3)
# moon10low.m:38
    y=x1 + x2 + dot(dot(3,x1),x3)
# moon10low.m:40
    return y
    
if __name__ == '__main__':
    pass
    