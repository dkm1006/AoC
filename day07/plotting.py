import matplotlib.pyplot as plt
import numpy as np

def plot_solution(results):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    container = ax.bar(np.arange(len(results)), results)
    plt.show()
