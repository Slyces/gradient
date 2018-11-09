# Generated with SMOP  0.41
from libsmop import *
# colville.m

    
    
@function
def colville(xx=None,*args,**kwargs):
    varargin = colville.varargin
    nargin = colville.nargin

    ##########################################################################
    
    # COLVILLE FUNCTION
    
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
    
    # xx = [x1, x2, x3, x4]
    
    #########################################################################
    
    x1=xx(1)
# colville.m:36
    x2=xx(2)
# colville.m:37
    x3=xx(3)
# colville.m:38
    x4=xx(4)
# colville.m:39
    term1=dot(100,(x1 ** 2 - x2) ** 2)
# colville.m:41
    term2=(x1 - 1) ** 2
# colville.m:42
    term3=(x3 - 1) ** 2
# colville.m:43
    term4=dot(90,(x3 ** 2 - x4) ** 2)
# colville.m:44
    term5=dot(10.1,((x2 - 1) ** 2 + (x4 - 1) ** 2))
# colville.m:45
    term6=dot(dot(19.8,(x2 - 1)),(x4 - 1))
# colville.m:46
    y=term1 + term2 + term3 + term4 + term5 + term6
# colville.m:48
    return y
    
if __name__ == '__main__':
    pass
    