# Generated with SMOP  0.41
from libsmop import *
# stybtang.m

    
    
@function
def stybtang(xx=None,*args,**kwargs):
    varargin = stybtang.varargin
    nargin = stybtang.nargin

    ##########################################################################
    
    # STYBLINSKI-TANG FUNCTION
    
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
    
    # xx = [x1, x2, ..., xd]
    
    ##########################################################################
    
    d=length(xx)
# stybtang.m:36
    sum=0
# stybtang.m:37
    for ii in arange(1,d).reshape(-1):
        xi=xx(ii)
# stybtang.m:39
        new=xi ** 4 - dot(16,xi ** 2) + dot(5,xi)
# stybtang.m:40
        sum=sum + new
# stybtang.m:41
    
    y=sum / 2
# stybtang.m:44
    return y
    
if __name__ == '__main__':
    pass
    