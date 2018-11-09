# Generated with SMOP  0.41
from libsmop import *
# shekel.m

    
    
@function
def shekel(xx=None,*args,**kwargs):
    varargin = shekel.varargin
    nargin = shekel.nargin

    ##########################################################################
    
    # SHEKEL FUNCTION
    
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
    
    # xx = [x1, x2, x3, x4]
    
    #########################################################################
    
    m=10
# shekel.m:36
    b=dot(0.1,concat([1,2,2,4,4,6,3,7,5,5]).T)
# shekel.m:37
    C=concat([[4.0,1.0,8.0,6.0,3.0,2.0,5.0,8.0,6.0,7.0],[4.0,1.0,8.0,6.0,7.0,9.0,3.0,1.0,2.0,3.6],[4.0,1.0,8.0,6.0,3.0,2.0,5.0,8.0,6.0,7.0],[4.0,1.0,8.0,6.0,7.0,9.0,3.0,1.0,2.0,3.6]])
# shekel.m:38
    outer=0
# shekel.m:43
    for ii in arange(1,m).reshape(-1):
        bi=b(ii)
# shekel.m:45
        inner=0
# shekel.m:46
        for jj in arange(1,4).reshape(-1):
            xj=xx(jj)
# shekel.m:48
            Cji=C(jj,ii)
# shekel.m:49
            inner=inner + (xj - Cji) ** 2
# shekel.m:50
        outer=outer + 1 / (inner + bi)
# shekel.m:52
    
    y=- outer
# shekel.m:55
    return y
    
if __name__ == '__main__':
    pass
    