# Generated with SMOP  0.41
from libsmop import *
# goldprsc.m

    
    
@function
def goldprsc(xx=None,*args,**kwargs):
    varargin = goldprsc.varargin
    nargin = goldprsc.nargin

    ##########################################################################
    
    # GOLDSTEIN-PRICE FUNCTION, SCALED
    
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
    
    ##########################################################################
    
    x1bar=dot(4,xx(1)) - 2
# goldprsc.m:36
    x2bar=dot(4,xx(2)) - 2
# goldprsc.m:37
    fact1a=(x1bar + x2bar + 1) ** 2
# goldprsc.m:39
    fact1b=19 - dot(14,x1bar) + dot(3,x1bar ** 2) - dot(14,x2bar) + dot(dot(6,x1bar),x2bar) + dot(3,x2bar ** 2)
# goldprsc.m:40
    fact1=1 + dot(fact1a,fact1b)
# goldprsc.m:41
    fact2a=(dot(2,x1bar) - dot(3,x2bar)) ** 2
# goldprsc.m:43
    fact2b=18 - dot(32,x1bar) + dot(12,x1bar ** 2) + dot(48,x2bar) - dot(dot(36,x1bar),x2bar) + dot(27,x2bar ** 2)
# goldprsc.m:44
    fact2=30 + dot(fact2a,fact2b)
# goldprsc.m:45
    prod=dot(fact1,fact2)
# goldprsc.m:47
    y=(log(prod) - 8.693) / 2.427
# goldprsc.m:49
    return y
    
if __name__ == '__main__':
    pass
    