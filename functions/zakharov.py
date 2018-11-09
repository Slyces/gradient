# Generated with SMOP  0.41
from libsmop import *
# zakharov.m

    
    
@function
def zakharov(xx=None,*args,**kwargs):
    varargin = zakharov.varargin
    nargin = zakharov.nargin

    ##########################################################################
    
    # ZAKHAROV FUNCTION
    
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
    
    # xx = [x1, x2, ..., xd]
    
    ##########################################################################
    
    d=length(xx)
# zakharov.m:36
    sum1=0
# zakharov.m:37
    sum2=0
# zakharov.m:38
    for ii in arange(1,d).reshape(-1):
        xi=xx(ii)
# zakharov.m:41
        sum1=sum1 + xi ** 2
# zakharov.m:42
        sum2=sum2 + dot(dot(0.5,ii),xi)
# zakharov.m:43
    
    y=sum1 + sum2 ** 2 + sum2 ** 4
# zakharov.m:46
    return y
    
if __name__ == '__main__':
    pass
    