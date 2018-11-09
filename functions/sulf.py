# Generated with SMOP  0.41
from libsmop import *
# sulf.m

    
    
@function
def sulf(xx=None,*args,**kwargs):
    varargin = sulf.varargin
    nargin = sulf.nargin

    ##########################################################################
    
    # SULFUR MODEL FUNCTION
    
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
    
    # DeltaF = direct radiative forcing by sulfate aerosols
# xx = [Tr, Ac, Rs, beta_bar, Psi_e, f_Psi_e, Q, Y, L]
    
    #########################################################################
    
    Tr=xx(1)
# sulf.m:37
    Ac=xx(2)
# sulf.m:38
    Rs=xx(3)
# sulf.m:39
    beta_bar=xx(4)
# sulf.m:40
    Psi_e=xx(5)
# sulf.m:41
    f_Psi_e=xx(6)
# sulf.m:42
    Q=xx(7)
# sulf.m:43
    Y=xx(8)
# sulf.m:44
    L=xx(9)
# sulf.m:45
    S0=1366
# sulf.m:47
    A=dot(5,10 ** 14)
# sulf.m:48
    fact1=dot(dot(dot(dot(dot(dot((S0 ** 2),(1 - Ac)),(Tr ** 2)),(1 - Rs) ** 2),beta_bar),Psi_e),f_Psi_e)
# sulf.m:50
    fact2=dot(dot(dot(3,Q),Y),L) / A
# sulf.m:51
    DeltaF=dot(dot(- 1 / 2,fact1),fact2)
# sulf.m:53
    return DeltaF
    
if __name__ == '__main__':
    pass
    