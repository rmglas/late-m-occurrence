import numpy as np
from matplotlib import pyplot as plt

fig, ax = plt.subplots(figsize=(8, 8))

x = np.linspace(0, 10, 10)
y = np.random.rand(len(x))
ax.plot(x, y)

fig.savefig("total_occurrence.pdf", bbox_inches="tight")