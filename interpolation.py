# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 22:43:43 2023

@author: johnn

We will use this file to interpolate for ME40
"""
#First let us define the function
def interp(x1,y1,x2,y2,input):
    slope = (y2-y1) / (x2-x1) 
    b = y1-(slope*x1)
    y = (slope * input) + b
    return print(f'The output is: {y} \nThe slope is: {slope} \nThe y-intercept is: {b}')

def quality(f=None, g=None, fg=None, x=None, input=None, find=None, check=None):
    if find=='x':
        x = (input-f) / fg
        return print(f'The quality is: {x}') #, check)
    elif find=='x-v':
        check = (input-f) / (g-f)
        return print(f'The quality is: {check}')
    elif find=='output':
        input = f + x*fg
        return print(f'The output is: {input}')
    elif find=='output-v':
        input = (f*(1-x))+(x*g)
        return print(f'The output is: {input}')