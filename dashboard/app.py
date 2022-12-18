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

# Show df 
st.dataframe(df)


#-------------------#
# BODY

st.subheader("Visualization 1: Bar plot analyzing cause of death")

# Bar plot

var_list_V1 = ['gender', 'cause']

source_V1 = df[var_list_V1]

c = alt.Chart(source_V1).mark_bar().encode(
    x=alt.X('cause', 
            sort= '-y',
            # custom axis titles
            axis=alt.Axis(title="Cause of death", # title of x axis: Cause of death
                          labelAngle=0)), # angle of x axis text: 0
      y=alt.Y('count(cause)',
            axis=alt.Axis(title = "Count of deaths due to this cause", # title of y axis: Count of deaths due to this cause
                        titleAnchor="end")), # show title in end of axis
      color= alt.Color ('cause', type="nominal", legend=alt.Legend(title="Which cause?")),
      tooltip=['cause', 'count(cause)']

).interactive(

).configure_title(
    fontSize=13,
    font='Arial',
    anchor='start',
    color='black'

).properties( 
    title= 'What is the most common cause of death among police killings?',
    width= 500,
    height= 450
)
st.altair_chart(c, use_container_width=True)

#second visualization
st.subheader("Visualization 2: Pie chart analysing race/ethnicity of deceased")

#-------------------#
#Pie chart

# DATA CORRECTION

df.raceethnicity = df.raceethnicity.astype("category")

# Create a list of variables for visualization 2
source_V2 = pd.DataFrame(df.raceethnicity.value_counts())

# Set index to column
source_V2 = source_V2.reset_index()

# Rename columns
source_V2.rename(columns={"index": "race", "raceethnicity": "value"}, inplace=True)


c = alt.Chart(source_V2).mark_arc().encode(
    theta=alt.Theta(field="value", type="quantitative"),
    color= alt.Color ('race', 
                     legend=alt.Legend(title="Which race?")),
    tooltip = ["race"]

).configure_title(
    fontSize=12,
    font='Arial',
    anchor='start',
    color='black'


).properties( 
    title= 'Which race is most effected by police killings?',
    width= 300,
    height= 300
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