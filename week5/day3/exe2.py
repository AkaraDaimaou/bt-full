import matplotlib.pyplot as plt

# Data points
data = [(1, 2), (1.5, 3), (2, 1), (2.5, 4), (3, 1), (3.5, 3)]

# Extract x and y coordinates
x = [point[0] for point in data]
y = [point[1] for point in data]

# Create scatter plot
plt.scatter(x, y)

# Set labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot')

# Show the plot
plt.show()