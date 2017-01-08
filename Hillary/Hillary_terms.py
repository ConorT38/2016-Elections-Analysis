import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from ast import literal_eval

with open('Hillary_load.json') as f:
    data = literal_eval(f.read())

df = pd.DataFrame(data,index=[0])
print df

df2 = pd.DataFrame(df,columns=list(df.columns.values),index=[0])
df2.plot.bar()
plt.show()
