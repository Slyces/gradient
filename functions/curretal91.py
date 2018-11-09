# Generated with SMOP  0.41
from libsmop import *
# curretal91.m

    
    
@function
def curretal91(xx=None,*args,**kwargs):
    varargin = curretal91.varargin
    nargin = curretal91.nargin

    ##########################################################################
    
    # CURRIN ET AL. (1991) FUNCTION
    
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
# curretal91.m:36
    x2=xx(2)
# curretal91.m:37
    term1=dot(21.15,x1)
# curretal91.m:39
    term2=dot(- 2.17,x2)
# curretal91.m:40
    term3=dot(- 15.88,x1 ** 2)
# curretal91.m:41
    term4=dot(- 1.38,x2 ** 2)
# curretal91.m:42
    term5=dot(dot(- 5.26,x1),x2)
# curretal91.m:43
    y=4.9 + term1 + term2 + term3 + term4 + term5
# curretal91.m:45
    return y
    
if __name__ == '__main__':
    pass
    