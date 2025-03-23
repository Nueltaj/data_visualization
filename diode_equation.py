import matplotlib.pyplot as plt
import numpy as np

x_input = np.arange(0.0, 0.8, 0.1)
y_input = 0.03 * (np.exp(5 * x_input) - 1) 
plt.title("Diode Equation", fontsize=24)
plt.xlabel("Voltage(V)", fontsize=14)
plt.ylabel("Current Density(A/cm^2)", fontsize=14)
plt.plot(x_input, y_input, linewidth=2, color="red")
plt.tick_params(which="major", axis="both", labelsize=14)

plt.show()
