"""Helper module for building Jupyter notebooks as .ipynb JSON files."""
import json

def new_notebook():
    return {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.10.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

def _to_source(text):
    """Convert a string into the .ipynb source format (list of lines)."""
    lines = text.split('\n')
    result = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            result.append(line + '\n')
        else:
            if line:  # Don't add empty trailing line
                result.append(line)
    return result

def md(nb, text):
    """Add a markdown cell."""
    nb["cells"].append({
        "cell_type": "markdown",
        "metadata": {},
        "source": _to_source(text.strip())
    })

def code(nb, text):
    """Add a code cell."""
    nb["cells"].append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": _to_source(text.strip())
    })

def save(nb, filepath):
    """Save notebook to file."""
    with open(filepath, 'w') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f"Saved: {filepath} ({len(nb['cells'])} cells)")
