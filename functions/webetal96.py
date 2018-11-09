# Generated with SMOP  0.41
from libsmop import *
# webetal96.m

    
    
@function
def webetal96(xx=None,*args,**kwargs):
    varargin = webetal96.varargin
    nargin = webetal96.nargin

    ##########################################################################
    
    # WEBSTER ET AL. (1996) FUNCTION
    
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
#
    
    ##########################################################################
    
    # INPUT:
    
    # xx = [A, B]
    
    #########################################################################
    
    A=xx(1)
# webetal96.m:36
    B=xx(2)
# webetal96.m:37
    y=A ** 2 + B ** 3
# webetal96.m:39
    return y
    
if __name__ == '__main__':
    pass
    