# Generated with SMOP  0.41
from libsmop import *
# bratleyetal92.m

    
    
@function
def bratleyetal92(xx=None,*args,**kwargs):
    varargin = bratleyetal92.varargin
    nargin = bratleyetal92.nargin

    ##########################################################################
    
    # BRATLEY ET AL. (1992) FUNCTION
    
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
    
    #########################################################################
    
    # INPUT:
    
    # xx = [x1, x2, ..., xd]
    
    #########################################################################
    
    d=length(xx)
# bratleyetal92.m:36
    sum=0
# bratleyetal92.m:37
    for ii in arange(1,d).reshape(-1):
        prod=1
# bratleyetal92.m:40
        for jj in arange(1,ii).reshape(-1):
            xj=xx(jj)
# bratleyetal92.m:42
            prod=dot(prod,xj)
# bratleyetal92.m:43
        sum=sum + dot(prod,(- 1) ** ii)
# bratleyetal92.m:45
    
    y=copy(sum)
# bratleyetal92.m:48
    return y
    
if __name__ == '__main__':
    pass
    