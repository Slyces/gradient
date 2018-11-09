# Generated with SMOP  0.41
from libsmop import *
# curretal88exp.m

    
    
@function
def curretal88exp(xx=None,*args,**kwargs):
    varargin = curretal88exp.varargin
    nargin = curretal88exp.nargin

    ##########################################################################
    
    # CURRIN ET AL. (1988) EXPONENTIAL FUNCTION
    
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
# curretal88exp.m:36
    x2=xx(2)
# curretal88exp.m:37
    fact1=1 - exp(- 1 / (dot(2,x2)))
# curretal88exp.m:39
    fact2=dot(2300,x1 ** 3) + dot(1900,x1 ** 2) + dot(2092,x1) + 60
# curretal88exp.m:40
    fact3=dot(100,x1 ** 3) + dot(500,x1 ** 2) + dot(4,x1) + 20
# curretal88exp.m:41
    y=dot(fact1,fact2) / fact3
# curretal88exp.m:43
    return y
    
if __name__ == '__main__':
    pass
    