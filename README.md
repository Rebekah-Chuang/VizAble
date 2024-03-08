# VizAble
![PyPI - Version](https://img.shields.io/pypi/v/VizAble?style=for-the-badge&logo=PyPI&logoColor=white&color=blue&link=https%3A%2F%2Fpypi.org%2Fproject%2FVizAble%2F)
![GitHub Release](https://img.shields.io/github/v/release/Rebekah-Chuang/VizAble?display_name=release&style=for-the-badge&link=https%3A%2F%2Fgithub.com%2FRebekah-Chuang%2FVizAble%2Freleases)
![GitHub License](https://img.shields.io/github/license/Rebekah-Chuang/VizAble?style=for-the-badge&link=https%3A%2F%2Fgithub.com%2FRebekah-Chuang%2FVizAble%3Ftab%3DMIT-1-ov-file%23readme)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/Rebekah-Chuang/VizAble/run-pytest-with-tox.yaml?style=for-the-badge&label=Tests)](https://github.com/Rebekah-Chuang/VizAble/actions/workflows/run-pytest-with-tox.yaml)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/VizAble?style=for-the-badge&link=https%3A%2F%2Fpypi.org%2Fproject%2FVizAble%2F)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white&style=for-the-badge)](https://conventionalcommits.org)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json&style=for-the-badge)](https://python-poetry.org/)

**VizAble** is a web-based data visualization tool that generates accessible visualizations for all users, including people with visual impairments (low vision or blind).

## Prerequisites
Before getting started, ensure you have the following requirements in place:
1. **Python Version:** Ensure you have Python version **3.9** or higher installed. You can verify your Python version by running:
    ```python
    python --version
    ```
2. **Virtual Environment Setup:** It's recommended to create and activate a virtual environment before installation. Below is an example of creating and activating a virtual environment using Python's built-in `venv` module. Note that this is just one example, and there are other options available for creating virtual environments:

    a. Create a virtual environment (replace `env_name` with your desired environment name):
    ```
    python -m venv env_name
    ```
    b. Activate the virtual environment:
    ```
    source env_name/bin/activate
    ```

## Installation
You can install **VizAble** either from **PyPI** for the latest stable version or directly from **GitHub** for the latest development version:

a. Install the latest stable version from **PyPI** using `pip`:
```
pip install -U VizAble
```
b. Or, install the latest development version from **GitHub**:
```
pip install -U git+https://github.com/Rebekah-Chuang/VizAble.git
```

## Usage
To run the **VizAble** application, execute the following command:
```
VizAble.run_app
```
Once executed, a link will be displayed in the terminal. You can open this link in your web browser to access the application.
