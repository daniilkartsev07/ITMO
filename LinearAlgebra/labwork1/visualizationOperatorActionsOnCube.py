import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

"""
Действие оператора на куб
"""

A = np.array([
    [3, 0, 0],
    [0, -1, 0],
    [0, 0, 2]
])



vertices = np.array([
    [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
    [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]
])


edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],
    [4, 5], [5, 6], [6, 7], [7, 4],
    [0, 4], [1, 5], [2, 6], [3, 7]
]


faces_indices = [
    [0, 1, 2, 3], [4, 5, 6, 7],
    [0, 1, 5, 4], [2, 3, 7, 6],
    [0, 3, 7, 4], [1, 2, 6, 5]
]



transformed_vertices = (A @ vertices.T).T


fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')


for idx in faces_indices:
    poly = Poly3DCollection([vertices[idx]], alpha=0.2, facecolor='blue', edgecolor='blue')
    ax.add_collection3d(poly)

for start, end in edges:
    ax.plot([vertices[start][0], vertices[end][0]],
            [vertices[start][1], vertices[end][1]],
            [vertices[start][2], vertices[end][2]], 'b--', linewidth=1)


for idx in faces_indices:
    poly = Poly3DCollection([transformed_vertices[idx]], alpha=0.6, facecolor='red', edgecolor='darkred')
    ax.add_collection3d(poly)

for start, end in edges:
    ax.plot([transformed_vertices[start][0], transformed_vertices[end][0]],
            [transformed_vertices[start][1], transformed_vertices[end][1]],
            [transformed_vertices[start][2], transformed_vertices[end][2]], 'r-', linewidth=1.5)


ax.set_xlim(-1, 4)
ax.set_ylim(-2, 2)
ax.set_zlim(-1, 3)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'Действие оператора A на куб\nA = {A.tolist()}')

plt.show()

