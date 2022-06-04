import streamlit as st
import pandas as pd
import numpy as np

"""
# Layout and Theme
"""

"""
## Add Sidebar With `st.sidebar`

- `st` controls the main-area widgets
- `st.sidebar` controls the sidebar-area widgets
- We can use `st.sidebar` to add a left sidebar
  - Each elements passed to `st.sidebar` is pinned to the left
  - Allows to separate UI controls from contents
  - `st.slider()`: Adds a Slider to the main window
  - `st.sidebar.slider()`: Adds a Slider to the sidebar
- **Note: `st.sidebar.echo` and `st.sidebar.spinner` are currently not supported**

```python
import streamlit as st

# Add a selectbox to the sidebar
sb_selectbox = st.sidebar.selectbox(
    label='How would you like to be contacted?',
    options=('Email', 'Home phone', 'Mobile phone')
)
# Add a slider to the sidebar
sb_slider = st.sidebar.slider(
    label='Select a range of values',
    min_value=0.0, 
    max_value=100.0, 
    value=(25.0, 75.0)
)
```
"""

# Add a selectbox to the sidebar
sb_selectbox = st.sidebar.selectbox(
    label='How would you like to be contacted?',
    options=('Email', 'Home phone', 'Mobile phone')
)
# Add a slider to the sidebar
sb_slider = st.sidebar.slider(
    label='Select a range of values',
    min_value=0.0, 
    max_value=100.0, 
    value=(25.0, 75.0)
)

"""
## Setup Column-Based Layout With `st.columns()` and `st.expander`

- `st.columns` allows to divide the main area into multiple columns
  - Pass the number of columns that we want and capture each column into a variable
  - We can use a column just list a sidebar or the main area
  - We can use the `with` context selector to select which column to work with
- `st.expander` allows to show/hide contents dynamically
- **Note: `st.echo` and `st.spinner` are currently not supported inside columns**

```python
with st.expander(label="Expand divided columns", expanded=False):
    # Divide the main area into 2 columns
    left_column, right_column = st.columns(2)
    # We can use a column just like st.sidebar:
    left_column.text_input(
        label="Password", 
        value="", 
        type="password", 
        help="Must be 10 characters-long, a-z and 0-9", 
        autocomplete=None, 
        on_change=None, 
        placeholder="password", 
        disabled=False
    )
    left_column.button(
        label="Submit",
        help="Submit the form", 
        on_click=None, 
        disabled=False
    )
    # Or better, use a context manager
    with right_column:
        chosen = st.radio(
            label='Sorting hat',
            options=("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")
        )
        st.write(f"You are in {chosen} house!")
```
"""

with st.expander(label="Expand divided columns", expanded=False):
    # Divide the main area into 2 columns
    left_column, right_column = st.columns(2)
    # We can use a column just like st.sidebar:
    left_column.text_input(
        label="Password", 
        value="", 
        type="password", 
        help="Must be 10 characters-long, a-z and 0-9", 
        autocomplete=None, 
        on_change=None, 
        placeholder="password", 
        disabled=False
    )
    left_column.button(
        label="Submit",
        help="Submit the form", 
        on_click=None, 
        disabled=False
    )
    # Or better, use a context manager
    with right_column:
        chosen = st.radio(
            label='Sorting hat',
            options=("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")
        )
        st.write(f"You are in {chosen} house!")

"""
## Theme

- Streamlit supports *Light* and *Dark* themes out of the box
- First check if the user viewing an app has a Light or Dark mode preference set by their OS and browser
- Else, *Light* theme by default
- User can also change the theme in the Settings of the app

### Defining Custom Theme

- Use the *Settings* menu and Click on *Edit Active Theme*
- Use the editor to define your theme
- Themes can be saved by setting config options in the `[theme]` config section
  - It will appear as *Custom Theme* in the theme selector
  - It will be applied by default instead of the included *Light* and *Dark* themes
- **Note: The theme editor menu is available only in local development**
  - Deployed app to Streamlit Cloud would not have that available
"""