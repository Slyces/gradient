# Generated with SMOP  0.41
from libsmop import *
# michal.m

    
    
@function
def michal(xx=None,m=None,*args,**kwargs):
    varargin = michal.varargin
    nargin = michal.nargin

    ##########################################################################
    
    # MICHALEWICZ FUNCTION
    
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
    
    # xx = [x1, x2]
# m = constant (optional), with default value 10
    
    ##########################################################################
    
    if (nargin == 1):
        m=10
# michal.m:38
    
    d=length(xx)
# michal.m:41
    sum=0
# michal.m:42
    for ii in arange(1,d).reshape(-1):
        xi=xx(ii)
# michal.m:45
        new=dot(sin(xi),(sin(dot(ii,xi ** 2) / pi)) ** (dot(2,m)))
# michal.m:46
        sum=sum + new
# michal.m:47
    
    y=- sum
# michal.m:50
    return y
    
if __name__ == '__main__':
    pass
    