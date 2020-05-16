from scipy.stats import gamma
from scipy.stats import nbinom
from scipy.stats import expon
from scipy.stats import poisson
import numpy as np
import pandas as pd

def solve_uSeir(ti_shape     = 5.5,
                   ti_scale     = 1,
                   tr_shape     = 6.5,
                   tr_scale     = 1,
                   R0           = 3.5):
    """
    The pure python version only uses the gamma distribution and fine grain.
    It's sole purpose is benchmarking the cython version
    """

    def compute_gamma_pde(t_shape, t_scale, eps, tol):
        ne = int(gamma.ppf(tol, a=t_shape, scale=t_scale) / eps)
        pdE = np.zeros(ne)
        cd1 = 0
        for i in np.arange(ne):
            cd2    = gamma.cdf(i*eps, a=t_shape, scale=t_scale)
            pdE[i] = cd2-cd1
            cd1    = cd2

        return ne, pdE

    N       = 1e+6
    Smin    = 1e-10
    Emin    = 1e-10
    nmax    = 75000
    eps     = 0.01
    prob    = R0 / tr_shape
    pn      = prob * eps
    tol     = 0.9999

    nE, pdE = compute_gamma_pde(ti_shape, ti_scale, eps, tol)
    nI, pdI = compute_gamma_pde(tr_shape, tr_scale, eps, tol)

    print(f' Function solve_uSeir: time epsilon = {eps}')
    print(f' statistical distribution is Gamma , ti = {ti_shape}, tr = {tr_shape}')
    print(f' number of exposed compartments = {nE}, infected compartments = {nI}')
    print(f' R0 = {R0}, prob = {prob}, pn = {pn}')

    I   = np.zeros(nI)
    E   = np.zeros(nE)
    S    = 1 - 1/N
    E[0] = 1 / N

    R    = 0
    sI   = 0

    TT = []
    SS = []
    EE = []
    II = []
    RR = []
    n    = 0

    while True:

        R += I[0]
        end = nI - 1
        for k in np.arange(end):
            I[k] = I[k+1] + pdI[k] * E[0]
        I[end] = pdI[end] * E[0]

        #print(I)

        end = nE - 1
        for k in np.arange(end):
            E[k] = E[k+1] + pn * pdE[k] * sI * S
        E[end]   = pn * pdE[end] * sI * S

        #print(E)

        S  = S - pn * sI * S

        sI = np.sum(I)
        sE = np.sum(E)

        #print(sI)
        #print(sE)
        TT.append(n * eps)
        SS.append(S)
        EE.append(sE)
        II.append(sI)
        RR.append(R)

        #print(f't = {n*eps} S = {S} E ={sE} I ={sI} R = {R}')
        n+=1
        if (sE < Smin and sI < Emin) or n > nmax:
            break

    df = pd.DataFrame(list(zip(TT, SS, EE, II, RR)),
               columns =['t', 'S', 'E', 'I', 'R'])

    return df
