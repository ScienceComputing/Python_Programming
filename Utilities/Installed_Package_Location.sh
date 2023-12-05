# Reference: https://stackoverflow.com/questions/122327/how-do-i-find-the-location-of-my-python-site-packages-directory

python -c 'import site; print(site.getsitepackages())

python -c "import scanpy as _; print(_.__path__)"
# ['/Users/user_name/.pyenv/versions/3.11.6/lib/python3.11/site-packages/scanpy']

python -c "import scanpy as _; print(_.__file__)"
# /Users/anniliu/.pyenv/versions/3.11.6/lib/python3.11/site-packages/scanpy/__init__.py

pip show scanpy
# Name: scanpy
# Version: 1.9.6
# Summary: Single-Cell Analysis in Python.
# Home-page:
# Author: Alex Wolf, Philipp Angerer, Fidel Ramirez, Isaac Virshup, Sergei Rybakov, Gokcen Eraslan, Tom White, Malte Luecken, Davide Cittaro, Tobias Callies, Marius Lange, Andrés R. Muñoz-Rojas
# Author-email:
# License:
# Location: /Users/user_name/.pyenv/versions/3.11.6/lib/python3.11/site-packages
# Requires: anndata, h5py, joblib, matplotlib, natsort, networkx, numba, numpy, packaging, pandas, patsy, scikit-learn, scipy, seaborn, session-info, statsmodels, tqdm, umap-learn
3 Required-by: sc-toolbox
