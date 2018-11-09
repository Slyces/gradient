# Generated with SMOP  0.41
from libsmop import *
# steelcol.m

    
    
@function
def steelcol(xx=None,*args,**kwargs):
    varargin = steelcol.varargin
    nargin = steelcol.nargin

    ##########################################################################
    
    # STEEL COLUMN FUNCTION
    
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
    
    # xx = [Fs, P1, P2, P3, B, D, H, F0, E]
    
    #########################################################################
    
    Fs=xx(1)
# steelcol.m:37
    P1=xx(2)
# steelcol.m:38
    P2=xx(3)
# steelcol.m:39
    P3=xx(4)
# steelcol.m:40
    B=xx(5)
# steelcol.m:41
    D=xx(6)
# steelcol.m:42
    H=xx(7)
# steelcol.m:43
    F0=xx(8)
# steelcol.m:44
    E=xx(9)
# steelcol.m:45
    L=7500
# steelcol.m:47
    P=P1 + P2 + P3
# steelcol.m:49
    Eb=dot(dot(dot(dot((pi ** 2),E),B),D),(H ** 2)) / (dot(2,(L ** 2)))
# steelcol.m:50
    term1=1 / (dot(dot(2,B),D))
# steelcol.m:52
    term2=dot(F0,Eb) / (dot(dot(dot(B,D),H),(Eb - P)))
# steelcol.m:53
    y=Fs - dot(P,(term1 + term2))
# steelcol.m:55
    return y
    
if __name__ == '__main__':
    pass
    