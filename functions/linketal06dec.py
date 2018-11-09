# Generated with SMOP  0.41
from libsmop import *
# linketal06dec.m

    
    
@function
def linketal06dec(xx=None,*args,**kwargs):
    varargin = linketal06dec.varargin
    nargin = linketal06dec.nargin

    ##########################################################################
    
    # LINKLETTER ET AL. (2006) DECREASING COEFFICIENTS FUNCTION
    
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
    
    # xx = [x1, x2, ..., x10]
    
    #########################################################################
    
    x1=xx(1)
# linketal06dec.m:36
    x2=xx(2)
# linketal06dec.m:37
    x3=xx(3)
# linketal06dec.m:38
    x4=xx(4)
# linketal06dec.m:39
    x5=xx(5)
# linketal06dec.m:40
    x6=xx(6)
# linketal06dec.m:41
    x7=xx(7)
# linketal06dec.m:42
    x8=xx(8)
# linketal06dec.m:43
    term1=dot(0.2,x1) + dot((0.2 / 2),x2)
# linketal06dec.m:45
    term2=dot((0.2 / 4),x3) + dot((0.2 / 8),x4)
# linketal06dec.m:46
    term3=dot((0.2 / 16),x5) + dot((0.2 / 32),x6)
# linketal06dec.m:47
    term4=dot((0.2 / 64),x7) + dot((0.2 / 128),x8)
# linketal06dec.m:48
    y=term1 + term2 + term3 + term4
# linketal06dec.m:50
    return y
    
if __name__ == '__main__':
    pass
    