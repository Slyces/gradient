# Generated with SMOP  0.41
from libsmop import *
# shubert.m

    
    
@function
def shubert(xx=None,*args,**kwargs):
    varargin = shubert.varargin
    nargin = shubert.nargin

    ##########################################################################
    
    # SHUBERT FUNCTION
    
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
    
    # xx = [x1, x2]
    
    ##########################################################################
    
    x1=xx(1)
# shubert.m:36
    x2=xx(2)
# shubert.m:37
    sum1=0
# shubert.m:38
    sum2=0
# shubert.m:39
    for ii in arange(1,5).reshape(-1):
        new1=dot(ii,cos(dot((ii + 1),x1) + ii))
# shubert.m:42
        new2=dot(ii,cos(dot((ii + 1),x2) + ii))
# shubert.m:43
        sum1=sum1 + new1
# shubert.m:44
        sum2=sum2 + new2
# shubert.m:45
    
    y=dot(sum1,sum2)
# shubert.m:48
    return y
    
if __name__ == '__main__':
    pass
    