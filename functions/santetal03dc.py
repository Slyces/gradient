# Generated with SMOP  0.41
from libsmop import *
# santetal03dc.m

    
    
@function
def santetal03dc(x=None,*args,**kwargs):
    varargin = santetal03dc.varargin
    nargin = santetal03dc.nargin

    ##########################################################################
    
    # SANTNER ET AL. (2003) DAMPED COSINE FUNCTION
    
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
    
    fact1=exp(dot(- 1.4,x))
# santetal03dc.m:30
    fact2=cos(dot(dot(3.5,pi),x))
# santetal03dc.m:31
    y=dot(fact1,fact2)
# santetal03dc.m:33
    return y
    
if __name__ == '__main__':
    pass
    