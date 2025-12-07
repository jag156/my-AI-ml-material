import streamlit as st
import pandas as pd
import numpy as np

#title of streamlit
st.title("Hello Streamlit")

#display simple text
st.write("This is simple text")

#create simple DataFrame
df=pd.DataFrame(
    {
        'First Column':[1,2,3,4],
        'Second Column':[10,20,30,40]
    }
)

#display the dataframe
st.write("This is your Dataframe")
st.write(df)

#create a line chart
chart_data=pd.DataFrame(
    np.random.rand(20,3),#20rows and 3columns
    columns=['A','B','C']
)
st.line_chart(chart_data)