# Welcome to electricity_usage

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/weyandtim/electricity_usage/ci.yml?branch=main)](https://github.com/weyandtim/electricity_usage/actions/workflows/ci.yml)
[![Documentation Status](https://readthedocs.org/projects/electricity_usage/badge/)](https://electricity_usage.readthedocs.io/)
[![codecov](https://codecov.io/gh/weyandtim/electricity_usage/branch/main/graph/badge.svg)](https://codecov.io/gh/weyandtim/electricity_usage)

## Installation

The Python package `electricity_usage` can be installed by cloning the git repository and installing it using pip install.

```
git clone https://github.com/weyandtim/electricity_usage
pip install electricity_usage
```
<!-- Hier muss auf jeden Fall noch eine Beschreibung wie der Spaß mit dem AP key funktioniert! -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

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

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

The electricity\_usage package provides a scheduler which will kick off processes only when there is a surplus in local energy production.  
For more information see the usage documentation.
<!-- usage should be linked properly here, if possible -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

This project was done as a software practical by Tim Weyand and Nemo Glade, under supervision of Dominic Kempf.

If you wish to contribute to electricity\_usage open an issue in the issue tracker of the [GitHub project](https://github.com/weyandtim/electricity_usage/issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments

This repository was set up using the [SSC Cookiecutter for Python Packages](https://github.com/ssciwr/cookiecutter-python-package).

The project relies on data from [electricity maps](https://github.com/electricitymaps/electricitymaps-contrib).
