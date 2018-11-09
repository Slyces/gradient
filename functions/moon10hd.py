# Generated with SMOP  0.41
from libsmop import *
# moon10hd.m

    
    
@function
def moon10hd(xx=None,*args,**kwargs):
    varargin = moon10hd.varargin
    nargin = moon10hd.nargin

    ##########################################################################
    
    # MOON (2010) HIGH-DIMENSIONALITY FUNCTION
    
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
    
    # xx = [x1, x2, ..., x20]
    
    #########################################################################
    
    coefflin=concat([- 2.08,2.11,0.76,- 0.57,- 0.72,- 0.47,0.39,1.4,- 0.09,- 0.7,- 1.27,- 1.03,1.07,2.23,2.46,- 1.31,- 2.94,2.63,0.07,2.44])
# moon10hd.m:36
    sumdeg1=0
# moon10hd.m:38
    for ii in arange(1,20).reshape(-1):
        ci=coefflin(ii)
# moon10hd.m:40
        xi=xx(ii)
# moon10hd.m:41
        sumdeg1=sumdeg1 + dot(ci,xi)
# moon10hd.m:42
    
    coeffs=zeros(20,20)
# moon10hd.m:45
    coeffs[arange(),1]=concat([1.42,2.18,0.58,- 1.21,- 7.15,- 1.29,- 0.19,- 2.75,- 1.16,- 1.09,0.89,- 0.16,4.43,1.65,- 1.25,- 1.35,1.15,- 19.71,23.72,1.42]).T
# moon10hd.m:46
    coeffs[arange(),2]=concat([0,- 1.7,0.84,1.2,- 2.35,- 0.16,- 0.19,- 5.93,- 1.15,1.89,- 3.47,- 0.07,- 0.6,- 1.09,- 3.23,0.44,1.24,2.13,- 0.71,1.64]).T
# moon10hd.m:47
    coeffs[arange(),3]=concat([0,0,1.0,- 0.49,1.74,1.29,- 0.35,- 4.73,3.27,1.87,1.42,- 0.96,- 0.91,2.06,2.89,0.25,1.97,3.04,2.0,1.64]).T
# moon10hd.m:48
    coeffs[arange(),4]=concat([0,0,0,- 3.23,2.75,- 1.4,0.24,- 0.7,- 0.17,- 3.38,- 1.87,- 0.17,1.56,2.4,- 1.7,0.32,2.11,- 0.2,1.39,- 2.01]).T
# moon10hd.m:49
    coeffs[arange(),5]=concat([0,0,0,0,- 1.1,2.34,- 3.9,- 0.8,0.13,- 3.97,1.99,0.45,1.77,- 0.5,1.86,0.02,- 2.08,- 1.78,1.76,1.3]).T
# moon10hd.m:50
    coeffs[arange(),6]=concat([0,0,0,0,0,0.21,- 0.03,- 0.37,- 1.27,2.78,1.37,- 2.75,- 3.15,1.86,0.12,- 0.74,1.06,- 3.76,- 0.43,1.25]).T
# moon10hd.m:51
    coeffs[arange(),7]=concat([0,0,0,0,0,0,- 4.16,0.26,- 0.3,- 2.69,- 2.56,28.99,- 2.13,1.36,1.45,3.09,- 1.73,- 1.66,- 3.94,- 2.56]).T
# moon10hd.m:52
    coeffs[arange(),8]=concat([0,0,0,0,0,0,0,- 1.0,0.77,1.09,- 1.15,- 1.09,- 2.74,1.59,1.41,0.48,2.16,0.34,4.17,0.73]).T
# moon10hd.m:53
    coeffs[arange(),9]=concat([0,0,0,0,0,0,0,0,3.06,2.46,5.8,- 5.15,- 2.05,3.17,3.4,- 0.49,- 6.71,- 0.74,2.78,- 0.41]).T
# moon10hd.m:54
    coeffs[arange(),10]=concat([0,0,0,0,0,0,0,0,0,3.34,2.36,- 1.77,- 3.16,1.89,2.2,- 0.71,- 3.78,0.98,1.4,- 0.59]).T
# moon10hd.m:55
    coeffs[arange(),11]=concat([0,0,0,0,0,0,0,0,0,0,- 1.17,- 2.45,6.04,3.22,0.19,- 0.03,- 2.65,- 1.02,- 1.96,- 2.66]).T
# moon10hd.m:56
    coeffs[arange(),12]=concat([0,0,0,0,0,0,0,0,0,0,0,1.52,1.36,- 0.59,- 1.05,- 0.84,- 1.3,0.42,1.86,- 0.32]).T
# moon10hd.m:57
    coeffs[arange(),13]=concat([0,0,0,0,0,0,0,0,0,0,0,0,0.42,- 0.5,0.21,- 0.18,3.04,- 0.53,- 0.12,0.09]).T
# moon10hd.m:58
    coeffs[arange(),14]=concat([0,0,0,0,0,0,0,0,0,0,0,0,0,- 1.13,- 2.42,- 3.93,- 2.3,0.4,0.81,- 1.1]).T
# moon10hd.m:59
    coeffs[arange(),15]=concat([0,0,0,0,0,0,0,0,0,0,0,0,0,0,- 0.26,5.31,1.66,- 3.1,3.37,4.32]).T
# moon10hd.m:60
    coeffs[arange(),16]=concat([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,- 2.26,0.0,- 0.77,- 3.9,- 1.08]).T
# moon10hd.m:61
    coeffs[arange(),17]=concat([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.62,- 1.06,- 0.86,0.44]).T
# moon10hd.m:62
    coeffs[arange(),18]=concat([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.35,- 1.99,1.5]).T
# moon10hd.m:63
    coeffs[arange(),19]=concat([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,- 13.34,1.34]).T
# moon10hd.m:64
    coeffs[arange(),20]=concat([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,- 0.38]).T
# moon10hd.m:65
    sumdeg2=0
# moon10hd.m:67
    for ii in arange(1,20).reshape(-1):
        xi=xx(ii)
# moon10hd.m:69
        for jj in arange(1,ii).reshape(-1):
            cij=coeffs(ii,jj)
# moon10hd.m:71
            xj=xx(jj)
# moon10hd.m:72
            sumdeg2=sumdeg2 + dot(dot(cij,xi),xj)
# moon10hd.m:73
    
    y=sumdeg1 + sumdeg2
# moon10hd.m:77
    return y
    
if __name__ == '__main__':
    pass
    