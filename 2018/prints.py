try:
    import logging
    import os
    from enum import Enum
    import pandas as pd
    import numpy as np
    import math

    from prints import *

except:
    print("Imports failed")


def print_track(df_track_map):
    x_lim, y_lim = df_track_map.shape
    print(" ", end ="")

    for i in range(y_lim):
        print(i, end="")

    print("")

    for x in range(x_lim) : #x across, y down
        print(x, end="")

        for y in range(y_lim):
            item = df_track_map.iloc[(x,y)]
            print(item.track_string, end="")

        print("")

#def print_cart(df_track_map):