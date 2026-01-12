#!/bin/bash

# clean_and_push.sh
# Automates the cleaning of Jupyter notebooks and the Git commit/push process.

if [ -z "$1" ]; then
    echo "Error: No commit message provided."
    echo "Usage: ./scripts/clean_and_push.sh \"Your commit message\""
    exit 1
fi

COMMIT_MESSAGE=$1

echo "--- 1. Cleaning Jupyter Notebooks ---"
python3 scripts/clean_notebooks.py

if [ $? -ne 0 ]; then
    echo "Error: Notebook cleaning failed. Aborting commit."
    exit 1
fi

echo "--- 2. Staging changes ---"
git add .

echo "--- 3. Committing ---"
git commit -m "$COMMIT_MESSAGE"

if [ $? -ne 0 ]; then
    echo "Error: Git commit failed. Aborting push."
    exit 1
fi

echo "--- 4. Pushing to remote ---"
git push

echo "--- Done! ---"
