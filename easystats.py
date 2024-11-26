import numpy as np
import sympy as sp
from scipy.stats import chi2

class EasyStats:

    def __init__(self) -> None:
        pass


    def bereken_gemiddelde(self, metingen: list):
        gem = sum(metingen)/(len(metingen))
        return gem
    
    def bereken_variantie_gekend_gemiddelde(self, metingen: list, gekend_gem):
        s2 = sum((metingen - gekend_gem)**2)/(len(metingen))
        s = np.sqrt(s2)
        return s
    
    def bereken_variantie_ongekend_gemiddelde(self, metingen: list, ongekend_gem):
        s2 = sum((metingen - ongekend_gem)**2)/(len(metingen - 1))
        s = np.sqrt(s2)
        return s
    
    def foutpropagatie_som(self, a, b, s_x, s_y):
        return np.sqrt((a*s_x)**2 + (b*s_y)**2)
    
    def foutpropagatie_product(self, p, q, s_x, s_y, X, Y, Z):
        return Z*np.sqrt((p*(s_x/X))**2 + (q*(s_y/Y))**2)