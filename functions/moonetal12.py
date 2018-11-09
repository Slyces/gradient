# Generated with SMOP  0.41
from libsmop import *
# moonetal12.m

    
    
@function
def moonetal12(xx=None,*args,**kwargs):
    varargin = moonetal12.varargin
    nargin = moonetal12.nargin

    ##########################################################################
    
    # MOON ET AL. (2012) FUNCTION
# Calls: borehole.m, wingweight.m, otlcircuit.m, piston.m
    
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
    
    # xx = [x1, x2, ..., x31]
    
    #########################################################################
    
    y[1]=borehole(xx(arange(1,8)))
# moonetal12.m:37
    y[2]=wingweight(xx(arange(9,18)))
# moonetal12.m:38
    y[3]=otlcircuit(xx(arange(19,24)))
# moonetal12.m:39
    y[4]=piston(xx(arange(25,31)))
# moonetal12.m:40
    miny=min(y)
# moonetal12.m:42
    maxy=max(y)
# moonetal12.m:43
    for ii in arange(1,4).reshape(-1):
        ystar[ii]=(y(ii) - miny) / (maxy - miny)
# moonetal12.m:46
    
    y=sum(ystar)
# moonetal12.m:49
    return y
    
if __name__ == '__main__':
    pass
    