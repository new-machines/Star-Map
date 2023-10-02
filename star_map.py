import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define the coordinates and distances of the stars from our Sun
star_data = [
    {"name": "Barnard's Star", "distance": 5.96, "ra": 17.96, "dec": 4.69},
    {"name": "Alpha Centauri A", "distance": 4.37, "ra": 14.66, "dec": -60.84},
    {"name": "Alpha Centauri B", "distance": 4.37, "ra": 14.66, "dec": -60.84},
    {"name": "Sirius A", "distance": 8.58, "ra": 101.29, "dec": -16.72},
    {"name": "Luyten's Star", "distance": 12.36, "ra": 111.85, "dec": 5.23},
]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the Sun at the center
ax.scatter(0, 0, 0, marker='o', s=100, label='Sun', color='yellow')

# Plot the stars at their respective scaled positions based on distance
for star in star_data:
    x = star["distance"] * np.cos(np.radians(star["dec"])) * np.cos(np.radians(star["ra"]))
    y = star["distance"] * np.cos(np.radians(star["dec"])) * np.sin(np.radians(star["ra"]))
    z = star["distance"] * np.sin(np.radians(star["dec"]))
    ax.scatter(x, y, z, marker='o', s=50, label=star["name"])

# Set labels and title
ax.set_xlabel('X (Light-years)')
ax.set_ylabel('Y (Light-years)')
ax.set_zlabel('Z (Light-years)')
ax.set_title('Stellar Positions in 3D Space (Relative to Our Sun)')

# Add a legend
ax.legend()

# Show the plot
plt.show()