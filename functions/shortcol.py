# Generated with SMOP  0.41
from libsmop import *
# shortcol.m

    
    
@function
def shortcol(xx=None,b=None,h=None,*args,**kwargs):
    varargin = shortcol.varargin
    nargin = shortcol.nargin

    ##########################################################################
    
    # SHORT COLUMN FUNCTION
    
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
    
    # xx = [Y, M, P]
# b  = width of cross-section (optional), with nominal value 5
# h  = depth of cross-section (optional), with nominal value 15
    
    #########################################################################
    
    Y=xx(1)
# shortcol.m:38
    M=xx(2)
# shortcol.m:39
    P=xx(3)
# shortcol.m:40
    if (nargin == 1):
        b=5
# shortcol.m:43
        h=15
# shortcol.m:44
    else:
        if (nargin == 2):
            h=15
# shortcol.m:46
    
    term1=dot(- 4,M) / (dot(dot(b,(h ** 2)),Y))
# shortcol.m:49
    term2=- (P ** 2) / (dot(dot((b ** 2),(h ** 2)),(Y ** 2)))
# shortcol.m:50
    y=1 + term1 + term2
# shortcol.m:52
    return y
    
if __name__ == '__main__':
    pass
    