# Generated with SMOP  0.41
from libsmop import *
# trid.m

    
    
@function
def trid(xx=None,*args,**kwargs):
    varargin = trid.varargin
    nargin = trid.nargin

    ##########################################################################
    
    # TRID FUNCTION
    
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
    
    # xx = [x1, x2, ..., xd]
    
    ##########################################################################
    
    d=length(xx)
# trid.m:36
    sum1=(xx(1) - 1) ** 2
# trid.m:37
    sum2=0
# trid.m:38
    for ii in arange(2,d).reshape(-1):
        xi=xx(ii)
# trid.m:41
        xold=xx(ii - 1)
# trid.m:42
        sum1=sum1 + (xi - 1) ** 2
# trid.m:43
        sum2=sum2 + dot(xi,xold)
# trid.m:44
    
    y=sum1 - sum2
# trid.m:47
    return y
    
if __name__ == '__main__':
    pass
    