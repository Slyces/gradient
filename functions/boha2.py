# Generated with SMOP  0.41
from libsmop import *
# boha2.m

    
    
@function
def boha2(xx=None,*args,**kwargs):
    varargin = boha2.varargin
    nargin = boha2.nargin

    ##########################################################################
    
    # BOHACHEVSKY FUNCTION 2
    
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
    
    #########################################################################
    
    x1=xx(1)
# boha2.m:36
    x2=xx(2)
# boha2.m:37
    term1=x1 ** 2
# boha2.m:39
    term2=dot(2,x2 ** 2)
# boha2.m:40
    term3=dot(dot(- 0.3,cos(dot(dot(3,pi),x1))),cos(dot(dot(4,pi),x2)))
# boha2.m:41
    y=term1 + term2 + term3 + 0.3
# boha2.m:43
    return y
    
if __name__ == '__main__':
    pass
    