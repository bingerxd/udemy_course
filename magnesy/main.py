import numpy as np
import matplotlib.pyplot as plt

# Wymiary siatki
n_rows, n_cols = 50, 50

# Liczba punktów w rzędzie i kolumnie
n_points = 19

# Odległość między punktami
point_spacing = (n_rows - 1) / (n_points - 1)

# Utworzenie siatki
grid = np.zeros((n_rows, n_cols))
for i in range(n_points):
    for j in range(n_points):
        row = int(i * point_spacing)
        col = int(j * point_spacing)
        grid[row, col] = 1

# Stworzenie wykresu
plt.imshow(grid, cmap='Greys')
plt.axis('off')
plt.title('Siatka punktów')
plt.show()