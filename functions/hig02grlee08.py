# Generated with SMOP  0.41
from libsmop import *
# hig02grlee08.m

    
    
@function
def hig02grlee08(x=None,*args,**kwargs):
    varargin = hig02grlee08.varargin
    nargin = hig02grlee08.nargin

    ##########################################################################
    
    # HIGDON (2001) AND GRAMACY & LEE (2008) FUNCTION
    
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
    
    if (x < 10):
        y=sin(dot(pi,x) / 5) + dot(0.2,cos(dot(dot(4,pi),x) / 5))
# hig02grlee08.m:31
    else:
        y=x / 10 - 1
# hig02grlee08.m:33
    
    return y
    
if __name__ == '__main__':
    pass
    