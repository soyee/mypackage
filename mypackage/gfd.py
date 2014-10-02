# -*- coding: utf-8 -*-
"""
Triple quotes good for documentation
"""

import numpy as np
# Earth radius
A = 6.371e6 # m
# rotation rate
Om = 7.292e-5 # s^-1
# gravity
g = 9.81 # m/s^2


def f_coriolis(lat): 
    """Calculate the Coriolis parameter.
    Latitude is assumed to be in degrees."""
    return 2*Om*np.sin(np.radians(lat))