# Commit Guidelines

To maintain a clean and efficient repository, please follow these steps before committing and pushing your changes:

1.  **Clear Notebook Outputs & Remove Empty Cells**: 
    Always clean your Jupyter notebooks before committing. This reduces file size and prevents unnecessary diffs.
    Use the provided utility script:
    ```bash
    python scripts/clean_notebooks.py
    ```
    This script automatically clears outputs and removes empty cells from all `.ipynb` files in the project.

2.  **Update README.md**: 
    If your changes introduce new topics, notebooks, or dependencies, ensure the `README.md` is updated accordingly to reflect the current state of the project.

3.  **Verify Code & Tests**: 
    If applicable, ensure that any scripts or code snippets in the notebooks are functioning as expected.

4.  **Commit and Push**:
    Once the above steps are completed, stage your changes, commit with a descriptive message, and push to the remote repository.

---
*These guidelines are enforced to ensure project quality and consistency.*
