# Generated with SMOP  0.41
from libsmop import *
# ackley.m

    
    
@function
def ackley(xx=None,a=None,b=None,c=None,*args,**kwargs):
    varargin = ackley.varargin
    nargin = ackley.nargin

    ##########################################################################
    
    # ACKLEY FUNCTION
    
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
    
    # xx = [x1, x2, ..., xd]
# a = constant (optional), with default value 20
# b = constant (optional), with default value 0.2
# c = constant (optional), with default value 2*pi
    
    ##########################################################################
    
    d=length(xx)
# ackley.m:39
    if (nargin < 4):
        c=dot(2,pi)
# ackley.m:42
    
    if (nargin < 3):
        b=0.2
# ackley.m:45
    
    if (nargin < 2):
        a=20
# ackley.m:48
    
    sum1=0
# ackley.m:51
    sum2=0
# ackley.m:52
    for ii in arange(1,d).reshape(-1):
        xi=xx(ii)
# ackley.m:54
        sum1=sum1 + xi ** 2
# ackley.m:55
        sum2=sum2 + cos(dot(c,xi))
# ackley.m:56
    
    term1=dot(- a,exp(dot(- b,sqrt(sum1 / d))))
# ackley.m:59
    term2=- exp(sum2 / d)
# ackley.m:60
    y=term1 + term2 + a + exp(1)
# ackley.m:62
    return y
    
if __name__ == '__main__':
    pass
    