# Generated with SMOP  0.41
from libsmop import *
# curretal88explc.m

    
    
@function
def curretal88explc(xx=None,*args,**kwargs):
    varargin = curretal88explc.varargin
    nargin = curretal88explc.nargin

    ##########################################################################
    
    # CURRIN ET AL. (1988) EXPONENTIAL FUNCTION, LOWER FIDELITY CODE
# Calls: curretal88exp.m
# This function, from Xiong et al. (2013), is used as the "low-accuracy
# code" version of the function curretal88exp.m.
    
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
    
    # xx = [x1, x2]
    
    #########################################################################
    
    x1=xx(1)
# curretal88explc.m:39
    x2=xx(2)
# curretal88explc.m:40
    maxarg=max(concat([0,x2 - 1 / 20]))
# curretal88explc.m:42
    yh1=curretal88exp(concat([x1 + 1 / 20,x2 + 1 / 20]))
# curretal88explc.m:44
    yh2=curretal88exp(concat([x1 + 1 / 20,maxarg]))
# curretal88explc.m:45
    yh3=curretal88exp(concat([x1 - 1 / 20,x2 + 1 / 20]))
# curretal88explc.m:46
    yh4=curretal88exp(concat([x1 - 1 / 20,maxarg]))
# curretal88explc.m:47
    y=(yh1 + yh2 + yh3 + yh4) / 4
# curretal88explc.m:49
    return y
    
if __name__ == '__main__':
    pass
    