import matplotlib.pyplot as plt
import numpy as np

def plot(vectors, xlim=(-10, 10), ylim=(-10, 10), figsize=(6, 6)):
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


def add(v1, v2, xlim=(-10, 10), ylim=(-10, 10), figsize=(6, 6)):
    """
    Calcola la somma di due vettori e visualizza i due vettori, la loro somma e il parallelogramma risultante.

    :param v1: Primo vettore (tuple o array).
    :param v2: Secondo vettore (tuple o array).
    :param xlim: Limiti dell'asse x (default: (-10, 10)).
    :param ylim: Limiti dell'asse y (default: (-10, 10)).
    :param figsize: Dimensioni della figura in pollici (default: (6, 6)).
    :return: La somma dei due vettori come array numpy.
    """
    # Calcolo della somma dei vettori
    v_sum = np.array(v1) + np.array(v2)

    # Vettori del parallelogramma
    parallelogram = [
        (0, 0),
        (v1[0], v1[1]),
        (v1[0] + v2[0], v1[1] + v2[1]),
        (v2[0], v2[1]),
        (0, 0)
    ]

    # Estrarre le coordinate x e y del parallelogramma
    px, py = zip(*parallelogram)

    # Plot dei vettori e del parallelogramma
    plt.figure(figsize=figsize)
    plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label='v1', width=0.005)
    plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b', label='v2', width=0.005)
    plt.quiver(0, 0, v_sum[0], v_sum[1], angles='xy', scale_units='xy', scale=1, color='g', label='v1 + v2', width=0.005)
    plt.plot(px, py, linestyle='--', color='gray', label='Parallelogramma')

    # Impostazioni del grafico
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.axhline(0, color='black', linewidth=1.5, linestyle='-')
    plt.axvline(0, color='black', linewidth=1.5, linestyle='-')
    plt.xticks(np.arange(xlim[0], xlim[1] + 1, 1))
    plt.yticks(np.arange(ylim[0], ylim[1] + 1, 1))
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()

    return v_sum



def test():
    print("ciao")
