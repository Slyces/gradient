# Generated with SMOP  0.41
from libsmop import *
# grlee09.m

    
    
@function
def grlee09(xx=None,*args,**kwargs):
    varargin = grlee09.varargin
    nargin = grlee09.nargin

    ##########################################################################
    
    # GRAMACY & LEE (2009) FUNCTION
    
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
    
    #########################################################################
    
    x1=xx(1)
# grlee09.m:36
    x2=xx(2)
# grlee09.m:37
    x3=xx(3)
# grlee09.m:38
    x4=xx(4)
# grlee09.m:39
    x5=xx(5)
# grlee09.m:40
    x6=xx(6)
# grlee09.m:41
    term1=exp(sin((dot(0.9,(x1 + 0.48))) ** 10))
# grlee09.m:43
    term2=dot(x2,x3)
# grlee09.m:44
    term3=copy(x4)
# grlee09.m:45
    y=term1 + term2 + term3
# grlee09.m:47
    return y
    
if __name__ == '__main__':
    pass
    