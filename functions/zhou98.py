# Generated with SMOP  0.41
from libsmop import *
# zhou98.m

    
    
@function
def zhou98(xx=None,*args,**kwargs):
    varargin = zhou98.varargin
    nargin = zhou98.nargin

    ##########################################################################
    
    # ZHOU (1998) FUNCTION
    
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
    
    # xx = [x1, x2, ..., xd]
    
    #########################################################################
    
    d=length(xx)
# zhou98.m:36
    for ii in arange(1,d).reshape(-1):
        xxa[ii]=dot(10,(xx(ii) - 1 / 3))
# zhou98.m:39
    
    for ii in arange(1,d).reshape(-1):
        xxb[ii]=dot(10,(xx(ii) - 2 / 3))
# zhou98.m:43
    
    phi1=dot((dot(2,pi)) ** (- d / 2),exp(dot(- 0.5,(norm(xxa)) ** 2)))
# zhou98.m:46
    phi2=dot((dot(2,pi)) ** (- d / 2),exp(dot(- 0.5,(norm(xxb)) ** 2)))
# zhou98.m:47
    y=dot((10 ** d) / 2,(phi1 + phi2))
# zhou98.m:49
    return y
    
if __name__ == '__main__':
    pass
    