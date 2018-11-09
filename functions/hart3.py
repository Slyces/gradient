# Generated with SMOP  0.41
from libsmop import *
# hart3.m

    
    
@function
def hart3(xx=None,*args,**kwargs):
    varargin = hart3.varargin
    nargin = hart3.nargin

    ##########################################################################
    
    # HARTMANN 3-DIMENSIONAL FUNCTION
    
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
    
    # xx = [x1, x2, x3]
    
    ##########################################################################
    
    alpha=concat([1.0,1.2,3.0,3.2]).T
# hart3.m:36
    A=concat([[3.0,10,30],[0.1,10,35],[3.0,10,30],[0.1,10,35]])
# hart3.m:37
    P=dot(10 ** (- 4),concat([[3689,1170,2673],[4699,4387,7470],[1091,8732,5547],[381,5743,8828]]))
# hart3.m:41
    outer=0
# hart3.m:46
    for ii in arange(1,4).reshape(-1):
        inner=0
# hart3.m:48
        for jj in arange(1,3).reshape(-1):
            xj=xx(jj)
# hart3.m:50
            Aij=A(ii,jj)
# hart3.m:51
            Pij=P(ii,jj)
# hart3.m:52
            inner=inner + dot(Aij,(xj - Pij) ** 2)
# hart3.m:53
        new=dot(alpha(ii),exp(- inner))
# hart3.m:55
        outer=outer + new
# hart3.m:56
    
    y=- outer
# hart3.m:59
    return y
    
if __name__ == '__main__':
    pass
    