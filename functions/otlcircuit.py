# Generated with SMOP  0.41
from libsmop import *
# otlcircuit.m

    
    
@function
def otlcircuit(xx=None,*args,**kwargs):
    varargin = otlcircuit.varargin
    nargin = otlcircuit.nargin

    ##########################################################################
    
    # OTL CIRCUIT FUNCTION
    
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
    
    # Vm = midpoint voltage
# xx = [Rb1, Rb2, Rf, Rc1, Rc2, beta]
    
    #########################################################################
    
    Rb1=xx(1)
# otlcircuit.m:37
    Rb2=xx(2)
# otlcircuit.m:38
    Rf=xx(3)
# otlcircuit.m:39
    Rc1=xx(4)
# otlcircuit.m:40
    Rc2=xx(5)
# otlcircuit.m:41
    beta=xx(6)
# otlcircuit.m:42
    Vb1=dot(12,Rb2) / (Rb1 + Rb2)
# otlcircuit.m:44
    term1a=dot(dot((Vb1 + 0.74),beta),(Rc2 + 9))
# otlcircuit.m:45
    term1b=dot(beta,(Rc2 + 9)) + Rf
# otlcircuit.m:46
    term1=term1a / term1b
# otlcircuit.m:47
    term2a=dot(11.35,Rf)
# otlcircuit.m:49
    term2b=dot(beta,(Rc2 + 9)) + Rf
# otlcircuit.m:50
    term2=term2a / term2b
# otlcircuit.m:51
    term3a=dot(dot(dot(0.74,Rf),beta),(Rc2 + 9))
# otlcircuit.m:53
    term3b=dot((dot(beta,(Rc2 + 9)) + Rf),Rc1)
# otlcircuit.m:54
    term3=term3a / term3b
# otlcircuit.m:55
    Vm=term1 + term2 + term3
# otlcircuit.m:57
    return Vm
    
if __name__ == '__main__':
    pass
    