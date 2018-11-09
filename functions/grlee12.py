# Generated with SMOP  0.41
from libsmop import *
# grlee12.m

    
    
@function
def grlee12(x=None,*args,**kwargs):
    varargin = grlee12.varargin
    nargin = grlee12.nargin

    ##########################################################################
    
    # GRAMACY & LEE (2012) FUNCTION
    
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
    
    term1=sin(dot(dot(10,pi),x)) / (dot(2,x))
# grlee12.m:30
    term2=(x - 1) ** 4
# grlee12.m:31
    y=term1 + term2
# grlee12.m:33
    return y
    
if __name__ == '__main__':
    pass
    