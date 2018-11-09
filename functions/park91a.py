# Generated with SMOP  0.41
from libsmop import *
# park91a.m

    
    
@function
def park91a(xx=None,*args,**kwargs):
    varargin = park91a.varargin
    nargin = park91a.nargin

    ##########################################################################
    
    # PARK (1991) FUNCTION 1
    
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
# park91a.m:36
    x2=xx(2)
# park91a.m:37
    x3=xx(3)
# park91a.m:38
    x4=xx(4)
# park91a.m:39
    term1a=x1 / 2
# park91a.m:41
    term1b=sqrt(1 + dot((x2 + x3 ** 2),x4) / (x1 ** 2)) - 1
# park91a.m:42
    term1=dot(term1a,term1b)
# park91a.m:43
    term2a=x1 + dot(3,x4)
# park91a.m:45
    term2b=exp(1 + sin(x3))
# park91a.m:46
    term2=dot(term2a,term2b)
# park91a.m:47
    y=term1 + term2
# park91a.m:49
    return y
    
if __name__ == '__main__':
    pass
    