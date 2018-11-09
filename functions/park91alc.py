# Generated with SMOP  0.41
from libsmop import *
# park91alc.m

    
    
@function
def park91alc(xx=None,*args,**kwargs):
    varargin = park91alc.varargin
    nargin = park91alc.nargin

    ##########################################################################
    
    # PARK (1991) FUNCTION 1, LOWER FIDELITY CODE
# Calls: park91a.m
# This function, from Xiong et al. (2013), is used as the "low-accuracy
# code" version of the function park91a.m.
    
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
    
    # xx = [x1, x2, x3, x4]
    
    #########################################################################
    
    x1=xx(1)
# park91alc.m:39
    x2=xx(2)
# park91alc.m:40
    x3=xx(3)
# park91alc.m:41
    x4=xx(4)
# park91alc.m:42
    yh=park91a(xx)
# park91alc.m:44
    term1=dot((1 + sin(x1) / 10),yh)
# park91alc.m:46
    term2=dot(- 2,x1) + x2 ** 2 + x3 ** 2
# park91alc.m:47
    y=term1 + term2 + 0.5
# park91alc.m:49
    return y
    
if __name__ == '__main__':
    pass
    