import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.DataFrame(np.random.rand(10, 3), columns=list("ABC"))
df.plot(title="3 random columns")
plt.show()
