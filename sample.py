test = 'Wow this works!'
print(test)

! pip install plotly
from plotly import offline
offline.init_notebook_mode()

offline.iplot([{"y": [1, 2, 1]}])


import numpy as np
import pandas as pd


df = pd.DataFrame({'A': 1.,
                   'B': pd.Timestamp('20130102'),
                   'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                   'D': np.array([3] * 4, dtype='int32'),
                   'E': pd.Categorical(["test", "train", "test", "train"]),
                   'F': 'foo'})

df


import numpy as np
import matplotlib.pyplot as plt
from plotly import offline as py
py.init_notebook_mode()

t = np.linspace(0, 20, 500)
plt.plot(t, np.sin(t))

py.iplot_mpl(plt.gcf())


from IPython.display import JSON

data = {"foo": {"bar": "baz"}, "a": 1}
JSON(data)
