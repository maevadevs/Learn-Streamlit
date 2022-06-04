import streamlit as st
import pandas as pd
import numpy as np

"""
# Main Concepts
"""

"""
## App Model

- Streamlit apps are Python scripts that run from top to bottom
- Every time a user opens a browser tab pointing to your app, the script is re-executed
- As the script executes, Streamlit draws its output live in a browser
- Scripts use the Streamlit cache to avoid recomputing expensive functions, so updates happen very fast
- Every time a user interacts with a widget, your script is re-executed and the output value of that widget is set to the new value during that run
- Streamlit apps can contain multiple pages, which are defined in separate .py files in a pages folder
"""

"""
## Data Flow

- Any time something must be updated on the screen, Streamlit reruns the entire Python script from top to bottom
  - Modification in app's source code
  - User interactions with widgets in the app
  - Event Callbacks in the script will always run before the rest of the script
- Streamlit does some heavy lifting behind the scenes with `@st.cache` decorator
"""

"""
## Displaying and Styling

There are different ways to display data on screen

- We can output text/paragraph using `st.write()` or Markdown style with `\"\"\"`
- To output raw text, use `st.text()`

```python
st.write("This is a regular text using `st.write()`")
```
"""

st.write("This is a regular text using `st.write()`")

"""
```python
st.text("This is a raw text using `st.text()`")
```
"""

st.text("This is a raw text using `st.text()`")

"""
- `st.write()` can be used to write anything
  - It is Streamlit's *Swiss Army knife*
  - You can pass almost anything to `st.write()`
  - Streamlit will figure it out and render things the right way
- There are also other specifications that we can use
  - `st.dataframe()` can be used to output an interactive dataframe
  - `st.table` can be used to display a static, non-interactive table
  - Streamlit also supports *Magic Commands*
    - Any time that Streamlit sees a variable or a literal value on its own line, it automatically writes that to your app using `st.write()`
    - Similar behavior as in Jupyter Notebook's `display()`
"""

"""
### Outputing a Dataframe With `st.write()`

```python
df = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)
st.write(df)
```
"""

df = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)
st.write(df)

"""
### Outputing a Dataframe With `st.dataframe()`
"""

"""
We also added some additional styling on this one but this would be the same as with `st.write()`

```python
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)
st.dataframe(dataframe.style.highlight_max(axis=0, color="red"))
```
"""

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)
st.dataframe(dataframe.style.highlight_max(axis=0, color="red"))

"""
### Outputing a Dataframe as Static Table With `st.table()`

```python
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)
st.table(dataframe)
```
"""

st.table(dataframe)

"""
### Why Not Always Use `st.write()`

- It draws based on its own logic, but you might want to render things differently
- *Method Chaining*: Other methods return an object that can be used and modified, either by adding data to it or replacing it
- If you use a more specific Streamlit method, you can pass additional arguments to customize its behavior
"""

"""
### Outputing Charts and Maps
"""

"""
- Streamlit support different Python libraries for chart and maps
- We can `st.line_chart()` for a simple line-chart

```python
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)
```
"""

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

"""
- We can use `st.map()` to display data points on a map
- For example, here, we are plotting random data on a map of San Francisco

```python
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)
```
"""

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)

"""
## Widgets

- Widgets are GUI elements that we can use to manipulate data
- Example of Streamlit Widgets:
  - `st.slider()`
  - `st.checkbox()`
  - `st.selectbox()`
  - `st.button()`
  - `st.selectbox()`
- We treat Widgets and their values as Python variables

### `st.slider()`

- We can use `st.slider()` to select a value from a range

```python
# This is a widget: Capture its value with a variable
x_wdgt = st.slider(
    label='Select the value for X',
    min_value=0,
    max_value=1000,
    value=500, # Default value
    step=1
)
st.write(x_wdgt, 'squared is', x_wdgt * x_wdgt)
```
"""

# This is a widget: Capture its value with a variable
x_wdgt = st.slider(
    label='Select the value for X',
    min_value=0,
    max_value=1000,
    value=500, # Default value
    step=1
)
st.write(x_wdgt, 'squared is', x_wdgt * x_wdgt)

"""
- We can also assign a *key* to widget as a short-name to access them quickly
- Every widget with a key is automatically added to *Session State*
  - So we can also access their value with `st.session_state.<key>`

```python
x_wdgt = st.slider(
    label='Select the value for X',
    key='X',
    min_value=0,
    max_value=1000,
    value=500, # Default value
    step=1
)
st.write(st.session_state.X, 'squared is', st.session_state.X * st.session_state.X)
```
"""

x_wdgt = st.slider(
    label='Select the value for X',
    key='X',
    min_value=0,
    max_value=1000,
    value=500, # Default value
    step=1
)
st.write(st.session_state.X, 'squared is', st.session_state.X * st.session_state.X)

"""
### `st.checkbox()`

- We can use `st.checkbox()` to show or hide section of the page

```python
show_df = st.checkbox(
    label='Show dataframe', 
    value=False
)

if show_df:
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c']
    )
    chart_data
```
"""

show_df = st.checkbox(
    label='Show dataframe', 
    value=False
)

if show_df:
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c']
    )
    chart_data

"""
### `st.selectbox()`

- We can use `st.selectbox()` to choose value options from a list

```python
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

option = st.selectbox(
    label='Which number do you like best?',
    options=df['first column']
)

'You selected option ', option, ' which corresponds to', str(df[df['first column'] == option]['second column'].values)
```
"""

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

option = st.selectbox(
    label='Which number do you like best?',
    options=df['first column']
)

'You selected option ', option, ' which corresponds to', str(df[df['first column'] == option]['second column'].values)

"""
## Showing Progress With `st.progress()`
"""

"""
- `st.progress()`: When adding long-running computation, use this to display status in real-time
- Here, we use `time.sleep` to simulate a long-running application

```python
import streamlit as st
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we are done!'
```
"""

import time

'Starting a long computation...'

# Add a placeholder: Set initial values
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    # Update the progress bar with each iteration
    bar.progress(i + 1)
    time.sleep(0.1)

'...and now we are done!'

"""
## Caching With `@st.cache` Decorator

- **Note:** This section is bound to change with *Experimental Cache Primitives*
- Caching allows the app to execute quickly
  - Loading data from the web
  - Manipulating large datasets
  - Performing expensive computations

```python
import streamlit as st

@st.cache # This function will be cached
def my_slow_function(arg1, arg2):
    # Do something really slow in here!
    return the_output
```

Whenever the function runs, Streamlit will check a few things:

- The input parameters that you called the function with
- The value of any external variable used in the function
- The body of the function
- The body of any function used inside the cached function

The next time the function is called, if none of these has changed, return the cached value
"""