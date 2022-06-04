# Installation

## Requirements

- Python 3.7+
- A Virtual Environment Manager
  - pipenv
  - poetry
  - venv
  - virtualenv
  - conda

## Installation on Windows (Using `Pipenv`)

- Create a virtual environment
- Install Streamlit as dependency: `pipenv install streamlit`
- Activate the virtual environment: `pipenv shell`
- Test that the installation worked: `streamlit --version`
- To run a demo app in memory: `streamlit hello`
- To turn off analytics collections:
  - Create a `config.toml` file in `C:\Users\<username>\.streamlit`
  - Add the follwing to the file

```toml
[browser]
gatherUsageStats = false
```