# SETUP

import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from pathlib import Path

home_path = str(Path.home())
#-------------------
#-------------------#
# IMPORT DATA


# Data import (you may need to change the path)
df = pd.read_csv("https://raw.githubusercontent.com/FabioRaab/bigData-HW1/main/data/external/police_killings.csv")


###-------------------###
# START OF APP

#-------------------#
# HEADER
st.header("Groupe: O - Dashboard")
# Title of  app
st.title("Task 5: Streamlit")
st.dataframe(df)


#-------------------#
# BODY

# Show df 

st.write("Visualization 1: Bar plot analyzing cause of death")

# Bar plot
st.subheader("Bar chart")

c = alt.Chart(df).mark_bar().encode(
    x='country',
    y='life_satisfaction',
    tooltip = ['country', "life_satisfaction"]
)

st.altair_chart(c, use_container_width=True)

# Show metric
st.subheader("Display Metrics")
st.metric("My metrics", 32, 4)

# Add slider with user input
st.subheader("Slider")
st.write("This is a Slider")
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

# Show code
st.subheader("Show some code")

code = '''def hello():
     print("Hello, Streamlit!")'''

st.code(code, language='python')