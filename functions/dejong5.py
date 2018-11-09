# Generated with SMOP  0.41
from libsmop import *
# dejong5.m

    
    
@function
def dejong5(xx=None,*args,**kwargs):
    varargin = dejong5.varargin
    nargin = dejong5.nargin

    ##########################################################################
    
    # DE JONG FUNCTION N. 5
    
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
    
    x1=xx(1)
# dejong5.m:36
    x2=xx(2)
# dejong5.m:37
    sum=0
# dejong5.m:38
    A=zeros(2,25)
# dejong5.m:40
    a=concat([- 32,- 16,0,16,32])
# dejong5.m:41
    A[1,arange()]=repmat(a,1,5)
# dejong5.m:42
    ar=repmat(a,5,1)
# dejong5.m:43
    ar=ravel(ar).T
# dejong5.m:44
    A[2,arange()]=ar
# dejong5.m:45
    for ii in arange(1,25).reshape(-1):
        a1i=A(1,ii)
# dejong5.m:48
        a2i=A(2,ii)
# dejong5.m:49
        term1=copy(ii)
# dejong5.m:50
        term2=(x1 - a1i) ** 6
# dejong5.m:51
        term3=(x2 - a2i) ** 6
# dejong5.m:52
        new=1 / (term1 + term2 + term3)
# dejong5.m:53
        sum=sum + new
# dejong5.m:54
    
    y=1 / (0.002 + sum)
# dejong5.m:57
    return y
    
if __name__ == '__main__':
    pass
    