"""
Single-Cell RNA-Seq Analysis

This script performs analysis on single-cell RNA-Seq data.
"""

# Standard library imports
import datetime
import os
import sys

# Third-party package imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scanpy as sc
import seaborn as sns

# Local module and package imports
from clustering import perform_clustering
from preprocessing import preprocess_data
from visualization import visualize_results
