#!/usr/bin/env python3
"""
simulate_pca.py
Visualize PCA on a simple 2D dataset.
"""

import numpy as np
import matplotlib.pyplot as plt

# --- Step 1: Create a 2D dataset
X = np.array([
    [2, 0],
    [0, 1],
    [3, 2],
    [4, 3],
    [5, 5]
])

# --- Step 2: Center the data (subtract the mean)
X_centered = X - X.mean(axis=0)

# --- Step 3: Compute covariance matrix
C = np.cov(X_centered.T)

# --- Step 4: Compute eigenvalues & eigenvectors
eigvals, eigvecs = np.linalg.eig(C)

# --- Step 5: Sort by largest eigenvalue
order = np.argsort(eigvals)[::-1]
eigvals, eigvecs = eigvals[order], eigvecs[:, order]

# --- Step 6: Project data onto the first principal component
X_pca = X_centered @ eigvecs[:, 0]

# --- Step 7: Plot original vs PCA direction
plt.figure(figsize=(6, 6))
plt.scatter(X_centered[:, 0], X_centered[:, 1], color='blue', label='Original data')

# Principal axes
origin = np.zeros(2)
for i in range(2):
    plt.quiver(*origin, *eigvecs[:, i], angles='xy', scale_units='xy', scale=1,
               color=['red', 'green'][i], label=f'PC{i+1}')

plt.axis('equal')
plt.title('PCA Visualization: Eigenvectors as Principal Axes')
plt.legend()
plt.xlabel('x₁ (centered)')
plt.ylabel('x₂ (centered)')
plt.grid(True)
plt.show()
