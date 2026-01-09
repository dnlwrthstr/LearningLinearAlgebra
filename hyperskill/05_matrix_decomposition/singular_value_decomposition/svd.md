# Understanding the Singular Value Decomposition (SVD)

## 1. The Basic Idea

For **any** \(m \times n\) matrix \(A\), there exist matrices \(U\), \(\Sigma\), and \(V\) such that:

$$
A = U\,\Sigma\,V^{T}
$$

Where:

- \(U\) is an \(m \times m\) **orthogonal** matrix  
- \(V\) is an \(n \times n\) **orthogonal** matrix  
- \(\Sigma\) is an \(m \times n\) **diagonal** matrix with **non-negative** entries  

Orthogonal means:

$$
U^T U = I, \qquad V^T V = I
$$

SVD decomposes any linear map into:

1. Rotate/reflect the input: \(V^T\)  
2. Scale along axes: \(\Sigma\)  
3. Rotate/reflect the output: \(U\)

In other words:

$$
\text{rotation} \;\rightarrow\; \text{scaling} \;\rightarrow\; \text{rotation}
$$

---

## 2. The Components of SVD

### 2.1 The Diagonal Matrix \(\Sigma\)

$$
\Sigma =
\begin{pmatrix}
\sigma_1 & 0 & \cdots & 0 \\
0 & \sigma_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \sigma_r
\end{pmatrix}
$$

Where:

- \(\sigma_1 \ge \sigma_2 \ge \dots \ge 0\) (singular values)  
- \(r = \text{rank}(A)\)

Key fact:

$$
\sigma_i = \sqrt{\lambda_i}
$$

where \(\lambda_i\) are the eigenvalues of \(A^T A\) or \(A A^T\).

---

### 2.2 Left Singular Vectors — Columns of \(U\)

The columns of \(U\) are eigenvectors of \(A A^T\):

$$
A A^{T} u_i = \sigma_i^2 \, u_i
$$

They describe important directions in the **output space** of \(A\).

---

### 2.3 Right Singular Vectors — Columns of \(V\)

The columns of \(V\) are eigenvectors of \(A^T A\):

$$
A^{T} A v_i = \sigma_i^2 \, v_i
$$

They describe important directions in the **input space** of \(A\).

---

## 3. The Core Relationship

For each singular triplet \((\sigma_i, u_i, v_i)\):

$$
A v_i = \sigma_i u_i
$$

Meaning:

- \(v_i\) is a direction in the input  
- \(A\) maps it to direction \(u_i\), scaled by \(\sigma_i\)

Matrix form:

$$
A = \sum_{i=1}^{r} \sigma_i \, u_i v_i^{T}
$$

A sum of rank-1 matrices.

---

## 4. Why SVD is the “Best” Decomposition

### 4.1 Works for all matrices
Square, rectangular, rank-deficient — everything.

### 4.2 Reveals rank

$$
\text{rank}(A) = |\{ \sigma_i > 0 \}|
$$

### 4.3 Best low-rank approximation

$$
A_k = \sum_{i=1}^{k} \sigma_i u_i v_i^{T}
$$

Minimizes:

- The Frobenius norm  
- The spectral norm  

### 4.4 Extremely useful

Used in:

- PCA  
- Pseudoinverses  
- Recommender systems  
- Denoising  
- Image compression  

---

## 5. A Small Example

Let:

$$
A =
\begin{pmatrix}
3 & 1 \\
0 & 2
\end{pmatrix}
$$

SVD represents \(A\) as:

1. Rotate  
2. Scale by \(\sigma_1, \sigma_2\)  
3. Rotate again  

---

## 6. Summary

$$
\boxed{A = U \Sigma V^T}
$$

Where:

- \(\Sigma\) contains the singular values  
- Columns of \(U\) are eigenvectors of \(A A^T\)  
- Columns of \(V\) are eigenvectors of \(A^T A\)  

SVD = **rotation → scaling → rotation**.

---