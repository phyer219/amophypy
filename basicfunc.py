import numpy as np

def bose(energy, beta):
    '''
    Bose Einstein distribution:
    bose = 1 / (exp(beta * energy) - 1)
    '''
    bose = np.exp(-beta*energy) / (1 - exp(-beta*energy))
    return bose
    
