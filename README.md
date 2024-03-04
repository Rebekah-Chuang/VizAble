# VizAble
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