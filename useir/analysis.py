import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def useir_imax(dfs):
    I = dfs.I.values
    return np.max(I), np.argmax(I)


def useir_simax(dfs):
    SI = dfs.I.values * dfs.S.values
    return np.max(SI), np.argmax(SI)


def useir_s_at_simax(dfs):
    _, tsi = useir_simax(dfs)
    return dfs.S.values[tsi]


def useir_i_above_thr(dfs, thr=0.01):
    I = dfs.I.values
    return np.argmax(I>thr)



def useir_compared(quenched = False, I0 = 1e-3, r0 = 3.5, ti = 5.5, tr = 6.5, r1=0.5, tq = 50, eps= 0.01, dim = 20000):

    pdf = csolve_uSeir(dist = 'poisson',
                       quenched = quenched,
                       I0       = I0,
                       ti_shape = ti,
                       tr_shape = tr,
                       R0       = r0,
                       R1       = r1,
                       tq       = tq,
                       eps      = eps,
                       dim      = dim
                  )

    gdf = csolve_uSeir(dist = 'gamma',
                       quenched = quenched,
                       I0       = I0,
                       ti_shape = ti,
                       tr_shape = tr,
                       ti_scale = 1,
                       tr_scale = 1,
                       R0       = r0,
                       R1       = r1,
                       tq       = tq,
                       eps      = eps,
                       dim      = dim
                  )

    edf = csolve_uSeir(dist = 'expon',
                       quenched = quenched,
                       I0       = I0,
                       ti_scale = ti,
                       tr_scale = tr,
                       R0       = r0,
                       R1       = r1,
                       tq       = tq,
                       eps      = eps,
                       dim      = dim
                  )
    return gdf, edf, pdf


def useir_imax_and_i_above_thr_compared(pdfs, tpdfs, thr=0.001, eps=0.01):

    for i, dfs in enumerate(pdfs):
        imax, tmax = useir_imax(dfs)
        th         =useir_i_above_thr(dfs, thr)
        print(f'for distributions {tpdfs[i]}, imax = {imax}, tmax = {tmax}, t > th ({thr}) = {th * eps}')



def plot_useir(dfs, lbls, lines, T = 'uSEIR', xlim=(0,100), ylim=(0,0.3),figsize=(10,10)):

    fig = plt.figure(figsize=figsize)

    ax=plt.subplot(1,2,1)
    for i, df in enumerate(dfs):
        df.head()
        ls = f'S-{lbls[i]}'
        lr = f'R-{lbls[i]}'
        plt.plot(df.t, df.S, lw=2, linestyle=lines[i],label=ls)
        plt.plot(df.t, df.R, lw=2, linestyle=lines[i], label=lr)

    plt.xlim(*xlim)
    plt.ylim(0,1)
    plt.xlabel('time (days)')
    plt.ylabel('Fraction of population')
    plt.legend()
    plt.title(T)

    ax=plt.subplot(1,2,2)
    for i, df in enumerate(dfs):
        le = f'E-{lbls[i]}'
        li = f'I-{lbls[i]}'
        #plt.plot(df.t, df.E, lw=2, linestyle=lines[i], label=le)
        plt.plot(df.t, df.I, lw=2, linestyle=lines[i], label=li)

    plt.xlim(*xlim)
    plt.ylim(*ylim)
    plt.xlabel('time (days)')
    plt.ylabel('Fraction of population')
    plt.legend()

    plt.title(T)
    plt.tight_layout()
    plt.show()


def plot_useir_IS(dfs, lbls, T = 'uSEIR', figsize=(10,10)):

    fig = plt.figure(figsize=figsize)

    ax=plt.subplot(1,1,1)
    for i, df in enumerate(dfs):
        df.head()
        ls = f'S-{lbls[i]}'
        lr = f'R-{lbls[i]}'
        plt.plot(df.t, df.S * df.I, lw=2, label=ls)
        plt.plot(df.t, df.S, lw=2, linestyle='dashed',label=ls)


    plt.xlabel('time (days)')
    plt.ylabel('Fraction of population')
    plt.legend()
    plt.title(T)

    plt.title(T)
    plt.tight_layout()
    plt.show()
