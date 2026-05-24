import numpy as np
import matplotlib.pyplot as plt


A = np.array([
    [3, 0, 0],
    [0, -1, 0],
    [0, 0, 2]
])


eigenvalues, eigenvectors = np.linalg.eig(A)


idx = eigenvalues.argsort()
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

print("Собственные значения (Lambda):")
for i in range(3):
    print(f"λ_{i + 1} = {eigenvalues[i]:.2f}")


fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')


colors = ['r', 'g', 'b']
labels = [r'$\lambda_1 = 3$', r'$\lambda_2 = -1$', r'$\lambda_3 = 2$']


for i in range(3):
    vec = eigenvectors[:, i]

    scale = 2.5

    ax.quiver(0, 0, 0, vec[0] * scale, vec[1] * scale, vec[2] * scale,
              color=colors[i], linewidth=2, arrow_length_ratio=0.1,
              label=labels[i])


    ax.text(vec[0] * scale * 1.2, vec[1] * scale * 1.2, vec[2] * scale * 1.2,
            f"λ={eigenvalues[i]}", color=colors[i], fontsize=12, fontweight='bold')


ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-3, 3)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Собственные векторы оператора')
ax.legend()


ax.scatter(0, 0, 0, color='black', s=50)

plt.grid(True)
plt.show()
