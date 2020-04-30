# Authors: Bogdan Marinski, Konstantin Boev
# Version: 1.0.0 (30.04.2020)

def get_cap():

    # This function returns the name and a path to a random image of a cap

    import os
    import random as rdm

    a = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'resources\caps'))
    b = str('\\')
    c = rdm.choice(os.listdir(r'.\resources\caps'))
    d = a+b+c
    
    return([str(c), str(d)])
