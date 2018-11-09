# Generated with SMOP  0.41
from libsmop import *
# park91b.m

    
    
@function
def park91b(xx=None,*args,**kwargs):
    varargin = park91b.varargin
    nargin = park91b.nargin

    ##########################################################################
    
    # PARK (1991) FUNCTION 2
    
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
    
    # xx = [x1, x2, x3, x4]
    
    #########################################################################
    
    x1=xx(1)
# park91b.m:36
    x2=xx(2)
# park91b.m:37
    x3=xx(3)
# park91b.m:38
    x4=xx(4)
# park91b.m:39
    term1=dot((2 / 3),exp(x1 + x2))
# park91b.m:41
    term2=dot(- x4,sin(x3))
# park91b.m:42
    term3=copy(x3)
# park91b.m:43
    y=term1 + term2 + term3
# park91b.m:45
    return y
    
if __name__ == '__main__':
    pass
    