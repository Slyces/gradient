# Generated with SMOP  0.41
from libsmop import *
# spherefmod.m

    
    
@function
def spherefmod(xx=None,*args,**kwargs):
    varargin = spherefmod.varargin
    nargin = spherefmod.nargin

    ##########################################################################
    
    # SPHERE FUNCTION, MODIFIED
    
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
    
    # xx = [x1, x2, x3, x4, x5, x6]
    
    ##########################################################################
    
    sum=0
# spherefmod.m:36
    for ii in arange(1,6).reshape(-1):
        xi=xx(ii)
# spherefmod.m:38
        sum=sum + dot((xi ** 2),(2 ** ii))
# spherefmod.m:39
    
    y=(sum - 1745) / 899
# spherefmod.m:42
    return y
    
if __name__ == '__main__':
    pass
    