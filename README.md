# Welcome to electricity_usage

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/weyandtim/electricity_usage/ci.yml?branch=main)](https://github.com/weyandtim/electricity_usage/actions/workflows/ci.yml)
[![Documentation Status](https://readthedocs.org/projects/electricity_usage/badge/)](https://electricity_usage.readthedocs.io/)
[![codecov](https://codecov.io/gh/weyandtim/electricity_usage/branch/main/graph/badge.svg)](https://codecov.io/gh/weyandtim/electricity_usage)

## Installation

The Python package `electricity_usage` can be installed from PyPI:

```
python -m pip install electricity_usage
```

## Development installation

If you want to contribute to the development of `electricity_usage`, we recommend
the following editable installation from this repository:

```
git clone https://github.com/weyandtim/electricity_usage
cd electricity_usage
python -m pip install --editable .[tests]
```

Having done so, the test suite can be run using `pytest`:

```
python -m pytest
```

## Acknowledgments

This repository was set up using the [SSC Cookiecutter for Python Packages](https://github.com/ssciwr/cookiecutter-python-package).
