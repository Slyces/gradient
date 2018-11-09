# Generated with SMOP  0.41
from libsmop import *
# loepetal13.m

    
    
@function
def loepetal13(xx=None,*args,**kwargs):
    varargin = loepetal13.varargin
    nargin = loepetal13.nargin

    ##########################################################################
    
    # LOEPPKY ET AL. (2013) FUNCTION
    
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
# loepetal13.m:36
    x2=xx(2)
# loepetal13.m:37
    x3=xx(3)
# loepetal13.m:38
    x4=xx(4)
# loepetal13.m:39
    x5=xx(5)
# loepetal13.m:40
    x6=xx(6)
# loepetal13.m:41
    x7=xx(7)
# loepetal13.m:42
    term1=dot(6,x1) + dot(4,x2)
# loepetal13.m:44
    term2=dot(5.5,x3) + dot(dot(3,x1),x2)
# loepetal13.m:45
    term3=dot(dot(2.2,x1),x3) + dot(dot(1.4,x2),x3)
# loepetal13.m:46
    term4=x4 + dot(0.5,x5)
# loepetal13.m:47
    term5=dot(0.2,x6) + dot(0.1,x7)
# loepetal13.m:48
    y=term1 + term2 + term3 + term4 + term5
# loepetal13.m:50
    return y
    
if __name__ == '__main__':
    pass
    