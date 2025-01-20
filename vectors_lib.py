import matplotlib.pyplot as plt
import numpy as np

def plot_vectors(vectors, xlim=(-10, 10), ylim=(-10, 10), figsize=(6, 6)):
    """
    Plotta una serie di vettori su una griglia cartesiana, assegnando un colore diverso a ciascun vettore.
    
    :param vectors: Dizionario con i nomi dei vettori come chiavi e i vettori (tuple o array) come valori.
    :param xlim: Limiti dell'asse x (default: (-10, 10)).
    :param ylim: Limiti dell'asse y (default: (-10, 10)).
    :param figsize: Dimensioni della figura in pollici (default: (6, 6)).
    """
    plt.figure(figsize=figsize)
    
    colors = ['r', 'b', 'g', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown']
    for i, (name, vector) in enumerate(vectors.items()):
        color = colors[i % len(colors)]
        plt.quiver(0, 0, *vector, angles='xy', scale_units='xy', scale=1, label=name, color=color, width=0.005)
    
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.axhline(0, color='black', linewidth=1.5, linestyle='-')
    plt.axvline(0, color='black', linewidth=1.5, linestyle='-')
    plt.xticks(np.arange(xlim[0], xlim[1] + 1, 1))
    plt.yticks(np.arange(ylim[0], ylim[1] + 1, 1))
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()



def test():
    print("ciao")
