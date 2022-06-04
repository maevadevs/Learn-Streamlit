# Run Linux: Execute ./run.sh or ./run-dev.sh
# Run Windows: Execute ./run-dev.ps1 or ./run.ps1
""""""
"""
# Hello Streamlit
"""

"""
## Running Streamlit App

- Create a Python file: `Home.py`
- Add Python codes with Streamlit syntaxes
- Run the python file with Streamlit
  - If passing arguments to `Home.py`, use `--`

```sh
# Starting a Streamlit app in a pipenv context
pipenv run python -m streamlit run Home.py [-- args]
```

```python
# Home.py
import streamlit as st

st.write("Hello Streamlit!!")
st.text("This is a basic raw text")

\"\"\"
Markdown can also be used here
\"\"\"
```
"""

"""
## Adding Additional Pages

- As apps grow large, it becomes useful to organize them into multiple pages
- Streamlit provides a way to create multipage apps
- Create a `pages` folder in the root of the application
- Add new pages as `<Page_Name>.py` in this folder
  - Use `_` as separator for the page name: It will be automatically replaced with a space in the app
- Run `streamlit run main.py` as usual
  - `main.py` will correspond to the Home Page
- **Note:**
  - Streamlit does not automatically watch all pages for changes during development
  - Streamlit only watch for changes for the file passed to the `streamlit run` command
  - To fix this:
    - Create a main shell file in the root of the app: `run-dev.sh`
    - Add the command to start the app in the file
    - Also list all the pages files that should be watched
    - Call `./run-dev.sh` to bootstrap the app

```sh
# run-dev.sh
pipenv run python -m streamlit run Home.py pages/Page_1.py pages/Page_2.py [-- args]
```
"""

"""
## Hiding Footer and Streamlit Settings Menu

```python
import streamlit as st

hide_streamlit_style = \"\"\"
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        footer:after {
            content:'This is a custom footer for testing'; 
            visibility: visible;
            display: block;
            position: relative;
            #background-color: red;
            padding: 5px;
            top: 2px;
        }
    </style>
\"\"\"
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
```
"""
import streamlit as st

hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        footer:after {
            content:'This is a custom footer for testing'; 
            visibility: visible;
            display: block;
            position: relative;
            #background-color: red;
            padding: 5px;
            top: 2px;
        }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)