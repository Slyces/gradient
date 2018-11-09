# Generated with SMOP  0.41
from libsmop import *
# branin.m

    
    
@function
def branin(xx=None,a=None,b=None,c=None,r=None,s=None,t=None,*args,**kwargs):
    varargin = branin.varargin
    nargin = branin.nargin

    ##########################################################################
    
    # BRANIN FUNCTION
    
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
# a = constant (optional), with default value 1
# b = constant (optional), with default value 5.1/(4*pi^2)
# c = constant (optional), with default value 5/pi
# r = constant (optional), with default value 6
# s = constant (optional), with default value 10
# t = constant (optional), with default value 1/(8*pi)
    
    #########################################################################
    
    x1=xx(1)
# branin.m:42
    x2=xx(2)
# branin.m:43
    if (nargin < 7):
        t=1 / (dot(8,pi))
# branin.m:46
    
    if (nargin < 6):
        s=10
# branin.m:49
    
    if (nargin < 5):
        r=6
# branin.m:52
    
    if (nargin < 4):
        c=5 / pi
# branin.m:55
    
    if (nargin < 3):
        b=5.1 / (dot(4,pi ** 2))
# branin.m:58
    
    if (nargin < 2):
        a=1
# branin.m:61
    
    term1=dot(a,(x2 - dot(b,x1 ** 2) + dot(c,x1) - r) ** 2)
# branin.m:64
    term2=dot(dot(s,(1 - t)),cos(x1))
# branin.m:65
    y=term1 + term2 + s
# branin.m:67
    return y
    
if __name__ == '__main__':
    pass
    