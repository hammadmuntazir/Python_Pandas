# Plotting
# Pandas uses the plot() method to create diagrams.

# We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.
#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
