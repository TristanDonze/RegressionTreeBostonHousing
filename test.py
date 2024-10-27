import numpy as np

y_t = np.array([10, 10])
pred = 35

print(np.mean(np.absolute((y_t - pred))))