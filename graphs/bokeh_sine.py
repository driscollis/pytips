import numpy as np

from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show

N = 100
x = np.linspace(0, 4*np.pi, N)
y0 = np.sin(x)

output_file("sinewave.html")

sine = figure(width=500, plot_height=500, title="Sine")
sine.circle(x, y0, size=10, color="navy", alpha=0.5)

p = gridplot([[sine]], toolbar_location=None)

show(p)