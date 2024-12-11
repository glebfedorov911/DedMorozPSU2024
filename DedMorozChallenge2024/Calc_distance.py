# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 17:25:50 2024

@author: AM4
"""
######################################

# Пример использования функции:
# lon1 = 110.114
# lat1 = 44.427
# lon2 = -71.3593
# lat2 = 53.568

# geo_distance(lon1, lat1, lon2, lat2)

#######################################

def geo_distance(lon1, lat1, lon2, lat2):
    from math import radians, cos, sin, asin, sqrt
    # Формула гаверсинуса для вычисления расстояний между двумя точками на сфере Земли
    dlon = radians(lon2) - radians(lon1)
    dlat = radians(lat2) - radians(lat1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))     
    r = 6371 # радиус Земли
    return c * r
