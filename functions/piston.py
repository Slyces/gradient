# Generated with SMOP  0.41
from libsmop import *
# piston.m

    
    
@function
def piston(xx=None,*args,**kwargs):
    varargin = piston.varargin
    nargin = piston.nargin

    ##########################################################################
    
    # PISTON SIMULATION FUNCTION
    
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
    
    # C = cycle time
# xx = [M, S, V0, k, P0, Ta, T0]
    
    #########################################################################
    
    M=xx(1)
# piston.m:37
    S=xx(2)
# piston.m:38
    V0=xx(3)
# piston.m:39
    k=xx(4)
# piston.m:40
    P0=xx(5)
# piston.m:41
    Ta=xx(6)
# piston.m:42
    T0=xx(7)
# piston.m:43
    Aterm1=dot(P0,S)
# piston.m:45
    Aterm2=dot(19.62,M)
# piston.m:46
    Aterm3=dot(- k,V0) / S
# piston.m:47
    A=Aterm1 + Aterm2 + Aterm3
# piston.m:48
    Vfact1=S / (dot(2,k))
# piston.m:50
    Vfact2=sqrt(A ** 2 + dot(dot(dot(4,k),(dot(P0,V0) / T0)),Ta))
# piston.m:51
    V=dot(Vfact1,(Vfact2 - A))
# piston.m:52
    fact1=copy(M)
# piston.m:54
    fact2=k + dot(dot((S ** 2),(dot(P0,V0) / T0)),(Ta / (V ** 2)))
# piston.m:55
    C=dot(dot(2,pi),sqrt(fact1 / fact2))
# piston.m:57
    return C
    
if __name__ == '__main__':
    pass
    