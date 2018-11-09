# Generated with SMOP  0.41
from libsmop import *
# detpep10exp.m

    
    
@function
def detpep10exp(xx=None,*args,**kwargs):
    varargin = detpep10exp.varargin
    nargin = detpep10exp.nargin

    ##########################################################################
    
    # DETTE & PEPELYSHEV (2010) EXPONENTIAL FUNCTION
    
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
    
    # INPUT:
    
    # xx = [x1, x2, x3]
    
    #########################################################################
    
    x1=xx(1)
# detpep10exp.m:36
    x2=xx(2)
# detpep10exp.m:37
    x3=xx(3)
# detpep10exp.m:38
    term1=exp(- 2 / (x1 ** 1.75))
# detpep10exp.m:40
    term2=exp(- 2 / (x2 ** 1.5))
# detpep10exp.m:41
    term3=exp(- 2 / (x3 ** 1.25))
# detpep10exp.m:42
    y=dot(100,(term1 + term2 + term3))
# detpep10exp.m:44
    return y
    
if __name__ == '__main__':
    pass
    