# Generated with SMOP  0.41
from libsmop import *
# detpep108d.m

    
    
@function
def detpep108d(xx=None,*args,**kwargs):
    varargin = detpep108d.varargin
    nargin = detpep108d.nargin

    ##########################################################################
    
    # DETTE & PEPELYSHEV (2010) 8-DIMENSIONAL FUNCTION
    
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
    
    # xx = [x1, x2, ..., x8]
    
    #########################################################################
    
    x1=xx(1)
# detpep108d.m:36
    x2=xx(2)
# detpep108d.m:37
    x3=xx(3)
# detpep108d.m:38
    term1=dot(4,(x1 - 2 + dot(8,x2) - dot(8,x2 ** 2)) ** 2)
# detpep108d.m:40
    term2=(3 - dot(4,x2)) ** 2
# detpep108d.m:41
    term3=dot(dot(16,sqrt(x3 + 1)),(dot(2,x3) - 1) ** 2)
# detpep108d.m:42
    outer=0
# detpep108d.m:44
    for ii in arange(4,8).reshape(-1):
        inner=0
# detpep108d.m:46
        for jj in arange(3,ii).reshape(-1):
            xj=xx(jj)
# detpep108d.m:48
            inner=inner + xj
# detpep108d.m:49
        new=dot(ii,log(1 + inner))
# detpep108d.m:51
        outer=outer + new
# detpep108d.m:52
    
    y=term1 + term2 + term3 + outer
# detpep108d.m:55
    return y
    
if __name__ == '__main__':
    pass
    