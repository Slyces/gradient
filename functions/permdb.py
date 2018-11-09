# Generated with SMOP  0.41
from libsmop import *
# permdb.m

    
    
@function
def permdb(xx=None,b=None,*args,**kwargs):
    varargin = permdb.varargin
    nargin = permdb.nargin

    ##########################################################################
    
    # PERM FUNCTION d, beta
    
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
# b  = constant (optional), with default value 0.5
    
    ##########################################################################
    
    if (nargin == 1):
        b=0.5
# permdb.m:38
    
    d=length(xx)
# permdb.m:41
    outer=0
# permdb.m:42
    for ii in arange(1,d).reshape(-1):
        inner=0
# permdb.m:45
        for jj in arange(1,d).reshape(-1):
            xj=xx(jj)
# permdb.m:47
            inner=inner + dot((jj ** ii + b),((xj / jj) ** ii - 1))
# permdb.m:48
        outer=outer + inner ** 2
# permdb.m:50
    
    y=copy(outer)
# permdb.m:53
    return y
    
if __name__ == '__main__':
    pass
    