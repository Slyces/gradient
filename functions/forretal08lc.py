# Generated with SMOP  0.41
from libsmop import *
# forretal08lc.m

    
    
@function
def forretal08lc(x=None,A=None,B=None,C=None,*args,**kwargs):
    varargin = forretal08lc.varargin
    nargin = forretal08lc.nargin

    ##########################################################################
    
    # FORRESTER ET AL. (2008) FUNCTION, LOWER FIDELITY CODE
# Calls: forretal08.m
# This function is used as the "low-accuracy code" version of the function
# forretal08.m.
    
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
    
    # INPUTS:
    
    # x = scalar
# A = constant (optional), with default value 0.5
# B = constant (optional), with default value 10
# C = constant (optional), with default value -5
    
    #########################################################################
    
    if (nargin < 4):
        C=- 5
# forretal08lc.m:43
    
    if (nargin < 3):
        B=10
# forretal08lc.m:46
    
    if (nargin < 2):
        A=0.5
# forretal08lc.m:49
    
    yh=forretal08(x)
# forretal08lc.m:52
    term1=dot(A,yh)
# forretal08lc.m:54
    term2=dot(B,(x - 0.5))
# forretal08lc.m:55
    y=term1 + term2 - C
# forretal08lc.m:57
    return y
    
if __name__ == '__main__':
    pass
    