#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 16:05:54 2018

@author: 3415104
"""

import numpy as np, utils, os


def getData(directory):
    
    if not os.path.exists(directory):
        print("Directory doesn't exist")
    
    else:
        for point in os.listdir(directory):
            if os.path.isdir(point):
                # We try if the point is completely calculated
                if "adam" not in os.listdir(os.path.join(directory, point)):
                    continue
                elif "summary" not in os.listdir(os.path.join(directory, point, 'adam')):
                    continue
                else:
                    # Do
                    print("Point completely calculated")
                    return True
    