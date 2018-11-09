# Generated with SMOP  0.41
from libsmop import *
# hart6sc.m

    
    
@function
def hart6sc(xx=None,*args,**kwargs):
    varargin = hart6sc.varargin
    nargin = hart6sc.nargin

    ##########################################################################
    
    # HARTMANN 6-DIMENSIONAL FUNCTION, RESCALED
    
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
    
    alpha=concat([1.0,1.2,3.0,3.2]).T
# hart6sc.m:36
    A=concat([[10,3,17,3.5,1.7,8],[0.05,10,17,0.1,8,14],[3,3.5,1.7,10,17,8],[17,8,0.05,10,0.1,14]])
# hart6sc.m:37
    P=dot(10 ** (- 4),concat([[1312,1696,5569,124,8283,5886],[2329,4135,8307,3736,1004,9991],[2348,1451,3522,2883,3047,6650],[4047,8828,8732,5743,1091,381]]))
# hart6sc.m:41
    outer=0
# hart6sc.m:46
    for ii in arange(1,4).reshape(-1):
        inner=0
# hart6sc.m:48
        for jj in arange(1,6).reshape(-1):
            xj=xx(jj)
# hart6sc.m:50
            Aij=A(ii,jj)
# hart6sc.m:51
            Pij=P(ii,jj)
# hart6sc.m:52
            inner=inner + dot(Aij,(xj - Pij) ** 2)
# hart6sc.m:53
        new=dot(alpha(ii),exp(- inner))
# hart6sc.m:55
        outer=outer + new
# hart6sc.m:56
    
    y=- outer
# hart6sc.m:59
    return y
    
if __name__ == '__main__':
    pass
    