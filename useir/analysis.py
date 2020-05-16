import matplotlib.pyplot as plt

def plot_useir(dfs, lbls, T = 'uSEIR', figsize=(10,10)):

    fig = plt.figure(figsize=figsize)

    ax=plt.subplot(1,2,1)
    for i, df in enumerate(dfs):
        df.head()
        ls = f'S-{lbls[i]}'
        lr = f'R-{lbls[i]}'
        plt.plot(df.t, df.S, lw=2, label=ls)
        plt.plot(df.t, df.R, lw=2, label=lr)


    plt.xlabel('time (days)')
    plt.ylabel('Fraction of population')
    plt.legend()
    plt.title(T)

    ax=plt.subplot(1,2,2)
    for i, df in enumerate(dfs):
        le = f'E-{lbls[i]}'
        li = f'I-{lbls[i]}'
        plt.plot(df.t, df.E, lw=2, label=le)
        plt.plot(df.t, df.I, lw=2, label=li)

    plt.xlabel('time (days)')
    plt.ylabel('Fraction of population')
    plt.legend()

    plt.title(T)
    plt.tight_layout()
    plt.show()
