#more interactive application
import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name=st.text_input("Enter your name :")
age=st.slider("Select your age :",0,100,25) #by default 25 age

options=["C","Java","Python","C#","VB.net"]
choice=st.selectbox("Choose your favorite Language :",options)

if name:
    st.write(f"Hello, {name}")
    st.write(f"Your age is : {age}")
    st.write(f"Your selected Languages : {choice}")

data={
    'name':["jagruti","pooja","mohit","Dharmesh"],
    'age':[32,34,32,35],
    'city':["Rajkot","Ahmedabad","Baroda","Surat"]
}

df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

#upload csv file
uploaded_file=st.file_uploader("Choose a csv file",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
