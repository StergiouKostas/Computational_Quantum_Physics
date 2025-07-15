import numpy as np
from math import pi, sqrt

# =============================================
# Slater-Type Orbitals in POSITION SPACE (Sr)
# =============================================

# ---- s-orbitals ---- #
def Sr1s(z, r):
    return 2 * z**(1.5) * np.exp(-z * r)

def Sr2s(z, r):
    return (2/sqrt(3)) * z**(2.5) * r * np.exp(-z * r)

def Sr3s(z, r):
    return (2**1.5)/(3*sqrt(5)) * z**(3.5) * r**2 * np.exp(-z * r)

def Sr4s(z, r):
    return 2/(3*sqrt(35)) * z**(4.5) * r**3 * np.exp(-z * r)

def Sr5s(z, r):
    return (2**1.5)/(45*sqrt(7)) * z**(5.5) * r**4 * np.exp(-z * r)

# ---- p-orbitals ---- #
def Sr2p(z, r):
    return (2/sqrt(3)) * z**(2.5) * r * np.exp(-z * r)

def Sr3p(z, r):
    return (2**1.5)/(3*sqrt(5)) * z**(3.5) * r**2 * np.exp(-z * r)

def Sr4p(z, r):
    return 2/(3*sqrt(35)) * z**(4.5) * r**3 * np.exp(-z * r)

def Sr5p(z, r):
    return (2**1.5)/(45*sqrt(7)) * z**(5.5) * r**4 * np.exp(-z * r)

# ---- d-orbitals ---- #
def Sr3d(z, r):
    return (2**1.5)/(3*sqrt(5)) * z**(3.5) * r**2 * np.exp(-z * r)

def Sr4d(z, r):
    return 2/(3*sqrt(35)) * z**(4.5) * r**3 * np.exp(-z * r)

# =============================================
# Slater-Type Orbitals in MOMENTUM SPACE (Sk)
# =============================================

# ---- s-orbitals ---- #
def Sk1s(z, k):
    return (2*pi)**(-1.5) * 16*pi * z**(2.5) / (z**2 + k**2)**2

def Sk2s(z, k):
    return (2*pi)**(-1.5) * 16*pi * z**(2.5) * (3*z**2 - k**2) / (sqrt(3) * (z**2 + k**2)**3)

def Sk3s(z, k):
    return (2*pi)**(-1.5) * 64*sqrt(10)*pi * z**(4.5) * (z**2 - k**2) / (5 * (z**2 + k**2)**4)

def Sk4s(z, k):
    return (2*pi)**(-1.5) * 64*pi * z**(4.5) * (5*z**4 - 10*z**2*k**2 + k**4) / (sqrt(35) * (z**2 + k**2)**5)

def Sk5s(z, k):
    return (2*pi)**(-1.5) * 128*sqrt(14)*pi * z**(6.5) * (3*z**4 - 10*z**2*k**2 + 3*k**4) / (21 * (z**2 + k**2)**6)

# ---- p-orbitals ---- #
def Sk2p(z, k):
    return (2*pi)**(-1.5) * 64*pi * k * z**(3.5) / (sqrt(3) * (z**2 + k**2)**3)

def Sk3p(z, k):
    return (2*pi)**(-1.5) * 64*sqrt(10)*pi * k * z**(3.5) * (5*z**2 - k**2) / (15 * (z**2 + k**2)**4)

def Sk4p(z, k):
    return (2*pi)**(-1.5) * 128*pi * k * z**(5.5) * (5*z**2 - 3*k**2) / (sqrt(35) * (z**2 + k**2)**5)

def Sk5p(z, k):
    return (2*pi)**(-1.5) * 128*sqrt(14)*pi * k * z**(5.5) * (35*z**4 - 42*z**2*k**2 + 3*k**4) / (105 * (z**2 + k**2)**6)

# ---- d-orbitals ---- #
def Sk3d(z, k):
    return (2*pi)**(-1.5) * 128*sqrt(10)*pi * k**2 * z**(4.5) / (5 * (z**2 + k**2)**4)

def Sk4d(z, k):
    return (2*pi)**(-1.5) * 128*pi * k**2 * z**(4.5) * (7*z**2 - k**2) / (sqrt(35) * (z**2 + k**2)**5)