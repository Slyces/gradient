# Generated with SMOP  0.41
from libsmop import *
# ishigami.m

    
    
@function
def ishigami(xx=None,a=None,b=None,*args,**kwargs):
    varargin = ishigami.varargin
    nargin = ishigami.nargin

    ##########################################################################
    
    # ISHIGAMI FUNCTION
    
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
    
    # xx = [x1, x2, x3]
# a = coefficient (optional), with default value 7
# b = coefficient (optional), with default value 0.1
    
    #########################################################################
    
    x1=xx(1)
# ishigami.m:38
    x2=xx(2)
# ishigami.m:39
    x3=xx(3)
# ishigami.m:40
    if (nargin == 1):
        a=7
# ishigami.m:43
        b=0.1
# ishigami.m:44
    else:
        if (nargin == 2):
            b=0.1
# ishigami.m:46
    
    term1=sin(x1)
# ishigami.m:49
    term2=dot(a,(sin(x2)) ** 2)
# ishigami.m:50
    term3=dot(dot(b,x3 ** 4),sin(x1))
# ishigami.m:51
    y=term1 + term2 + term3
# ishigami.m:53
    return y
    
if __name__ == '__main__':
    pass
    