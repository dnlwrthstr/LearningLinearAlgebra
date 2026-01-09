#!/usr/bin/env python3
"""
simulate_pca_projection.py
Visualize PCA projection onto the first principal component.
"""

import numpy as np
import matplotlib.pyplot as plt

# --- Step 1: Dataset
X = np.array([
    [2, 0],
    [0, 1],
    [3, 2],
    [4, 3],
    [5, 5]
])

# --- Step 2: Center data
X_centered = X - X.mean(axis=0)

# --- Step 3: Covariance & Eigen Decomposition
C = np.cov(X_centered.T)
eigvals, eigvecs = np.linalg.eig(C)
order = np.argsort(eigvals)[::-1]
eigvals, eigvecs = eigvals[order], eigvecs[:, order]

# --- Step 4: Project onto first principal component
pc1 = eigvecs[:, 0]
X_proj = (X_centered @ pc1[:, None]) * pc1  # re-expand to 2D coordinates

# --- Step 5: Plot
plt.figure(figsize=(6, 6))
plt.scatter(X_centered[:, 0], X_centered[:, 1], color='blue', label='Original data')

# Projection lines
for i in range(len(X)):
    plt.plot([X_centered[i, 0], X_proj[i, 0]],
             [X_centered[i, 1], X_proj[i, 1]],
             'k--', alpha=0.5)

# Projected points
plt.scatter(X_proj[:, 0], X_proj[:, 1], color='orange', label='Projected (onto PC1)')

# Principal component arrows
origin = np.zeros(2)
plt.quiver(*origin, *pc1, angles='xy', scale_units='xy', scale=1, color='red', label='PC1')

plt.axis('equal')
plt.title('PCA: Projection onto First Principal Component')
plt.legend()
plt.xlabel('x₁ (centered)')
plt.ylabel('x₂ (centered)')
plt.grid(True)
plt.show()
