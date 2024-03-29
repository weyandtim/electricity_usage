# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'electricity_usage'
copyright = '2024, Tim Weyand, Nemo Glade'
author = 'Tim Weyand, Nemo Glade'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "nbsphinx",
    "nbsphinx_link",
    "sphinx_mdinclude",
    "sphinx.ext.autodoc",
    "sphinx_rtd_theme",
    "sphinx_click"
]

# Modifying sy.path for click doc
import os
import sys
sys.path.insert(0, os.path.abspath('../electricity_usage'))

# Add any paths that contain templates here, relative to this directory.
templates_path = []

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_context = {
        'display_github': True,
        'github_user': 'weyandtim',
        'github_repo': 'electricity_usage',
        'github_version': 'main/doc/'
    }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []
