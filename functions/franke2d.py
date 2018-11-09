# Generated with SMOP  0.41
from libsmop import *
# franke2d.m

    
    
@function
def franke2d(xx=None,*args,**kwargs):
    varargin = franke2d.varargin
    nargin = franke2d.nargin

    ##########################################################################
    
    # FRANKE'S FUNCTION
    
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
    
    #########################################################################
    
    x1=xx(1)
# franke2d.m:36
    x2=xx(2)
# franke2d.m:37
    term1=dot(0.75,exp(- (dot(9,x1) - 2) ** 2 / 4 - (dot(9,x2) - 2) ** 2 / 4))
# franke2d.m:39
    term2=dot(0.75,exp(- (dot(9,x1) + 1) ** 2 / 49 - (dot(9,x2) + 1) / 10))
# franke2d.m:40
    term3=dot(0.5,exp(- (dot(9,x1) - 7) ** 2 / 4 - (dot(9,x2) - 3) ** 2 / 4))
# franke2d.m:41
    term4=dot(- 0.2,exp(- (dot(9,x1) - 4) ** 2 - (dot(9,x2) - 7) ** 2))
# franke2d.m:42
    y=term1 + term2 + term3 + term4
# franke2d.m:44
    return y
    
if __name__ == '__main__':
    pass
    