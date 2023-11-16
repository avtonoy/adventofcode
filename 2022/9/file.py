import gnuplotlib as gp
import numpy as np

x = np.linspace(-5,5,100)
gp.plot( (x, np.sin(x), {'with': 'boxes'}),
             (x, np.cos(x), {'legend': 'cosine'}),
            terminal = 'dumb 80,40',
            unset    = 'grid')

import termplotlib as tpl 
x = np.linspace(0, 2 * np.pi, 10)
y = np.sin(x)


x=[1,2]
y=[3,4]
fig = tpl.figure()
fig.plot(x, y, label="data", width=50, height=15, )
fig.show()