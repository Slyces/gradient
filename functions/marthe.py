# Generated with SMOP  0.41
from libsmop import *
# marthe.m

    
    ##########################################################################
    
    # MARTHE DATASET READ-IN
    
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
    
    # OBSERVATIONS: 300
    
    # INPUT VARIABLES:
    
    # per1  = hydraulic conductivity layer 1
# per2  = hydraulic conductivity layer 2
# per3  = hydraulic conductivity layer 3
# perz1 = hydraulic conductivity zone 1
# perz2 = hydraulic conductivity zone 2
# perz3 = hydraulic conductivity zone 3
# perz4 = hydraulic conductivity zone 4
# d1    = longitudinal dispersivity layer 1
# d2    = longitudinal dispersivity layer 2
# d3    = longitudinal dispersivity layer 3
# dt1   = transversal dispersivity layer 1
# dt2   = transversal dispersivity layer 2
# dt3   = transversal dispersivity layer 3
# kd1   = volumetric distribution coefficient 1.1
# kd2   = volumetric distribution coefficient 1.2
# kd3   = volumetric distribution coefficient 1.3
# poros = porosity
# i1    = infiltration type 1
# i2    = infiltration type 2
# i3    = infiltration type 3
    
    # OUTPUT VARIABLES:
    
    # p102K
# p104
# p106
# p2_76
# p29K
# p31K
# p35K
# p37K
# p38
# p4b
    
    #########################################################################
    
    marthe=importdata('marthedata.txt')
# marthe.m:68
    marthedata=marthe.data
# marthe.m:69
    per1=marthedata(arange(),1)
# marthe.m:71
    per2=marthedata(arange(),2)
# marthe.m:72
    per3=marthedata(arange(),3)
# marthe.m:73
    perz1=marthedata(arange(),4)
# marthe.m:74
    perz2=marthedata(arange(),5)
# marthe.m:75
    perz3=marthedata(arange(),6)
# marthe.m:76
    perz4=marthedata(arange(),7)
# marthe.m:77
    d1=marthedata(arange(),8)
# marthe.m:78
    d2=marthedata(arange(),9)
# marthe.m:79
    d3=marthedata(arange(),10)
# marthe.m:80
    dt1=marthedata(arange(),11)
# marthe.m:81
    dt2=marthedata(arange(),12)
# marthe.m:82
    dt3=marthedata(arange(),13)
# marthe.m:83
    kd1=marthedata(arange(),14)
# marthe.m:84
    kd2=marthedata(arange(),15)
# marthe.m:85
    kd3=marthedata(arange(),16)
# marthe.m:86
    poros=marthedata(arange(),17)
# marthe.m:87
    i1=marthedata(arange(),18)
# marthe.m:88
    i2=marthedata(arange(),19)
# marthe.m:89
    i3=marthedata(arange(),20)
# marthe.m:90
    p102K=marthedata(arange(),21)
# marthe.m:92
    p104=marthedata(arange(),22)
# marthe.m:93
    p106=marthedata(arange(),23)
# marthe.m:94
    p2_76=marthedata(arange(),24)
# marthe.m:95
    p29K=marthedata(arange(),25)
# marthe.m:96
    p31K=marthedata(arange(),26)
# marthe.m:97
    p35K=marthedata(arange(),27)
# marthe.m:98
    p37K=marthedata(arange(),28)
# marthe.m:99
    p38=marthedata(arange(),29)
# marthe.m:100
    p4b=marthedata(arange(),30)
# marthe.m:101