# Generated with SMOP  0.41
from libsmop import *
# dixonpr.m

    
    
@function
def dixonpr(xx=None,*args,**kwargs):
    varargin = dixonpr.varargin
    nargin = dixonpr.nargin

    ##########################################################################
    
    # DIXON-PRICE FUNCTION
    
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
    
    #########################################################################
    
    x1=xx(1)
# dixonpr.m:36
    d=length(xx)
# dixonpr.m:37
    term1=(x1 - 1) ** 2
# dixonpr.m:38
    sum=0
# dixonpr.m:40
    for ii in arange(2,d).reshape(-1):
        xi=xx(ii)
# dixonpr.m:42
        xold=xx(ii - 1)
# dixonpr.m:43
        new=dot(ii,(dot(2,xi ** 2) - xold) ** 2)
# dixonpr.m:44
        sum=sum + new
# dixonpr.m:45
    
    y=term1 + sum
# dixonpr.m:48
    return y
    
if __name__ == '__main__':
    pass
    