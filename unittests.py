from math import pi

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError('Radius must be type string or float')
    if r < 0:
        raise ValueError('Radius cannot be a negative number.')
    
    return pi * (r**2)