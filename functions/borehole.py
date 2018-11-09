# Generated with SMOP  0.41
from libsmop import *
# borehole.m

    
    
@function
def borehole(xx=None,*args,**kwargs):
    varargin = borehole.varargin
    nargin = borehole.nargin

    ##########################################################################
    
    # BOREHOLE FUNCTION
    
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
    
    # OUTPUT AND INPUT:
    
    # y  = water flow rate
# xx = [rw, r, Tu, Hu, Tl, Hl, L, Kw]
    
    #########################################################################
    
    rw=xx(1)
# borehole.m:37
    r=xx(2)
# borehole.m:38
    Tu=xx(3)
# borehole.m:39
    Hu=xx(4)
# borehole.m:40
    Tl=xx(5)
# borehole.m:41
    Hl=xx(6)
# borehole.m:42
    L=xx(7)
# borehole.m:43
    Kw=xx(8)
# borehole.m:44
    frac1=dot(dot(dot(2,pi),Tu),(Hu - Hl))
# borehole.m:46
    frac2a=dot(dot(2,L),Tu) / (dot(dot(log(r / rw),rw ** 2),Kw))
# borehole.m:48
    frac2b=Tu / Tl
# borehole.m:49
    frac2=dot(log(r / rw),(1 + frac2a + frac2b))
# borehole.m:50
    y=frac1 / frac2
# borehole.m:52
    return y
    
if __name__ == '__main__':
    pass
    