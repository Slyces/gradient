# Generated with SMOP  0.41
from libsmop import *
# boreholelc.m

    
    
@function
def boreholelc(xx=None,*args,**kwargs):
    varargin = boreholelc.varargin
    nargin = boreholelc.nargin

    ##########################################################################
    
    # BOREHOLE FUNCTION, LOWER FIDELITY CODE
# This function is used as the "low-accuracy code" version of the function
# borehole.m.
    
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
    
    # y = water flow rate
# xx = [rw, r, Tu, Hu, Tl, Hl, L, Kw]
    
    #########################################################################
    
    rw=xx(1)
# boreholelc.m:39
    r=xx(2)
# boreholelc.m:40
    Tu=xx(3)
# boreholelc.m:41
    Hu=xx(4)
# boreholelc.m:42
    Tl=xx(5)
# boreholelc.m:43
    Hl=xx(6)
# boreholelc.m:44
    L=xx(7)
# boreholelc.m:45
    Kw=xx(8)
# boreholelc.m:46
    frac1=dot(dot(5,Tu),(Hu - Hl))
# boreholelc.m:48
    frac2a=dot(dot(2,L),Tu) / (dot(dot(log(r / rw),rw ** 2),Kw))
# boreholelc.m:50
    frac2b=Tu / Tl
# boreholelc.m:51
    frac2=dot(log(r / rw),(1.5 + frac2a + frac2b))
# boreholelc.m:52
    y=frac1 / frac2
# boreholelc.m:54
    return y
    
if __name__ == '__main__':
    pass
    