# Generated with SMOP  0.41
from libsmop import *
# welchetal92.m

    
    
@function
def welchetal92(xx=None,*args,**kwargs):
    varargin = welchetal92.varargin
    nargin = welchetal92.nargin

    ##########################################################################
    
    # WELCH ET AL. (1992) FUNCTION
    
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
    
    # INPUT:
    
    # xx = [x1, x2, ..., x20]
    
    ##########################################################################
    
    x1=xx(1)
# welchetal92.m:36
    x2=xx(2)
# welchetal92.m:37
    x3=xx(3)
# welchetal92.m:38
    x4=xx(4)
# welchetal92.m:39
    x5=xx(5)
# welchetal92.m:40
    x6=xx(6)
# welchetal92.m:41
    x7=xx(7)
# welchetal92.m:42
    x8=xx(8)
# welchetal92.m:43
    x9=xx(9)
# welchetal92.m:44
    x10=xx(10)
# welchetal92.m:45
    x11=xx(11)
# welchetal92.m:46
    x12=xx(12)
# welchetal92.m:47
    x13=xx(13)
# welchetal92.m:48
    x14=xx(14)
# welchetal92.m:49
    x15=xx(15)
# welchetal92.m:50
    x16=xx(16)
# welchetal92.m:51
    x17=xx(17)
# welchetal92.m:52
    x18=xx(18)
# welchetal92.m:53
    x19=xx(19)
# welchetal92.m:54
    x20=xx(20)
# welchetal92.m:55
    term1=dot(5,x12) / (1 + x1)
# welchetal92.m:57
    term2=dot(5,(x4 - x20) ** 2)
# welchetal92.m:58
    term3=x5 + dot(40,x19 ** 3) - dot(5,x19)
# welchetal92.m:59
    term4=dot(0.05,x2) + dot(0.08,x3) - dot(0.03,x6)
# welchetal92.m:60
    term5=dot(0.03,x7) - dot(0.09,x9) - dot(0.01,x10)
# welchetal92.m:61
    term6=dot(- 0.07,x11) + dot(0.25,x13 ** 2) - dot(0.04,x14)
# welchetal92.m:62
    term7=dot(0.06,x15) - dot(0.01,x17) - dot(0.03,x18)
# welchetal92.m:63
    y=term1 + term2 + term3 + term4 + term5 + term6 + term7
# welchetal92.m:65
    return y
    
if __name__ == '__main__':
    pass
    