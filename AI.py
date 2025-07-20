# --- (1) User Input and Parameter Setup ---
import numpy as np
import matplotlib.pyplot as plt
import hashlib

# Ask for user input
name = input("Enter your first name: ")
zoom_input = input("Enter zoom level (1-100): ")

# Convert input to numeric values
zoom = max(1, min(100, int(zoom_input)))  # clamp zoom to [1, 100]

# Generate a deterministic color shift based on the user's name
name_hash = int(hashlib.sha256(name.encode()).hexdigest(), 16)
color_shift = name_hash % 256

# Image dimensions and plot settings
width, height = 800, 800
max_iter = 256

# --- (2) Mandelbrot Set Computation ---
# Set plot boundaries based on zoom
scale = 1 / zoom
x_min, x_max = -2.5 * scale, 1.5 * scale
y_min, y_max = -2.0 * scale, 2.0 * scale

# Create meshgrid of complex numbers
x = np.linspace(x_min, x_max, width)
y = np.linspace(y_min, y_max, height)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y
Z = np.zeros_like(C)
mandelbrot = np.zeros(C.shape, dtype=int)

for i in range(max_iter):
    mask = np.abs(Z) < 1000
    Z[mask] = Z[mask] ** 2 + C[mask]
    mandelbrot[mask & (np.abs(Z) >= 1000)] = i

# --- (3) Plotting and Saving the Image ---
# Create a colormap that is shifted by the user's name
colors = (mandelbrot + color_shift) % 256
plt.figure(figsize=(8, 8))
plt.imshow(colors, cmap="twilight", extent=(x_min, x_max, y_min, y_max))
plt.axis("off")
plt.title(f"Mandelbrot Set for {name} (Zoom: {zoom})")
plt.savefig(f"mandelbrot_{name}.png", bbox_inches='tight')
plt.show()

