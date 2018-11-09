# Generated with SMOP  0.41
from libsmop import *
# levy.m

    
    
@function
def levy(xx=None,*args,**kwargs):
    varargin = levy.varargin
    nargin = levy.nargin

    ##########################################################################
    
    # LEVY FUNCTION
    
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
# levy.m:36
    for ii in arange(1,d).reshape(-1):
        w[ii]=1 + (xx(ii) - 1) / 4
# levy.m:39
    
    term1=(sin(dot(pi,w(1)))) ** 2
# levy.m:42
    term3=dot((w(d) - 1) ** 2,(1 + (sin(dot(dot(2,pi),w(d)))) ** 2))
# levy.m:43
    sum=0
# levy.m:45
    for ii in arange(1,(d - 1)).reshape(-1):
        wi=w(ii)
# levy.m:47
        new=dot((wi - 1) ** 2,(1 + dot(10,(sin(dot(pi,wi) + 1)) ** 2)))
# levy.m:48
        sum=sum + new
# levy.m:49
    
    y=term1 + sum + term3
# levy.m:52
    return y
    
if __name__ == '__main__':
    pass
    