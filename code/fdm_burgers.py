#!/usr/bin/env python
"""
fdm_burgers.py

1D Burgers' Equation Solver

SHSH <sandy.herho@email.ucr.edu>
01/09/24
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import seaborn as sns

def main():
    plt.style.use("bmh")

    nt = 1000  
    nx = 101   
    nu = 0.01 / np.pi  
    dt = 0.001 
    dx = 2 / (nx - 1) 

    x = np.linspace(-1, 1, nx)  
    u = np.sin(np.pi * x)
    uf = np.zeros((nt, nx))  
    uf[0, :] = u  

    for n in range(1, nt):
        un = uf[n-1, :].copy()
        for i in range(1, nx - 1):
            # Updated diffusion scheme
            u[i] = un[i] + nu * dt / dx**2 * (un[i+1] - 2 * un[i] + un[i-1])
        uf[n, :] = u

    X, T = np.meshgrid(x, np.linspace(0, nt*dt, nt))

    fig_3d = plt.figure(figsize=(12, 9))
    ax_3d = fig_3d.add_subplot(111, projection='3d')
    surf = ax_3d.plot_surface(X, T, uf, cmap=cm.coolwarm, edgecolor='none')
    ax_3d.set_xlabel(r"$x$ [m]", fontsize=12, labelpad=10)
    ax_3d.set_ylabel(r"$t$ [s]", fontsize=12, labelpad=10)
    ax_3d.set_zlabel(r"$u$ [m/s]", fontsize=12, labelpad=10)
    fig_3d.colorbar(surf, ax=ax_3d, shrink=0.5, aspect=5)

    fig_heatmap = plt.figure(figsize=(12, 9))
    ax_heatmap = fig_heatmap.add_subplot(111)
    sns.heatmap(uf.T, cmap="coolwarm", cbar_kws={"label": r"$u$ [m/s]"})
    ax_heatmap.set_xlabel(r"$x$ [m]", fontsize=12)
    ax_heatmap.set_ylabel(r"$t$ [s]", fontsize=12)

    plt.show()

if __name__ == "__main__":
    main()
