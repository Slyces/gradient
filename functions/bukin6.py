# Generated with SMOP  0.41
from libsmop import *
# bukin6.m

    
    
@function
def bukin6(xx=None,*args,**kwargs):
    varargin = bukin6.varargin
    nargin = bukin6.nargin

    ##########################################################################
    
    # BUKIN FUNCTION N. 6
    
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
    
    #########################################################################
    
    x1=xx(1)
# bukin6.m:36
    x2=xx(2)
# bukin6.m:37
    term1=dot(100,sqrt(abs(x2 - dot(0.01,x1 ** 2))))
# bukin6.m:39
    term2=dot(0.01,abs(x1 + 10))
# bukin6.m:40
    y=term1 + term2
# bukin6.m:42
    return y
    
if __name__ == '__main__':
    pass
    