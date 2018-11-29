# Generated with SMOP  0.41
from libsmop import *
# limetal02pol.m

    
    
@function
def limetal02pol(xx=None,*args,**kwargs):
    varargin = limetal02pol.varargin
    nargin = limetal02pol.nargin

    ##########################################################################
    
    # LIM ET AL. (2002) POLYNOMIAL FUNCTION
    
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
# limetal02pol.m:36
    x2=xx(2)
# limetal02pol.m:37
    term1=dot((5 / 2),x1) - dot((35 / 2),x2)
# limetal02pol.m:39
    term2=dot(dot((5 / 2),x1),x2) + dot(19,x2 ** 2)
# limetal02pol.m:40
    term3=dot(- (15 / 2),x1 ** 3) - dot(dot((5 / 2),x1),x2 ** 2)
# limetal02pol.m:41
    term4=dot(- (11 / 2),x2 ** 4) + dot((x1 ** 3),(x2 ** 2))
# limetal02pol.m:42
    y=9 + term1 + term2 + term3 + term4
# limetal02pol.m:44
    return y
    
if __name__ == '__main__':
    pass
    