#!/usr/bin/env python3
# Name: (Daniel Rice)
# Class: (INFO 1200)
# Section: (001)
# Professor: (Dr. Crandall)
# Date: 2/22/2023
# Project #: MO5_P2_converter
# I declare that the source code contained in this assignment was written solely by me.
# I understand that copying any source code, in whole or in part,
# constitutes cheating, and that I will receive a zero on this project
# if I am found in violation of this policy.

def to_meters(feet):
    """Converts meters to feet

    Args:
        feet (_type_): User inputs amount of feet

    Returns:
        _type_: _description_
    """
    meters = feet * 0.3048  # meters variable is feet input mulitplied by conversion rate
    return meters  # reset meters value


def to_feet(meters):
    '''
    Converts feet to meters
    param: user inputs meter value
    '''
    feet = meters / 0.3048  # feet variable is meters input divided by conversion rate
    return feet  # reset feet value
