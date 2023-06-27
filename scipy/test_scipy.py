import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Sample data
x = np.array([1, 2, 4, 5, 8])
y = np.array([2, 3, 4, 5, 6])

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# Print the results
print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", r_value ** 2)
print("P-value:", p_value)
print("Standard error:", std_err)


# plot
fig, ax = plt.subplots()
#
ax.scatter(x, y)



plt.show()