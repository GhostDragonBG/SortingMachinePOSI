def get_cap():

    # This function returns the name and a path to a random image of a cap

    import os
    import random as rdm

    a = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'resources\caps'))
    b = str('\\')
    c = rdm.choice(os.listdir(r'.\resources\caps'))
    d = a+b+c
    
    return([str(c), str(d)])
