# Generated with SMOP  0.41
from libsmop import *
# fried.m

    
    
@function
def fried(xx=None,*args,**kwargs):
    varargin = fried.varargin
    nargin = fried.nargin

    ##########################################################################
    
    # FRIEDMAN FUNCTION
    
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
    
    # xx = [x1, x2, x3, x4, x5]
    
    #########################################################################
    
    x1=xx(1)
# fried.m:36
    x2=xx(2)
# fried.m:37
    x3=xx(3)
# fried.m:38
    x4=xx(4)
# fried.m:39
    x5=xx(5)
# fried.m:40
    term1=dot(10,sin(dot(dot(pi,x1),x2)))
# fried.m:42
    term2=dot(20,(x3 - 0.5) ** 2)
# fried.m:43
    term3=dot(10,x4)
# fried.m:44
    term4=dot(5,x5)
# fried.m:45
    y=term1 + term2 + term3 + term4
# fried.m:47
    return y
    
if __name__ == '__main__':
    pass
    