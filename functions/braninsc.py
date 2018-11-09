# Generated with SMOP  0.41
from libsmop import *
# braninsc.m

    
    
@function
def braninsc(xx=None,*args,**kwargs):
    varargin = braninsc.varargin
    nargin = braninsc.nargin

    ##########################################################################
    
    # BRANIN FUNCTION, RESCALED
    
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
# braninsc.m:36
    x2=xx(2)
# braninsc.m:37
    x1bar=dot(15,x1) - 5
# braninsc.m:39
    x2bar=dot(15,x2)
# braninsc.m:40
    term1=x2bar - dot(5.1,x1bar ** 2) / (dot(4,pi ** 2)) + dot(5,x1bar) / pi - 6
# braninsc.m:42
    term2=dot((10 - 10 / (dot(8,pi))),cos(x1bar))
# braninsc.m:43
    y=(term1 ** 2 + term2 - 44.81) / 51.95
# braninsc.m:45
    return y
    
if __name__ == '__main__':
    pass
    