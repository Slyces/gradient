# Generated with SMOP  0.41
from libsmop import *
# perm0db.m

    
    
@function
def perm0db(xx=None,b=None,*args,**kwargs):
    varargin = perm0db.varargin
    nargin = perm0db.nargin

    ##########################################################################
    
    # PERM FUNCTION 0, d, beta
    
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
# b = constant (optional), with default value 10
    
    ##########################################################################
    
    if (nargin == 1):
        b=10
# perm0db.m:38
    
    d=length(xx)
# perm0db.m:41
    outer=0
# perm0db.m:42
    for ii in arange(1,d).reshape(-1):
        inner=0
# perm0db.m:45
        for jj in arange(1,d).reshape(-1):
            xj=xx(jj)
# perm0db.m:47
            inner=inner + dot((jj + b),(xj ** ii - (1 / jj) ** ii))
# perm0db.m:48
        outer=outer + inner ** 2
# perm0db.m:50
    
    y=copy(outer)
# perm0db.m:53
    return y
    
if __name__ == '__main__':
    pass
    