import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header("st.write")

st.write("**Hello** *world*! :sunny:")

st.write(1234)

df = pd.DataFrame(np.random.randn(200,3),
                  columns=['a', 'b', 'c']
                  )
st.write(df)

c = alt.Chart(df).mark_circle().encode(
    x='a',
    y='b',
    color='c'
).properties(title="Hello")

st.write(c)