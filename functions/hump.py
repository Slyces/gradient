# Generated with SMOP  0.41
from libsmop import *
# hump.m

    
    
@function
def hump(xx=None,*args,**kwargs):
    varargin = hump.varargin
    nargin = hump.nargin

    ##########################################################################
    
    # HUMP FUNCTION
    
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
# hump.m:36
    x2=xx(2)
# hump.m:37
    term1=dot(4,x1 ** 2)
# hump.m:39
    term2=dot(- 2.1,x1 ** 4)
# hump.m:40
    term3=x1 ** 6 / 3
# hump.m:41
    term4=dot(x1,x2)
# hump.m:42
    term5=dot(- 4,x2 ** 2)
# hump.m:43
    term6=dot(4,x2 ** 4)
# hump.m:44
    y=1.0316285 + term1 + term2 + term3 + term4 + term5 + term6
# hump.m:46
    return y
    
if __name__ == '__main__':
    pass
    