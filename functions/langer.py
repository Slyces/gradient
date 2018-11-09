# Generated with SMOP  0.41
from libsmop import *
# langer.m

    
    
@function
def langer(xx=None,m=None,c=None,A=None,*args,**kwargs):
    varargin = langer.varargin
    nargin = langer.nargin

    ##########################################################################
    
    # LANGERMANN FUNCTION
    
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
#
    
    ##########################################################################
    
    # INPUTS:
    
    # xx = [x1, x2, ..., xd]
# m  = constant (optional), with default value 5
# c  = m-dimensional vector (optional), with default value [1, 2, 5, 2, 3]
#      (when m=5)
# A  = (mxd)-dimensional matrix (optional), with default value
#      [3, 5; 5, 2; 2, 1; 1, 4; 7, 9] (when m=5 and d=2)
    
    ##########################################################################
    
    d=length(xx)
# langer.m:41
    if (nargin < 2):
        m=5
# langer.m:44
    
    if (nargin < 3):
        if (m == 5):
            c=concat([1,2,5,2,3])
# langer.m:49
        else:
            error('Value of the m-dimensional vector c is required.')
    
    if (nargin < 4):
        if (m == 5 and d == 2):
            A=concat([[3,5],[5,2],[2,1],[1,4],[7,9]])
# langer.m:57
        else:
            error('Value of the (mxd)-dimensional matrix A is required.')
    
    outer=0
# langer.m:63
    for ii in arange(1,m).reshape(-1):
        inner=0
# langer.m:65
        for jj in arange(1,d).reshape(-1):
            xj=xx(jj)
# langer.m:67
            Aij=A(ii,jj)
# langer.m:68
            inner=inner + (xj - Aij) ** 2
# langer.m:69
        new=dot(dot(c(ii),exp(- inner / pi)),cos(dot(pi,inner)))
# langer.m:71
        outer=outer + new
# langer.m:72
    
    y=copy(outer)
# langer.m:75
    return y
    
if __name__ == '__main__':
    pass
    