# Generated with SMOP  0.41
from libsmop import *
# egg.m

    
    
@function
def egg(xx=None,*args,**kwargs):
    varargin = egg.varargin
    nargin = egg.nargin

    ##########################################################################
    
    # EGGHOLDER FUNCTION
    
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
    
    # xx = [x1, x2]
    
    ##########################################################################
    
    x1=xx(1)
# egg.m:36
    x2=xx(2)
# egg.m:37
    term1=dot(- (x2 + 47),sin(sqrt(abs(x2 + x1 / 2 + 47))))
# egg.m:39
    term2=dot(- x1,sin(sqrt(abs(x1 - (x2 + 47)))))
# egg.m:40
    y=term1 + term2
# egg.m:42
    return y
    
if __name__ == '__main__':
    pass
    