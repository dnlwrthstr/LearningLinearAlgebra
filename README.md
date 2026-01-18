# Learning Linear Algebra

A collection of Jupyter notebooks and Python scripts dedicated to learning and practicing Linear Algebra. The materials are organized based on different courses and difficulty levels.

## Project Structure

The project is divided into several main directories:

### 1. [Hyperskill](./hyperskill/)
Contains notebooks following the Hyperskill Linear Algebra track, organized by topics:
- **01 Vector and Vector Spaces**: Basics of vectors, operations, spaces, projections, and norms.
- **02 Matrices**: Introduction to matrices, types, operations, determinants, and inverses.
- **03 Systems of Linear Equations**: Solving systems using Gauss elimination and row transformations.
- **04 Linear Operators**: Subspaces, null space, range, and eigenvalues/eigenvectors.
- **05 Matrix Decomposition**: LU decomposition, diagonalization, SVD, and applications.
- **11 Advanced Concepts**: Fourier analysis, orthogonality, and advanced inner product spaces.

### 2. [Coursera](./coursera/)
Materials and assignments from Coursera Linear Algebra courses, including labs on NumPy, linear systems, and eigenvalues.

### 3. [Advanced Concepts](./advanced_concepts/)
Deep dives into more complex topics such as:
- Spectral theory
- Inner product spaces
- Orthogonal and unitary transformations
- Least squares optimization
- Pseudoinverse and rank deficiency
- Canonical forms
- Linear algebra in machine learning

### 4. Root Files
- `basic_notation.ipynb`: Introduction to fundamental notation.
- `simulate_pca.py` & `simulate_pca_2.py`: Python scripts for simulating Principal Component Analysis.

## Getting Started

To explore these notebooks, you will need a Python environment with Jupyter installed along with common scientific libraries. You can install all dependencies using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Before contributing or committing changes, you can use the following command to automatically clean your notebooks, stage changes, commit, and push in one go:

```bash
./scripts/clean_and_push.sh "Your commit message"
```

Alternatively, to just clean the notebooks:

```bash
python scripts/clean_notebooks.py
```

For more details, please refer to the [Commit Guidelines](.junie/guidelines.md).

Then, you can start the Jupyter Notebook server:

```bash
jupyter notebook
```

## License
This project is for educational purposes.
