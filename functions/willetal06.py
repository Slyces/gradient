# Generated with SMOP  0.41
from libsmop import *
# willetal06.m

    
    
@function
def willetal06(xx=None,*args,**kwargs):
    varargin = willetal06.varargin
    nargin = willetal06.nargin

    ##########################################################################
    
    # WILLIAMS ET AL. (2006) FUNCTION
    
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
# willetal06.m:36
    x2=xx(2)
# willetal06.m:37
    x3=xx(3)
# willetal06.m:38
    term1=dot((x1 + 1),cos(dot(pi,x2)))
# willetal06.m:40
    y=term1 + dot(0,x3)
# willetal06.m:42
    return y
    
if __name__ == '__main__':
    pass
    