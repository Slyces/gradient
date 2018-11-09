# Generated with SMOP  0.41
from libsmop import *
# easom.m

    
    
@function
def easom(xx=None,*args,**kwargs):
    varargin = easom.varargin
    nargin = easom.nargin

    ##########################################################################
    
    # EASOM FUNCTION
    
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
# easom.m:36
    x2=xx(2)
# easom.m:37
    fact1=dot(- cos(x1),cos(x2))
# easom.m:39
    fact2=exp(- (x1 - pi) ** 2 - (x2 - pi) ** 2)
# easom.m:40
    y=dot(fact1,fact2)
# easom.m:42
    return y
    
if __name__ == '__main__':
    pass
    