# Generated with SMOP  0.41
from libsmop import *
# wingweight.m

    
    
@function
def wingweight(xx=None,*args,**kwargs):
    varargin = wingweight.varargin
    nargin = wingweight.nargin

    ##########################################################################
    
    # WING WEIGHT FUNCTION
    
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
    
    # OUTPUT AND INPUT:
    
    # y  = wing weight
# xx = [Sw, Wfw, A, LamCaps, q, lam, tc, Nz, Wdg, Wp]
    
    #########################################################################
    
    Sw=xx(1)
# wingweight.m:37
    Wfw=xx(2)
# wingweight.m:38
    A=xx(3)
# wingweight.m:39
    LamCaps=dot(xx(4),(pi / 180))
# wingweight.m:40
    q=xx(5)
# wingweight.m:41
    lam=xx(6)
# wingweight.m:42
    tc=xx(7)
# wingweight.m:43
    Nz=xx(8)
# wingweight.m:44
    Wdg=xx(9)
# wingweight.m:45
    Wp=xx(10)
# wingweight.m:46
    fact1=dot(dot(0.036,Sw ** 0.758),Wfw ** 0.0035)
# wingweight.m:48
    fact2=(A / ((cos(LamCaps)) ** 2)) ** 0.6
# wingweight.m:49
    fact3=dot(q ** 0.006,lam ** 0.04)
# wingweight.m:50
    fact4=(dot(100,tc) / cos(LamCaps)) ** (- 0.3)
# wingweight.m:51
    fact5=(dot(Nz,Wdg)) ** 0.49
# wingweight.m:52
    term1=dot(Sw,Wp)
# wingweight.m:54
    y=dot(dot(dot(dot(fact1,fact2),fact3),fact4),fact5) + term1
# wingweight.m:56
    return y
    
if __name__ == '__main__':
    pass
    