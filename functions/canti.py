# Generated with SMOP  0.41
from libsmop import *
# canti.m

    
    
@function
def canti(xx=None,w=None,t=None,*args,**kwargs):
    varargin = canti.varargin
    nargin = canti.nargin

    ##########################################################################
    
    # CANTILEVER BEAM FUNCTIONS
    
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
    
    # OUTPUTS AND INPUTS:
    
    # D  = displacement
# S  = stress
# xx = [R, E, X, Y]
# w  = width (optional)
# t  = thickness (optional)
    
    #########################################################################
    
    R=xx(1)
# canti.m:40
    E=xx(2)
# canti.m:41
    X=xx(3)
# canti.m:42
    Y=xx(4)
# canti.m:43
    L=100
# canti.m:45
    D_0=2.2535
# canti.m:46
    if (nargin == 1):
        w=4
# canti.m:49
        t=2
# canti.m:50
    else:
        if (nargin == 2):
            t=2
# canti.m:52
    
    Sterm1=dot(600,Y) / (dot(w,(t ** 2)))
# canti.m:55
    Sterm2=dot(600,X) / (dot((w ** 2),t))
# canti.m:56
    S=Sterm1 + Sterm2
# canti.m:58
    Dfact1=dot(4,(L ** 3)) / (dot(dot(E,w),t))
# canti.m:60
    Dfact2=sqrt((Y / (t ** 2)) ** 2 + (X / (w ** 2)) ** 2)
# canti.m:61
    D=dot(Dfact1,Dfact2)
# canti.m:63
    return D,S
    
if __name__ == '__main__':
    pass
    