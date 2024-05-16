import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

fig, axs = plt.subplots(2, 2)

# First subplot
axs[0, 0].plot(x, y, label='y')
axs[0, 0].annotate(f"Max: {np.max(y):.2f}", xy=(np.argmax(y), np.max(y)), xytext=(np.argmax(y), np.max(y)+0.5),
                   arrowprops=dict(facecolor='black', arrowstyle='->'))
axs[0, 0].annotate(f"Min: {np.min(y):.2f}", xy=(np.argmin(y), np.min(y)), xytext=(np.argmin(y), np.min(y)-0.5),
                   arrowprops=dict(facecolor='black', arrowstyle='->'))
axs[0, 0].legend(title='Legend', loc='upper right', shadow=True)

# Second subplot
axs[0, 1].plot(x, -y, label='-y')
axs[0, 1].annotate(f"Max: {np.max(-y):.2f}", xy=(np.argmax(-y), np.max(-y)), xytext=(np.argmax(-y), np.max(-y)+0.5),
                   arrowprops=dict(facecolor='black', arrowstyle='->'))
axs[0, 1].annotate(f"Min: {np.min(-y):.2f}", xy=(np.argmin(-y), np.min(-y)), xytext=(np.argmin(-y), np.min(-y)-0.5),
                   arrowprops=dict(facecolor='black', arrowstyle='->'))
axs[0, 1].legend(title='Legend', loc='upper right', shadow=True)

# Third subplot
axs[1, 0].plot(x, y**2, label='y squared')
axs[1, 0].annotate(f"Max: {np.max(y**2):.2f}", xy=(np.argmax(y**2), np.max(y**2)), xytext=(np.argmax(y**2), np.max(y**2)+0.5),
                   arrowprops=dict(facecolor='black', arrowstyle='->'))
axs[1, 0].annotate(f"Min: {np.min(y**2):.2f}", xy=(np.argmin(y**2), np.min(y**2)), xytext=(np.argmin(y**2), np.min(y**2)-0.5),
                   arrowprops=dict(facecolor='black', arrowstyle='->'))
axs[1, 0].legend(title='Legend', loc='upper right', shadow=True)

# Fourth subplot
axs[1, 1].plot(x, -y**2, label='-y squared')
axs[1, 1].annotate(f"Max: {np.max(-y**2):.2f}", xy=(np.argmax(-y**2), np.max(-y**2)), xytext=(np.argmax(-y**2), np.max(-y**2)+0.5),
                   arrowprops=dict(facecolor='black', arrowstyle='->'))
axs[1, 1].annotate(f"Min: {np.min(-y**2):.2f}", xy=(np.argmin(-y**2), np.min(-y**2)), xytext=(np.argmin(-y**2), np.min(-y**2)-0.5),
                   arrowprops=dict(facecolor='black', arrowstyle='->'))
axs[1, 1].legend(title='Legend', loc='upper right', shadow=True)

plt.show()