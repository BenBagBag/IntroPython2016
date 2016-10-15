#!/usr/bin/env python3
"""
String Formatting Lab -- October 13, 2016
"""
import random

print('file_00{:} :     {:.2f},  {:.0e}'.format(2,123.4567,10000))

x = random.randrange(101)
y = random.randrange(101)
z = random.randrange(101)

print('The first 3 numbers are: {:d}, {:d}, {:d}'.format(x, y, z))