# Generated with SMOP  0.41
from libsmop import *
# robot.m

    
    
@function
def robot(xx=None,*args,**kwargs):
    varargin = robot.varargin
    nargin = robot.nargin

    ##########################################################################
    
    # ROBOT ARM FUNCTION
    
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
    
    #########################################################################
    
    # OUTPUT AND INPUTS:
    
    # y = distance from the end of the arm to the origin
# xx = [theta1, theta2, theta3, theta4, L1, L2, L3, L4]
    
    #########################################################################
    
    theta=xx(arange(1,4))
# robot.m:37
    L=xx(arange(5,8))
# robot.m:38
    sumu=0
# robot.m:40
    sumv=0
# robot.m:41
    for ii in arange(1,4).reshape(-1):
        Li=L(ii)
# robot.m:43
        sumtheta=0
# robot.m:44
        for jj in arange(1,ii).reshape(-1):
            thetai=theta(jj)
# robot.m:46
            sumtheta=sumtheta + thetai
# robot.m:47
        sumu=sumu + dot(Li,cos(sumtheta))
# robot.m:49
        sumv=sumv + dot(Li,sin(sumtheta))
# robot.m:50
    
    u=copy(sumu)
# robot.m:53
    v=copy(sumv)
# robot.m:54
    y=(u ** 2 + v ** 2) ** (0.5)
# robot.m:56
    return y
    
if __name__ == '__main__':
    pass
    