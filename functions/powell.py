# Generated with SMOP  0.41
from libsmop import *
# powell.m

    
    
@function
def powell(xx=None,*args,**kwargs):
    varargin = powell.varargin
    nargin = powell.nargin

    ##########################################################################
    
    # POWELL FUNCTION
    
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
    
    # xx = [x1, x2, ..., xd]
    
    ##########################################################################
    
    d=length(xx)
# powell.m:36
    sum=0
# powell.m:37
    for ii in arange(1,(d / 4)).reshape(-1):
        term1=(xx(dot(4,ii) - 3) + dot(10,xx(dot(4,ii) - 2))) ** 2
# powell.m:40
        term2=dot(5,(xx(dot(4,ii) - 1) - xx(dot(4,ii))) ** 2)
# powell.m:41
        term3=(xx(dot(4,ii) - 2) - dot(2,xx(dot(4,ii) - 1))) ** 4
# powell.m:42
        term4=dot(10,(xx(dot(4,ii) - 3) - xx(dot(4,ii))) ** 4)
# powell.m:43
        sum=sum + term1 + term2 + term3 + term4
# powell.m:44
    
    y=copy(sum)
# powell.m:47
    return y
    
if __name__ == '__main__':
    pass
    